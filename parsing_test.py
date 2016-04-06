'''from selenium import webdriver

#Class which accesses user's Quora page to find its source - navigation is handled by Selenium
#Returns string with source formatting
		#Launch Firefox Driver
driver = webdriver.Firefox()
print ("Launching User's Quora Page")

		#Acess webpage and scroll down to generate most recent content
driver.get('https://www.quora.com/Donald-Trump-2016-Presidential-Campaign-Who-is-Donald-Trumps-base-Why-is-he-popular-Why-are-people-voting-for-him')
print ("Populating page by scrolling down")


driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

print ("done")
		#Get page source code
html_source = driver.page_source
print (html_source)
html_source = html_source.encode("ascii","ignore")
print (html_source)
driver.close()'''


import bs4
import urllib
import time
from urllib.request import urlopen
#url = html_source
url_list = []
#empty url list to append later

#url = 'https://www.quora.com/Is-Donald-Trump-a-political-conservative'
url = 'https://www.quora.com/Why-is-Donald-Trump-running-for-president'

html = urlopen(url)
bsobj = bs4.BeautifulSoup(html, "lxml")


#find title of the question
title = bsobj.find('title')
title_discrip = bsobj.find('div', 'question_details_text inline_editor_content')

print (title.get_text())
print (title_discrip.get_text())
print ()
#print (bsobj.prettify())


# find all links in the page
question_links = bsobj.find_all('a', 'question_link')

#print the total answers
total_answer_count = bsobj.find_all('div', 'answer_count')
for answer_count in total_answer_count:
  print (answer_count.get_text())

print()

#print the top five answers, the author/views/text
answers = bsobj.find_all('div', 'Answer AnswerBase')
for answer in answers:
    #print (answers)
  user = answer.find('a', 'user')
  view = answer.find('span', 'meta_num')
  answer_text =  answer.find('div', 'ExpandedQText ExpandedAnswer')
  if user is not None:
    print (user.get_text())
  else:
    print ('None')
  print (view.get_text())
  print (answer_text.get_text())
  print ('------')

#Find links of 'related questions'
#append each link to the list for later use
for question in question_links:
  temp_url = question.get('href')
  url = "https://www.quora.com" + temp_url
  if url not in url_list:
    url_list.append(url)
#print (url_list)

#lets it rest 3 seconds
time.sleep(3)
