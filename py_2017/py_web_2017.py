__author__ = 'Hannah Cat'
import urllib.request, urllib.error, urllib.parse

url='http://www.google.com'
x = urllib.request.urlopen(url)
print(x.read())
