#!/usr/bin/env python
# encoding: utf-8

def dic_demo():
    age_dic = {'xiaozhang':18,'laogao':53,"hanmeimei":20}
    print(age_dic.keys())
    print(age_dic.get('xiaozhang'))
    print(age_dic.values())
    for k, v in age_dic.items():
        print(k, v)

if __name__== '__main__':
    dic_demo()
