import requests
import constants
import utils.extract as extract

class Hashtag:
  def __init__(self, hashtagName):
    self.hashtagName = hashtagName

    self.minLikes = 1E10
    self.minComments = 1E10
    self.maxLikes = 0
    self.maxComments = 0

  def removeUnnecessaryJSON(self, json):
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

  def extractHashtag(self):
    r = requests.get(constants.HASHTAG_URL.format(tagName = self.hashtagName))
    jsonResponse = r.json()
    jsonResponse = self.removeUnnecessaryJSON(jsonResponse["graphql"]["hashtag"])

    self.name = extract.hashtagName(jsonResponse)
    self.mediaCount = extract.mediaCount(jsonResponse)
    self.topPosts = extract.topPosts(jsonResponse)

    self.calculateMinMaxOfTopPosts()
    self.calculateEngagement()

    return self

  def calculateMinMaxOfTopPosts(self):
    for post in self.topPosts:
      if post.likes < self.minLikes:
        self.minLikes = post.likes
      if post.likes > self.maxLikes:
        self.maxLikes = post.likes

      if post.comments < self.minComments:
        self.minComments = post.comments
      if post.comments > self.maxComments:
        self.maxComments = post.comments

    return self

  def calculateEngagement(self):
    self.engagement = ((self.minLikes + 1) / self.mediaCount) * 10
    return self