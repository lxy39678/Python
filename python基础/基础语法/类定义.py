#有构造函数
class Person:
    total_person = 0
    def __init__(self,name,sex,province):
        print("Init the class")
        self.name = name
        self.sex = sex
        self.province = province
        Person.total_person += 1

    def get_name(self):
        return self.name

if __name__=="__main__":
    person = Person("zhangsan","male","shandong")
    print(person.name)
    print(person.get_name())
    print(person.sex)
    print(person.total_person)
    print("*"*100)

#无构造函数
class Person1:
    def get_name1(self):
        return self.name
    def set_name1(self,name):
        self.name = name

    def set_person_attribute(self,sex,province):
         self.sex = sex
         self.province = province
    def get_sex(self):
        return self.sex

if __name__=="__main__":
    per1 = Person1()
    per1.set_name1("hanmeimei")
    print(per1.get_name1())
    per1.set_person_attribute("male","shanghai")
    print(per1.get_sex())
