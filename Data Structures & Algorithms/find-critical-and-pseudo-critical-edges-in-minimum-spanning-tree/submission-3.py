class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1  
        return True
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        critics = set()
        pseudos = set()
        if len(edges) == n - 1:
            for i in range(n-1):
                critics.add(i)
            return [list(critics), list(pseudos)]
        minHeap = []
        for u, v, w in edges:
            heapq.heappush(minHeap, ((w, u, v)))
        mst = []
        mstW = 0
        UF = UnionFind(n)
        while len(mst) < n - 1:
            w, u, v = heapq.heappop(minHeap)
            if not UF.union(u, v):
                continue
            mst.append([u, v])
            mstW += w
        i = 0
        for x, y, w in edges:
            minHeap = []
            for u, v, w1 in edges:
                if (u, v) != (x, y):
                    heapq.heappush(minHeap, ((w1, u, v)))
            mst = []
            newMstW = 0
            UF = UnionFind(n)
            while len(mst) < n - 1 and minHeap:
                w2, u, v = heapq.heappop(minHeap)
                if not UF.union(u, v):
                    continue
                mst.append([u, v])
                newMstW += w2
            if len(mst) < n - 1 or newMstW > mstW:
                    critics.add(i)
            i += 1
        UF = UnionFind(n)
        i = 0
        for x, y, w in edges:
            minHeap = []
            for u, v, w1 in edges:
                # if (u, v) != (x, y):
                    heapq.heappush(minHeap, ((w1, u, v)))
            mst = []
            mst.append([x, y])
            newMstW = w
            UF = UnionFind(n)
            UF.union(x, y)
            while len(mst) < n - 1 and minHeap:
                w2, u, v = heapq.heappop(minHeap)
                if not UF.union(u, v):
                    continue
                mst.append([u, v])
                newMstW += w2

            if newMstW == mstW and i not in critics:
                    pseudos.add(i)
            i += 1

        
        return [list(critics), list(pseudos)]


