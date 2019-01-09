from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import pandas as pd
import jieba

df = pd.read_csv('music_message.csv', header=None)

text = ''
for line in df[2]:
    text += ' '.join(jieba.cut(line, cut_all=False))
backgroud_Image = plt.imread('job.jpg')
stopwords = set('')
stopwords.update(['封面', 'none介绍', '介绍', '歌单', '歌曲', '我们', '自己', '没有', '就是', '可以', '知道', '一起', '不是', '因为', '什么', '时候', '还是', '如果', '不要', '那些', '那么', '那个', '所有', '一样', '一直', '不会', '现在', '他们', '这样', '最后', '这个', '只是', '有些', '其实', '开始', '曾经', '所以', '不能', '你们', '已经', '后来', '一切', '一定', '这些', '一些', '只有', '还有'])

wc = WordCloud(
    background_color='white',
    mask=backgroud_Image,
    font_path='C:\Windows\Fonts\STZHONGS.TTF',
    max_words=2000,
    max_font_size=150,
    random_state=30,
    stopwords=stopwords
)
wc.generate_from_text(text)
# 看看词频高的有哪些,把无用信息去除
process_word = WordCloud.process_text(wc, text)
sort = sorted(process_word.items(), key=lambda e:e[1], reverse=True)
print(sort[:50])
img_colors = ImageColorGenerator(backgroud_Image)
wc.recolor(color_func=img_colors)
plt.imshow(wc)
plt.axis('off')
wc.to_file("活着.jpg")
print('生成词云成功!')

