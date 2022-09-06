import os
import prawscripts.getinstance
import prawscripts.searchmessageinboxkeyword

reddit = prawscripts.getinstance(os.path.dirname(os.getcwd()))
print(reddit)

result = prawscripts.searchmessageinboxkeyword(reddit, "praw")
print(result)