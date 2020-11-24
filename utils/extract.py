from post import Post

def hashtagName(json):
  return json["name"]

def mediaCount(json):
  return json["edge_hashtag_to_media"]["count"]

def topPosts(json):
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