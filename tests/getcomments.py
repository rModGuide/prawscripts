import os
import prawscripts.getinstance

reddit = prawscripts.getinstance(os.path.dirname(os.getcwd()))

reddit.read_only = True

url = "https://www.reddit.com/r/funny/comments/3g1jfi/buttons/"
submission = reddit.submission(url=url)

for top_level_comment in submission.comments:
    print(top_level_comment.body)