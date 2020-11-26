import hashtagGenerator

def findRelatedHashtags(keywords):
  relatedHashtags = []
  for keyword in keywords:
    related = hashtagGenerator.getRelatedHashtags(keyword)
    relatedHashtags = relatedHashtags + related

  return relatedHashtags

# TODO: Add related hashtags to search list.
# In search list, we will check each hashtag in Instagram.

hashtagInput = input("Enter sample hashtags for your image (seperated with ','): ")

print("Finding related hashtags.")
enteredKeywords = hashtagInput.split(',')
relatedHashtags = findRelatedHashtags(enteredKeywords)
print("Found {0} hashtags related for your search term.".format(len(relatedHashtags)))