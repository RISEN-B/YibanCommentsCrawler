#!/usr/bin/python3
import requests


def get_comments():
    url = "https://q.yiban.cn/comment/getCommentList"
    data = {
        'appid': '135991',
        'type': 'extendcomment',
        'code': 'extendcomment-1502763105087',
        'page': '1',
        'size': '5',
        'reply_comment_id': '',
        'flag': ''
    }
    r = requests.post(url, data=data)
    r.encoding = 'utf-8'
    r = r.json()
    print(r)


if __name__ == '__main__':
    get_comments()
