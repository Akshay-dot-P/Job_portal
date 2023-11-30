from bs4 import BeautifulSoup
import requests

url = "https://offcampusjobs4u.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
a_tags = soup.find_all('a', class_='td-image-wrap')

# Find all <time> tags with class "entry-date updated td-module-date"
date_tags = soup.find_all('time', class_='entry-date updated td-module-date')

# Iterate over corresponding <a> tags and <time> tags using zip
for a_tag, date_tag in zip(a_tags, date_tags):
    title = a_tag.get('title')
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
    date_text = date_tag.get_text(strip=True)
    desig_full = additional_info + desig.replace("[", ",").replace("]", ".")
    result_string = desig_full.replace(',', '').replace("'", '')


    
    if additional_info and location is not '':
        if location in {'B.E/B.Tech/M.Sc/MCA','B.E/B.Tech/MCA' ,'B.Tech/MCA', 'MCA', 'Mca'} :
            print(f"Title: {info},\n Degree/ batch: {result_string + location},\n Date Text: {date_text}\n")
        else:    

            print(f"Title: {info},\n Degree/ batch: {result_string},\n location: {location},\n Date Text: {date_text}\n")
    else:
        print(f"Title: {info},\n Date Text: {date_text}\n")
