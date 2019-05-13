import requests
import json_example
from bs4 import BeautifulSoup

'''
query ruby keywords: https://docs.ruby-lang.org/en/2.2.0/keywords_rdoc.html

'''


def parseHtml(url):
    response = requests.get(url, {'timeout':30})
    if response.status_code == 200:
        soap = BeautifulSoup(response.text, "html.parser")
        hot_list = soap.find_all("dt")

        result = []
        if hot_list is not None:
            for i in range(len(hot_list)):
                text = hot_list[i].contents[0]
                result.append(text)

        return result
    else:
        return None


def main():
    print("starting to query ruby keyword from ruby-lang ...")
    hot_list = parseHtml("https://docs.ruby-lang.org/en/2.2.0/keywords_rdoc.html")
    if hot_list is not None:
        for i in range(len(hot_list)):
            print(hot_list[i])

    return


if __name__ == '__main__':
    main()

