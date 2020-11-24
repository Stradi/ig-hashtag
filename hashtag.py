class Hashtag:
  def __init__(self, name, mediaCount, topPosts):
    self.name = name
    self.mediaCount = mediaCount
    self.topPosts = topPosts

    self.minLikes = 1E10
    self.minComments = 1E10
    self.maxLikes = 0
    self.maxComments = 0

    self.calculateMinMaxOfTopPosts()
    self.calculateEngagement()

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

  def calculateEngagement(self):
    self.engagement = ((self.minLikes + 1) / self.mediaCount) * 10