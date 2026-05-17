from PIL import Image

# 打开原图
img = Image.open(r"C:\Users\29576\Downloads\origin.png")

# 上下翻转（垂直翻转）
flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)

# 保存结果
flipped_img.save('XP_flipped.jpg')

print("已生成 XP_flipped.jpg，请将此文件上传至所需位置。")