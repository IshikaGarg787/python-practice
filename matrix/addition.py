m1=[[2,3,4],[4,5,6]]
m2=[[1,1,6],[8,1,2]]
r1=len(m1)
c1=len(m1[0])
r2=len(m2)
c2=len(m2[0])

if (r1,c1)==(r2,c2):
    m=eval(str([[0]*c1]*r1))
    for i in range(r1):
        for j in range(c1):
            m[i][j] = m1[i][j] +m2[i][j]
    print('matrix m1')
    for i in m1:
        print(*i)
    print('\nmatrix m2')
    for i in m2:
        print(*i)
    print('\naddition of matrix m')
    for i in m:
        print(*i,sep='\t')
else:
    print('invalid dimension for addition')                        