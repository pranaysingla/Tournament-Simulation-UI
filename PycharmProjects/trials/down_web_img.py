import urllib.request
import random


def down_img(url):
    name = random.randrange(1, 100)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)

down_img('https://fys1.followyoursport.com/wp-content/uploads/2017/08/Maria-Sharapova-2-1.jpg')