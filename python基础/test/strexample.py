#!/usr/bin/env python
#coding=utf-8

path = '/Users/lixiangyu/IdeaProjects/apache-maven-3.6.0/bin:' \
       '/Library/Java/JavaVirtualMachines/jdk1.8.0_191.jdk/Contents/Home/bin:' \
       '/Users/lixiangyu/Library/Android/sdk/build-tools/28.0.3:' \
       '/Users/lixiangyu/Library/Android/sdk/platform-tools:' \
       '/Users/lixiangyu/Library/Android/sdk/tools/bin:' \
       '/Users/lixiangyu/Library/Android/sdk/tools:' \
       '/Users/lixiangyu/anaconda3/bin:' \
       '/Library/Frameworks/Python.framework/Versions/3.6/bin:' \
       '/Library/Frameworks/Python.framework/Versions/3.6/bin:' \
       '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:'

for item in path.split(":"):
    print (item)

path1='-rw-r--r--    1 root root   182 Nov  6 23:31 month.py'
list = path1.split()
list1 = path1.split(" ")
print (list[-4:])

love = "i love java"
loveNew = love.replace("java","python")
print (loveNew)
print (love.upper())
print (love.lower())
print ("i love java".capitalize())
print (love.startswith("i"))

list2 = ["I","love","Python"]
print (" ".join(list2))





