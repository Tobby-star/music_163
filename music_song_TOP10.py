import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('music_message_3.csv', header=None, names=['title'], encoding='utf-8-sig')
# 数据聚合分组
place_message = df.groupby(['title'])
place_com = place_message['title'].agg(['count'])
place_com.reset_index(inplace=True)
place_com_last = place_com.sort_index()
dom = place_com_last.sort_values('count', ascending=False)[0:10]
# 设置显示数据
names = [i for i in dom.title]
names.reverse()
nums = [i for i in dom['count']]
nums.reverse()
data = pd.Series(nums, index=names)
# 设置图片显示属性,字体及大小
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['font.size'] = 10
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
# 设置坐标轴刻度
lines.xaxis.set_ticks_position('none')
lines.yaxis.set_ticks_position('none')
# 绘制柱状图,设置柱状图颜色
data.plot.barh(ax=ax, width=0.7, alpha=0.7, color=(16/255, 152/255, 168/255))
# 添加标题,设置字体大小
ax.set_title('网易云音乐华语歌单歌曲 TOP10', fontsize=18, fontweight='light')
# 添加歌曲出现次数文本
for x, y in enumerate(data.values):
    plt.text(y+3.5, x-0.12, '%s' % y, ha='center')
# 显示图片
plt.show()
