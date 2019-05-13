import requests
import json_example
from bs4 import BeautifulSoup

'''
query today's hot: https://news.qq.com/ninja/qqnews_jinrihuati.htm
query prevent new: https://news.qq.com/ext2020/apub/json/prevent.new.json
'''

def parseHtml(url):
    response = requests.get(url, {'timeout':30})
    if response.status_code == 200:
        soap = BeautifulSoup(response.text, "html.parser")
        hot_content = soap.find("ul", class_ = "list")
        hot_list = hot_content.find_all("a", attrs={"target": "_blank"})

        hot_news = []
        if hot_list is not None:
            for i in range(len(hot_list)):
                new_herf = hot_list[i]['href']
                new_text = hot_list[i].get_text()
                hot_news.append({'href':new_herf, 'text':new_text})

        return hot_news
    else:
        return None


def parseJson(url):
    response = requests.get(url, {'timeout': 30})
    if response.status_code == 200:
        json_content = json_example.loads(response.text, encoding='UTF-8')
        return json_content
    else:
        return None


def main():
    print("starting to query content from news.qq.com -- today's hot ...")
    hot_list = parseHtml("https://news.qq.com/ninja/qqnews_jinrihuati.htm")
    if hot_list is not None:
        for i in range(len(hot_list)):
            print(hot_list[i])

    print("starting to query content from news.qq.com -- prevent news ...")
    prevent_news = parseJson("https://news.qq.com/ext2020/apub/json/prevent.new.json")
    if prevent_news is not None:
        for i in range(len(prevent_news)):
            print(prevent_news[i])

    return


if __name__ == '__main__':
    main()

