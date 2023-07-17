import urllib.request as req
import json

# 取得資料
url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with req.urlopen(url) as response:
    data = response.read().decode("utf-8")

# 解析資料，將資料從 json 轉為 dict
data_todic = json.loads(data)

result = data_todic["result"]["results"]
info = result[0]

print(info)
# attraction stitle address longitude latitude file

# MRT stitle
