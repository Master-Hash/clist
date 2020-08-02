#!/usr/bin/python3.8
#coding=utf8
import requests
from lxml import etree
from typing import NoReturn, List, Tuple
from datetime import datetime, timedelta, timezone
from warnings import warn
import pytz
tp = List[str]

# Master Hash custom
class package:
    def __init__(self,
                 Name: str,
                 URL: str, # 爬虫直接从此爬取
                 Homepage: str,
                 Description: str,
                 License: str,
                 ) -> NoReturn:
        for i in ("Name",
                  "URL",
                  "Homepage",
                  "Description",
                  "License",
                  ):
            exec(f"self.{i} = {i}")

vscodium_bin = package("vscodium-bin",
                       "https://github.com/VSCodium/vscodium/releases",
                       "https://vscodium.com/",
                       "Free/Libre Open Source Software Binaries of VSCode",
                       "MIT",
                       )

code = package("code",
               "https://github.com/Microsoft/vscode/releases",
               "https://github.com/Microsoft/vscode",
               "The Open Source build of Visual Studio Code (vscode) editor",
               "MIT",
               )

fenix = package("fenix",
                "https://github.com/mozilla-mobile/fenix/releases",
                "https://github.com/mozilla-mobile/fenix",
                "新版 Firefox 浏览器，7 月底即将替换正式版，用于测试 pre 的 tag",
                "MPL-2.0"
                )
'''
visual_studio_code_bin = package("visual-studio-code-bin",
                                 "https://"
                                 )
visual_studio_code_insiders_bin = package("",

                                          )'''
Maintained = (vscodium_bin,
              code,
              fenix
              )
#定义函数，爬取对应的数据
def getText(url: str) -> str:
    my_headers = {'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
                  'Cookie': r'_octo=GH1.1.2066394762.1594658673; logged_in=no; tz=Asia%2FShanghai',
                  'Accept-Language': r'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                  }
    response = requests.get(url, headers=my_headers)
    return response.text

#定义函数，保存爬取到的数据
def parse(content: str) -> Tuple[tp]:
    xml = etree.HTML(content)
    datas = xml.xpath('/html/body/div[4]/div/main/div[2]/div/div[2]/div/div/div[1]/ul/li[1]/a/span/text()')
    # 获取时间
    times = xml.xpath("/html/body/div[4]/div/main/div[2]/div/div[2]/div/div/div[2]/div[1]/p/relative-time/@datetime") # 因为爬虫的时区（headers？未调查清楚）原因，不能 @title
    # 获取 tag
    tags = xml.xpath("/html/body/div[4]/div/main/div[2]/div/div[2]/div/div/@class")
    #tag = xml.xpath("/html/body/div[4]/div/main/div[2]/div/div[2]/div/div/div[1]/div/span")
    if len(tags) != len(datas):
        warn("存在没有 tag 的 release") # 有些 releases 被折叠了！不过我不需要那么多。所以不管了。
        # ['release pt-2 pt-md-...el-latest', 'release pt-2 pt-md-...ix label-', 'release pt-2 pt-md-...ix label-', 'release pt-2 pt-md-...ix label-', 'release pt-2 pt-md-...ix label-', 'release-entry', 'release-entry posit... expander', 'release-entry collapsable', 'release-entry collapsable', 'release-entry collapsable', 'release-entry ']
    elif len(tags) == len(datas) == 0: ...
    return datas, times, tags


#定义主程序接口
# if __name__ != '__main__':
#     url = 'https://github.com/mozilla-mobile/fenix/releases'
#     content = getText(url)
#     print(parse(content))

# 优化输出
# 暂时不能区分预发布和稳定发布，敬请期待
# 时区处理完毕，虽然格式很丑

def out(pac: package, datas: tp, times: tp, tags: tp) -> NoReturn:
    print(f"[{pac.Name}]")
    for i, j, k in zip(datas, times, tags):
        tz = pytz.timezone("Asia/Shanghai")
        date = datetime.strptime(j, r"%Y-%m-%dT%H:%M:%SZ")
        date_8 = date + timedelta(hours=8)

        j = date_8.astimezone(tz).isoformat()
        tmpa = k.split()[-1]
        tmpb = tmpa.split("-")
        if tmpb[-1]: print(f"{i}: {j}", tmpb[-1])
        else: print(f"{i}: {j}")
    #print("="*len(i))

if __name__ == "__main__":
    for i in Maintained:
        j = getText(i.URL)
        #print(parse(j))
        out(i, *parse(j))
