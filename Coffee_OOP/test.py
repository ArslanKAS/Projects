import numpy as np

def function4():
    #Swap columns 1 and 2 in the array arr.

    arr = np.arange(9).reshape(3,3)
    print(arr)


    return arr[:,[0,1]] = arr[:,[1,0]] #wrtie your code here
    """
    Expected Output:
          array([[1, 0, 2],
                [4, 3, 5],
                [7, 6, 8]])
    """

print(function4())
