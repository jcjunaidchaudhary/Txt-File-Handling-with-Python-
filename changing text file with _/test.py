f = open("Biology.txt", "r")
f2 = open("Biology_mod.txt", "w")
j=1
for i in f: 
    # snt=f.readline()
    sc=i.replace(" ", "_").strip()
    chap=sc+' = '+str(j)
    print(chap)
    f2.write(chap+"\n")
    j += 1
