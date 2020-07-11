import os
import requests
import smtplib
from bs4 import BeautifulSoup

def alert_me(product_url,title, price):
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('venumalladi18@gmail.com','SastryVani@18')
	subject = 'Price fell down for ' + title
	body = 'Buy now at : '+ product_url

	msg = f"Subject:{subject}\n\n{body}"

	server.sendmail('venumalladi18@gmail.com','venumalladi18@gmail.com',msg)
	print("Email alert sent")
	server.quit()


def check_price(product_url,threshold_amt):
	headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"}
	price = our_price = deal_price = Title = ''

	r = requests.get(product_url,headers=headers)
	soup = BeautifulSoup(r.text, "html.parser")

	titles = soup.select('#productTitle')
	for title in titles:
			title_text = title.get_text(strip=True)
			Title = Title + title_text

	deal_prices = soup.select('#priceblock_dealprice')
	for i in deal_prices:
			i_text = i.get_text(strip=True)
			deal_price = deal_price + i_text

	our_prices = soup.select('#priceblock_ourprice')
	for i in our_prices:
			i_text = i.get_text(strip=True)
			our_price = our_price + i_text

	price = deal_price if deal_price else our_price

	print("\nTitle of the product is : {}".format(Title))
	print("Price of the product is : {}".format(price))

	Price = price[2:].replace(',','')

	if(float(Price)<=threshold_amt):
			alert_me(product_url,Title, Price)

if __name__=="__main__":
	product_url = input("Enter the url of the product: ")
	threshold_amt = float(input("Enter the threshold price of the product: "))
	check_price(product_url,threshold_amt)
