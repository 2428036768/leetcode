
def reconstructQueue(people):
    people.sort(key=lambda x: (x[0],-x[1]))
    ans=[[] for _ in range(len(people))]       #声明长度为n的空列表
    for person in people:
        space=person[1]+1           #用于判断该person前空多少格
        for i in range(len(people)):
            if not ans[i]:     #如果ans[i]为空
                space-=1
                if space==0:   #已经找到足够空格
                    ans[i]=person
    return ans

people=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(reconstructQueue(people))

