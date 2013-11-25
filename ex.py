from collections import Counter
def check(header,data):
    l=data.rstrip("\n").split(",")
    header=header.rstrip("\n").split(",")
    #print l
    d=Counter()
    j=2
    v=2
    for i in range(len(l[2:])):
        d[header[j]]=l[v]
        j=j+1
        v=v+1
    new=[]
    new.append(l[0])
    new.append(l[1])
    new.append(d.most_common(1)[0][0])
    new.append(d.most_common(1)[0][1])
    return new

def f1():
    new_list=[]
    fp=open("Book1.csv","r")
    lines=fp.readlines()
    for dat in lines[1:]:
        s=check(lines[0],dat)
        new_list.append(s)
    print "***Highest share price companys (year and month wise) *****"
    for n in new_list:
        print n
    

if __name__ == '__main__' :
    f1()
    
    
    

