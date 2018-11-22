colors=['red', 'blue','green'] //join을 이용해서 글자를 합쳤다
result=''.join(colors)
print(result)

colors=['red', 'blue','green']
result=', '.join(colors)
items = 'zero one two three'.split() //split을 이용해서 글자를 리스트로 나눴다
print(items)

items = 'python, jquery, javascript' //split을 이용해 ,을 기준으로 나눴다
items.split(",")
print(items)


example= 'knu.ac.kr'  //split을 이용해서 unpacking을 했다
a,b,c= example.split(".")
print(a)

result=[i for i in range(10)]// list comprehension을 이용해 리스트를 만들었다
print(result)

result=[i for i in range(10) if i % 2] // filter를 이용한 list comprehension
print(result)

word_1 ="Hello"
word_2 ="world"
result1=[i+j for i in word_1 for j in word_2]//1차원 리스트 생성
print(result1)
result2=[[i+j for i in word_1] for j in word_2] //2차원 리스트 생성
print(result2)


case_1 =["A","B","C"]
case_2 =["D","E","A"]
result=[i+j for i in case_1 for j in case_2 if not(i==j)]//cartasian product 생성
print(result)

words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
for i in stuff:
    print(i)


#enumerate
for i,v in enumerate(['tic','tac','toe']):  //리스트의 있는 index값을 unpacking
    print (i,v)

mylist = ["a","b","c","d"]
list(enumerate(mylist)) //list의 있는 index와 값을 unpacking하여 list로 저장

{i:j for i,j in enumerate('Kyungpook national University eletronic engineering'.split())}
//문장을 list로 만들고 list의 index와 값을 unpacking하여 dict로 저장


#zip
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):
     print (a,b)

[sum(x) for x in zip((1,2,3), (10,20,30), (100,200,300))]


alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for i, (a, b) in enumerate(zip(alist, blist)):
    print (i, a, b)


f = lambda x, y: x + y #lamda함수 이용
print(f(1, 4))

f = lambda x: x ** 2
print(f(3))

print((lambda x: x+1)(5))

list = [2, 3, 4, 5]
f = lambda x: x ** 2
print(list(map(f, list))) #map을 이용해서 하나하나 대입


list(map(lambda x: x ** 2 if x % 2 == 0 else x,list))#filter 이용

[value ** 2 for value in list] #list comprehension으로 똑같은 결과

f = lambda x: x ** 2
print(map(f, ex))
for i in map(f, ex):
    print(i)

# Reduce
from functools import reduce
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))


def factorial(n):
    return reduce(
            lambda x, y: x*y, range(1, n+1))

factorial(5)

#asterisk -인자를 한번에 넘겨줄때 유용
def asterisk_test(a, *args): #tuple형태로 넘어옴
    print(a, args)
    print(type(args))

asterisk_test(1,2,3,4,5,6)

def asterisk_test(a, **kargs): #dict형태로 넘어옴
    print(a, kargs)
    print(type(kargs))

asterisk_test(1, b=2, c=3, d=4, e=5, f=6)


def asterisk_test(a, *args):
    print(a, args)
    print(type(args))


asterisk_test(1, (2, 3, 4, 5, 6)) #(2, 3, 4, 5, 6)은 하나의 변수


def asterisk_test(a, args):
    print(a, *args) #받은 뒤에 unpacking
    print(type(args))

asterisk_test(1, (2,3,4,5,6))

a, b, c = ([1, 2], [3, 4], [5, 6])
print(a, b, c)

data = ([1, 2], [3, 4], [5, 6])  #윗줄과 동일한 결과
print(*data)


for data in zip(*([1, 2], [3, 4], [5, 6])):
    print(sum(data))


def asterisk_test(a, b, c, d, e=0):
    print(a, b, c, d, e)

data = {"d":1 , "c":2, "b":3, "e":56}
asterisk_test(10, **data)

#선형대수를 python으로 표현
u = [2, 2]
v = [2, 3]
z = [3, 5]

result = [t for t in zip(u, v, z)] #list comprehension과 zip로 vector의 합
print (result)


u = [1, 2, 3]
v = [4, 5, 6]
alpha = 2
result = [alpha *sum(t) for t in zip(u, v)] #scalr곱
print(result)

matrix_a = [[3, 6], [4, 5]]
matrix_b = [[5, 8], [6, 7]]
result = [[sum(row) for row in zip(*t)]
          for t in zip(matrix_a, matrix_b)] #matrix의 합

print(result)


matrix_a = [[3, 6], [4, 5]]
alpha = 4
result = [[alpha * element for element in t] for t in matrix_a] #scalr matrix preduct

print(result)


matrix_a = [[1, 2, 3], [4, 5, 6]]
result = [[element for element in t] for t in zip(*matrix_a)] #matrix transpose


matrix_a = [[1, 1, 2], [2, 1, 1]]
matrix_b = [[1, 1], [2, 1], [1, 3]]
result = [[sum(a * b for a, b in zip(row_a, column_b))
          for column_b in zip(*matrix_b)] for row_a in matrix_a]#matrix product
print(result)
