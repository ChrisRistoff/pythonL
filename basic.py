def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(a, b):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(a) == True and b != 2 :
      return f"Month {b} of year {a} has {month_days[b-1]} days in it"
    if not is_leap(a) :
      return f"Month {b} of year {a} has {month_days[b-1]} days in it"
    else : 
      return f"Month {b} of year {a} has 29 days in it"
      
  
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







