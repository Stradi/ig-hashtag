import requests
import constants
import utils.extract as extract

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

# TODO: Delete unnecessary elements from initial JSON response in order to
# increase the performance.

req = requests.get(constants.HASHTAG_URL.format(tagName = "itworks"))
jsonResponse = req.json()
jsonResponse = removeUnnecessaryJSON(jsonResponse["graphql"]["hashtag"])

topPosts = extract.topPosts(jsonResponse)