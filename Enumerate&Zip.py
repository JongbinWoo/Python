#enumerate: list의 값들을 추출할때 index num과 같이 추출
for i,v in enumerate(['tic','tac','toe']): #리스트의 있는 index값을 unpacking
    print (i,v)

mylist = ["a","b","c","d"]
list(enumerate(mylist)) #list의 있는 index와 값을 unpacking하여 list로 저장

{i:j for i,j in enumerate('Kyungpook national University eletronic engineering'.split())}
#문장을 split을 이용해 list로 만들고 list의 index와 값을 unpacking하여 dict로 저장


#zip : n개의 list에서 값을 병렬적으로 추출(같은 index끼리)
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):
     print (a,b)

a,b,c = zip((1,2,3),(4,5,6),(7,8,9)) #같은 index끼리 unpacking

[sum(x) for x in zip((1,2,3), (10,20,30), (100,200,300))]

#Enumerate와 zip을 같이 사용
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for i, (a, b) in enumerate(zip(alist, blist)):
    print (i, a, b)
