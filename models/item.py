import requests
from bs4 import BeautifulSoup
import re
import urllib
import youtube_dl


def find_search_content(search):
    url = "https://www.youtube.com/results?search_query="+urllib.parse.quote_plus(search)

    request = requests.get(url)
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    return soup

def find_vedeo(soup,i=1):
    url_link = "https://www.youtube.com/watch?v="
    all_item = {}
    for element in soup.find_all('a', {"rel": "spf-prefetch"}):
        video_title = element.get('title')
        link = element.get('href').split('=')[1]
      #  print(link)
        images = soup.find_all('img', {'alt': True, 'onload': True, 'src': True, 'width': True, 'height': True,'data-ytimg': True})
        image = str(re.findall('https://i.ytimg.com/vi/{}/[\S]+'.format(link), str(images))).strip('[\']')
     #   print(image)
        video_image = image.replace("&amp;", "&")
        video_image= video_image[:-1]

        link = url_link+link
        all_item['{}'.format(i)] = {'title':video_title,'link':link,'image':video_image}
        i = i+1
    return all_item

def video_time(soup,all_item,i=1):
    for music_length in soup.find_all('span', {'class': 'video-time'}):
        all_item.get('{}'.format(i))['time'] = music_length.text
        i = i+1
    return all_item

def every_video(soup):
    #all_item = {}
    all_item = find_vedeo(soup, i=1)
    video_time(soup, all_item, i=1)
    return all_item

def page_bar(soup):
    page_list = {}
    for page in soup.find_all('a', {'class': True, 'data-sessionlink': True, 'aria-label': True,
                                    'data-visibility-tracking': True}):
        # print(page.text)
        # print(page.get('href'))
        page_list['{}'.format(page.text)] = page.get('href')
    return page_list

def download_mp3(url):
    print('the mp3 url is {}'.format(url))
    # ydl_ops = {'outtmpl': '/video/%(title)s.%(ext)s'}
    ydl_ops = {'format': 'bestaudio/best',
               'postprocessors': [{
                   'key': 'FFmpegExtractAudio',
                   'preferredcodec': 'mp3',
                   'preferredquality': '192',
               }]}
    with youtube_dl.YoutubeDL(ydl_ops) as ydl:
        ydl.download([url])

def download_mp4(url):
    print('the mp4 url is {}'.format(url))
    ydl_ops = {'format': 'best'}
    with youtube_dl.YoutubeDL(ydl_ops) as ydl:
        ydl.download([url])




