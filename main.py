import logging
import hashtagGenerator

from user import User
from hashtag import Hashtag

#TODO: Create a base class for User and Hashtag.

def setupLogger(fileName = "log"):
  loggingFormat = "%(asctime)s %(levelname)s %(message)s"
  logging.basicConfig(filename=fileName + ".log", filemode="a", level=logging.DEBUG, format=loggingFormat)
  logging.getLogger("urllib3").setLevel(logging.WARNING)

setupLogger()
logging.info("Instagram Hashtag Finder is started.")

def findRelatedHashtags(keywords):
  logging.info("Finding related hashtags.")

  relatedHashtags = []
  for keyword in keywords:
    related = hashtagGenerator.getRelatedHashtags(keyword)
    relatedHashtags = relatedHashtags + related
    logging.debug("Found {0} hashtags related to \"{1}\"".format(len(related), keyword))

  logging.info("Found {0} hashtags related to your keywords.".format(len(relatedHashtags)))
  return relatedHashtags

# TODO: Add related hashtags to search list.
# In search list, we will check each hashtag in Instagram.
usernameInput = input("Enter your username: ")
user = User(usernameInput).extractUserProfile()

hashtagInput = input("Enter sample hashtags for your image (seperated with ','): ")

enteredKeywords = hashtagInput.split(',')
relatedHashtags = findRelatedHashtags(enteredKeywords)

# Only getting information of first hashtag.
relatedHashtags[0].extractHashtag()