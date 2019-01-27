my_dict = {"name":"xiaozhang","company":"baidu","grade":"T7"}
dict = {"name1":"xiaozhang1","company1":"baidu1","grade1":"T8"}
my_dict.update(dict)
print(my_dict)
print(my_dict["company"])

my_dict["sex"] = "male"
print(my_dict)

my_dict["grade"] = "p8"
print(my_dict)

del my_dict["name"]
print(my_dict)

print(my_dict.get("grade"))

print(my_dict.items())


