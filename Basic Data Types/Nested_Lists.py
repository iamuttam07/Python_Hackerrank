if __name__ == '__main__':
    li=[]
    sc=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        li.append([name,score])
        sc.append(score)
    x=sorted(list(set(sc)))[1]
    for i,j in sorted(li):
        if j==x:
            print(i)

