from bs4 import  BeautifulSoup as bs
import requests
from urllib.request import urlopen as uReq



searchString ="iphone"
try:

    ebay_url = "https://www.ebay.com/"+searchString
    uClient = uReq(ebay_url)
    ebayPage = uClient.read()
except HTTPError as e:
    print('e')
except URLError as e:
   print('The Server could not be found')


try:
     ebay_html = bs(ebayPage,'html.parser')
     badContent = ebay_html.find("nonExistingTag") # ebay product landing page
except AttributeError as e:
     print('Tag was not found')


review_items=ebay_html.find("div",class_="s-item__reviews")

reviews=[]
reviews_page=uReq(review_items.a['href']) # user-reviews link
reviews_html=bs(reviews_page.read(),"html.parser")
try:
    all_reviews=reviews_html.find('div',class_="see--all--reviews")
except Exception as e:
    print(e)
all_reviews_page=uReq(all_reviews.a["href"])
all_reviews_html=bs(all_reviews_page.read(),'html.parser')
reviews_count=0
all_user_reviews=all_reviews_html.find_all('div',class_='ebay-review-section')

for review in all_user_reviews:
        reviews_rating=review.find('div',class_="ebay-star-rating")
        rating=reviews_rating.span["aria-label"]
        author=review.find('div',class_="ebay-review-section-l").a['title']
        body=review.find('div',class_='ebay-review-section-r')
        title=body.h3.text
        body_text=body.p.text
        mydict={'Product':'iphone','Author': author, 'Rating':rating,'Title':title,'Comment':body_text}
        reviews_count=reviews_count+1
        reviews.append(mydict)
        print(reviews)

