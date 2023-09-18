from bs4 import  BeautifulSoup
import  time
import re
import requests
import csv
html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup=BeautifulSoup(html_text,'lxml')


jobs=soup.findAll('li',class_="clearfix job-bx wht-shd-bx")
with open('job.csv', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["no","job name","company name","experience required","skills required","job links"])
    for index,job in enumerate(jobs):
        job_name=soup.find('h2').a.text
        job_requirements=job.find('ul',class_="top-jd-dtl clearfix")
        job_experience="".join(re.findall('[0-9-]',job_requirements.li.text))
        job_link=job.find('h2').a['href']
        company_name=job.find('h3',class_="joblist-comp-name").text.replace(" ",'')
        skill_required=job.find('span',class_="srp-skills").text.replace(" ","")
        csv_writer.writerow([index,job_name,company_name,job_experience,skill_required,job_link])







