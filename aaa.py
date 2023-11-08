


value=[]
def base2hex(str_4):
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

def hex2base(hex_val):
    val=hex_val
    s=[]
    for i in range(6):
        s.append(val%16)
        val=int(val/16)

    return s



s=input('base64\n')

equal_length_chunks = [s[i:i+4] for i in range(0, len(s), 4)]
print(equal_length_chunks)
print([0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3])
for i in equal_length_chunks:
    val=hex2base(base2hex(i))

    print('%.2d--%.2d--%.2d--%.2d--%.2d--%.2d'%(val[0],val[1],val[2],val[3],val[4],val[5]))

    # print(hex2base(base2hex(i)))
    # print(val)

