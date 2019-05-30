def tese1():
     print('tese1')
def tese2():
   print('tese2')
def tese3():
   print('tese3')
def float1():
    d=0.1
    print(d)
def type_zhuanghuan():
    a='100'
    print(type(int(a)))
def type_zhuanghuan1():
    a=100
    print(type(str(a)))
def type_join():
    a='你'
    b=123456
    c='好'
    print(a+str(b))
    print(a+c)
    print(str(b)+c)
    print('%s%s'%(a,c))
    print('%s%s'%(a,b))
    print('%s%s%s'%(a,c,b))
def add_abc(num1,num2):
    return num1 + num2
    # print(num1)
    # print(num2)
    # print(num1+num2)







if __name__ == '__main__':
    a=5
    print(type(a))
    b='5'
    print(type(b))
    a=0.1
    print(type(a))
    tese3()
    tese1()
    tese2()
    float1()

    type_zhuanghuan()
    type_zhuanghuan1()
    type_join()
    lkjhio=add_abc(1,4)
    print(lkjhio)