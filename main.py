from hashtag import Hashtag
from user import User
import hashtagGenerator

# TODO: Add related hashtags to search list.
# In search list, we will check each hashtag in Instagram.
relatedHashtags = hashtagGenerator.getRelatedHashtags("oslo")
print(relatedHashtags[5].hashtagName)