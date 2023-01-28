import os
import chardet
from bs4 import BeautifulSoup
import re

folder_path = "D:/桌面/mfyx.top/archives"
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
                header_text = header.get_text().strip().replace('\n', '_')
                header_text = re.sub(r'[\\/*?:"<>|]', '', header_text)
                new_file_path = os.path.join(folder_path, header_text + ".html")
                with open(new_file_path, "w", encoding=result["encoding"]) as new_file:
                    new_file.write(str(soup))
            else:
                print(f"{filename} does not contain a div element with class 'header'.")
                missing_header += 1
print(f"{missing_header} files are missing the class 'header'.")
