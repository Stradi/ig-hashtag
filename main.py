import requests
import constants
from hashtag import Hashtag
import utils.extract as extract

# TODO: Check if hashtag is banned or not.

def removeUnnecessaryJSON(json):
  del json["allow_following"]
  del json["is_following"]
  del json["is_top_media_only"]
  del json["profile_pic_url"]
  del json["edge_hashtag_to_media"]["edges"]
  del json["edge_hashtag_to_media"]["page_info"]
  del json["edge_hashtag_to_content_advisory"]
  del json["edge_hashtag_to_related_tags"]
  del json["edge_hashtag_to_null_state"]

  return json

req = requests.get(constants.HASHTAG_URL.format(tagName = "fashion"))
jsonResponse = req.json()
jsonResponse = removeUnnecessaryJSON(jsonResponse["graphql"]["hashtag"])

hashtag = Hashtag(extract.hashtagName(jsonResponse), extract.mediaCount(jsonResponse), extract.topPosts(jsonResponse))
print("Hashtag {0}".format(hashtag.name))
print("\tMinLikes\t: {0}".format(hashtag.minLikes))
print("\tMaxLikes\t: {0}".format(hashtag.maxLikes))
print("\tMinComments\t: {0}".format(hashtag.minComments))
print("\tMaxComments\t: {0}".format(hashtag.maxComments))
print("\tEngagement\t: {:.10f}".format(hashtag.engagement))