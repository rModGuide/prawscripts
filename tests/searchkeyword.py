import os
from prawscripts import getinstance, searchmessageinboxkeyword

reddit = getinstance(os.path.dirname(os.getcwd()))
print(reddit)

result = searchmessageinboxkeyword(reddit, "praw")
print(result)