
import random as r
import GI_imgreader as GI
import GI_deckrule as dr

# 生成随机卡组：
# better：卡组合理等级
# 0-完全随机
# 1-不会出现无法装备的武器
# 2+：还没做
# character：指定卡组包含某一角色
# card：还没做
# same_country：还没做
# same_element：还没做

def randeck(better=0, character='0', card=0, same_country=0, same_element=0,path='random.png'):
    a=GI.get_size('card')
    b=GI.get_size('character')
    if character=='0':
        cc = r.sample(range(1, b), 3)
    else:
        cc=r.sample(range(1, b), 3)
        c_append=dr.search('character', character, 'name','ID')-2000
        if c_append not in cc:
            cc[0]=c_append
    cc.sort()
    c_deck=[GI.characterlist['name'][x] for x in cc]
    if same_country==0:
        same_country=dr.same_xx(cc,'阵营')
    if same_element == 0:
        same_element=dr.same_xx(cc,'元素')

    weapon=[]
    if better>0:
        weapon=[dr.search('character',x,'name','武器') for x in c_deck]

    valid_cardlist=[]
    valid_cardlist.append(dr.search('card',c_deck[0],'C3'))
    valid_cardlist.append(dr.search('card',c_deck[1],'C3'))
    valid_cardlist.append(dr.search('card',c_deck[2],'C3'))
    for i in range(a):
        if GI.cardlist['C2'][i]=='阵营' and GI.cardlist['C3'][i]!=same_country:
            continue
        elif GI.cardlist['C2'][i]=='共鸣' and GI.cardlist['C3'][i]!=same_element:
            continue
        elif GI.cardlist['C1'][i]=='天赋牌':
            continue
        elif better>0 and GI.cardlist['C2'][i]=='武器' and (GI.cardlist['C3'][i] not in weapon):
            continue
        else:
            valid_cardlist.append(GI.cardlist['name'][i])
            if GI.cardlist['C2'][i]!='秘传':
                valid_cardlist.append(GI.cardlist['name'][i])

    c = r.sample(range(1, len(valid_cardlist)), 30)
    c.sort()

    deck=[valid_cardlist[x] for x in c]

    ccstr=','.join(c_deck)
    cstr = ','.join(deck)

    res=','.join([ccstr,cstr])

    deck_img=GI.toDeck(res)
    deck_img.save('GIoutput//%s'%path)
    return res



