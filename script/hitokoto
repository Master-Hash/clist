#!/usr/bin/env python3
import requests, json

url = "https://v1.hitokoto.cn?"

s_type = {
    "a": "动画",
    "b": "漫画",
    "c": "游戏",
    "d": "文学",
    "e": "原创",
    "f": "来自网络",
    "g": "其他",
    "h": "影视",
    "i": "诗词",
    "j": "网易云",
    "k": "哲学",
    "l": "抖机灵"
}

blocked = 'il'

for blocked_type in blocked:
    url = url + 'c!=' + blocked_type + '&'
url = url.rstrip('&')

raw = requests.get(url)
url = "https://v1.hitokoto.cn?c!=i"
obj = json.loads(raw.text)

for item in obj:
    if not obj[item]:
        obj[item] = ''
    

print(obj['hitokoto'])
#print('\t\t\t\t--', obj['from_who'] + ',', s_type[obj['type']], '"' + obj['from'] + '"')
print("\t\t\t\t-- %s《%s》"%(obj["from_who"], obj["from"]))

