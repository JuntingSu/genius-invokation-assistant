from PIL import Image
# import pandas as pd

from pandas import read_csv

# 初始化图片信息
cardlist = read_csv('cardlist.csv')
characterlist=read_csv('characterlist.csv')
# 行动牌图片列表
card_imgs=[]
# 角色牌图片列表
character_imgs=[]
# 读取图片
for j in range(len(cardlist)):
    img = Image.open("cardlist\\%d.png" % cardlist["ID"][j])
    card_imgs.append(img)
for j in range(len(characterlist)):
    img = Image.open("characterlist\\%d.png" % characterlist["ID"][j])
    character_imgs.append(img)

# 卡组的相对坐标，依次为：
# x0，y0：第一张牌的左上角坐标
# dx，dy：行动牌大小
# ix，iy：两张牌之间的横/纵坐标差
x0, y0, dx, dy, ix, iy = 251, 519, 96, 160, 114, 178
# 分享卡组中，角色牌的坐标：
# x1，y1：第一张牌的左上角坐标
# cx1，cy1：角色牌大小
# xc1：两张牌之间的横/纵坐标差
x1, y1, cx1, cy1, xc1 = 351, 177, 142, 238, 162
# 胜冠之试中，角色牌的坐标：
# x1，y1：第一张牌的左上角坐标
# cx1，cy1：角色牌大小
# xc1：两张牌之间的横/纵坐标差
x2, y2, cx2, cy2, xc2 = 589, 228, 96, 160, 114


# 将胜冠之试截图或者牌库截图拆分成3张角色牌+30张行动牌的图片数组
# filename：需要拆分的图片路径
# mode:表示图片是胜冠还是分享
# champion-胜冠，deck-分享
def split(filename, mode):
    img = Image.open(filename)
    img=img.resize((1200,1630))
    # 截取矩形部分
    deck = []
    # 胜冠之试——角色部分
    if mode == 'deck':
        for i in range(3):
            x = x1 + xc1 * i
            y = y1
            card_img=img.crop((x, y, x + cx1, y + cy1))
            card_img = card_img.resize((cx2, cy2))
            deck.append(card_img)
    # 卡组分享——角色部分
    elif mode == 'champion':
        for i in range(3):
            x = x2 + xc2 * i
            y = y2
            card_img = img.crop((x, y, x + cx2, y + cy2))
            deck.append(card_img)
    # 行动牌部分
    for j in range(30):
        x = x0 + ix * (j % 6)
        y = y0 + iy *int( (j - j % 6) / 6)
        deck.append(img.crop((x, y, x + dx, y + dy)))


    return deck

# 判断两张牌是否相同
def is_same_img(img1, img2,tol=10):
    # tol是允许的误差（一般来说1够用，如果识别失败可以尝试加大此值，但不建议加到20以上）
    image1_gray = img1.convert('L')
    image2_gray = img2.convert('L')

    pixel1 = list(image1_gray.getdata())
    pixel2 = list(image2_gray.getdata())

    diff = [abs(x - y) for x, y in zip(pixel1, pixel2)]
    avg_diff = sum(diff) / len(pixel1)

    return avg_diff < tol

# 将卡牌图片数组转换成ID数组和字符串数组
# 请输入一个图片数组，这个数组可以由split()函数提供
# 返回值共两个，第一个是数字数组，第二个是字符串
def toString(deck):
    deckcode = []
    deckstr = []
    # 转换角色部分
    for i in range(0,3):
        for j in range(len(characterlist)):
            if is_same_img(deck[i], character_imgs[j],20):
                deckcode.append(characterlist['ID'][j])
                deckstr.append(characterlist['name'][j])
                break
    #转换行动牌部分
    for i in range(3,len(deck)):
        if is_same_img(deck[i],deck[i-1]):
            deckcode.append(deckcode[-1])
            deckstr.append(deckstr[-1])
        else:
            for j in range(len(cardlist)):
                if is_same_img(deck[i], card_imgs[j],1):
                    deckcode.append(cardlist['ID'][j])
                    deckstr.append(cardlist['name'][j])
                    break
    dstr = ','.join(deckstr)
    return deckcode, dstr

# 将字符串代表的卡组生成卡组图片
def toDeck(s):
    ss = s.split(',')
    background = Image.open("module.png")
    card = card_imgs[0]
    c_card=card.resize((cx1, cy1))
    mask = Image.new('L', card.size, 255)
    c_mask = Image.new('L', c_card.size, 255)
    for i in range(3):
        for j in range(len(characterlist)):
            if ss[i] == characterlist['name'][j] or ss[i] == characterlist['ID'][j]:
                card = character_imgs[j]
                card = card.resize((cx1, cy1))
                position = (x1 + xc1 * i, y1)
                background.paste(card, position, c_mask)
                break

    for i in range(3,len(ss)):
        for j in range(len(cardlist)):
            if ss[i] == cardlist['name'][j] or ss[i] == cardlist['ID'][j]:
                card = Image.open("cardlist\\%d.png" % (cardlist['ID'][j]))
                position = (x0 + ix * ((i-3) % 6), int(y0 + iy * ((i-3) - (i-3) % 6) / 6))
                background.paste(card, position, mask)
                break
    return background


def get_size(member):
    if member=='card':
        return len(cardlist)
    elif member=='character':
        return len(characterlist)
def get_list(member):
    if member=='card':
        return cardlist
    elif member=='character':
        return characterlist

