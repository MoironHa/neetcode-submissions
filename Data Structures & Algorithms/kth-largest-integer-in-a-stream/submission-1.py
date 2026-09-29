class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [0]
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        self.heap.append(val)
        i = len(self.heap) - 1

        while i != 1 and self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2

        if len(self.heap) > self.k+1:
            self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
            self.heap.pop()
        i = 1
        while i * 2 < len(self.heap):
            if 2 * i + 1 < len(self.heap) and self.heap[2*i+1] < self.heap[2*i] and self.heap[i] > self.heap[2*i + 1]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i * 2 + 1]
                self.heap[i * 2 + 1] = tmp
                i = i * 2 + 1
            elif self.heap[2*i] < self.heap[i]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i * 2]
                self.heap[i * 2] = tmp
                i = i * 2
            else:
                break
        
        print(self.heap)
        return self.heap[1]
        
