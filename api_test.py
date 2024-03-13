import requests
import os

from flask import request

cover_url = "http://127.0.0.1:10423/api/data/get_cover/"
book_url = "http://127.0.0.1:10423/api/data/get_book/"
level_url = "http://106.13.248.184:8088/api/data/get_level/"

cover_json = {
    "level": "AA",
}
book_json = {
    "level": "AA",
    "word": "Big",
}


# cover_res = requests.post(url=cover_url, json=cover_json)
# book_res = requests.post(url=book_url, json=book_json)
level_res = requests.post(url=level_url, json={})

print('----------------------------------------------------')
# print('cover content:', cover_res.content)

# print('----------------------------------------------------')
# print('book content:', book_res.content)

print('----------------------------------------------------')
print('level content:', level_res.content)