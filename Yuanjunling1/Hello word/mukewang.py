#coding=utf-8
import requests
URL_IP='https://cas.dev.great-tao.com/cas-server/login?service=http://boss.dev.great-tao.com/cas'
def use_Simple_requests():
    response = requests.get(URL_IP)
    print '>>>>Response Headers:'
    print response.headers
    print response.text
    s = requests.Session()  # 保持Cookie










if __name__ == '__main__':
    use_Simple_requests()