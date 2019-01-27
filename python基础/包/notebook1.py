def add(args):
    sum = 0
    for i in args:
        try:
            sum += i
        except TypeError:
            print("不是数字")
        else:
            print("")
        # finally:
        #     print("任何情况下都有我的存在")
    print(sum)

# add([1,2,3,'a',4])