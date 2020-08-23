import requests
from html.parser import HTMLParser

username = input("Enter a username: ")

r = requests.get('https://www.instagram.com/' + username + '/')
page_Source = r.text

followerCount = []

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        pass
    def handle_endtag(self, tag):
        pass
    def handle_data(self, data):
        list1 = data.split('"')
        if 'edge_followed_by' in list1:
            followerCount.append(list1[list1.index('edge_followed_by') + 3])

clean_Source = page_Source.replace("\n", "").replace('}','').replace(':','').replace(',','')
parser = MyHTMLParser()
parser.feed(clean_Source)
print(int(followerCount[0]))
