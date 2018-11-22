f = lambda x, y: x + y #lamda함수 이용
print(f(1, 4))

f = lambda x: x ** 2
print(f(3))

print((lambda x: x+1)(5))

#map:각 element에 동일하게 function적용
list = [2, 3, 4, 5]
f = lambda x: x ** 2
print(list(map(f, list))) #map을 이용해서 하나하나 대입


list(map(lambda x: x ** 2 if x % 2 == 0 else x,list))#filter 이용

[value ** 2 for value in list] #list comprehension으로 똑같은 결과

f = lambda x: x ** 2
print(map(f, ex))
for i in map(f, ex):
    print(i)

# Reduce : list에 똑같은 함수를 적용하여 통합
from functools import reduce
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))


def factorial(n):
    return reduce(
            lambda x, y: x*y, range(1, n+1))

factorial(5)
