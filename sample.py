
import GI_imgreader as GI
import GI_randomdeck as r

# 读取图片中的卡组信息
deck_1=GI.split('示例-胜冠之试.png', 'champion')
deck_2=GI.split('示例-卡组分享.png','deck')

c1,s1=GI.toString(deck_1)
c2,s2=GI.toString(deck_2)

print(c1)
print(c2)
print(s1)
print(s2)
# 将文字表述的卡组信息保存为图片
GI.toDeck(s1).save('GIoutput//new.png')
# 生成随机卡组
r.randeck(True,character='烟绯',path='随机卡组.png')

