n=int(input())
op=[]
for i in range(0,n):
    num=int(input())
    temp_dict={}
    for j in range(0,num):
        t1, t2 = map(str,input().split())
        if t1 not in temp_dict.keys():
            temp_dict[t1]=1
        else:
            temp_dict[t1]=temp_dict[t1]+1

    all_values = temp_dict.values()
    max_c = max(all_values)

    temp_dict=sorted(temp_dict.items(), key=lambda x: x[0], reverse=False)
    
    for temp in temp_dict:
        if temp[1]==max_c:
            op.append([temp[0], temp[1]])
            #print(temp[0]," ", temp[1])

for l in op:
    print(l[0]," ", l[1])
