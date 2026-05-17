from PIL import Image

# 打开原图
img = Image.open(r"C:\Users\29576\Downloads\origin.png")

# 方法一：直接调整尺寸（保持宽高比，128:72 与原始 1024:768 比例一致）
thumb = img.resize((128, 72), Image.LANCZOS)  # LANCZOS 为高质量重采样滤镜

# 或者使用 thumbnail 方法（自动保持比例，同样会得到 128x72）
# img.thumbnail((128, 72), Image.LANCZOS)
# thumb = img

# 保存缩略图
thumb.save('XP_thumb.jpg')

print("缩略图已保存为 'XP_thumb.jpg'")