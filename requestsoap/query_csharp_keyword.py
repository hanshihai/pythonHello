import requests
import json_example
from bs4 import BeautifulSoup

'''
query c# keywords: https://docs.microsoft.com/zh-cn/dotnet/csharp/language-reference/keywords/index

'''


def parseHtml(url):
    response = requests.get(url, {'timeout':30})
    if response.status_code == 200:
        soap = BeautifulSoup(response.text, "html.parser")
        hot_list = soap.find_all("span", class_="sxs-lookup")

        result = []
        if hot_list is not None:
            for i in range(len(hot_list)):
                text = hot_list[i].get_text()
                result.append(text)

        return result
    else:
        return None


def main():
    print("starting to query c# keyword from microsoft ...")
    hot_list = parseHtml("https://docs.microsoft.com/zh-cn/dotnet/csharp/language-reference/keywords/index")
    if hot_list is not None:
        for i in range(len(hot_list)):
            print(hot_list[i])

    return


if __name__ == '__main__':
    main()

