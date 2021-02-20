import urllib.request
url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
urllib.request.urlretrieve(url,'./http_access_log.txt')

file = open("http_access_log.txt")
data = file.read()
pastyear = data.count('1994')
all = data.count("1995")
total = pastyear + all

print ("This is the total requests made in the last year: ",pastyear)

answer = input ("This program will show the number of requests from a web server. Would you like to see them? (yes or no) ")
if answer == "yes":
    answer = input("Do you want the number of requests in the past year (past) or total number of requests (total)? ")
    if answer == "past":  
            print ("There have been " + str(pastyear) + " requests in the past year")
    elif answer == "total":
            print ("There have been " + str(total) + " requests in total")
elif answer == "no":
    print ("Thank you for your time")                  