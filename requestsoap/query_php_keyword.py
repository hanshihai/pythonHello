import requests
import json
from bs4 import BeautifulSoup

'''
query php keywords: http://www.php.net/manual/en/reserved.keywords.php

'''


def parseHtml(url):
    response = requests.get(url, {'timeout':30})
    if response.status_code == 200:
        soap = BeautifulSoup(response.text, "html.parser")
        hot_list = soap.find_all("a")

        result = []
        if hot_list is not None:
            for i in range(len(hot_list)):
                text = hot_list[i].get_text()
                result.append(text)

        return result
    else:
        return None


def main():
    print("starting to query php keyword from php.net ...")
    hot_list = parseHtml("http://www.php.net/manual/en/reserved.keywords.php")
    if hot_list is not None:
        for i in range(len(hot_list)):
            print(hot_list[i])

    return


if __name__ == '__main__':
    main()

