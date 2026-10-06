from .constants import OPR,NUM,STRL,NUML
from .errors import errorlist
def calculaTORR(base:str):
    stack,stackd,compiled,tempc,errstream=list(),list(),list(),'',''
    check=base.split()
    base+='#'
    def isnumber(a):
        try:
            float(a)
            return True
        except ValueError:
            return False
    def contains(a,b):
        k=0
        for i in range(len(b)):
            if b[i]==a:k+=1
        if k>0: return True
        else: return False
    def minel(a,b):
        r,i=int,(len(b)-1)
        while i>=0:
            if b[i]==a:r=i
            i-=1
        return r
    def hrc(a):
        if a=='*': return 3
        if a=='/': return 3
        if a=="+": return 2
        if a=="-": return 2
    def calc(a,b,c):
        if c=='+': return str(float(a)+float(b))
        if c=='/': return str(float(a)/float(b))
        if c=='-': return str(float(a)-float(b))
        if c=='*': return str(float(a)*float(b))
    if base.count(' ')==len(base)-1:
        errstream+=errorlist[0]
    if contains(' ',base):
        if len(check)>=2:
            for i in range(len(check)-1):
                if isnumber(check[i]) and isnumber(check[i+1]):
                    errstream+=errorlist[7]
    base=base.replace(' ','')       
    for i in range(len(base)+10):
        compiled.append(' ') 
    stack.append(' ')
    stackd.append(0)
    for i in range(len(base)):
        if (contains(base[i],NUM)==False and contains(base[i],OPR)==False and base[i]!='.') and (i<(len(base)-1)):
            errstream+=errorlist[1]  
        if contains(base[i],NUM) or base[i]=='.':
            if i==(len(base)-2):
                tempc+=base[i]
                compiled[minel(' ',compiled)]=tempc
                tempc=''
            if contains(base[i+1],OPR)==False:tempc+=base[i] 
            elif i != (len(base)-2):
                tempc+=base[i]
                compiled[minel(' ',compiled)]=tempc
                tempc=''
        if contains(base[i],OPR):
            if (contains(base[i],OPR) and (contains(base[i-1],OPR))) and not((contains(base[i],OPR[:-2]) and contains(base[i-1],OPR[:-2]))or(contains(base[i-1],OPR[-2:]) and contains(base[i],OPR[:-2]))):
                errstream+=errorlist[3]
            else:         
                if base[i]=='-':
                    if i==0:tempc+=base[i]
                    elif contains(base[i-1],OPR):tempc+=base[i]
                if base[i]=='+':
                    if i==0:tempc+=base[i]
                    elif contains(base[i-1],OPR):tempc+=base[i]
                if stackd[len(stackd)-1]>=hrc(base[i]) and contains(base[i],tempc)==False:
                    compiled[minel(' ',compiled)]=stack[len(stack)-1]
                    stack=stack[:-1]
                    stack.append(base[i])
                    stackd=stackd[:-1]
                    stackd.append(hrc(base[i]))
                elif contains(base[i],tempc)==False:
                    stack.append(base[i])
                    stackd.append(hrc(base[i]))
        if base[i]=='#':
            while len(stack)>0:
                compiled[minel(' ',compiled)]=stack[len(stack)-1]
                stack=stack[:-1]
                stackd=stackd[:-1]
    for l in range(len(compiled)):
        if compiled[l]=='.':compiled[l]='0'
    for t in range(len(compiled)-2):
        if isnumber(compiled[t]) and isnumber(compiled[t+1]) and contains(compiled[t+2],OPR):
            if all(x=='0' or x=='.' for x in compiled[t+1]) and compiled[t+2]=='/':
                errstream+=errorlist[4]
    d,f=0,0
    for j in range(len(compiled)):
        if contains(compiled[j],OPR): d+=1
        if isnumber(compiled[j]):f+=1
    if d!=(f-1):errstream+=errorlist[2]
    i=0
    print(compiled)
    if errstream !='': return errstream
    else:                                       
        while compiled[1]!=' ':
            if isnumber(compiled[i]) and isnumber(compiled[i+1]) and contains(compiled[i+2],OPR):
                compiled[i]=calc(compiled[i],compiled[i+1],compiled[i+2])
                del compiled[i+1]
                del compiled[i+1]
                compiled.append(' ')
                compiled.append(' ')
                i+=1
            else:
                for k in range(minel(' ',compiled)):
                    if isnumber(compiled[k]) and isnumber(compiled[k+1]) and contains(compiled[k+2],OPR): 
                        i=k           
        if errstream!='':return errstream
        elif float(compiled[0])-float(int(float(compiled[0])))==0.0:return str(int(float(compiled[0])))
        else: return compiled[0]
def converTORR(base:str,inu:str,outu:str):
    def contains(a,b):
        k=0
        for i in range(len(b)):
            if b[i]==a:k+=1
        if k>0: return True
        else: return False
    def change(a):
        for i in range(len(STRL)):
            for j in range(len(STRL[i])):
                if STRL[i][j]==a: return NUML[i][j]
    def isnumber(a):
        try:
            float(a)
            return True
        except ValueError:
            return False             
    k,res,errstream,rstr,ws=0,0.0,'','',['','']
    ws[0]=base
    ws[1]=inu
    expect=outu
    if isnumber(ws[0])==False :
        errstream+=errorlist[7]   
    else:       
        for l in range(len(STRL)):
            if contains(ws[1].lower(),STRL[l])==False:
                k+=1
            if k==3: errstream+=errorlist[5]
        k=0    
        for v in range(len(STRL)):    
            if contains(expect.lower(),STRL[v])==False:
                k+=1
            if k==3: errstream+=errorlist[5]        
        if errstream=='':
            k=0
            for n in range(len(STRL)):
                if (contains(ws[1].lower(),STRL[n]) and contains(expect.lower(),STRL[n]))==False:
                    k+=1
                    if k==3:errstream+=errorlist[6]
                elif errstream=='':
                    if contains(ws[1].lower(),STRL[1]) or contains(ws[1].lower(),STRL[0]):
                        res=(change(ws[1].lower())/change(expect.lower()))*float(ws[0])
                    else:
                        if ws[1].lower()=='c' or ws[1].lower()=='k':
                            if ws[1].lower()=='k' and float(ws[0])<0:errstream+=errorlist[8]
                            elif ws[1].lower()=='c' and float(ws[0])<-273.15:errstream+=errorlist[8]
                            else:
                                if ws[1].lower()=='c' and expect.lower()=='k':
                                    res=float(ws[0])+273.15

                                if ws[1].lower()=='k' and expect.lower()=='c':
                                    res=float(ws[0])-273.15
                                if ws[1].lower()=='c' and expect.lower()=='f':
                                    res=float(ws[0])*1.8+32
                                if ws[1].lower()=='k' and expect.lower()=='f':
                                    res=(float(ws[0])-273.15)*1.8+32.0
                                if ws[1].lower()=='c' and expect.lower()=='c':
                                    res=float(ws[0])
                                if ws[1].lower()=='k' and expect.lower()=='k':
                                    res=float(ws[0])  
                        else:
                            if float(ws[0])<(-459.67):errstream+=errorlist[7]
                            else:
                                if expect.lower()=='k':
                                    res=(float(ws[0])-32.0)*1.8+273.15
                                if expect.lower()=='c':
                                    res=(float(ws[0])-32.0)/(1.8)
                                if expect.lower()=='f':    
                                    res=float(ws[0])
    if errstream!='':return errstream
    else:
        rstr=rstr+str(res)+' '+expect
        return rstr