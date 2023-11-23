


value=[]
def base2value(str_4):
    ss=[ord(str_4[i]) for i in range(4)]
    res=[]
    for s in ss:
        if s==43:
            res.append(62)
        elif s==92:
            res.append(47)
        elif s==61:
            res.append(0)
        elif s<96:
            res.append(s-65)
        elif s>96:
            res.append(s-97+26)
    val=res[3]+64*(res[2]+64*(res[1]+64*res[0]))

    return val

def value2hex(value):
    val=value
    s=[]
    for i in range(6):
        s.append(val%16)
        val=int(val/16)

    return s

def delete(hex_array,character_id,seat):
    new_array=hex_array
    if seat%2==0:
        a=character_id%16
        b=int((character_id-a)/16)
        new_array[seat][1]=hex_array[seat][1]-a
        new_array[seat][4]=hex_array[seat][4]-b
    else:
        a=character_id%16
        b=int((character_id-a)/16)
        new_array[seat][2]=hex_array[seat][2]-a
        new_array[seat][3]=hex_array[seat][3]-b
    return new_array




# *************************************************************************************************88



# *****************************************************************************************************

def compare(s1,s2,index=0):
    e1=[s1[i:i+4] for i in range(0, len(s1), 4)]
    e2=[s2[i:i+4] for i in range(0, len(s2), 4)]
    for i in range(len(e2)):
        v1 = value2hex(base2value(e1[i]))
        v2 = value2hex(base2value(e2[i]))
        diff=[v1[i]-v2[i] for i in range(len(v1))]
        printarray(diff,i)
    return diff


def show(s1):
    val=[]
    e1 = [s1[i:i + 4] for i in range(0, len(s1), 4)]
    for i in range(len(e1)):
        v1 = value2hex(base2value(e1[i]))
        val.append(v1)
        printarray(v1, i)
    return val
def printarray(val,i=0):
    print('%d.%.2d--%.2d--%.2d--%.2d--%.2d--%.2d'%(i,val[0],val[1],val[2],val[3],val[4],val[5]))


def decode(s):
    data=s
    line = 0 #偶数
    # 修正
    # A位12-修正
    if data[line + 1][1]==12 or data[line + 1][1]==13 or data[line + 1][1]==14:
        data[line + 1][1]=data[line + 1][1]-12
        data[line + 1][2] = data[line + 1][2] +1
        data[line + 1][3] = int(( data[line + 1][3] +1 ) % 16)




    v1= data[line][1] + data[line][4] * 16
    if data[line + 1][1]==12 or data[line + 1][1]==13:
        v2= data[line + 1][2] + 2 + ((data[line + 1][3] + 1) % 16) * 16 + data[line][0] * 256
    else:
        v2= data[line + 1][2] + data[line + 1][3] * 16 + data[line][0] * 256
    v3=0

    return data

# s2=input('2.base64\n')
s=input('base64\n')
s2='APDwgA0IAADggXkIBxCQAHoABwCgAHsABwCwAHwABwDAAH0ABwDQAH4ABwDgAH8ABwAA'
s_blank='AADwAA0AAADgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
s_15='AADwAA0AAADgAEkABACQAEoABACgAEsABACwAHkABwCQAHoABwCgAHsABwCwAHwAAAAA'
s_name='AAAQAAIAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'

s_2='AHDQiAEIAIDwAHkABwCQAHoABwCgAHsABwCwAHwABwDAAH0ABwDQAIYACABgAIcACAAA'

val=show(s)
# v=decode(val)
#
# for i in range(len(v)):
#     printarray(v[i],i)
#
compare(s,s_2)



