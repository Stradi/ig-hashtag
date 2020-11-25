from utils.post import Post

def hashtagName(json):
  return json["name"]

def hashtagMediaCount(json):
  return json["edge_hashtag_to_media"]["count"]

# TODO: hashtagTopPosts and userPosts function is exactly the same
# Fix this.
def hashtagTopPosts(json):
  postsJsonArray = json["edge_hashtag_to_top_posts"]["edges"]
  posts = []
  for p in postsJsonArray:
    currentPostJson = p["node"]

    currentPostId = currentPostJson["id"]
    currentPostLikes = currentPostJson["edge_liked_by"]["count"]
    currentPostComments = currentPostJson["edge_media_to_comment"]["count"]
    currentPostCaption = currentPostJson["edge_media_to_caption"]["edges"][0]["node"]["text"]

    post = Post(currentPostId, currentPostLikes, currentPostComments, currentPostCaption)
    posts.append(post)
    #print("{0} has {1} likes and {2} comments.".format(currentPostId, currentPostLikes, currentPostComments))
  return posts

def hashtagIsBanned(json):
  return json["is_top_media_only"]

def userFullName(json):
  return json["full_name"]

def userFollowerCount(json):
  return json["edge_followed_by"]["count"]

def userFollowingCount(json):
  return json["edge_follow"]["count"]

def userPostCount(json):
  return json["edge_owner_to_timeline_media"]["count"]

def userIsPrivate(json):
  return json["is_private"]

def userPosts(json):
  postsJsonArray = json["edge_owner_to_timeline_media"]["edges"]
  posts = []
  for p in postsJsonArray:
    currentPostJson = p["node"]

    currentPostId = currentPostJson["id"]
    currentPostLikes = currentPostJson["edge_liked_by"]["count"]
    currentPostComments = currentPostJson["edge_media_to_comment"]["count"]
    currentPostCaption = currentPostJson["edge_media_to_caption"]["edges"][0]["node"]["text"]

    post = Post(currentPostId, currentPostLikes, currentPostComments, currentPostCaption)
    posts.append(post)

  return posts