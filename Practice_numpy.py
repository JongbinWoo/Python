import numpy as np
#array 생성후 shape,reshape,flatten 활용해 shape을 바꿔봤다.
a1= [[1,2,3,4],[5,6,7,8]]
np.array(a1).shape
np.array(a1).reshape(2,2,2)

a2=np.array(a1).reshape(8,)
print(a2)

a3=np.array(a2).reshape(-1,1)
print(a3)

np.array(a1).flatten() #일차원으로 쭉 펴준다

#indexing slicing
example=np.array([[1,2,3],[4,5,6.5]],int)
example[0][1]
example[0,1]  #윗줄과 같은 결과

example[0,2]=12
example

test_example = np.array([[1, 2, 5,8], [1, 2, 5,8],[1, 2, 5,8],[1, 2, 5,8]], int)
test_example[:2,:]
test_example[:, 1:3]

#creation function
b=np.arange(30).reshape(-1,6)  #arange와 reshape을 이용해 matrix를 만들었다

np.zeros((3,3))
np.zeros(shape=(10,),dtype=np.int8)

np.ones((3,3))

np.ones_like(b)#someting like를 이용해 b와 같은 모양의 1로만 이루어진 matrix를 생성

np.identity(n=5, dtype=np.int8)#단위행렬 생성

np.eye(N=5 ,M=3, dtype=np.int8)

#operating functions
b.sum(dtype=np.float)

b.sum(axis=0)
b.sum(axis=1)

a = np.array([[1, 2, 3]])
b = np.array([[2, 3, 4]])
np.concatenate( (a,b) ,axis=0)


a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
np.concatenate( (a,b.T) ,axis=1)

#operation
matrix_1=np.arange(1,13).reshape(3,4) #shape이 같을때
matrix_1 * matrix_1
matrix_1 + matrix_1

matrix_2=np.arange(0,12).reshape(4,3)# dot product
matrix_1.dot(matrix_2)

matrix_2.transpose() #transpose
matrix_2.T

matrix_3 =np.array([[1,2,3],[4,5,6]]) #broadcasting
scalar=3
matrix_3 + scalar
matrix_3 * scalar

test_matrix = np.arange(1,13).reshape(4,3)
test_vector = np.arange(10,40,10)
test_matrix+ test_vector

#comparsion

c = np.arange(10)
c<5 #리스트안에 값에 각각 적용
np.any(c>5)
np.all(c>5)

np.where(c>4,1,2)
np.where(c>4) #조건에 맞는 index값을 반환한다

d=np.arange(40).reshape(-1,8)
np.argmax(d), np.argmin(d)
np.argmax(d,axis=0)  #index값 나옴

e = np.array([1,4,2,5,6,3,9],float)
condition = e>3
e[condition] #위줄과는 다르게 값을 반환한다
