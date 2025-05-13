import os
import requests

login_url = "https://admin.alwaysdata.com/login/"
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

session = requests.Session()
session.headers.update({
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
})

# 获取登录页和csrf token
resp = session.get(login_url)
csrf_token = session.cookies.get('csrftoken', '')

login_data = {
    'csrfmiddlewaretoken': csrf_token,
    'login': username,
    'password': password,
}

# 提交登录请求
response = session.post(login_url, data=login_data, headers={'Referer': login_url})

# 访问登录后页面
result = session.get('https://admin.alwaysdata.com/log/', allow_redirects=False)

if result.status_code == 200:
    print("✅ 登录成功")
elif result.status_code in [301, 302]:
    print("❌ 登录失败，可能未通过身份验证")
else:
    print(f"⚠️ 未知响应状态码: {result.status_code}")
