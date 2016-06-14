
import re
import urllib

from BeautifulSoup import *


url = raw_input("Enter the URL here: ")

html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# print(soup.prettify())

d = list()
fin = list()

for each_a in soup.findAll('a',{'class':'product_link'}):

	d.append(each_a.contents[0])


	for item in d:
		item = str(item)

		if re.search('^(VESTIDO|vestido|Vestido)\s.*', item):
			if item not in fin:
				fin.append(item)

print fin 








# http://stackoverflow.com/questions/5041008/handling-class-attribute-in-beautifulsoup




