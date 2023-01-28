import os
import chardet
from bs4 import BeautifulSoup
import json
folder_path = "D:/桌面/mfyx.top/archive"
headers = {}
missing_header = 0
for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "rb") as file:
            result = chardet.detect(file.read())
            file.seek(0)
            soup = BeautifulSoup(file, "html.parser", from_encoding=result["encoding"])
            header = soup.find("div", class_="header")
            if header is not None:
                headers[filename] = header.get_text().strip()
            else:
                print(f"{filename} does not contain a div element with class 'header'.")
                missing_header += 1
                
json_file_path = os.path.join(folder_path, "headers.json")
with open(json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(headers, json_file, ensure_ascii=False)
print(f"{missing_header} files are missing the class 'header'.")
