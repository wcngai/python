#!/usr/bin/env python
"""
Provides some arithmetic functions
"""
import urllib
from bs4 import BeautifulSoup

# make a function to extract text from an url and save it to a file
def extract_text_from_html_and_save(url, filename):
    """
    Provides some arithmetic functions
    """
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
    with open(filename, 'w') as f:
        f.write(text)
    return text



aurl = "https://support.apple.com/en-us/HT212780"
atext = extract_text_from_html_and_save(aurl, "nytimes.txt")
print(atext)

# write a function using hugging face to summarize the text
from transformers import pipeline

def summarize_text(text):
    """
    Provides some arithmetic functions
    """
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary

