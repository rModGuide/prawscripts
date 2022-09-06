import os
import prawscripts.getinstance
import prawscripts.widgetbuilder

reddit = prawscripts.getinstance(os.path.dirname(os.getcwd()))
print(reddit);

widget = prawscripts.widgetbuilder(reddit, "ask", "some_title", "#000000", "#000000", ["help"]);
print(widget);