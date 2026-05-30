import numpy as np
import matplotlib.pyplot as plt

# 设置参数
W0 = 200
H0 = 200

# 生成 t 的值，范围 0 到 2π，步长 0.01
t = np.arange(0, 2 * np.pi, 0.01)

# 计算 x 和 y 坐标
x = (2/3) * W0 * (np.cos(t)**3 + np.sin(t))
y = (2/3) * H0 * (np.sin(t)**3 + np.cos(t))

# 创建图形
plt.figure(figsize=(10, 8))

# 绘制曲线
plt.plot(x, y, 'b-', linewidth=2, label='参数曲线')

# 添加标题和标签
plt.title('参数方程曲线绘制', fontsize=16, fontproperties='SimHei')
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)

# 添加网格
plt.grid(True, alpha=0.3)

# 添加图例
plt.legend()

# 设置坐标轴比例相等，保证图形不变形
plt.axis('equal')

# 显示图形
plt.show()