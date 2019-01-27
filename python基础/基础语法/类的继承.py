from 基础语法.类定义 import Person

class Student(Person):

    def __init__(self,name,sex,province,grade):
        #父类初始化
        super(Student, self).__init__(name,sex,province)
        # Person.__init__(self,name,sex,province)
        self.grade = grade

    def get_grade(self):
        return self.grade

    #多态
    def get_name(self):
        return "name"

    def get_nick_name(self):
        name = Person.get_name(self)
        if name.startswith("xiao"):
            return "small_" + name
        else:
            return name


if __name__=="__main__":
    ss = Student("xiaozhang","male","beijing",6)
    print(ss.get_name())
    print(ss.get_nick_name())