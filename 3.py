# problem number 3
import numpy as np
n = int(input())
l1 = []
for _ in range(n):
    s1 = str(input())
    l1.append(s1)

def unique(l1):
    unique_list = []
    for x in l1:
        if x not in unique_list:
            unique_list.append(x)
    cnt = len(unique_list)
    print(cnt)
    

def comp1(l1):
    for i in range(n-1):
        print(l1.count(l1[i]),end =" ");
            
unique(l1)
comp1(l1)