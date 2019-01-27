#双下划线为私有，单下划线为共有，但最好不要用
class Person:

    def __init__(self,name,sex,province,weather):
        print("init the class")
        self.__name = name
        self.sex = sex
        self.__province = province
        self._weather = weather

    def _get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name


if __name__=="__main__":
    pp = Person("zhangsan","male","jiangsu","warm")
    print(pp.sex)
    print(pp._weather)
    print(pp._get_name())
