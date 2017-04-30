import requests
from bs4 import BeautifulSoup
import re

url ="https://www.youtube.com/results?search_query=pitbull"
url_link = "https://www.youtube.com"
request = requests.get(url)
content = request.content
soup = BeautifulSoup(content,"html.parser")

for element in soup.find_all('a', {"rel": "spf-prefetch"}):
#    print (element)
    #video_title = element.get('title')
    link = element.get('href').split('=')[1]
    #print(link)
    #link = url_link+link
    #print("the title is \"{0}\" and the link is \"{1}\"".format(video_title,link))
    images = soup.find_all('img',{'alt':True,'onload' : True,'src' : True,'width' : True, 'height' : True,'data-ytimg':True})
    image = str(re.findall('https://i.ytimg.com/vi/{}/[\S]+'.format(link),str(images))).strip('[\']')
    image = image.replace("&amp;","&")
    #print(image)
for music_length in soup.find_all('span',{'class' : 'video-time'}):
    #print (music_length.text)
    pass
#get page
page_list = {}
for page in soup.find_all('a',{'class':True,'data-sessionlink':True,'aria-label':True,'data-visibility-tracking':True}):
    #print(page.text)
    #print(page.get('href'))
    page_list['{}'.format(page.text)] = page.get('href')

print(page_list)