def arithmetic_arranger(lst,result=False):
    if len(lst)>5: return "Error: Too many problems."
    tdict={}
    l1=""
    l2=""
    l3=""
    l4=""
    for i in range(len(lst)):
        tdict[i]=lst[i].split()

    for i in range(len(tdict)):
        if tdict[i][0].isnumeric()==False or tdict[i][2].isnumeric()==False: return "Error: Numbers must only contain digits."
        if len(tdict[i][0])>4 or len(tdict[i][2])>4: return "Error: Numbers cannot be more than four digits."
        mxlen=len(max(tdict[i],key=len))
        if tdict[i][1]=="+":
            tdict[i].append(int(tdict[i][0])+int(tdict[i][2]))
        elif tdict[i][1]=="-":
            tdict[i].append(int(tdict[i][0])-int(tdict[i][2]))
        else:
            return "Error: Operator must be '+' or '-'."
        if i==0:
            l1+=tdict[i][0].rjust(mxlen+2)
            l2+=tdict[i][1].ljust(2)+tdict[i][2].rjust(mxlen)
            l3+="-"*(mxlen+2)
            l4+=str(tdict[i][3]).rjust(mxlen+2)
        else:
            l1+=" "*4+tdict[i][0].rjust(mxlen+2)
            l2+=" "*4+tdict[i][1].ljust(2)+tdict[i][2].rjust(mxlen)
            l3+=" "*4+"-"*(mxlen+2)
            l4+=" "*4+str(tdict[i][3]).rjust(mxlen+2)
    if result==True:
        return l1+"\n"+l2+"\n"+l3+"\n"+l4
    else:
        return l1+"\n"+l2+"\n"+l3
