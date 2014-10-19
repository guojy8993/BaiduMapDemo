#coding=utf-8
def process_article(article):
    parray = article.split("\n")
    result = ""
    for p in parray:
        result += "&nbsp;&nbsp;%s\n"%p.strip()
    return result;

demo = "我们是\n生活在红旗下的新 一代年轻人 \n 继承先辈愿望"
print process_article(demo)