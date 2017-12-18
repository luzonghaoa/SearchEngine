f = open("pagelink.txt", "r")
fw = open("pagematrix.txt", "w+")

for line in f:
    if "myurl" in line:
        line = line[7: 14]
        fw.write(line + ' ' + '100' + ' ')
    elif "out_url" in line:
        line = line[9:]
        fw.write(line)

f.close()
fw.close()
