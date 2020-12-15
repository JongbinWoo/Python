"""
1. lambda
lambda x: f(x)

def func(x):
  return x+2

func = lambda x: x+2

func(2) // 4
-------------------
def sec2other(unit):
  return lambda sec: sec/unit   #람다를 return(람다함수도 하나의 객체))

sec2min = sec2other(60) #sec2min = lambda x: x/60, treat variable as a function

sec2min(180)

-----------------------
2. map
list1 = ['1', '100', '1000']
list2 = list(map(int, list1))

Iterable의 모든 멤버에 int함수를 적용하고 list로 변환
-map(int, list1) -> map object(Iterator) 

* Iterable객체 - 반복가능한 객체 (ex. list, dict, range, tuple ...)
** Iterator 객체 - 값을 차례대로 꺼낼 수 있는 객체
----------------------

3. lambda + map 
map(func, Iterable) 에서 func의 위치에 lambda를 넣는다.

def square(x):
    return x*x

list(map(square, range(1,5))) 

를 한줄로 표현 가능
list(map(lambda x:x*x, range(1,5)))
"""
