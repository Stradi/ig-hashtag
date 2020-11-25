from hashtag import Hashtag
from user import User

user = User("batinprefect").extractUserProfile()
user.printAllInfo()

hashtag = Hashtag("fashion").extractHashtag()
hashtag.printAllInfo()