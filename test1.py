from CubeManager import RubixCube as Rc

TestCube = Rc.ThreeByThree(name="Rubix") # Creates a 3x3 cube, right now  we can only create 3x3

print(TestCube)
# Testing for u, works fine ✅
TestCube.rotate('h', dir='o')
TestCube.do('D')

# Testing for r, works fine ✅  
TestCube.rotate('v')
TestCube.do('L')

# Testing for l, works fine ✅    
TestCube.rotate('v', dir='o')
TestCube.do('R')      

# Testing for d, works fine ✅
TestCube.rotate('h')
TestCube.do('U')

# Testing for f, works fine ✅
TestCube.do('z')
TestCube.do('B')

# Testing for b, works fine ✅    
TestCube.do("z'")
TestCube.do("F")

print(TestCube)

