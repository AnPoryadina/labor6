__author__ = 'student'
import random
def f(x):
    if x<-2 or x>2:
        y=0
    else:
        y=-x**2+4
    return y
m=int(input())
values=[random.random()*6-3 for i in range (m)]
res=[f(x) for x in values]
result=(6/m)*sum(res)
print(result)