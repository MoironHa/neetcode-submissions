class Solution:
    def findKthLargest(self, arr: List[int], k: int) -> int:
        def percolateDown(heap, i):
            while 2*i < len(heap):
                if 2 * i + 1 < len(heap) and heap[2*i] < heap[2*i+1] and heap[i] < heap[2*i+1]:
                    tmp = heap[i]
                    heap[i] = heap[2 * i + 1]
                    heap[2 * i + 1] = tmp
                    i = 2 * i + 1
                elif heap[2*i] > heap[i]:
                    tmp = heap[i]
                    heap[i] = heap[2 * i]
                    heap[2 * i] = tmp
                    i = 2 * i
                else:
                    break
            return heap
        
        def heapify(nums):
            nums.append(nums[0])
            heap = nums
            cur = (len(heap) - 1) // 2
            while cur > 0:
                i = cur
                percolateDown(heap, i)
                cur -= 1
            return heap
        def pop(heap):
            if len(heap) == 1:
                return None
            if len(heap) == 2:
                return heap[1]
            res = heap[1]
            heap[1] = heap.pop()
            percolateDown(heap, 1)
            return res

        maxHeap = heapify(arr)
        res = 0
        for i in range(k):
            res = pop(maxHeap)
        return res