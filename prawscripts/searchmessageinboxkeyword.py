def searchmessageinboxkeyword(instance, keyword):
    for message in instance.inbox.all(limit = None):
        if keyword in str(message.body) or keyword in str(message.subject):
            print(message.body)