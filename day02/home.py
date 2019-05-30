adict={'xingming':'liaojiayan','age':'200'}
def dict_sel():
    print(adict['xingming'])
def dict_del():
    adict.pop('age')
    print(adict)
def dict_add():
    adict['class']='1904'
    print(adict)
def dict_update():
    adict['xingming']='ljy'
    print(adict)
def dict_extend():
    bdict={"username":"admin","password":"123456"}
    adict.update(bdict)
    print(adict)
if __name__ == '__main__':
    dict_sel()
    dict_del()
    dict_add()
    dict_update()
    dict_extend()