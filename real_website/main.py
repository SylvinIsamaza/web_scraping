from bs4 import  BeautifulSoup
import  time
import re
import requests
html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup=BeautifulSoup(html_text,'lxml')


job=soup.find('li',class_="clearfix job-bx wht-shd-bx")
# for job in jobs:

job_name=soup.find('h2').a.text
job_requirements=job.find('ul',class_="top-jd-dtl clearfix")
job_experience="".join(re.findall('[0-9-]',job_requirements.li.text))
job_link=job.find('h2').a['href']
print(job_link)
company_name=job.find('h3',class_="joblist-comp-name").text.replace(" ",'')
skill_required=job.find('span',class_="srp-skills").text.replace(" ","")


