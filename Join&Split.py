from functools import reduce
colors = ['red', 'blue', 'green']  # join을 이용해서 글자를 합쳤다
result = ''.join(colors)
print(result)

colors = ['red', 'blue', 'green']
result = ', '.join(colors)
items = 'zero one two three'.split()  # split을 이용해서 글자를 리스트로 나눴다
print(items)

items = 'python, jquery, javascript'  # split을 이용해 ,을 기준으로 나눴다
items.split(",")
print(items)


example = 'knu.ac.kr'  # split을 이용해서 unpacking을 했다
a, b, c = example.split(".")
print(a)
