import iDco

start_id = "0Hhs2Ecw"
start_next = iDco.getRelateList(start_id)
start_content = iDco.getContent(start_id)

with open("./download/record.txt", "w+", encoding='utf-8') as f:
    f.write("myurl: " + start_id + '\n')
    f.write("content: " + start_content + '\n' + '\n')

with open("./download/pagelink.txt", "w+", encoding='utf-8') as f1:
    f1.write("myurl: " + start_id + '\n')
    f1.write("out_url: " + ",".join(start_next) + '\n' + '\n')

depth = 30
s = set()
iDco.dfs(start_id, depth)

