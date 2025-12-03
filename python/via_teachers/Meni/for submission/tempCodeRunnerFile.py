def midMax(a:float, b:float, c:float) -> int:
    if b > a and b > c:
        return 1
    return 0


def countPeaks(heights:list[int])->int:
    count_hights=0
    for i in range(1,len(heights)-1):
        if midMax(heights[i-1],heights[i],heights[i+1])==1:
            count_hights+=1
    return(count_hights)
    
print(countPeaks([206,350,300,167,406,310,328,250,200,120,400,380,435,200,337,200]))