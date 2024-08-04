from better_profanity import profanity
profanity.load_censor_words()
with open("recognized_speech.txt", "r") as file:
    text = file.read()
output = profanity.censor(text)
print(output)
