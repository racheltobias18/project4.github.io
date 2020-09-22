import urllib.request
urllib.request.urlretrieve('https://s3.amazonaws.com/tcmg476/http_access_log','serverlogs.txt')

file = open("serverlogs.txt", "r")
last_year = 0
total_requests = 0

request = "GET"
new_year = "remote - - [01/Jan/1995:00:31:54 -0700]"
January = "/Jan/"


i=0
for aline in file:
    line = aline.strip()
    words = line.split()
    #print(line)
    #print(words[3])

    if request in line:
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
        
file.close()        
