# 1. 设计一个表示服务器的类。包含服务器的属性有:CPU 个数， 内存大小， 磁盘空间大小，操作系统类型(Linux, Windows)
# 其中操作系统类型设置为私有变量，外部不可以更改。 实现一个方法，输出服务器的属性内容为以下格式: 8 核CPU， 40G 内存，150G 磁盘空间，Linux

#有构造函数
class Server:

    def __init__(self,cpuCount,memorySize,dishSize,System):
        self.cpuCount = cpuCount
        self.memorySize = memorySize
        self.dishSize = dishSize
        self.__System = System

    def get_System(self):
        return "Linux"


if __name__=="__main__":
    srv = Server("8核CPU","40G内存","150G磁盘空间","Linux")
    print(srv.cpuCount)
    print(srv.memorySize)
    print(srv.dishSize)
    print(srv.get_System())
    print("*"*50)

#无构造函数
class Server1:

    def set_cupCount(self,cupCount):
        self.cupCount = cupCount

    def get_cupCount(self):
        return self.cupCount

    def set_memorySize(self,memorySize):
        self.memorySize = memorySize

    def get_memorySize(self):
        return self.memorySize

    def set_dishSize(self,dishSize):
        self.dishSize = dishSize

    def get_dishSize(self):
        return self.dishSize

    def __set_System(self,System):
        self.__System = System

    def get_System(self):
        return "Linux"

if __name__=="__main__":
    srv1 = Server1()
    srv1.set_cupCount("8核CPU")
    print(srv1.get_cupCount())
    srv1.set_memorySize("40G内存")
    print(srv1.memorySize)
    srv1.set_dishSize("150G磁盘空间")
    print(srv1.dishSize)
    # srv1.set_System("Linux")
    print(srv1.get_System())
