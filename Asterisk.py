# asterisk -tuple, dict 자료형에 있는 자료를 unpacking, 인자를 한번에 넘겨줄때 유용

def asterisk_test(a, *args):  # tuple형태로 넘어옴
    print(a, args)
    print(type(args))


asterisk_test(1, 2, 3, 4, 5, 6)


def asterisk_test2(a, *args):
    print(a, args)
    print(type(args))


asterisk_test2(1, (2, 3, 4, 5, 6))  # (2, 3, 4, 5, 6)은 하나의 변수


def asterisk_test1(a, **kargs):  # dict형태로 넘어옴
    print(a, kargs)
    print(type(kargs))


# 키워드 인자는 패킹한 인자들(b=2, c=3, d=4, e=5, f=6)을 키워드와 인자 쌍으로 이루어진 딕셔너리로 관리
asterisk_test1(1, b=2, c=3, d=4, e=5, f=6)


############# unpacking ##########
def asterisk_test3(a, args):
    print(a, *args)  # 받은 뒤에 unpacking
    print(type(args))


asterisk_test3(1, (2, 3, 4, 5, 6))

a, b, c = ([1, 2], [3, 4], [5, 6])
print(a, b, c)

data = ([1, 2], [3, 4], [5, 6])  # 윗줄과 동일한 결과
print(*data)  # data를 unpacking해준다


for data in zip(*([1, 2], [3, 4], [5, 6])):
    print(sum(data))


def asterisk_test4(a, b, c, d, e=0):
    print(a, b, c, d, e)


data = {"d": 1, "c": 2, "b": 3, "e": 56}
asterisk_test4(10, **data)
