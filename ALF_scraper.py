#import argparse
#import re
#from multiprocessing.pool import ThreadPool as Pool
import requests
import bs4
from lxml import html
 
root_url = 'http://www.assisted-living-directory.com/content/'
index_url = root_url + 'new-jersey.htm'


# I don't use the function get_facility_names. I was playing around with the testing function to see if I could get it right. I can't
def get_facility_names():
    response = requests.get(index_url)
    soup = bs4.BeautifulSoup(response.text)
    mydivs = soup.findAll("div", attrs = { "class" : "detailText" }).string	
    print mydivs

#get_facility_names()

fo = open("ALF_list.txt", "wb")

def testing():
    response = requests.get(index_url)
    soup = bs4.BeautifulSoup(response.text)    
    for i in soup.findAll('div', attrs = {'class' : 'detailText'}):
        for j in i.findAll('p'): 	        	
			facility_info =  j.get_text
			total_facility_info = ""
			total_facility_info += str(facility_info)
			fo.write(total_facility_info)
	print total_facility_info
	    
    fo.close()
    
    return total_facility_info

testing()

# DELETED CODE BELOW
#print soup.get_text()
#review_tag  = {'class':re.compile("detailText")}
#   all_reviews = soup.findAll(attrs=review_tag)
#for pfound in soup.findAll('p'):
#    	print pfound
#mydivs = soup.find("div", attrs = { "class" : "detailText" }).findAll('p')
"""    
#facilities = soup.content('div', class_='detailText')
"""
