import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointdist=defaultdict(float)
        final=[]
        for i in points:
            dist=math.sqrt(pow(i[0],2)+pow(i[1],2))
            pointdist[tuple(i)]=dist
        pointdist=sorted(pointdist,key=lambda x:pointdist[x])
        for j in range(0,k):
            final.append(list(pointdist)[j])
        return final