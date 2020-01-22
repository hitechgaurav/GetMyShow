import requests
import time
import re
from bs4 import BeautifulSoup
city=input("\nEnter your city: ")
link="https://in.bookmyshow.com/"+city+"/movies"
input=requests.get(link)
page=input.content
#print(page)
soup=BeautifulSoup(page)
x = str(soup.find_all('div',{'class':'card-title'}))
content = str(re.sub("<.*?>","",x))
print("\nMovie in your city",city,"is: ")
time.sleep(5)
print(content)
time.sleep(3)
print("\nThank you for using product developed by ::GAURAV KUMAR::")
time.sleep(10000)
