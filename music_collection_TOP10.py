import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('music_message_4.csv', header=None)
# 数据清洗
dom = []
for i in df[3]:
    dom.append(int(i.replace('万', '0000')))
df['collection'] = dom
# 数据排序
names = df.sort_values(by='collection', ascending=False)[0][:10]
collections = df.sort_values(by='collection', ascending=False)['collection'][:10]
# 设置显示数据
names = [i for i in names]
names.reverse()
collections = [i for i in collections]
collections.reverse()
data = pd.Series(collections, index=names)
# 设置图片显示属性,字体及大小
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['font.size'] = 8
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
data.plot.barh(ax=ax, width=0.7, alpha=0.7, color=(8/255, 88/255, 121/255))
# 添加标题,设置字体属性
ax.set_title('网易云音乐华语歌单收藏 TOP10', fontsize=18, fontweight='light')
# 添加歌单收藏数量文本
for x, y in enumerate(data.values):
    num = str(y/10000)
    plt.text(y+20000, x-0.08, '%s' % (num + '万'), ha='center')
# 显示图片
plt.show()
