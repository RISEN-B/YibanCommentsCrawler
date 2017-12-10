#!/usr/bin/python3
import requests


def get_comments():
    url = "https://q.yiban.cn/app/index/appid/135991"
    r = requests.get(url)
    print(r.text)


if __name__ == '__main__':
    get_comments()
