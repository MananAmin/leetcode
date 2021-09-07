class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        ans = releaseTimes[0]
        index = 0
        for i in range(1,len(releaseTimes)):
            if releaseTimes[i] - releaseTimes[i-1] > ans or releaseTimes[i] - releaseTimes[i-1] >= ans and keysPressed[i]>keysPressed[index]:
                ans = releaseTimes[i] - releaseTimes[i-1]
                index = i
        return keysPressed[index]