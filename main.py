import requests
import constants
import utils.extract as extract

# TODO: Delete unnecessary elements from initial JSON response in order to
# increase the performance.

req = requests.get(constants.HASHTAG_URL.format(tagName = "itworks"))
jsonResponse = req.json()
jsonResponse = jsonResponse["graphql"]["hashtag"]

print("Hashtag '{0}' has {1} medias.".format(extract.hashtagName(jsonResponse), extract.mediaCount(jsonResponse)))

topPosts = extract.topPosts(jsonResponse)