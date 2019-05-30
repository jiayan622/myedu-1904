alist=[1,2,3,4,5,6,7,8,9,10]
def list_a():
    print(alist[2])
    print(alist[1:4])
    alist.pop(3)
    print(alist)
    alist.append(100)
    alist.append(520)
    alist[0]='5'
    print(len(alist))
    print(alist)







if __name__ == '__main__':
    list_a()
