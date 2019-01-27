import sys
import os

#启动一个python脚本run.py, 传入参数为/home/tools/src, 把 /home/tools/src加入到python path里面，打印出前后的 pythopath列表信息。 如果此目录下没有任何py 文件，程 序异常退出
#把上面的脚本出信息通过sys.stdout 重定向到log.txt

sys.path.append('/Users/lixiangyu/PycharmProjects/python基础/常用模块/sys/test')
print(sys.path)

# a = os.listdir('/Users/lixiangyu/PycharmProjects/python基础/常用模块/sys/test')

for dirpath,dirs,files in os.walk("/Users/lixiangyu/PycharmProjects/python基础/常用模块/sys/test"):
    for name in files:
        if(os.path.splitext(name)[1] == '.py'):
            print("py")
        else:
            print("none")
            f_handler = open("../test/log.txt","w")
            sys.stdout = f_handler
