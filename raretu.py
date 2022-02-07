#単純多角形から凸多面体を折ることができるか
#チャック接着で検証
#一般化
import numpy as np
import copy

M=14
v1=[90,270,90,90,270,180,90,90,180,270,90,90,270,90]
N1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]

v=[[90,270,90,90,270,180,90,90,180,270,90,90,270,90],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0]]
N=[[1,2,3,4,5,6,7,8,9,10,11,12,13,14],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0]]

T1=[[0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]]

V=[[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14]],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0]]
DOU=[]
T=[]

#チャック折り可否判定 0:可能 1:不可能
def check(i,n):
    i1=i % (M-2*n)
    i2=(i-1) % (M-2*n)
    i3=(i+1) % (M-2*n)
    if (v[n][i3]+v[n][i2])<361:
        return 0
    elif n==(int(M/2)-1):
        return 0
    else:
        return 1

def ori(i,n):
    i1=i % (M-2*n)
    i2=(i-1) % (M-2*n)
    i3=(i+1) % (M-2*n)
    v2=copy.deepcopy(v[n])
    N2=copy.deepcopy(N[n])
    V2=copy.deepcopy(V[n])
    tmp1=v2[i1]
    tmp2=v2[i2]
    tmp3=v2[i3]
    v2[i1]=tmp1
    v2[i2]=tmp2+tmp3
    v2[i3]=tmp2+tmp3
    V_1=V2[N2[i2]-1]
    V_2=V2[N2[i3]-1]
    for i in range(len(V_1)):
        for j in range(len(V_2)):
            y=V_2[j] in V2[V_1[i]-1]
            if y==False:
                V2[V_1[i]-1].append(V_2[j])
    for i in range(len(V_2)):
        for j in range(len(V_1)):
            y=V_1[j] in V2[V_2[i]-1]
            if y==False:
                V2[V_2[i]-1].append(V_1[j])
    if i2>i3:
        if i1<i2:
            v2.pop(i2);v2.pop(i1)
            N2.pop(i2);N2.pop(i1)
        else:
            v2.pop(i1);v2.pop(i2)
            N2.pop(i1);N2.pop(i2)
    else:
        if i1<i3:
            v2.pop(i3);v2.pop(i1)
            N2.pop(i3);N2.pop(i1)
        else:
            v2.pop(i1);v2.pop(i3)
            N2.pop(i1);N2.pop(i3)
    v2.extend([0,0])
    N2.extend([0,0])
    v[n+1]=v2;N[n+1]=N2
    V[n+1]=V2

def saiki(i,n):
    ori(i,n)
    T1[n]=N[n][i]
    n=n+1
    for j in range(M-2*n):
        v[n+2]=v[n+1];N[n+2]=N[n+1]
        if check(j,n)==0:
            if n==(int(M/2-1)):
                saikiend(j,n)
            else:
                saiki(j,n)

def saikiend(i,n):
    ori(i,n)
    T1[n]=N[n][i]
    T2=copy.deepcopy(T1)
    T.append(T2)
    DOU.append(V[n+1])

def main():
    for i in range(int(M/2)):
        V[0]=[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14]]
        n=0 #カウンタ n=0が始点
        if check(i,n)==0:
            saiki(i,n)
    for i in range(len(DOU)):
        for j in range(len(DOU[i])):
            DOU[i][j].sort()
        DOU[i].sort()
    #同値分類
    #まず左右対称
    B=[]
    for i in range(len(DOU)):
        B.append([])
        for j in range(len(DOU[i])):
            B[i].append([])
            for k in range(len(DOU[i][j])):
                B[i][j].append(15-DOU[i][j][k])
            B[i][j].sort()
        B[i].sort()
    #同値でないものの数え上げ
    tmp=[0]
    for i in range(len(T)):
        m=0
        for j in range(len(tmp)):
            if DOU[tmp[j]]==DOU[i]:
                m=m+1
            if DOU[tmp[j]]==B[i]:
                m=m+1
        if m==0:
            tmp.append(i)
    print("同値")
    print(len(tmp))
    for i in range(len(tmp)):
        print(T[tmp[i]])
        print(DOU[tmp[i]])

if __name__ == "__main__":
    main()
