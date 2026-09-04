import os
import requests

def checkin():
    cookie = os.environ.get('GLADOS_COOKIE')
    if not cookie:
        print("未找到 GLADOS_COOKIE 环境变量！")
        return

    url = "https://glados.space/api/user/checkin"
    headers = {
        "cookie": cookie,
        "origin": "https://glados.space",
        "referer": "https://glados.space/console/checkin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    data = {"token": "glados.network"}
    try:
        response = requests.post(url, headers=headers, json=data)
        print("签到响应状态码:", response.status_code)
        print("签到返回内容:", response.text)
    except Exception as e:
        print("签到请求出错:", e)

if __name__ == '__main__':
    checkin()
