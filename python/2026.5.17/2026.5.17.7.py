import jieba
import re
from collections import Counter

with open(r"C:\Users\29576\Desktop\TJ.txt", "r", encoding='utf-8') as f:
    txt = f.read()

words = jieba.lcut(txt)

filtered = [w for w in words if re.match(r'^[\u4e00-\u9fff]+$', w) and len(w) in (2, 3, 4)]

words_2 = [w for w in filtered if len(w) == 2]
words_3 = [w for w in filtered if len(w) == 3]
words_4 = [w for w in filtered if len(w) == 4]

c2 = Counter(words_2)
c3 = Counter(words_3)
c4 = Counter(words_4)

top2 = c2.most_common(1)[0]
top3 = c3.most_common(1)[0]
top4 = c4.most_common(1)[0]

for word, count in [top2, top3, top4]:
    print(f"{word},{count}")