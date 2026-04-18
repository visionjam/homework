def charfreq(s):
    s_upper = s.upper()
    freq = {}
    for char in s_upper:
        if 'A' <= char <= 'Z':
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq

a = input("请输入英文句子：")
result = charfreq(a)
print(result)