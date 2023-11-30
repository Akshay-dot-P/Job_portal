from bs4 import BeautifulSoup
import requests

def jobs4u(request):
    url = "https://offcampusjobs4u.com/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    a_tags = soup.find_all('a', class_='td-image-wrap')
    # Find all <time> tags with class "entry-date updated td-module-date"
    date_tags = soup.find_all('time', class_='entry-date updated td-module-date')

    # Iterate over corresponding <a> tags and <time> tags using zip
    for a_tag, date_tag in zip(a_tags, date_tags):
        title = a_tag.get('title')
        link = a_tag.get('href')
        split_title = title.split('|')
        info = split_title[0].strip() if len(split_title) > 1 else title
        additional_info3 = ""
        additional_info = split_title[1].strip() if len(split_title) >1 else additional_info3
        location = split_title[2].strip() if len(split_title) >2 else additional_info3
    
        # Find the index of the word 'for'
        index_of_for = additional_info.lower().find('for')

        # Extract the two words after 'for'
        designation = additional_info[index_of_for + 4:].split()[:1]
        desig = str(designation)
        date= date_tag.get_text(strip=True)
        desig_full = additional_info + desig.replace("[", ",").replace("]", ".")
        result_string = desig_full.replace(',', '').replace("'", '')
       

        
        if additional_info and location !='':
            if location in {'B.E/B.Tech/M.Sc/MCA','B.E/B.Tech/MCA' ,'B.Tech/MCA', 'MCA', 'Mca'} :
                result_string = print(f"Title: {info},\n Degree/ batch: {result_string + location},\n Date Text: {date_text}\n Link: {link}\n")
            else:    

                result_string = print(f"Title: {info},\n Degree/ batch: {result_string},\n location: {location},\n Date Text: {date_text}\n Link: {link}\n")
        else:
            result_string = print(f"Title: {info},\n Date Text: {date}\n  Link: {link}\n")
            
    return result_string
jobs4u(request=None)    



#from naukri_Jobs_Scraper import *

# Assuming naukri is a module or class with a job_scraper function

def naukri():
    response = naukri.job_scraper(location="indore", skills="SEO Executive")

# Corrected function call


def fresherhunt(request):
    url = "https://freshershunt.in/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    mains = soup.find_all('div', class_="inside-article")
    a_tags =soup.find_all('time', class_="entry-date published")
    h2_tags = soup.find_all('h2', class_='entry-title')
    
    # Extract and print the link and title for each entry

    for h2_tag, a_tage in zip(h2_tags, a_tags):
        a_tag = h2_tag.find('a')
        date = a_tage.text
        if a_tag and a_tages:
            link = a_tag.get('href')
            title = a_tag.text
            print(f"Title: {title}, \nLink: {link}\n date: {date} \n")


fresherhunt(request=None)