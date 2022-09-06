import os
from prawscripts import getinstance

reddit = getinstance(os.path.dirname(os.getcwd()))
print(reddit)