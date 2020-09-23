import urllib.request
urllib.request.urlretrieve('https://s3.amazonaws.com/tcmg476/http_access_log','serverlogs.txt')
from collections import Counter

file = open("serverlogs.txt", "r")
total_requests = 0

request = "GET"
January = "/Jan/"
February = "/Feb/"
March = "/Mar/"
April = "/Apr/"
May = "/May/"
June = "/Jun/"
July = "/Jul/"
August = "/Aug/"
September = "/Sep/"
October = "/Oct/"
November = "/Nov/"
December = "/Dec/"

total_files = []
requests = []
status_400 = 0
status_300 = 0

for aline in file:
    words = aline.strip()
    line = aline.split()


    if request in words:
        total_requests += 1

    jan = open("jan.txt", "a+")
    if January in line:
        jan.write(line)
        jan.write("\n")
        
    feb = open("feb.txt", "a+")
    if February in line:
        feb.write(line)
        feb.write("\n")

    mar = open("mar.txt", "a+")
    if March in line:
        mar.write(line)
        mar.write("\n")

    apr = open("apr.txt", "a+")
    if April in line:
        apr.write(line)
        apr.write("\n")

    may = open("may.txt", "a+")
    if May in line:
        may.write(line)
        may.write("\n")

    jun = open("jun.txt", "a+")
    if June in line:
        jun.write(line)
        jun.write("\n")

    jul = open("jul.txt", "a+")
    if July in line:
        jul.write(line)
        jul.write("\n")

    aug = open("aug.txt", "a+")
    if August in line:
        aug.write(line)
        aug.write("\n")

    sep = open("sep.txt", "a+")
    if September in line:
        sep.write(line)
        sep.write("\n")

    oct = open("oct.txt", "a+")
    if October in line:
        oct.write(line)
        oct.write("\n")

    nov = open("nov.txt", "a+")
    if November in line:
        nov.write(line)
        nov.write("\n")

    dec = open("dec.txt", "a+")
    if December in line:
        dec.write(line)
        dec.write("\n")
        
    x = len(line)
    if x == 10:
        value = line[x-2]
        value = int(value)
        request_file = line[6]
        if value >= 400 and value <= 499:
            status_400 +=1
        if value >= 300 and value <= 399:
            status_300 +=1
        total_files.append(request_file)

mostcommon = Counter(total_files)
mostcommon = mostcommon.most_common(1)[0][0]

leastcommon = Counter(total_files)
leastcommon = min(leastcommon, key = leastcommon.get)
            
file.close()

day_average = total_requests/365
week_average = total_requests/52
month_average = total_requests/12

percentage_notsuccessful = (status_400/total_requests)*100
percentage_successful = (status_300/total_requests)*100

print("The average amount of requests made each day is", day_average)
print("The average amount of requests made each week is", week_average)
print("The average amount of requests made each month is", month_average)
print(percentage_notsuccessful, "percent of the requests were not successful.")
print(percentage_successful, "percent of the requests were successful.")
print("The most requested file is", mostcommon)
print("The least requested file is", leastcommon)
