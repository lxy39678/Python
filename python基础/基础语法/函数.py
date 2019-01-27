#不定长函数
def student(profile,*mytuple):
    out_put=""
    for parameter in mytuple:
        if not out_put:
            out_put = out_put + parameter
        else:
            out_put = out_put + "," + parameter
    return profile + ":" + out_put
print(student(u"学生",u"大鹏",u"男性",u"7岁"))

def student_tuple(profile,mytuple):
    out_put=""
    for parameter in mytuple:
        if not out_put:
            out_put = out_put + parameter
        else:
            out_put = out_put + "," + parameter
    return profile + ":" + out_put
print(student_tuple(u"学生",(u"大鹏",u"男性",u"7岁")))

def add(x,**kwargs):
    total = x
    for arg,value in kwargs.items():
        print("adding",arg)
        total += value
    return total
print(add(10,y=11,z=12,w=13))

def add1(x,kwargs):
    total = x
    for arg,value in kwargs.items():
        print("adding",arg)
        total += value
    return total
input_dict = {"y":11,"z":12,"w":13}
print(add1(10,input_dict))

#匿名函数
add = lambda x,y: x+y
def addme(x,y):
    return x+y
addme(1,2)

#map函数
def sqr(x):
    return x ** 2
a = [4,5,8]
print(map(sqr,a))
print([sqr(a[0]),sqr(a[1]),sqr(a[2])])

def add(x,y):
    return x + y
x1 = (4,5,6)
y1 = [10,12,16]
print(map(add,x1,y1))