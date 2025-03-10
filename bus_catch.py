# import library
import urllib.request
# open the url
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
# read the data
data = u.read()
# print the data
print(data)