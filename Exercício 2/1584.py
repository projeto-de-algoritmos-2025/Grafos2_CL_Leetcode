class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set() 
        min_heap = [(0, 0)]  
        total_cost = 0

        while len(visited) < n:
            cost, point = heapq.heappop(min_heap)
            if point in visited:
                continue
            
            
            visited.add(point)
            total_cost += cost
            
            for next_point in range(n):
                if next_point not in visited:
                    distance = abs(points[point][0] - points[next_point][0]) + abs(points[point][1] - points[next_point][1])
                    heapq.heappush(min_heap, (distance, next_point))
        
        return total_cost
