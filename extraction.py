import urllib.request
from bs4 import BeautifulSoup

def extract_text_from_html(url):
    text = ""
    req = urllib.request.Request(
        url,
        data=None,
        headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req)
    parser = BeautifulSoup(html, 'html.parser')
    for paragraph in parser.find_all('p'):
        print(paragraph.get_text())
        text += paragraph.get_text()
    return text

url = "https://www.nytimes.com/2018/03/22/us/politics/trump-russia-investigation.html"
text = extract_text_from_html(url)
print(text)
