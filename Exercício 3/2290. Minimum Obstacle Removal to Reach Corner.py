from heapq import heappop, heappush
from typing import List

class Solution:
    """
    Conta o número de pares de nós que não são alcançáveis um do outro em um grafo não direcionado.
    
    Parâmetros:
    - n (int): Número total de nós no grafo.
    - edges (List[List[int]]): Lista de arestas, onde cada aresta é representada como [a, b],
      indicando que existe uma aresta não direcionada entre os nós 'a' e 'b'.
    
    Retorna:
    - int: O número de pares de nós que não são alcançáveis um do outro.
    
    Descrição:
    O grafo é considerado como uma coleção de componentes conectados. Para cada componente,
    calculamos o número de pares de nós dentro dele e o número de pares não alcançáveis
    entre componentes distintos. O resultado é a diferença entre o número total de pares
    possíveis e o número de pares alcançáveis.
    """
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # Movimentos: cima, baixo, esquerda, direita
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Fila de prioridade com (custo, x, y)
        heap = [(0, 0, 0)]
        # Matriz de custos iniciada com um valor alto
        cost = [[float('inf')] * n for _ in range(m)]
        cost[0][0] = 0
        
        while heap:
            curr_cost, x, y = heappop(heap)
            
            # Se chegarmos ao canto inferior direito, retornamos o custo
            if x == m - 1 and y == n - 1:
                return curr_cost
            
            # Verificar movimentos possíveis
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n:
                    # Calcular novo custo
                    new_cost = curr_cost + grid[nx][ny]
                    
                    # Se o novo custo for menor, atualizamos e empilhamos
                    if new_cost < cost[nx][ny]:
                        cost[nx][ny] = new_cost
                        heappush(heap, (new_cost, nx, ny))
        
        # Se não houver caminho, retornar -1 (não esperado neste problema)
        return -1
