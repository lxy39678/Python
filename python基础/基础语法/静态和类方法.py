class Person:

    total_person = 0
    def __init__(self,name,sex,province):
        print("init the class")
        self.name = name
        self.sex = sex
        self.province = province
        Person.total_person += 1

    #静态方法，不需要参数，不需要实例化就可以调用（实例化也可以调用）
    @staticmethod
    def set_new_name(new_name):
        return "new name is:"+new_name

    #类方法，不管是否实例化都可以调用
    @classmethod
    def set_new_province(cls,new_province):
        return "you province is:"+new_province

    #property方法，调用时不加括号
    @property
    def get_sex(self):
        return self.sex



if __name__=="__main__":
    print(Person.set_new_name("hanmeimei"))
    print(Person.set_new_province("beijing"))
    sg = Person("huahua","female","shanghai")
    print(sg.set_new_name("fanghua"))
    print(sg.set_new_province("zhejiang"))
    print(sg.get_sex)