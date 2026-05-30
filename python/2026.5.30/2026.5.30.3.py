import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

img_array = np.zeros((200, 200, 3), dtype=np.uint8)
img_array[0:100, 0:100] = [255, 0, 0] 
img_array[0:100, 100:200] = [0, 255, 0]  
img_array[100:200, 0:100] = [0, 0, 255] 
img_array[100:200, 100:200] = [255, 255, 0] 

test_image = Image.fromarray(img_array)
test_image.save("test_image.png") 

im = np.array(test_image) 

hd = 256 * [0]
for i in range(im.shape[0]):
    for j in range(im.shape[1]):
        k = im[i, j, 0] * 0.3 + im[i, j, 1] * 0.59 + im[i, j, 2] * 0.11
        hd[int(k)] += 1

index = range(256)
bar_width = 1
plt.bar(index, hd, bar_width, alpha=1, color='k')
plt.title("图像灰度直方图（使用测试图像）")
plt.xlabel("灰度级 (0-255)")
plt.ylabel("像素数量")
plt.xlim(0, 256)
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.show()