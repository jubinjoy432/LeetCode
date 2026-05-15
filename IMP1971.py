#Find if Path Exists in Graph
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbors=defaultdict(list)
        for n1,n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)
        q=deque([source])
        seen=set([source])
        while q:
            node=q.popleft()
            if node==destination:
                return True
            for n in neighbors[node]:
                if n not in seen:
                    seen.add(n)
                    q.append(n)
        return False

