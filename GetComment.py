from bs4 import BeautifulSoup
import requests
# fun for getting the comments
def getComments(URL):
    obj = requests.get(URL)
    soup = BeautifulSoup(obj.text, 'html.parser')
    comments = soup.find_all('p', {"class": "_2xg6Ul"})
    if(len(comments) == 0):
        print("**SORRY**\nThis Product Does'nt Have Any Reviews")
    elif(len(comments)<10):
        print("TOP COMMENTS OF THE PRODUCT :")
        for i in comments:
            print(i.text)
    else:
        print("TOP 10 REVIEWS OF THE PRODUCT :")
        for i in range(0,10):
            print(comments[i].text)

URL = input("Enter The URL Of The Product")
getComments(URL)