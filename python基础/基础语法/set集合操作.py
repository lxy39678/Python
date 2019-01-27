a = {}
print(type(a))

b = set()
print(type(b))

c = {1,2,3,4,1}
print(c)

my_set = {1,2,3}
set = {4,5,6,1}
set1 = {4,5,6,1,3}
set2 = {4,5,6,1,10}
set3 = {4,5,6,1,10,'python'}
print(my_set.union(set))
print(set1.difference(set))
print(set2.symmetric_difference(set1))

#删除不存在的不会给提示
set2.discard(4)
print(set2)

#删除不存在的会给提示
set3.remove("python")
print(set3)





