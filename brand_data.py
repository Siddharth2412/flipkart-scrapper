from bs4 import BeautifulSoup
from tkinter import messagebox
import requests
import datetime
import csv

def get_txt(data):
    return data.getText()

def get_brand_data(param: str):
    """
    get_brand_data => funstion withh get data and using parameter and creates a csv file with fetched data
    param: str => thisis the string whose perameters are passed
    """
    param = param.lower()
    url = 'https://www.flipkart.com/search?q=' + param +'&augment=false'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html5lib')

    div_data = soup.find('div', class_='_2MImiq')
    span_data = div_data.span.getText()
    limit = int(''.join(str(span_data.split()[-1]).split(',')))
    all_title, all_links, all_price, all_ratings, all_ratings_per = ['Title'], ['link'], ['Price'], ['Ratings and Revies'], ['Rating Out of 5']
    all_block = []
    if int(limit) > 100:
        limit = 20

    for i in range(1, int(limit) + 1):
        url = 'https://www.flipkart.com/search?q=' + param + '&augment=false&page=' + str(i)
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html5lib')

        whole_block = soup.find_all('div', class_='_4ddWXP')
        if len(whole_block) == 0:
            whole_block = soup.find_all('div', class_='_13oc-S')
        all_block.extend(whole_block)

    for block in all_block:
        link_temp = block.find('a', class_='_2rpwqI')
        if link_temp == None:
            link_temp = block.find('a', class_='_1fQZEK')
        all_links.append('https://www.flipkart.com' + link_temp.get('href'))

        title_temp = block.find('a', class_='s1Q9rs')
        if title_temp != None:
            title_temp = title_temp['title']
        else:
            title_temp = get_txt(block.find('div', class_='_4rR01T'))
        all_title.append(title_temp)

        price_temp = block.find('div', class_='_30jeq3')
        if price_temp == None:
            price_temp = block.find('div', class_='_30jeq3 _1_WHN1')
        all_price.append(get_txt(price_temp)[1:])

        rating_temp = block.find('div', class_='_2_R_DZ')
        if rating_temp == None:
            rating_temp = '-'
        else:
            rating_temp = get_text(rating_temp)
        all_ratings.append(rating_temp)

        rating_per_temp = block.find('div', class_='_3LWZlK')
        if rating_per_temp == None:
            rating_per_temp = '-'
        else:
            rating_per_temp = get_txt(rating_per_temp)
        all_ratings_per.append(rating_per_temp)

    data_temp = [all_title, all_price, all_ratings, all_ratings_per, all_links]
    date = datetime.datetime.now()
    data = list(map(list, zip(*data_temp)))
    filename = param.upper()+' '+str(date.strftime("%m-%d-%Y"))+'.csv'
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(data)
    messagebox.showinfo("Success", "Data import succesful")
