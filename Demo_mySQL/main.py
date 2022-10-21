# This is a sample Python script.
import mysql.connector
from decimal import Decimal
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def Connect(name) -> 'dbConnection':
    mydb = None
    pw = 'demo_password'
    try:
        mydb = mysql.connector.connect(
            #host="thor.net.nait.ca",  # host to connect, could be "localhost" if the server is on same box
            host="thor.cnt.sast.ca",  # host to connect, could be "localhost" if the server is on same box
            user="demo_user",
            # username - normally for remote connections, the server must be configured to accept connection requests (**security)
            password=pw,  # password - either literal, or prompted from the user, here pw is populated variable
            database='demo_project'  # the database to connect to, the default is main mysql database
        )
    except mysql.connector.Error as err:  # Specifically accept connector exceptions, catch and process appropriately
        print(f'Something went wrong: {err}')

    if mydb != None and mydb.is_connected():
        print(f'Connected : {mydb.get_server_info()}')
    return mydb

def Query1( mydb ):
    # Example : single parametized query substitution, column_name retrieval, resultset default of list-of-tuple
    # Always a chance that this fails
    try:
        # Retrieve a cursor for this operation, buffer=True indicates that resultset should be completely buffered, optimizing queries with small resultset
        cursor = mydb.cursor(buffered=True)
        # The query should be tested prior to being used here
        # Note the %s, ALL replaced parameter values will use the %s placeholder
        #query = f"select * from authors where state like %s"  # Single parameter to substitute
        query = f"select * from titles where title not like %s"  # Single parameter to substitute

        filter = 'CA'
        params = (filter,)  # TUPLE !, remember trailing comma(,) or result is just the single expression

        # Execute the query, supply the params tuple of arguments
        cursor.execute(query, params)

        # Retrieve the native ordered column names
        column_names = cursor.column_names

        # The execution is complete, the cursor could be used to iterate the resultset
        # In this case, the resultset is known to be small, so fetchall() will
        #   retrieve ALL that are left ( if you haven't taken any, it would be everything )
        resultset = cursor.fetchall()

    except mysql.connector.Error as err:
        print(f'Something went wrong: {err}')
        resultset = None
    finally:
        cursor.close()  # remember to close the cursor(), you are done with it

    print(f'Query1 : {query}')
    print(column_names)
    print(resultset)
    print( [ val[4] * 2 for val in resultset]) # the Decimal() type implicitly converts to 'numbers' supporting operations
    print( max([ val[4] * 2 for val in resultset])) # the Decimal() type implicitly converts to 'numbers' supporting operations
    print()

def Query2(mydb):
    # Example : multiple parametized query substitution, resultset set to list-of-dictionary
    # Always a chance that this fails
    try:
        # Retrieve a cursor for this operation, adding dictionary=True indicates the resultset should be a list of Dictionary, better for use with named key fields
        cursor = mydb.cursor(buffered=True, dictionary=True)
        # The query should be tested prior to being used here
        # Note the %s, ALL replaced parameter values will use the %s placeholder
        query = f"select * from authors where state like %s or state like %s"  # many parameters to substitute

        filter1 = 'UT'
        filter2 = 'IN'
        params = (filter1, filter2)  # one for each substitution : %s

        # Execute the query, supply the params tuple of arguments
        cursor.execute(query, params)

        # Retrieve ALL that are left ( could be an empty list )
        resultset = cursor.fetchall()

    except mysql.connector.Error as err:
        print(f'Something went wrong: {err}')
        resultset = None
    finally:
        cursor.close()  # remember to close the cursor(), you are done with it

    print(f'Query2 : {query}')
    for row in resultset:  # for each row returned
        print(row)  # print each dictionary=row/record

    print()

def Query3(mydb):
    # Example : parameterized wildcard substitution, resultset set to list-of-dictionary
    # Always a chance that this fails
    try:
        # Retrieve a cursor for this operation, adding dictionary=True indicates the resultset should be a list of Dictionary, better for use with named key fields
        cursor = mydb.cursor(buffered=True, dictionary=True)

        # The query should be tested prior to being used here
        # Note the %s, ALL replaced parameter values will use the %s placeholder
        query = f"select * from authors where au_lname like %s"  # Single parameter to substitute

        # Include a wildcard in the parameterized argument, it will appropriately escaped and incorporated.
        # Assume a variable holds filter value ( user entry ? )
        varFilter = 'o'
        filter = '%' + varFilter + '%'  # build parameter, pre/post fixing wildcards as required
        params = (filter,)  # one for each substitution : %s

        # Execute the query, supply the params tuple of arguments
        cursor.execute(query, params)

        # Retrieve ALL that are left ( could be an empty list )
        resultset = cursor.fetchall()

    except mysql.connector.Error as err:
        print(f'Something went wrong: {err}')
        resultset = None
    finally:
        cursor.close()  # remember to close the cursor(), you are done with it

    print(f'Query3 : {query}')
    for row in resultset:  # for each row returned
        print(row)  # print each dictionary=row/record


if __name__ == '__main__':
    mydb = Connect('Kevin')
    Query1(mydb)
    Query2(mydb)
    Query3(mydb)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
