f = open("processed.txt", "r")
fw = open("bool_easy_rank.txt", "w+")

for text in f:
    #text = "".join(text)
    text = text.split('\t')
    word = text[0]
    fw.write(word + ' ')
    text = text[1:]
    text = ''.join(text)
    text = text.split(";")
    text.sort(key = lambda s : int(s.split(':')[1]),reverse = True)
    text = ' '.join(text)
    text = text.split(" ")
    for i in text:
        i = i[0:8]
        fw.write(i + ' ')
    text = ' '.join(text)
    #fw.write(word + ' ' + text)
    fw.write('\n')

f.close()
fw.close()