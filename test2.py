from CubeManager import RubixCube as Rc 
from CubeManager.alg_name import test_dict

TestCube = Rc.ThreeByThree('Test')
TestCube.do(alg_name='sexy')

all_algs_by_name = list(test_dict.keys())
all_algs_by_list = list(test_dict.values())

for i in all_algs_by_name:
    print(i)
    TestCube.do(alg_name=i)
print('All algs succesfully called by name!')


for i in all_algs_by_list:
    print(i)
    TestCube.do(move_list=i)  
print('All algs succesfully called by their corresponding list of moves')

