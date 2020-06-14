from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
import requests.compat
from requests.compat import quote_plus
from . import models



# Create your views here.
BASE_CRAIG_URL = 'https://delhi.craigslist.org/search/sss?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'

def home_view(request):
    return render(request, "home.html", {})


def new_search_view(request, seach=None):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url = BASE_CRAIG_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')

    post_listings = soup.find_all('li', {'class' : 'result-row'})
    final_postings = []






    for i in range(len(post_listings)):

        post_title = post_listings[i].find(class_= 'result-title').text
        post_url= post_listings[i].find('a').get('href')

        if post_listings[i].find(class_='result-price'):
            post_price = post_listings[i].find(class_="result-price").text
        else:
            post_price='N/A'

        #image_scrapping
        if post_listings[i].find(class_="result-image").get('data-ids'):
            post_image_id = post_listings[i].find(class_="result-image").get('data-ids').split(',')[0].split(':')[1]
            post_image = BASE_IMAGE_URL.format(post_image_id)
            print(post_image)

        else:
            post_image='https://us.123rf.com/450wm/pavelstasevich/pavelstasevich1811/pavelstasevich181101032/112815935-stock-vector-no-image-available-icon-flat-vector-illustration.jpg?ver=6'

        final_postings.append((post_title, post_url, post_price,post_image))


    context = {
        'search_title': search,
        'final_postings': final_postings,

    }
    return render(request, "my_app/new_search.html", context)
