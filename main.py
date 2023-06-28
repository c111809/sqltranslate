# 把tab转换成txt 1
import os

# 指定tab文件所在的目录路径
tab_dir = 'D:/pyt/table'

# 指定输出txt文件所在的目录路径
txt_dir = 'D:/pyt/tabletxt'

# 遍历tab文件所在的目录
for filename in os.listdir(tab_dir):
    # 判断文件是否以".tab"结尾
    if filename.endswith('.tab'):
        # 构造tab文件路径和对应的txt文件路径
        tab_path = os.path.join(tab_dir, filename)
        txt_path = os.path.join(txt_dir, filename[:-4] + '.txt')
        # 打开tab文件和对应的txt文件，并逐行读取和写入
        with open(tab_path, 'r') as tab_file, open(txt_path, 'w') as txt_file:
            for line in tab_file:
                txt_file.write(line.replace('\t', ','))  # 将tab符替换为逗号

