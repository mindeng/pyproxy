#! /usr/bin/env python3

import requests
# pip install -U "requests[socks]"


def get_ip(proxy=False):
    if proxy:
        rsp = requests.get('https://httpbin.org/ip',
                       proxies=dict(http='socks5://localhost:1086',
                                    https='socks5://localhost:1086'))
    else:
        rsp = requests.get('https://httpbin.org/ip')
    return rsp.json()

if __name__ == "__main__":
    print(get_ip())
    print(get_ip(True))
