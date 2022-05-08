import os
path = 'D:\桌面\pic'
count = 1
for file in os.listdir(path):
    os.rename(os.path.join(path,file),os.path.join(path,str(count)+"E.jpg"))
    count+=1
