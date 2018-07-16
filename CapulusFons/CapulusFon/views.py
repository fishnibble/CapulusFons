from django.shortcuts import render
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#testing getting urls here before views implementation since it'll be done in views

# Create your views here.

def bluebottlecoffee(request):
    my_url = 'https://bluebottlecoffee.com/store/coffee'
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class":"dib dib-fix v-top wi-60 wi-100-ns pl20 pl0-ns"})
    names = []
    descs = []
    for item in containers:
        new_url = 'https://bluebottlecoffee.com'
        new_url += item.h2.a['href']
        uClient = uReq(new_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        name = page_soup.find("div", {"class":"f3 f2-ns mt0 lh-reset mb10"})
        
        names.append(name.get_text())
        desc = page_soup.find("div", {"class":"f5 lh-copy mt0 mb30 italic serif-font"})
        
        descs.append(desc.get_text())

    prep_choices = page_soup.findAll("div", {"class":"js-strategy-button spec-strategy-button grid-col compact grid-col-2"})
    choices = []
    for choice in prep_choices:
        choice = choice.label.get_text()
        choices.append(choice)
        chioce_prices = page_soup.findAll("span", {"class":"dib v-top js-variant-price"})
        for price in chioce_prices:
            price = price.get_text()
            print(price)
    
    context ={
        'names': names,
        'descs': descs,
        'choices': choices,
    }

    return render(request, 'CapulusFon/bluebottlecoffee.html', context)



