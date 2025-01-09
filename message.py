
# Email

sender = "MarioSantana@op.pl"
recipient = "DawidZaba@wp.pl"
title = "We learn the Python programming language"
attachment = "https://github.com/MarioSantana93"
messageContent = """Hey tiger, how's your Python learning going?
In the attachment I am sending you my profile created on gitHub"""
postscriptum = "don't forget to take modafinil and drink boar :)"

conversationBetween = sender + " from to " + recipient
print(conversationBetween)

titleAndValues = title + "\n" + attachment
print(titleAndValues)

messageAndForgetful = messageContent + "\n" + postscriptum
print(messageAndForgetful)

postscriptum2 = "don't forget to check file number Two xD"
print(postscriptum2)
