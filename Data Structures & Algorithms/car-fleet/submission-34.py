class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pands={}
        x=len(speed)
        for i in range(0,len(position)):
            pands[position[i]]=speed[i]
        position.sort(reverse=True)
        pands=dict(sorted(pands.items(),reverse=True))
        speed=list(pands.values())
        time=[(target-position[i])/speed[i] for i in range(0,len(speed))]
        while x>1:
            if time[-x]>=time[-x+1]:
                time.pop(-x+1)
            x-=1
        return len(time)