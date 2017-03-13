# strategy -
#count all the days - approximately 100 * 365.25 - not too large.
#keep track of the month to add correctly
#devide the day by %7 - if no rest, sunday if you counted correctly
#count the numbers of sundays

#months = {"jan": 31, "feb": 28, "mar":31, "apr":30, "may":31, "jun":30, 
#          "jul": 31, "aug": 31, "sep":30, "oct":31, "nov":30, "dec":31}

daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
monthchar = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
dayschar = ["sun", "mon", "tue", "wed", "thu", "fri", "sat", "sun"]
days = 1 #1.1.1900 was a Monday -count Mon=1 Sun = 7
sundays = 0
for year in range(1900,2001):
    #print("year ", year)
    for mon in range(len(daysInMonth)):
        print("year", year, "mon ", monthchar[mon], "firstDay ", dayschar[days%7])
        if (days%7 == 0 and year > 1900):
            sundays += 1
        days += daysInMonth[mon] # next first of month
        if mon == 1:
           if year%4 ==0:
               if year%100 != 0:
                      if year % 400 != 0:
                       days +=1
                       print("Schaltjahr - add 1")
#        print(mon, daysInMonth[mon], days, sundays)
        
        #print(mon, months[mon])
    #days += 365
    #if (i%4 == 0 ):
    #    days+1
    #    if (i%400 == 0):
    #        print(i)
    #        days += 1
print(sundays)
    
    