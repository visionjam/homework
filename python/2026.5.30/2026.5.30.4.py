import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 参数设置
a = 1  # 控制心形大小
theta = np.linspace(0, 2 * np.pi, 1000)  # θ从0到2π，取1000个点

# 根据参数方程计算坐标
rho = a * (1 - np.sin(theta))  # ρ = a(1 - sinθ)
x = rho * np.cos(theta)         # x = ρcosθ
y = rho * np.sin(theta)         # y = ρsinθ

# 创建绘图区
plt.figure(figsize=(8, 6))

# 绘制心形曲线
plt.plot(x, y, color='red', linewidth=2, label='心形曲线')

# 设置图表属性
plt.title('心形曲线-直角坐标系', fontsize=14, fontweight='bold')
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True, alpha=0.3, linestyle='--')
plt.axis('equal')  # 保持横纵轴比例一致
plt.legend()

# 显示图表
plt.tight_layout()
plt.show()