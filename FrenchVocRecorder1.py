import urllib3
from bs4 import BeautifulSoup
import csv

http = urllib3.PoolManager()
DictFile = open("FrenDict.csv","a")
DictWriter = csv.writer(DictFile)
StartText = """
To quit, press enter 'q'
To change language, enter 'change'

Look up:
"""

lang = 'FE'

while True:
    word = input(StartText)
    if word == 'q':
        break

    if word == 'change':
        lang = input('EF or FE?')
        pass

    else:    
        if lang == 'EF':
            r = http.request("GET",
                             ("http://www.larousse.com/en/dictionaries/english-french/"
                              + word)
                             )
            if r.status != 200:
                print(r.status)
                break
                    
            soup = BeautifulSoup(r.data)
            if 'Translation' not in soup.title.text:
                if soup.find('section', {'class' : 'corrector'}) == None:
                             print('check spelling')
                else:
                             print(soup.find('section', {'class' : 'corrector'}).text)
            else:
                article = soup.find('div', {"class" : "article_bilingue"})
                try:
                    Entry1 = article.h1.text
                    Translat_Set = article.find_all('table')

                    print(Entry1)
                    for item in Translat_Set:
                        defin = item.text
                        print(defin)
                        DictWriter.writerow(['en', Entry1, item])
                except:
                    print('you done fucked up mate-- see the try block')
        elif lang == 'FE':
            r = http.request("GET",
                             ("http://www.larousse.com/en/dictionaries/french-english/"
                              + word))
            if r.status != 200:
                print(r.status)
                break
                    
            soup = BeautifulSoup(r.data)
            if 'Translation' not in soup.title.text:
                if soup.find('section', {'class' : 'corrector'}) == None:
                             print('check spelling')
                else:
                             print(soup.find('section', {'class' : 'corrector'}).text)
            else:
                article = soup.find('div', {"class" : "article_bilingue"})
                try:
                    Entry1 = article.h1.text
                    Translat_Set = article.find_all('div')

                    print(Entry1)
                    for item in Translat_Set:
                        defin = item.text
                        print(defin)
                        DictWriter.writerow(['fr', Entry1, defin])
                        
                except:
                    print('you done fucked up mate-- see the try block')
                #ZoneEntree = soup.find('div', {"class" : "ZoneEntree"}).text
        else:
            print('lang not fe or ef')

DictFile.close()



### notes on fr dict layout

##"ZoneGram"
##article.find_all('div',{"class":"ZoneGram"})

                         
                         
