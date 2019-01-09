import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('music_message_4.csv', header=None)
# 对收藏数取对数
dom = []
for i in df[3]:
    dom.append(np.log(int(i.replace('万', '0000'))))
df['collection'] = dom
# 设置图片显示属性,字体及大小
plt.rcParams['font.sans-serif'] = ['STXihei']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False
# 设置图片显示属性
fig = plt.figure(figsize=(16, 8), dpi=80)
ax = plt.subplot(1, 1, 1)
ax.patch.set_color('white')
# 设置坐标轴属性
lines = plt.gca()
# 设置坐标轴颜色
lines.spines['right'].set_color('none')
lines.spines['top'].set_color('none')
lines.spines['left'].set_color((64/255, 64/255, 64/255))
lines.spines['bottom'].set_color((64/255, 64/255, 64/255))
lines.xaxis.set_ticks_position('none')
lines.yaxis.set_ticks_position('none')
# 绘制直方图,设置直方图颜色
ax.hist(df['collection'], bins=30, alpha=0.7, color=(21/255, 47/255, 71/255))
ax.set_title('华语歌单收藏数量分布情况', fontsize=20)
# 显示图片
plt.show()