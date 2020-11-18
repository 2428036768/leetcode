"""
加油站
"""
def canCompleteCircuit(gas,cost):
    i=0
    n=len(gas)
    while i<n:
        sumGas=0
        sumCost=0
        cnt=0
        while cnt<n:
            j=(i+cnt)%n
            sumGas+=gas[j]
            sumCost+=cost[j]
            if sumGas<sumCost:  #如果不可达则跳出循环
                break
            cnt+=1
        if cnt==n:
            return i
        else:
            i=cnt+i+1     #以第一个不可达的站点为起点
    return -1

gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(canCompleteCircuit(gas,cost))
