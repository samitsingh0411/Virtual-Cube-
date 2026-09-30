from CubeManager import RubixCube as Rc
# Example Code

# Basics
TestCube = Rc.ThreeByThree(name="Rubix") # Creates a 3x3 cube, right now  we can only create 3x3
print(TestCube) # Prints the cube as a string

# Moving and rotating

# Moving
'''
Does the following moves on the cube: R, R', L, L', U, U', F, F', B, B', D, D'.
You can enter them individually or pass a list of them.
'''
TestCube.do("U'")
TestCube.do(move_list=["R", "U", "R'"])
TestCube.do(alg_name='sexy')

# Rotating
'''
Rotates the cube some number of times in a give direction vertically or horizontally clockwise or anti-clockwise
n (normal) => LEFT to RIGHT or DOWN to UP
o (opposite) => RIGHT to LEFT or Down to UP
'''
TestCube.rotate("h", 2, "n") # n --> Normal
TestCube.rotate("v", 2, "o") # o --> Opposite

# Shuffling and Solving
# Shuffling
'''
Shuffles the cube and returns the shuffle sequence in the form of a list.
'''
print("Returns suffles sequence: ", TestCube.shuffle())
print(TestCube) 

# Solving
print(TestCube.solve()) # Simply solves the cube.

# Loading and saving the cube.

'''
You can save the cube, by default it'll save the cube in the currect directory, with like so <cube_name>.json.
You can however give your custom path with your custom name for the cube. Giving custom name is mandetory if loading. 
'''
TestCube.do(alg_name='sexy')
TestCube.save()
TestCube.solve()
TestCube.load('Cube_for_saving.json', cube_name='LoadTestCube')  
print(TestCube)

