cleaned=[]
def vacum(position):
    if position in cleaned:
        print("Already cleaned : ", position)
    else:
        print("start cleaning : ")
        cleaned.append(position)
vacum((1,0))
vacum((1,0))
