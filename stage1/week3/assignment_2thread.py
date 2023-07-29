import urllib.request as req
from bs4 import BeautifulSoup
import time
import threading

start = time.time()

# 最新頁
new_url = "https://www.ptt.cc/bbs/movie/index.html"
recent_page = 3
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}


def get_data(url):
    request = req.Request(url, headers=headers)

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    root = BeautifulSoup(data, "html.parser")

    return root


def get_title(title):
    title_text = title.a.string if title.a else "None"
    return title_text


def get_tweet(tweet):
    tweet_num = tweet.span.string if tweet.span else "None"
    return tweet_num


def get_article_time(title):
    link = title.find("a")
    article_time = None

    if link is None:
        pass
    else:
        article_url = "https://www.ptt.cc" + link["href"]
        article_meta = get_data(article_url).find_all("div", class_="article-metaline")
        target_div = article_meta[2] if len(article_meta) >= 3 else ""
        article_time = target_div.find("span", class_="article-meta-value")

    return article_time


def crawl_page(url):
    titles = get_data(url).find_all("div", class_="title")
    number_of_tweets = get_data(url).find_all("div", class_="nrec")

    page_data = []
    for title, tweet in zip(titles, number_of_tweets):
        title_text = get_title(title)
        if title_text == "[公告] 電影板板規 2022/12/5":
            continue  # 不將[公告] 電影板板規加入資料
        tweet_num = get_tweet(tweet)
        article_time = get_article_time(title)

        if time is not None:
            page_data.append((title_text, tweet_num, article_time.string))

    return page_data


def process_page(url, result_list):
    page_data = crawl_page(url)
    result_list.extend(page_data)


all_data = []

threads = []


# 抓取最新頁的資料
latest_data = crawl_page(new_url)
all_data.extend(latest_data)

# 抓取上一頁網址
prev_link = get_data(new_url).select("div.btn-group.btn-group-paging a")[1]["href"]

# 抓取上一頁的資料並加入到latest_data
for number in range(recent_page - 1):
    page = int(prev_link.split("index")[1].split(".")[0])
    page_number = int(page) - number
    prev_url = f"https://www.ptt.cc/bbs/movie/index{page_number}.html"
    thread = threading.Thread(target=process_page, args=(prev_url, all_data))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# 根據時間排序資料，最新的排在前面
sorted_data = sorted(all_data, key=lambda x: x[2], reverse=True)

# 寫入 movie.txt 檔案
with open("movie2.txt", "w", encoding="utf-8") as file:
    for title_text, tweet_num, article_time in sorted_data:
        line = f"{title_text} {tweet_num} {article_time}\n"
        file.write(line)

end = time.time()
print("執行時間: " + str(end - start))
