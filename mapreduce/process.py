f = open('part-r-00000', 'r', encoding='utf-8')

txt = f.read()
txt = txt.replace('hdfs://localhost:9000/user/lwz/index/input/', '')

# f1 = open('part-r-0000.txt', 'w', encoding='utf-8')
dic = {}
for line in txt.split('\n'):
    if line == '':
        continue
    key = line.split('\t')[0]
    values = line.split('\t')[1].split(';')

    if key in dic.keys():
        dic[key].extend(values)
    else:
        dic[key] = values
fout = open('part-r-00000.txt', 'w', encoding='utf-8')
for key in dic.keys():
    fout.write(key + '\t' + ';'.join([value for value in dic[key] if value != '']) + '\n')
