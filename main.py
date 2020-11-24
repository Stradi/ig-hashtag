import requests
import constants

req = requests.get(constants.HASHTAG_URL.format(tagName = "itworks"))
print(req.json())