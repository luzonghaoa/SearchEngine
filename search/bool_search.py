#f = open("bool_easy_rank.txt", "r")
f = open("bool_vector_rank.txt", "r")
txt = f.readlines()
str = input("Input search words(split with blank, use '+' '-' '*' for 'and' 'nor' 'or'):\n")
#str = "欧洲 + 球队 - 葡萄牙"
word_list = str.split(" ")
#print(word_list)
main_content = set()
plus_content = set()
min_content = set()
or_content = set()
result = set()
flag = 0
for word in word_list:
    if word == "+":
        flag = 1
        continue
    elif word == "-":
        flag = 2
        continue
    elif word == "*":
        flag = 3
        continue
    if flag == 0:
        for line in txt:
            if word in line:
                line = line.split(" ")
                line = line[1:]
                line = " ".join(line)
                line = line.split(" ")
                for item in line:
                    main_content.add(item)
    if flag == 1:
        for line in txt:
            if word in line:
                line = line.split(" ")
                line = line[1:]
                line = " ".join(line)
                line = line.split(" ")
                for item in line:
                    plus_content.add(item)
    if flag == 2:
        for line in txt:
            if word in line:
                line = line.split(" ")
                line = line[1:]
                line = " ".join(line)
                line = line.split(" ")
                for item in line:
                    min_content.add(item)
    if flag == 3:
        for line in txt:
            if word in line:
                line = line.split(" ")
                line = line[1:]
                line = " ".join(line)
                line = line.split(" ")
                for item in line:
                    or_content.add(item)
result = main_content & plus_content
result = result | or_content
result = result - min_content
f.close()
#print(main_content)
#print('\n')
#print(plus_content)
#print(min_content)
#print(result)
for item in result:
    print("https://www.yidianzixun.com/article/" + item + '\n')

    #print(text)
#print(main_content)