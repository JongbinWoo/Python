result = [i for i in range(10)]  # list comprehension을 이용해 리스트를 만들었다
print(result)

# 제어문 이용
list1 = [1, 2, 3, 4]
list2 = [x for x in list1 if x % 2 == 0]
# filter 클래스를 이용해도 같은 결과가능
list2 = filter(lambda x: x % 2 == 0, list1)
result = [i for i in range(10) if i % 2]  # filter를 이용한 list comprehension
print(result)  # 홀수만 출력된다.

word_1 = "Hello"
word_2 = "world"
result1 = [i+j for i in word_1 for j in word_2]  # 1차원 리스트 생성
print(result1)
result2 = [[i+j for i in word_1] for j in word_2]  # 2차원 리스트 생성
print(result2)


case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]
# cartasian product 생성, filter
result = [i+j for i in case_1 for j in case_2 if not(i == j)]
print(result)

words = 'The quick brown fox jumps over the lazy dog'.split()  # split
print(words)
stuff = [[w.upper(), w.lower(), len(w)]
         for w in words]  # 각 단어의 대문자, 소문자, 글자 길이를 하나의 리스트에 넣어준다
for i in stuff:
    print(i)


# 딕셔너리 컴프리핸션
ll = [('a', 1), ('b', 2)]
{x: y*y for x, y in ll}
