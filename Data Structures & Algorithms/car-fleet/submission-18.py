class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pands={}
        threshold=0
        fleets=len(speed)
        for i in range(0,len(position)):
            pands[position[i]]=speed[i]
        position.sort(reverse=True)
        pands=dict(sorted(pands.items(),reverse=True))
        speed=list(pands.values())
        time=[(target-position[i])/speed[i] for i in range(0,len(speed))]
        for i in range(0,len(speed)-1):
            if time[threshold]>=time[i+1]:
                fleets-=1
            else:
                threshold=i+1
        return fleets