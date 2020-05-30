#problem number 4
a,b= map(int,input().split())
count = 0 
for i in range(1, min(a, b)+1):
    if a%i==b%i==0:
        count+=1
print(count)
