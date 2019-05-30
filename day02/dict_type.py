#
adict={"username":"admin","password":"123456"}
def dict_a():
    print(adict["username"])
    print(adict["password"])
def dict_updata():
    adict['username']='ljy'
    print(adict)
def dict_del():
    adict.pop("username")
    adict.pop("password")
    print(adict)
def dict_add():
    adict['age']=18
    print(adict)
    bdict={'list':[1,2],'class':'1904'}
    adict.update(bdict)
    print(adict)
#字典转换字符串
def adict_zhaunghuan():
    adict

if __name__ == '__main__':
    dict_a()
    dict_updata()
    dict_del()
    dict_add()
