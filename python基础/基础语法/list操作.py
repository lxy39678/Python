my_list=['python',12,2.3,9.6,10,9,19,60]
my_list1=['python',12,2.3,9.6,10,9,19,60]
list2 = [3,4,5]

print(my_list+list2)
print(list2*3)

lang = [["python",0.4],["java",0.5]]

print(my_list[1:3])
print(my_list[-4:-2])
print(my_list[::2])

print(id(my_list1))
del my_list1[0]
print(my_list1)
print(id(my_list1))

my_list2 = my_list[0:]
print(my_list2)
print(id(my_list2))

my_list.append("java")
print(my_list)

my_list.extend(list2)
print(my_list)

print(my_list.pop())
print(my_list)

my_list.reverse()
print(my_list)

my_list4 = [100,95,99]
my_list4.sort()
print(my_list4)

my_list5 = [[1,2],["a","b"],[1,2,3,4]]
print(len(my_list5))


