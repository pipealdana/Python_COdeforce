def is_leap(year)->bool:
    if year%4==0 and year%400==0:
        return True
    else:
        return False
        


year = int(input())
print(is_leap(year))