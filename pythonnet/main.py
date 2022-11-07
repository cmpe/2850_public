#import pythonnet

import random
import clr

clr.AddReference('GDIDrawer')
from GDIDrawer import CDrawer
from GDIDrawer import RandColor

def GDITester():
    canvas = CDrawer()
    canvas.ContinuousUpdate = False
    for x in range(10):
        col = RandColor.GetColor()
        radius = random.randint(20,200)
        #p = Point( 2, 3)
        canvas.AddCenteredEllipse(
            random.randint(radius,canvas.ScaledWidth - radius),
            random.randint(radius,canvas.ScaledHeight - radius),
            radius * 2, radius * 2, col )
        canvas.Render()


if __name__ == '__main__':
    print( RandColor.GetColor())
    GDITester()
    _ = input('Enter to stop')

