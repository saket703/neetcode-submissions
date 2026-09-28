class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        h2=[i for i in range(len(heights))]
        h1=[i for i in h2[::-1]]

        stack1=[]
        stack2=[]
        final=[]
        prev=int()
        for i in range(len(heights)):
            while stack1 and heights[i]<heights[stack1[-1]]:
                prev=stack1.pop()
                h1[prev]=i-prev-1

            stack1.append(i)

        h2.reverse()
        heights.reverse()
        for j in range(len(heights)):
            while stack2 and heights[j]<heights[stack2[-1]]:
                prev=stack2.pop()
                h2[prev]=j-prev-1
            
            stack2.append(j)
        h2.reverse()
        heights.reverse()
        final=[x+y+1 for x,y in zip(h1,h2)]
        final=[a*b for a,b in zip(final,heights)]
        return max(final)