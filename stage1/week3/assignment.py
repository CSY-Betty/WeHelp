import urllib.request as req
import json
import re
import csv

# 取得資料
url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with req.urlopen(url) as response:
    data = response.read().decode("utf-8")

# 解析資料，將資料從 json 轉為 dict
data_todic = json.loads(data)

result = data_todic["result"]["results"]


# 取出地址的區域
def get_district(address):
    pattern = r"\s([^\s]+區)"
    parse = re.search(pattern, address)

    if parse:
        district = parse.group(1)
    else:
        district = ""

    return district


# 取出第一張圖檔網址
def get_first_image(file):
    file_lower = file.lower()
    image = file_lower.find(".jpg")
    first_image = file[: image + 4]

    return first_image


def attraction_data(attraction):
    attraction_name = data["stitle"]
    attraction_address = data["address"]  # 再處理 取區域
    attraction_longitude = data["longitude"]
    attraction_latitude = data["latitude"]
    attraction_file = data["file"]  # 再處理 取第一筆

    form = [
        attraction_name,
        get_district(attraction_address),
        attraction_longitude,
        attraction_latitude,
        get_first_image(attraction_file),
    ]
    return form


def group_attractions_by_mrt(result):
    attraction_by_mrt = {}

    for data in result:
        attraction_name = data["stitle"]
        attraction_mrt = data["MRT"]

        if attraction_mrt in attraction_by_mrt:
            attraction_by_mrt[attraction_mrt].append(attraction_name)
        else:
            attraction_by_mrt[attraction_mrt] = [attraction_name]

    return attraction_by_mrt


# 寫入 attracion.csv 檔案
with open("attracion.csv", "w", newline="") as file:
    writer = csv.writer(file)

    for data in result:
        form = attraction_data(data)
        writer.writerow(form)

# 寫入 mrt.csv 檔案
with open("mrt.csv", "w", newline="") as file:
    writer = csv.writer(file)
    attraction_by_mrt = group_attractions_by_mrt(result)
    for mrt, attractions in attraction_by_mrt.items():
        form = [mrt] + attractions
        writer.writerow(form)
