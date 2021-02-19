import urllib.request
url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
urllib.request.urlretrieve(url,'./http_access_log.txt')

file = open("http_access_log.txt")
data = file.read()
pastyear = data.count('1994')

print ("This is the total requests made in the last year: ",pastyear)