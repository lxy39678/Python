import codecs
import time

def open_example(in_file):
    '''
    r: read
    a: append
    w: write
    '''

    file_instance = open(in_file,"r")
    content = file_instance.read()
    file_instance.close()
    print(content)


def open_utf8(in_file):
    file_instance = codecs.open(in_file, encoding="utf-8")
    content = file_instance.read()
    file_instance.close()
    print(content)


def write_utf8(in_file):
    file_instance = codecs.open(in_file, encoding="utf-8",mode="a")
    file_instance.write(u"新的一行"+"\n")
    file_instance.write(u"新的二行"+"\n")
    file_instance.writelines([u"新的三行"+"\n",u"新的四行"+"\n"])

    file_instance.flush()
    print("I am sleeping")

    time.sleep(20)
    file_instance.close()


if __name__=="__main__":
    open_example("filexample.txt")
    open_utf8("filexample.txt")
    write_utf8("filexample.txt")