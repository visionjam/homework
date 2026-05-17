from PIL import Image

# 打开原始图片
img = Image.open(r"C:\Users\29576\Downloads\origin.png")

# 直接调整尺寸为 256x256（会强制拉伸，因为原图比例可能不同）
# 如果你希望保持原图比例，请使用 thumbnail 代替 resize，但会得到非正方形的结果
thumb_256 = img.resize((256, 256), Image.LANCZOS)

# 保存结果
thumb_256.save('XP_256x256.jpg')

print("已生成 XP_256x256.jpg，请手动上传此文件。")