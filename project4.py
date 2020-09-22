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
        
file.close()        
