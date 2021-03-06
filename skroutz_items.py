from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time

#create save file
filename = "mobile_phones.csv"
f = open(filename,"w")
headers = "title, brand, link, rating"
f.write(headers +"\n")
page=1
for page in range(1, 10):	
	my_url = 'https://www.skroutz.gr/c/40/kinhta-thlefwna.html?from=families&page=' +str(page)

	#opening up connection and get the page
	
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()

	#html parsing
	page_soup = soup(page_html,"html.parser")
	#graps its product

	items = page_soup.findAll("li",{"class":" cf card "})

	#check length so that you have all items
	#print(len(all_items))

	for item in items:
		#get product details
		details = item.find("div",{"class":"details"})
		#print(details)
		title = details.h2.a["title"]
		#print(title)
		link = details.h2.a["href"]
		#fix link
		link = "https://www.skroutz.gr" + link 
		#print(link)
		rating = details.div.a.div.span.text
	    	#print(rating)
		brand = details.h2.a["title"].partition(" ")[0]
		#print(brand)
		print(title)
		print(link)
		print(str(rating))
		print(brand)
		f.write(title + "," +brand + "," +link +","       +rating.replace(",",".") +"\n")

	time.sleep(10)
	print(my_url)
 
f.close()  
