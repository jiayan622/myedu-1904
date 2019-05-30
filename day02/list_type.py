list_b = ['是打发', 2, '你好', 6, 7, 1, 3]

def list_a():
    print(list_b[2:3])
    print(list_b[3:])
    print(list_b[:1:-1])
# 删除list元素
def list_delete():
    list_b.pop(1)
    print(list_b)
#增加元素
def list_add():
    list_b.append('哈喽')
    print(list_b)
 # 合并元素
    list_c=[100,200,300,400]
    list_b.extend(list_c)
    print(list_b)

def list_update():
    list_d=[1,2,3,4,5,6]
    list_d[2]=200
    print(list_d)
def  list_order():
    qlist=[100,200,99,300,400,520,120,50]
    qlist.sort()
    qlist.sort(reverse=True)
    print(qlist)
def list_distinct():
    wlist=[1,2,2,3,3,4,5,5,6,7,]
    wlist=list(set(wlist))
    print(wlist)
def list_len():
    zlist=[1,2,3,4,5,6]
    zlist=len(zlist)
    print(zlist)







if __name__ == '__main__':

    # a='风雨无阻'
    # print(a[0])
    # print(a[2:])
    # print(a[0]+a[3])
    # print(a[::-1])
    # # # 这就是一个列表的数据类型,英文 是 list, 也叫 数组
    # # alist = ['是打发', 2, '你好', 6, 7, 1, 3]
    # # list_a()
    # list_delete()
    # list_add()
    # list_update()
    list_order()
    list_distinct()
    list_len()