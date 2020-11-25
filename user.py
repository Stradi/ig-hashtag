import requests
import constants
import utils.extract as extract

class User:
  def __init__(self, username):
    self.username = username

  def removeUnnecessaryJSON(self, json):
    del json["biography"]
    del json["blocked_by_viewer"]
    del json["restricted_by_viewer"]
    del json["country_block"]
    del json["external_url"]
    del json["external_url_linkshimmed"]
    del json["followed_by_viewer"]
    del json["follows_viewer"]
    del json["has_ar_effects"]
    del json["has_clips"]
    del json["has_guides"]
    del json["has_channel"]
    del json["has_blocked_viewer"]
    del json["highlight_reel_count"]
    del json["has_requested_viewer"]
    del json["is_business_account"]
    del json["is_joined_recently"]
    del json["business_category_name"]
    del json["overall_category_name"]
    del json["category_enum"]
    del json["is_verified"]
    del json["edge_mutual_followed_by"]
    del json["profile_pic_url"]
    del json["profile_pic_url_hd"]
    del json["requested_by_viewer"]
    del json["connected_fb_page"]
    del json["edge_saved_media"]
    del json["edge_media_collections"]
    del json["edge_related_profiles"]

    return json

  def extractUserProfile(self):
    r = requests.get(constants.PROFILE_URL.format(username = self.username))
    jsonResponse = r.json()
    jsonResponse = self.removeUnnecessaryJSON(jsonResponse["graphql"]["user"])
    # jsonResponse can be empty (also in Hashtag class)

    self.isPrivate = extract.userIsPrivate(jsonResponse)
    self.mediaCount = extract.userPostCount(jsonResponse)
    self.follower = extract.userFollowerCount(jsonResponse)
    self.following = extract.userFollowingCount(jsonResponse)
    self.posts = extract.userPosts(jsonResponse)

    self.calculateAvgLikesOfPosts()

    return self

  def calculateAvgLikesOfPosts(self):
    if self.isPrivate:
      self.avg = 0
      return self

    for post in self.posts:
      self.avg += post.likes

    self.avg /= len(self.posts)
    return self

  def printAllInfo(self):
    privateMessage = "is private"
    if not self.isPrivate:
      privateMessage = "has {0} medias".format(str(self.mediaCount))

    print("User {0} {1}.".format(self.username, privateMessage))
    print("\tFollowers\t: {0}".format(self.follower))
    print("\tFollowings\t: {0}".format(self.following))
    print("\tMedia Count\t: {0}".format(self.mediaCount))
    print("\tAvgOf12Posts\t: {0}".format(self.avg))
    