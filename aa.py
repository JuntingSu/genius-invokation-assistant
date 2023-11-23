import GI_imgreader as GI

s1='''重云,甘雨,菲谢尔,吐纳真定,吐纳真定,赌徒的耳环,赌徒的耳环,风龙废墟,风龙废墟,\
立本,立本,常九爷,常九爷,万家灶火,元素共鸣：交织之冰,元素共鸣：交织之冰,元素共鸣：粉碎之冰,\
元素共鸣：粉碎之冰,最好的伙伴！,最好的伙伴！,换班时间,换班时间,一掷乾坤,一掷乾坤,本大爷还没有输！,\
交给我吧！,重攻击,温妮莎传奇,温妮莎传奇,莲花酥,莲花酥,蒙德土豆饼,蒙德土豆饼
'''

GI.toDeck(s1,1).save('GIoutput//new1.png')



# deck_2=GI.split('4-2.png','deck')
# for i in range(12):
#     deck_2[i].save('GIoutput//card%d.png'%i)

# C:\python\python.exe E:\python\genius-invokation-assistant\aa.py
