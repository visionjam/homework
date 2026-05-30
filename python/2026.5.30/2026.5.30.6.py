import matplotlib.pyplot as plt

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 准备数据（请根据实际消费修改金额）
categories = ['学习用品', '日常用品', '伙食费', '通讯费', '娱乐费', '其他开支']
expenses = [300, 500, 1200, 150, 400, 250]  # 各项支出金额（元）

# 2. 创建绘图区
plt.figure(figsize=(8, 6))

# 3. 设置突出显示（可选，突出最大支出项）
explode = (0, 0, 0.1, 0, 0, 0)  # 第3项（伙食费）突出显示

# 4. 绘制饼图
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F']
plt.pie(expenses, 
        explode=explode,           # 突出显示
        labels=categories,          # 标签
        colors=colors,              # 颜色
        autopct='%1.1f%%',          # 显示百分比（1位小数）
        startangle=90,              # 起始角度（从90°开始）
        pctdistance=0.85,           # 百分比距离圆心的距离
        textprops={'fontsize': 11}  # 文字大小
        )

# 5. 添加标题
plt.title('每月消费支出比例图', fontsize=16, fontweight='bold', pad=20)

# 6. 添加图例（显示具体金额）
legend_text = [f'{cat}: ¥{exp}' for cat, exp in zip(categories, expenses)]
plt.legend(legend_text, loc='best', fontsize=10, bbox_to_anchor=(1.02, 1))

# 7. 保持圆形（避免椭圆变形）
plt.axis('equal')

# 8. 显示图表
plt.tight_layout()
plt.show()

# 可选：打印消费统计信息
print("=" * 40)
print("📊 月度消费统计")
print("=" * 40)
total = sum(expenses)
for cat, exp in zip(categories, expenses):
    percentage = (exp / total) * 100
    print(f"{cat:8s}: ¥{exp:5d}  ({percentage:5.1f}%)")
print("=" * 40)
print(f"总支出: ¥{total}")
print("=" * 40)