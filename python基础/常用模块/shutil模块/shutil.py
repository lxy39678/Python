#!/usr/bin/python
# -*- coding:utf-8

from shutil import make_archive

def targz_dir():
    archive_name = "test"
    root_dir = "./test"
    make_archive(archive_name,'gztar',root_dir)


if __name__=="__main__":
    targz_dir()


# shutil.copy(src, dst) : 复制文件，dst可以是目录，也可以 是被复制后带文件名的全路径， 比如:dst可以
# /home/testerhome/， 也可以是
# home/testerhome/newfile.txt
# • shutil.copytree(src, dst): 复制目录包括子目录到目标目
# 录
# • shutil. rmtree(path): 删除目录包括子目录
# • shutil.move(src, dst): 移动源目录包括子目录的文件到
# 目标目录
# • shutil.make_archive(base_name, format):打包压缩文件