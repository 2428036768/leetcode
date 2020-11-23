"""
用最少数量的箭引爆气球
中等
排序+贪心算法
按照xend排序
"""
def findMinArrowShots(points):
    if not points:
        print(0)
    points.sort(key=lambda balloon: balloon[1])   #按照xend排序
    pos=points[0][1]    #当前箭的位置
    ans=1

    for i in range(1,len(points)):
        if points[i][0]>pos:   #当前箭已经无法刺破气球i
            ans+=1             
            pos=points[i][1]   #更新箭的位置
    
    print(ans)

points = [[1,2],[2,3],[3,4],[4,5]]
findMinArrowShots(points)