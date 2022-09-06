import os
from prawscripts import getinstance, widgetbuilder

reddit = getinstance(os.path.dirname(os.getcwd()))
print(reddit);

widget = widgetbuilder(reddit, "ask", "some_title", "#000000", "#000000", ["help"]);
print(widget);