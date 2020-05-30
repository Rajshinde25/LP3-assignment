#problem number 11
import datetime
year, month, day = map(int,input().split()) 
date1 = datetime.date(year, month, day)
print(date1.isocalendar()[1])