from datetime import date
import requests
from bs4 import BeautifulSoup
import re

response = requests.get("https://www.bing.com/?mkt=zh-CN")
parsed = BeautifulSoup(response.text, "lxml")
raw = parsed.find(class_="img_cont")["style"]
pattern = re.compile("https://.+\.jpg")
url = pattern.findall(raw)[0]
url = url.replace("1920x1080", "UHD")
pic = requests.get(url)
with open(f"{date.today().isoformat()}.jpg", "wb") as fp:
    fp.write(pic.content)