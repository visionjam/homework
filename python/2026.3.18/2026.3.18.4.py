sentence = input("请输入一个字符句子：")
words = sentence.split()
if len(words) == 0:
    print("错误：句子中没有单词！")
else:
    max_length = 0    
    longest_words = []    
    for i in words:
        length = len(i)
        if length > max_length:
            max_length = length
            longest_words = [i]
        elif length == max_length:
            longest_words.append(i)

    if len(longest_words) == 1:
        print(f"最长的单词是：{longest_words[0]},长度是：{max_length}")
    else:
        a = ""
        for i in range(len(longest_words)):
            if i == 0:
                a = longest_words[i]
            else:
                a = a + "," + longest_words[i]
        print(f"最长的单词是：{a},长度是：{max_length}")