import array as arr

array_num = arr.array('i',[1,2,3,4,5])
total_count = len(array_num)
print("No. of numbers:",total_count)


array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))