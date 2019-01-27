x = 10
y = 0
try:
    result = x / y
except ZeroDivisionError:
    print ("除数不能为0")

else:
    print("结果是",result)
finally:
    print("任何情况下都有我的存在")