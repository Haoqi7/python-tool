import os
file_path="D:\桌面\pic"

file_names = os.listdir(file_path)
count=101
print(file_names)
for file in file_names:
    #调试代码的方法：关键地方打上print语句，判断这一步是不是执行成功
    print(file)
    #如果文件名中带有大写字母“E”,则重命名该文件
    if "E" in file:
        print("s")
        os.rename(os.path.join(file_path, file), os.path.join(file_path, str(count) + ".jpg"))
        count+=1
    else:
        print(file)
