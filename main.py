from bs4 import BeautifulSoup
import requests
import os
import smtplib

PASSWORD=os.getenv('PASSWORD')
EMAIL=os.getenv('GMAIL')

url='https://www.amazon.com/PlayStation%C2%AE5-Digital-slim-PlayStation-5/dp/B0CL5KNB9M/ref=sr_1_1?dib=eyJ2IjoiMSJ9.cUZfu1B3JuMnfxCTgkdZmFD881cPgFHGjfpeDHmLhnA4LleKDXItOnIXoht_mW3Tvl2z6Rkqkyom_8mndTCM6Q6gfKZqI8LflGYlIQL6a_MtVpv6BmZCxSMWcPKHrjxn6lYQ8OFt3Pi0al98x4jbilQ16IXtTOeYO3uwsUpYr2SJA8ZMctWzlrEkw3RolYv4qAzeoYzDQ2cEqTyB0rZNGQ45x5TY0U0fh_vBTBxpFG8.UIkIHoSuoP5lMvvlGpnRGvwLSFue4OrcFTOkADvvk98&dib_tag=se&keywords=ps5&qid=1712803058&sr=8-1&th=1'
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response=requests.get(url,headers=header)
web=response.text
soup=BeautifulSoup(web,'html.parser')
title=soup.find('span',id='productTitle').text.strip('><')
price_whole = soup.find('span',class_='a-price-whole').text.strip('><')
price_fraction = soup.select_one("span.a-price-fraction").text.strip('><')
price = float(f"{price_whole}{price_fraction}")
# print(price)
# print(title)

target_price=500
print(price<target_price)
if price <target_price:
    message=f'{title} is now${price}'
    with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
        connection.starttls()
        result =connection.login(EMAIL,PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f'Subject:Amazon Price Alert!\n\n{message}\n'.encode('utf-8')
        )
    print('finished')

