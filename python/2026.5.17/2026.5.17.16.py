from PIL import Image, ImageFilter

# 打开原图
img = Image.open(r"C:\Users\29576\Downloads\origin.png")

# 应用浮雕滤镜
emboss_img = img.filter(ImageFilter.EMBOSS)

# 保存结果
emboss_img.save('XP_emboss.jpg')

print("已生成 XP_emboss.jpg，请手动上传此文件。")