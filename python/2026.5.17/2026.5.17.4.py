import os
def count_names(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        count_daiyu = text.count('黛玉')
        count_baoyu = text.count('宝玉')
        return count_daiyu, count_baoyu

def name():
    file_path = r"C:\Users\29576\Downloads\红楼梦.txt"
    daiyu_count, baoyu_count = count_names(file_path)
    if daiyu_count is not None and baoyu_count is not None:
        print(f"黛玉出现次数: {daiyu_count}")
        print(f"宝玉出现次数: {baoyu_count}")

name()