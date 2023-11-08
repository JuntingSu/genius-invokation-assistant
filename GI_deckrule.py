from pandas import read_csv

cardlist = read_csv('cardlist.csv')
characterlist=read_csv('characterlist.csv')


def same_xx(character_id_list,column):
    a= characterlist[column][character_id_list[0]]
    b= characterlist[column][character_id_list[1]]
    c= characterlist[column][character_id_list[2]]
    if a==b or a==c: return a
    if b==c: return b
    return 'null'
def search(file,context,column,return_column='name'):
    if file=='card':
        for i in range(len(cardlist)):
            if cardlist[column][i]==context:
                return cardlist[return_column][i]
    elif file=='character':
        for i in range(len(characterlist)):
            if characterlist[column][i]==context:
                return characterlist[return_column][i]

