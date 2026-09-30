from CubeManager import RubixCube as Rc

MyCube = Rc.ThreeByThree("ColorTest")
print(MyCube)

"""
Testing if colors work, so right now padding I have to add to the front and back row for them to render directly above the the second row in 
the middle seems to be variable. I pressume this is because of varyinig lengths strings of the colors given by termcolor lib.

I suspect this becuase if I use cyan, it works fine but if I use orange, it doesn't. I need all the colors to have the same length.
"""
