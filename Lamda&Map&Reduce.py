from functools import reduce


def f(x, y): return x + y  # lamda함수 이용
def f2(x): return x ** 2


print((lambda x: x+1)(5))
print(f(1, 4))
print(f2(3))


# map:각 element에 동일하게 function적용
list1 = [2, 3, 4, 5]
print(list(map(f, list1)))  # map을 이용해서 하나하나 대입
list(map(lambda x: x ** 2 if x % 2 == 0 else x, list1))  # filter 이용
[value ** 2 for value in list1]  # list comprehension으로 똑같은 결과

# Reduce : list에 똑같은 함수를 적용하여 통합
# reduce(집계함수, iterable, 초기값)
print(reduce(lambda acc, cur: acc+cur, [1, 2, 3, 4, 5], 0))


def factorial(n):
    return reduce(
        lambda x, y: x*y, range(1, n+1))


factorial(5)
