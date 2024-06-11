class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        tempIndices = []

        for currIndex, currValue in enumerate(temperatures):
            while tempIndices and temperatures[tempIndices[-1]] < currValue:
                prevIndex = tempIndices.pop()
                answer[prevIndex] = currIndex - prevIndex
            tempIndices.append(currIndex)
        
        return answer
