with open('GoldLabel.txt') as fp, open('AFINNdata.txt') as f2:
    line = fp.readline()
    line2 = f2.readline()
    neg_count = 0
    neg_correct = 0
    
    pos_count = 0
    pos_correct = 0
    
    neu_count = 0
    neu_correct = 0
    cnt = 0
    while line:
        if line.strip() == "Negative":
            if line.strip() == line2.strip():
                neg_correct += 1
                print ("Correct")
            else:
                print ("Wrong")
            neg_count += 1
            
        
        if line.strip() == "Neutral":
            if line.strip() == line2.strip():
                neu_correct += 1
                print ("Correct")
            else:
                print ("Wrong")
            neu_count += 1

        if line.strip() == "Positive":
            if line.strip() == line2.strip():
                pos_correct += 1
                print ("Correct")
            else:
                print ("Wrong")
            pos_count += 1



        line = fp.readline()
        line2 = f2.readline()
        cnt +=1
pos_result = float(pos_correct/pos_count)
neg_result = float(neg_correct/neg_count)
neu_result = float(neu_correct/neu_count)
print(cnt)
print(str(pos_correct)+"/"+str(pos_count)+"= "+str(pos_result))
print(str(neg_correct)+"/"+str(neg_count)+"= "+str(neg_result))
print(str(neu_correct)+"/"+str(neu_count)+"= "+str(neu_result))

"""
with open('GoldOut.txt') as fp, open('Vaderdata.txt') as f2:
    line = fp.readline()
    line2 = f2.readline()
    neg_count = 0
    neg_correct = 0
    
    pos_count = 0
    pos_correct = 0
    
    neu_count = 0
    neu_correct = 0
    cnt = 0
    while line:
        if line.strip() == "Negative":
            if line.strip() == line2.strip():
                neg_correct += 1
                print (line.strip() + ":" + line2.strip() + "   CORRECT")
            else:
                print (line.strip() + ":" + line2.strip() + "   WRONG")
            neg_count += 1
        
        
        if line.strip() == "Neutral":
            if line.strip() == line2.strip():
                neu_correct += 1
                print (line.strip() + ":" + line2.strip() + "   CORRECT")
            else:
                print (line.strip() + ":" + line2.strip() + "   WRONG")
            neu_count += 1
        
        if line.strip() == "Positive":
            if line.strip() == line2.strip():
                pos_correct += 1
                print (line.strip() + ":" + line2.strip() + "   CORRECT")
            else:
                print (line.strip() + ":" + line2.strip() + "   WRONG")
            pos_count += 1
        
        
        
        line = fp.readline()
        line2 = f2.readline()
        cnt +=1
pos_result = float(pos_correct/pos_count)
neg_result = float(neg_correct/neg_count)
neu_result = float(neu_correct/neu_count)
print(cnt)
print(str(pos_correct)+"/"+str(pos_count)+"= "+str(pos_result))
print(str(neg_correct)+"/"+str(neg_count)+"= "+str(neg_result))
print(str(neu_correct)+"/"+str(neu_count)+"= "+str(neu_result))

"""
