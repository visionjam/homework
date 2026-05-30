import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 生成角度序列θ（0到2π，1000个点保证曲线平滑）
theta = np.linspace(0, 2 * np.pi, 1000)

# 2. 计算极径ρ（参数方程ρ = a(1 - sinθ)，这里取a=1）
a = 1
rho = a * (1 - np.sin(theta))

# 3. 创建极坐标绘图区
plt.figure(figsize=(8, 8))

# 4. 使用polar()函数绘制心形
plt.polar(theta, rho, color='blue', linewidth=2, label='ρ=1-(sinθ)')

# 5. 设置图表属性
plt.title('心形图案-极坐标系', fontsize=16, pad=20)
plt.thetagrids(np.arange(0, 360, 45),  # 设置角度刻度为45°间隔
               labels=[f'{angle}°' for angle in np.arange(0, 360, 45)])  # 显示角度标签
plt.grid(True, alpha=0.3, linestyle='--')  # 显示网格线
plt.legend(loc='upper right', fontsize=10)  # 显示图例

# 6. 显示图表
plt.tight_layout()
plt.show()