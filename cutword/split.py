import jieba
import re

jieba.set_dictionary('dict.txt')
r = '[’!"#$%&\'()*，（）“”‘’？+\s,-.。、/:;：；<=>?@[\\]^_`{|}~]+'


fnc = open('record.txt', 'r')
f = open('record_cut.txt', 'w+')
for line in fnc:
    print(line)
    if 'myurl' in line:
        f.write(line)
        continue
    elif line == '\n':
        continue
    else:
        line = line.strip()
        line = re.sub(r, '', line)
        sec = jieba.cut_for_search(line)
        f.write(",".join(sec) + '\n')

fnc.close()
f.close()
#seg_list = jieba.cut_for_search("「台中」正确应该不会被切开")
#print(", ".join(seg_list))