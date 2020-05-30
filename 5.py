#problem number 5
s1 = str(input())
output =''
for ch in s1:
    if ch not in output:
        output=output+ch
print(output)