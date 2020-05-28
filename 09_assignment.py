sentence = list(input('please enter a sentence: ').lower())
char_dict = dict()
for i in range(len(sentence)):
    count = 0
    for j in range(len(sentence)):
        if sentence[i] == sentence[j]:
            count +=1 
    char_dict.update({sentence[i]: count})
print(char_dict)