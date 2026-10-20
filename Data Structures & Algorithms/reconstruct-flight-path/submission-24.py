class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)    
        def build(key):
            adj[key].sort()
            while adj[key]:
                destination = adj[key][0]
                adj[key].remove(destination)
                build(destination)
            output.append(key)
        output = []
        build("JFK")
        output.reverse()
            
        
        return output