def disp_mat(ls):
    for i in ls:
        print(*i,sep='\t')

#main program
#if __name__=='main':
r,c=list(map(int,input().split()))  
M=[]
for i in range(r):
    ls=list(map(int,input().split()))
    M.append(ls) 
disp_mat(M)         