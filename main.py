from bs4 import BeautifulSoup

with open('./basic/base.html','r') as html_file:
    content=html_file.read()


    soup=BeautifulSoup(content,"lxml")
    # print((soup.prettify()))
    # find is used to find for one element in the html
    # while findAll is used to find all elements that are specified
    # tags=soup.findAll('h5')
    # for tag in tags:
    #     print(tag.text)
    #     # element.text is used to correct the text content of tag

    #  this is how we find for certain element using class
    divisions=soup.findAll('div',class_="card")
    for div in divisions:

        course_name=div.h5.text
        course_price=div.a.text.split[-1]
