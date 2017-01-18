'''
5 Crucial Projects for Beginners - https://www.daniweb.com/programming/software-development/threads/131973/5-crucial-projects-for-beginners

2 - Sentence Generator:

Overview:

A series of different parts of sentences will be randomly 
put together to come up with new interesting sentences.
What you will be Using:
Random, Integers, Print, Strings, Breaks, Functions, For, Range
My Thoughts on Project:
A very fun beginning project, have fun with this... 
Come up with some wacky sentences! 
Also, this project really gets you to experiment with strings, 
piecing them together, randoming from a set of strings, and more.
'''

import random

import urllib.request
from bs4 import BeautifulSoup

url = 'http://www.reddit.com'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)
final_text = ''

for script in soup(['script', 'style']):
    script.extract()  

text = soup.get_text()

lines = (line.strip() for line in text.splitlines())

chunks = (phrase.strip() for line in lines for phrase in line.split('  '))

word_list = [word for word in chunks]

sentence_list = [''.join(random.choice(word_list)) for i in range(random.randint(0, 30))]

capitalized_list = [i.title() for i in sentence_list]

for i in capitalized_list:
  final_text += '{0}.\n'.format(i)

print(final_text)
