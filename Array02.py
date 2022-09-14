import array as arr
a = arr.array('i', [1, 2, 3, 4, 5])
lenOfArray = len(a)
print("No of elements in array is : ", lenOfArray)
for element in range(0, lenOfArray):
    print(a[element])
