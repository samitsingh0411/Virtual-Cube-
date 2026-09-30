# Import the RubixCube class from the CubeManager module
from CubeManager import RubixCube as Rc

# Create a 3x3 Rubik's Cube instance with the name "Rubix"
MyCube = Rc.ThreeByThree("Rubix")

# Print the initial state of the cube
print(MyCube)

# Perform a right face clockwise rotation (R move)
MyCube.do("R")

# Print the cube after the moves (should be back to original state)
print(MyCube)

MyCube.solve()

MyCube.do(move_list=["R", "L"])

MyCube.solve()

MyCube.do(alg_name='Aa')