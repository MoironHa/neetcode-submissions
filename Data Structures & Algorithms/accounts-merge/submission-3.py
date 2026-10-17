class UnionFind:
    def __init__(self, accounts):
        self.par = {}
        self.name = {}
        self.rank = {}
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                if accounts[i][j] not in self.par:
                    self.par[accounts[i][j]] = accounts[i][j]
                    self.name[accounts[i][j]] = accounts[i][0]
                    self.rank[accounts[i][j]] = 0

    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1 = self.find(n1)    
        p2 = self.find(n2)
        if p1 != p2:
            if self.rank[p1] > self.rank[p2]:
                self.par[p2] = self.par[p1]
            if self.rank[p1] < self.rank[p2]:
                self.par[p1] = self.par[p2]
            else:
                self.par[p1] = self.par[p2]
                self.rank[p2] += 1


        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        UF = UnionFind(accounts)
        for account in accounts:
            for i in range(2, len(account)):
                UF.union(account[1], account[i])
        res = []
        dictionary = {}
        for email in UF.par:
            rep = UF.find(email)
            if rep not in dictionary:
                dictionary[rep] = set()
            dictionary[rep].add(email)
        for key, value in dictionary.items():
            name = UF.name[key]
            sortedList = sorted(value)
            ans = []
            ans.append(name)
            for val in sortedList:
                ans.append(val)
            res.append(ans)
        return res