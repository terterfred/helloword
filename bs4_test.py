import bs4
import urllib

html = open("test.htm")
soup = bs4.BeautifulSoup(html)

print (soup)
