import requests
from .globals import *
import json

def get_user_info(user_id):
    endpoint = "https://graph.facebook.com/{}?fields=first_name,last_name,profile_pic&access_token={}".format(user_id, ACCESS_TOKEN)
    res_str= requests.get(endpoint).content.decode('utf8')
    return json.loads(res_str)