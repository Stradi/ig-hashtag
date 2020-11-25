from hashtag import Hashtag

hashtag = Hashtag("fashion").extractHashtag()

banMessage = "is banned"
if not hashtag.isBanned:
  banMessage = "has {0} medias".format(str(hashtag.mediaCount))

print("Hashtag {0} {1}.".format(hashtag.name, banMessage))
print("\tMinLikes\t: {0}".format(hashtag.minLikes))
print("\tMaxLikes\t: {0}".format(hashtag.maxLikes))
print("\tMinComments\t: {0}".format(hashtag.minComments))
print("\tMaxComments\t: {0}".format(hashtag.maxComments))
print("\tEngagement\t: {:.10f}".format(hashtag.engagement))