import urllib.request
from bs4 import  BeautifulSoup
import pandas as pd

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = urllib.request.urlopen(wiki)
soup = BeautifulSoup(page,"lxml")
#This will print all the content of the website
print(soup.prettify())
#This will print the title
print(soup.title.string)
#This is for extracting all the links
alllinks = soup.findAll('a')
print("list of all links")
for i in alllinks:
    print(i.get('href'))
allheadings=soup.findAll('h2')
print("All the heading which are h2")
for i in allheadings:
    print(i.text)
all_tables=soup.find_all('table')
print("This is the list of all tables")
for i in all_tables:
    print(i.text)
right_table=soup.find('table', class_='wikitable sortable plainrowheaders')
print(right_table)
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
print(df)
