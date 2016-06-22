import pdb
from instagram.client import  InstagramAPI
import json

with open('access_token.txt') as token:
    data = json.load(token)
user_id='262005832'

api = InstagramAPI(access_token=data['access_token'], client_secret=data['client_secret'])

recent_media, next_ = api.user_recent_media(user_id='262005832', count=10)

for media in recent_media:
    link = media.link
    titulo = media.caption
    tags = media.tags
    thumb = media.get_thumbnail_url()
    print("""
        href : {0}\n
        h3 : {1}\n
        span : {2}\n
        img_url : {3}\n
        """.format(link, titulo, tags, thumb)
            )
    

