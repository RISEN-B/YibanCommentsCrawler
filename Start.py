#!/usr/bin/python3
import requests


def get_comments():
    url = "https://q.yiban.cn/comment/getCommentList"
    data = {
        'appid': '135991',
        'type': 'extendcomment',
        'code': 'extendcomment - 1502763105087',
        'page': '1',
        'size': '5',
        'reply_comment_id': '',
        'flag': ''
    }
    cookies = dict(
        UM_distinctid='15f7beee3d21c-03c051c56b6b7c-12666d4a-1fa400-15f7beee3d3321',
        CNZZDATA1254633902='2027200784-1511412959-null|1512907567',
        analytics='0c8e0b9ba3c07bf3',
        project_user_token='16b60a09893c2fe6ab4a483d21a2edcc',
        ticket_user_token='16b60a09893c2fe6ab4a483d21a2edcc',
        YB_SSID='53ecde7f3abc0fd239e2098a30ca04a8',
        PHPSESSID='307550b35fe774994d810d9f48dca6ca',
        laravel_session='eyJpdiI6InZqN2dVZHpZcXhVSnNrK3hcL3NJa3FRPT0iLCJ2YWx1ZSI6IkR6VjhLc1pZSTRYTmp0Y3k1N0xcL3p3d2hBNTkwc3YweUo2VlhQdm9ScDQ4RURlV0RyQUhCcGRMVjZPN3JOcXhjNmRHY2g2QUFtaTRXMEFEWW9VRzNsUT09IiwibWFjIjoiMzYxZDRiMzFmZWVkNzgzNzc1ZmU2YjQzZWI4MDUxYmMzZjhiMmYwOTU0Mzk4ODA1ODE5OWFkZWFkNzcxZDNmMCJ9'
    )

    headers = {
        'Host': 'q.yiban.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://q.yiban.cn/app/index/appid/135991',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '120',
        'Cookie': 'UM_distinctid=15f7beee3d21c-03c051c56b6b7c-12666d4a-1fa400-15f7beee3d3321; CNZZDATA1254633902=2027200784-1511412959-null%7C1512907567; analytics=0c8e0b9ba3c07bf3; project_user_token=16b60a09893c2fe6ab4a483d21a2edcc; ticket_user_token=16b60a09893c2fe6ab4a483d21a2edcc; YB_SSID=53ecde7f3abc0fd239e2098a30ca04a8; PHPSESSID=307550b35fe774994d810d9f48dca6ca; laravel_session=eyJpdiI6IlNjaHp1NG1cL01BT3V5Wk82NWY2RzZBPT0iLCJ2YWx1ZSI6IjZCOWpxRjB5b0VoUTdUZXRzcWZiXC9US3dtdHlDRGRDQTdhVkpJdmhmSE9PUzJTS0FUc21lb2FOKytSU0oyYWNmOTlxSTJIR0UzOVNlOEd3cTd3OVI4Zz09IiwibWFjIjoiOTg3ZjVmYzQ2M2QzNDYzODY2YzUzMTBkNmYzOTVjMWFlYzI5MTBkOGZhOWM3MTI0MjhkYzY3MDIzNjIxZjlmNyJ9',
        'Connection': 'Connection'
    }
    session = requests.Session()
    r = session.post(url, data=data)
    r.encoding = 'utf-8'
    r = r.json()
    print(r)


if __name__ == '__main__':
    get_comments()
