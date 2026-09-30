class Solution:
    def climbStairs(self, n: int) -> int:
        ax1=1
        ax2=2
        ax3=ax2+ax1
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            for i in range(0,n-3):
                ax1=ax2
                ax2=ax3
                ax3=ax1+ax2
            return ax3