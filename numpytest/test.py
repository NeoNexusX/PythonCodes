import numpy as np

testarray = [[[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]],
             [[10, 11, 12],
              [13, 14, 15],
              [16, 17, 18]]]
test_numpy_array = np.array(testarray)
print('test_numpy_array.reshape(9, -1) :')
print(test_numpy_array.reshape(9, -1))
print('test_numpy_array.reshape(-1, 9) :')
print(test_numpy_array.reshape(-1, 9))
print('test_numpy_array.reshape(-1, 9).T :')
print(test_numpy_array.reshape(-1, 9).T)
print(test_numpy_array.shape)
print(test_numpy_array)
print('test_numpy_array.T')
print(test_numpy_array.T.shape)
print(test_numpy_array.T)

testarray2 = np.arange(3 * 4).reshape((6, 2))
print(testarray2)
testarray3 = testarray2.reshape(2, 2, 3)
print(testarray3)
np.arange(2 * 2 * 4).reshape((2, 2, 4))
