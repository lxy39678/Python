# 1. 设计一个作业1中服务器的子类，实现一个新的方法，根据 cpu个数，内存大小，磁盘空间大小计算出服务器当前价
# 格 ，计算公式为: CPU 个数* 1527.679+ 内存大小G * 100.21+ 磁盘空间大小G * 50.789 。 返回数据类型为浮点型。 保留小数点后2位 。 并实例化此方法，打印出价格。
from 作业.基础作业.基础作业三 import Server

class sonServer(Server):

    def __init__(self,cpuCount,memorySize,dishSize,System):
        Server.__init__(self,cpuCount,memorySize,dishSize,System)
        # super(Server, self).__init__(cpuCount,memorySize,dishSize,System)

    def get_price(self):
        price = self.cpuCount * 1527.679 + self.memorySize * 100.21 + self.dishSize * 50.789
        return round(price,2)

if __name__=="__main__":

    getPrice = sonServer(8,40,150,"linux")
    print(getPrice.get_price())

