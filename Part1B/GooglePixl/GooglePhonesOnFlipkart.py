import requests
from bs4 import BeautifulSoup
from pandas import*

Names = []
Camera = []
RAM = []
Size = []
Battery = []
Warrant = []
Processor = []

url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&param=7564&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&fm=neo%2Fmerchandising&iid=M_b49965b5-ad80-4493-88b1-7a1828555879_3.Q1PDG4YW86MF&ppt=hp&ppn=homepage&ssid=paxle4idvk0000001669033731730&p%5B%5D=facets.brand%255B%255D%3DGoogle&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkdPT0dMRSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D&otracker=clp_metro_expandable_3_5.metroExpandable.METRO_EXPANDABLE_GOOGLE_mobile-phones-store_0TAYGN3KGJ9F_wp2&fm=neo%2Fmerchandising&iid=M_3eb7a5cd-2b73-4de1-8d21-92e9a0d56574_5.0TAYGN3KGJ9F&ppt=hp&ppn=homepage&ssid=gpvr1u0vls0000001684076910568"
website = requests.get(url)
contents = website.content
soup = BeautifulSoup(contents, 'html.parser')

names = soup.find_all('div',class_="_4rR01T")
for name in names:
    Names.append(name.text)

otherinfo = soup.find_all('li', class_="rgWa7D")
for index,oi in enumerate(otherinfo):
    if index % 6 == 0 :
        RAM.append(oi.text)
    if index % 6 == 1 :
        Size.append(oi.text)
    if index % 6 == 2 :
        Camera.append(oi.text)
    if index % 6 == 3 :
        Battery.append(oi.text)
    if index % 6 == 4 :
        Processor.append(oi.text)
    if index % 6 == 5 :
        Warrant.append(oi.text)

dictionary1 = {"Name" : Names, "CameraQuality" : Camera,"Processor" : Processor, "Size" : Size,"BatteryLife" : Battery,"Warranty" : Warrant}
df = DataFrame(dictionary1)
df.to_csv('GooglePixl.csv')

