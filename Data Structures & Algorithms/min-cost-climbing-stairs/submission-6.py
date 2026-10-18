class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pointer=len(cost)
        total=0
        while pointer>3:
            if cost[pointer-1]>=cost[pointer-2]:
                pointer-=2
                total+=cost[pointer]
            else:
                if cost[pointer-1]+cost[pointer-3]>=cost[pointer-2]+cost[pointer-4]:
                    pointer-=2
                    total+=cost[pointer]
                    pointer-=2
                    total+=cost[pointer]
                else:
                    pointer-=1
                    total+=cost[pointer]
                    pointer-=2
                    total+=cost[pointer]
        if pointer==2:
                total+=min(cost[1],cost[0])
        if pointer==3:
                total+=min(cost[1],cost[0]+cost[2])
        return total