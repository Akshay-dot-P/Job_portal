from django.shortcuts import render

# Create your views here.
def indexview(request):
    return render(request, 'index.html')

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import JobSerializer
from bs4 import BeautifulSoup
import requests

class Jobs4uView(APIView):
    def get(self, request):
        url = "https://offcampusjobs4u.com/"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        a_tags = soup.find_all('a', class_='td-image-wrap')
        date_tags = soup.find_all('time', class_='entry-date updated td-module-date')

        jobs_data = []
        for a_tag, date_tag in zip(a_tags, date_tags):
            title = a_tag.get('title')
            link = a_tag.get('href')
            split_title = title.split('|')
            info = split_title[0].strip() if len(split_title) > 1 else title
            additional_info3 = ""
            additional_info = split_title[1].strip() if len(split_title) >1 else additional_info3
            location = split_title[2].strip() if len(split_title) >2 else additional_info3
            index_of_for = additional_info.lower().find('for')
            designation = additional_info[index_of_for + 4:].split()[:1]
            desig = str(designation)
            date_text = date_tag.get_text(strip=True)
            desig_full = additional_info + desig.replace("[", ",").replace("]", ".")
            result_string = desig_full.replace(',', '').replace("'", '')

            if additional_info and location !='':
                if location in {'B.E/B.Tech/M.Sc/MCA','B.E/B.Tech/MCA' ,'B.Tech/MCA', 'MCA', 'Mca'}:
                    jobs_data.append({
                        "title": info,
                        "degree_batch": result_string + location,
                        "location": "",
                        "date_text": date_text,
                        "link": link,
                    })
                else:
                    jobs_data.append({
                        "title": info,
                        "degree_batch": result_string,
                        "location": location,
                        "date_text": date_text,
                        "link": link,
                    })
            else:
                jobs_data.append({
                    "title": info,
                    "degree_batch": "",
                    "location": "",
                    "date_text": date_text,
                    "link": link,
                })

        serializer = JobSerializer(jobs_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
