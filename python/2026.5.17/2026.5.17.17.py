from PIL import Image, ImageEnhance

# 打开原始图片
img = Image.open(r"C:\Users\29576\Downloads\origin.png")

# 创建对比度增强器
enhancer = ImageEnhance.Contrast(img)

# 将对比度提升为原来的 2 倍
enhanced_img = enhancer.enhance(2.0)

# 保存结果
enhanced_img.save('XP_contrast.jpg')

print("对比度增强后的图片已保存为 'XP_contrast.jpg'，请手动上传。")