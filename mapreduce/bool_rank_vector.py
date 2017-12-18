import math

f = open("processed.txt", "r")
fw = open("bool_vector_rank.txt", "w+")
for line in f:
    line = line.split("\t")
    word = line[0]
    fw.write(word + ' ')
    line = line[1:]
    line = ''.join(line)
    line = line.split(';')
    dft = len(line)
    '''for item in line:
        #url = item.split(':')[0]
        wtd = int(item.split(':')[1])
        wtd = (1 + math.log10(wtd)) * math.log10(293.0 / dft)
        wtd = str(wtd)
        item = item.split(':')[0] + ":" + wtd
        print(line)'''
    for i in range(0,dft):
        #item = line[i]
        wtd = int(line[i].split(':')[1])
        wtd = (1 + math.log10(wtd)) * math.log10(293.0 / dft)
        wtd = str(wtd)
        line[i] = line[i].split(':')[0] + ":" + wtd
    #print(line)
    line.sort(key = lambda s : float(s.split(':')[1]),reverse = True)
    line = ' '.join(line)
    line = line.split(" ")
    for i in line:
        i = i[0:8]
        fw.write(i + ' ')
    line = ' '.join(line)
    fw.write('\n')
f.close()
fw.close()