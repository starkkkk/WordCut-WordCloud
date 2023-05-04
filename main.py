import jieba
from wordcloud import WordCloud
import PIL
import numpy as np
import matplotlib.pyplot as plt


# 分词
def cut_word(dictname,datafilename):
    # 加载自定义词典
    jieba.load_userdict(dictname)
    # 加载停用词
    stopwords = ['z', 'b', 'c']
    txt = open(datafilename,'r',encoding='utf-8').read()

    wordsls=jieba.lcut(txt)
    wcdict={}
    for word in wordsls:
        if len(word)==1:
            continue
        else:
            if word not in stopwords:
                wcdict[word]=wcdict.get(word,0)+1
    wclist = sorted(wcdict.items(), key=lambda x: x[1], reverse=True)
    return wclist


#制作词云图  “background.png”为背景形状   “mysh.ttc”是字体，这里选用微软雅黑  “cloud.png”为输出图片名称
def word_cloud(wlist):
    wordDict = {}
    for tup in wlist[:n]:
        wordDict[tup[0]] = tup[1]
    image_background = PIL.Image.open('./word_cloud/bg1.png')
    MASK = np.array(image_background)
    wc = WordCloud(font_path='./word_cloud/msyh.ttc',background_color='white', width=4000, height=4000, margin=10, max_words=2000, mask =MASK).fit_words(wordDict)
    plt.imshow(wc)
    plt.show()
    wc.to_file('./word_cloud/cloud.png')


if __name__ == '__main__':
    n = 500

    # 分词
    wordList = cut_word('.\data\dict.txt', r'.\data\test_data.txt')
    # 显示出现次数最多的n个词语
    print(wordList[:n])

    # 绘制词云图
    word_cloud(wordList)