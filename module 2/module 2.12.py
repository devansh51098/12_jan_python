sentence = 'Twinkle Twinkle little star'

words = sentence.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word] =1

for key, value in word_count.items():
    print(key, ":", value)