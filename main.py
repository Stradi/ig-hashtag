from hashtag import Hashtag

# TODO: Check if hashtag is banned or not.

hashtag = Hashtag("fashion").extractHashtag()

print("Hashtag {0}".format(hashtag.name))
print("\tMinLikes\t: {0}".format(hashtag.minLikes))
print("\tMaxLikes\t: {0}".format(hashtag.maxLikes))
print("\tMinComments\t: {0}".format(hashtag.minComments))
print("\tMaxComments\t: {0}".format(hashtag.maxComments))
print("\tEngagement\t: {:.10f}".format(hashtag.engagement))