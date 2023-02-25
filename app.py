from flask import Flask, render_template, request,jsonify
from bs4 import  BeautifulSoup
import requests
from csv import writer



url = "https://housing.com/in/buy/searches/P679xe73u28050522"
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find_all('div',class_="css-zrd0bv")
with open('housing.csv','w',encoding='utf8',newline='') as f:
    thewriter = writer(f)
    header = ['price_and_EMI','location','sale_location','possesionStatus_and_pricePerSqft']
    thewriter.writerow(header)
    for result in lists:
        price_and_EMI = result.find('div',class_="css-70qvj9").text
        location = result.find('div',class_ ="css-2rx1iy").text
        sale_location = result.find('div',class_ ="css-4in8py").text
        possesionStatus_and_pricePerSqft = result.find('div',class_="css-1ywl03").text
        info = [price_and_EMI,location,sale_location,possesionStatus_and_pricePerSqft]
        thewriter.writerow(info)
        




