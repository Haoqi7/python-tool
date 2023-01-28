import os
import re
from bs4 import BeautifulSoup

folder_path = "D:/桌面/mfyx.top/archives"
missing_header = 0
for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
            header = soup.find("div", class_="header")
            if header is not None:
                header_text = re.sub(r'[^\w\s]','',header.get_text().strip().replace('\n', '_'))
                new_file_path = os.path.join(folder_path, header_text + ".html")
                with open(new_file_path, "w", encoding="utf-8") as new_file:
                    new_file.write(str(soup))
            else:
                print(f"{filename} does not contain a div element with class 'header'.")
                missing_header += 1
print(f"{missing_header} files are missing the class 'header'.")
