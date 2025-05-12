class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set() #para rastrear os pontos ja incluidos no plano
        min_heap = [(0, 0)]  #(custo, índice do ponto), começando do ponto 
        total_cost = 0

        while len(visited) < n:
            cost, point = heapq.heappop(min_heap)
            if point in visited:
                continue
            
            #adicionar o ponto atual ao plano
            visited.add(point)
            total_cost += cost
            
            #adicionar todas as arestas que conectam este ponto a outros pontos ainda não visitados
            for next_point in range(n):
                if next_point not in visited:
                    distance = abs(points[point][0] - points[next_point][0]) + abs(points[point][1] - points[next_point][1])
                    heapq.heappush(min_heap, (distance, next_point))
        
        return total_cost
