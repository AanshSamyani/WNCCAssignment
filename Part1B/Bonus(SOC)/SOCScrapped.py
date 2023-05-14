from pandas import*
import requests
from bs4 import BeautifulSoup

# Setup
url1 = "https://itc.gymkhana.iitb.ac.in/wncc/soc/"
website1 = requests.get(url1)
contents1 = website1.content
soup1 = BeautifulSoup(contents1, 'html.parser')
firstpartoflink = "https://itc.gymkhana.iitb.ac.in"

# ListsRequired
ls4Categories = []
ls4Mentors = []
ls4Mentees = []
ls4Projects = []
ls4Links = []

# Scrapping
Projects = soup1.find_all('div', class_="col-lg-4 col-6 mb-4 shuffle-item")
Links = soup1.find_all('div', class_="rounded hover-wrapper pr-3 pl-3 pt-3 pb-3 bg-white")

for project in Projects:
    project_name = project.text.strip()
    ls4Projects.append(project_name)
    category_name = project['data-groups']
    ls4Categories.append(category_name)

for link in Links:
    secondpartoflink = link['href']
    finallink = firstpartoflink + secondpartoflink
    ls4Links.append(finallink)

for totallink in ls4Links:
    url2 = totallink
    website2 = requests.get(url2)
    contents2 = website2.content
    soup2 = BeautifulSoup(contents2, 'html.parser')
    namesofmentor = []
    numberofmentees = []
    givendata = soup2.find_all('li')
    for data in givendata:
        if (data.p != None):
            writing = data.p.text
            if ord(writing[0]) >= 49 and ord(writing[0]) <= 57:
                numberofmentees.append(writing)
            else:
                namesofmentor.append(writing)

    ls4Mentees.append(numberofmentees)
    if len(namesofmentor) == 1:
        ls4Mentors.append(namesofmentor)
    else:
        ls4Mentors.append(namesofmentor)

# Saving as CSV using pandas
dictionary = {"Category" : ls4Categories, "Name of Project" : ls4Projects, "Mentors" : ls4Mentors, "No. of Mentees" : ls4Mentees, "Links" : ls4Links}
df = DataFrame(dictionary)
df.to_csv('SOC.csv')
