import hashlib
import requests
import constants
from hashtag import Hashtag

def buildApiToken(tag):
  toBeHashed = constants.HASH_TEMPLATE.format(
    constants.USER_AGENT,
    tag,
    constants.SECRET_FUNC
  ).encode("utf-8")

  return hashlib.md5(toBeHashed).hexdigest()

def getRelatedHashtags(tag):
  headers = {
    "user-agent": constants.USER_AGENT,
    "api-token": buildApiToken(tag)
  }

  req = requests.get(constants.GENERATOR_URL.format(tag), headers=headers)
  jsonResponse = req.json()

  relatedHashtags = []

  for h in jsonResponse["results"]:
    relatedHashtags.append(Hashtag(h["tag"]))

  return relatedHashtags