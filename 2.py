# problem number 2
def is_leap(year):
    leap = False
    if 1900 <= year <= pow(10,5):
        if year % 400 == 0:
            leap = True
        elif year % 100 == 0:
            leap = False
        elif year % 4 == 0:
            leap = True
    return leap


year = int(input())
print(is_leap(year))