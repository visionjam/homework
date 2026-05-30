import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体（防止中文乱码）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 1. 生成数据
x = np.linspace(-np.pi, np.pi, 50)  # 从-π到π生成50个点
y = np.sin(x)

# 2. 创建图形
plt.figure(figsize=(10, 6))

# 3. 使用scatter绘制sin函数曲线（彩色散点）
plt.scatter(x, y, c=y, cmap='rainbow', s=100, marker='*', label='sin(x)')

# 4. 绘制X轴和Y轴直线
plt.plot([-4, 4], [0, 0], 'b-', linewidth=2, label='X轴')  # X轴
plt.plot([0, 0], [-1.2, 1.2], 'orange', linewidth=2, label='Y轴')  # Y轴

# 5. 添加刻度标记文本
plt.text(-3.2, -0.15, '-π', fontsize=12, ha='center')
plt.text(0, -0.15, '0', fontsize=12, ha='center')
plt.text(3.2, -0.15, 'π', fontsize=12, ha='center')
plt.text(0.2, 1.1, 'Y', fontsize=12)
plt.text(3.8, -0.15, 'X', fontsize=12)

# 6. 设置标题和标签
plt.title('Sin函数曲线', fontsize=14)
plt.xlabel('')
plt.ylabel('')

# 7. 设置坐标轴范围
plt.xlim(-4, 4)
plt.ylim(-1.2, 1.2)

# 8. 添加网格（可选）
plt.grid(True, alpha=0.3)

# 9. 显示图形
plt.tight_layout()
plt.show()