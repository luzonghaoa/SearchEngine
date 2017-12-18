import requests
import json

from bs4 import BeautifulSoup

def getRelateList(docid):
    url = "https://www.yidianzixun.com/home/q/getrelatednews?docid="+docid+"&start=0&length=10&s=&appid=yidian&_=1508931998751"
    r = requests.get(url)
    docs = json.loads(r.text)["documents"]
    return [doc['docid'] for doc in docs][0:4]

def getContent(docid):
    url = 'https://www.yidianzixun.com/article/' + docid
    txt = requests.get(url).text
    ans = ''
    soup = BeautifulSoup(txt, "html.parser").find_all('p')
    for txt in soup:
        if "京公网安备" in txt.get_text():
            break
        ans = ans + txt.get_text()
    return ans


s = set()


def dfs(docid, depth):
    #global cnt
    # a = set()
    if docid in s:
        # print(docid)
        return
    s.add(docid)
    if depth == 0:
        #cnt = cnt + 1
        print(1)
        return
    rel_list = getRelateList(docid)
    #print(docid)
    #print(rel_list)
    #with open("record.txt", "a") as f:
        #f.write("myurl: " + docid + '\n')
        #f.write("out_url: " + ",".join(rel_list) + '\n')
    for relate_docid in rel_list:
        content_txt = getContent(relate_docid)
        next_url = getRelateList(relate_docid)
        if relate_docid in s:
            continue
        with open("./download/record.txt", "a", encoding='utf-8') as f:
            f.write("myurl: " + relate_docid + '\n')
            f.write("content: " + content_txt + '\n' + '\n')
        with open("./download/pagelink.txt", "a+", encoding='utf-8') as f1:
            f1.write("myurl: " + relate_docid + '\n')
            f1.write("out_url: " + ",".join(next_url) + '\n' + '\n')
        dfs(relate_docid, depth - 1)


# a = getRelateList("0Hhs2Ecw")
# print(a)
# for id in a:
    # print(getContent(id))
    # print('\n')