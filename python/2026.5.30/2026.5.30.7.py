import jieba
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 文件路径（请根据实际调整）
names_path = r'python\2026.5.30\三国人名汇总.txt'
text_path  = r'python\2026.5.30\三国演义.txt'
encodings = ['utf-8', 'gbk', 'gb18030']

# ---------- 1. 读取人物名单 ----------
names = []
for enc in encodings:
    try:
        with open(names_path, 'r', encoding=enc) as f:
            names = [line.strip() for line in f.readlines() if line.strip()]
        print(f"成功读取人物列表 ({len(names)} 个名字，编码 {enc})")
        break
    except UnicodeDecodeError:
        continue
if not names:
    print("无法读取人物名单，请检查文件编码。")
    exit(1)

# ---------- 2. 读取《三国演义》全文 ----------
text = ''
for enc in encodings:
    try:
        with open(text_path, 'r', encoding=enc) as f:
            text = f.read()
        print(f"成功读取三国演义全文（编码 {enc}）")
        break
    except UnicodeDecodeError:
        continue
if not text:
    print("无法读取小说文本。")
    exit(1)

# ---------- 3. 加载自定义词典（人名列表） ----------
for name in names:
    jieba.add_word(name)  # 确保人名被完整切分

# ---------- 4. 对全文进行分词，统计词频 ----------
words = jieba.lcut(text)              # 精准模式分词
word_count = {}
for w in words:
    if w in names:                    # 只统计在人物名单中的词
        word_count[w] = word_count.get(w, 0) + 1

# ---------- 5. 筛选 > 100 次的人物 ----------
count_dict = {k: v for k, v in word_count.items() if v > 100}

if not count_dict:
    print("没有出现次数超过 100 次的人物。")
    exit()

# ---------- 6. 绘制柱状图 ----------
plt.figure(figsize=(12, 6))
plt.bar(count_dict.keys(), count_dict.values(), color='cornflowerblue')
plt.xticks(rotation=90)
plt.title('《三国演义》中人物出现次数（超过100次）—— jieba分词版')
plt.xlabel('人物名字')
plt.ylabel('出现次数')
plt.tight_layout()
plt.show()