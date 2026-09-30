class MedianFinder:

    def __init__(self):
        self.array = []

        

    def addNum(self, num: int) -> None:
        self.array.append(num)
        self.array.sort()
        

    def findMedian(self) -> float:
        length = len(self.array)
        isOdd = length % 2
        if length == 1:
            return self.array[0]
        if isOdd:
            return self.array[length // 2]
        return (self.array[length // 2] + self.array[(length // 2) - 1]) / 2
        
        