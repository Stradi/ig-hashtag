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
    if not jsonResponse:
      print("Could not fetch hashtag.")
      return self

    jsonResponse = self.removeUnnecessaryJSON(jsonResponse["graphql"]["hashtag"])

    self.name = extract.hashtagName(jsonResponse)
    self.mediaCount = extract.hashtagMediaCount(jsonResponse)
    self.topPosts = extract.hashtagTopPosts(jsonResponse)
    self.isBanned = extract.hashtagIsBanned(jsonResponse)

    self.calculateAnalytics()

    return self

  def calculateMinMaxOfTopPosts(self):
    if self.isBanned:
      self.minLikes = 0
      self.maxLikes = 0
      self.minComments = 0
      self.maxComments = 0
      return self

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
    if self.isBanned:
      self.engagement = 0
      return self

    self.engagement = ((self.minLikes + 1) / self.mediaCount) * 10
    return self

  def calculateAnalytics(self):
    self.calculateMinMaxOfTopPosts()
    self.calculateEngagement()

  def printAllInfo(self):
    banMessage = "is banned"
    if not self.isBanned:
      banMessage = "has {0} medias".format(str(self.mediaCount))

      print("Hashtag {0} {1}.".format(self.name, banMessage))
      print("\tMinLikes\t: {0}".format(self.minLikes))
      print("\tMaxLikes\t: {0}".format(self.maxLikes))
      print("\tMinComments\t: {0}".format(self.minComments))
      print("\tMaxComments\t: {0}".format(self.maxComments))
      print("\tEngagement\t: {:.10f}".format(self.engagement))