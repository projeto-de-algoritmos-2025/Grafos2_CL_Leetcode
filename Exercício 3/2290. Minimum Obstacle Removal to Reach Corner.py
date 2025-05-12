from heapq import heappop, heappush
from typing import List

class Solution:
    """
    Encontra o caminho com o menor número de obstáculos em uma grade binária.
    
    Parâmetros:
    - grid (List[List[int]]): Uma matriz binária onde '0' representa uma célula livre e '1' representa um obstáculo.
    
    Retorna:
    - int: O menor número de obstáculos que precisam ser removidos para alcançar o canto inferior direito da grade a partir do canto superior esquerdo.
    
    Descrição:
    O algoritmo utiliza um algoritmo de caminho mínimo com prioridade, similar ao Dijkstra, usando uma fila de prioridade (min-heap). 
    Cada célula na grade é considerada um nó, e as arestas têm peso 0 para células livres e 1 para obstáculos.
    A busca começa na posição (0, 0) e termina na posição (m-1, n-1). A cada movimento válido (cima, baixo, esquerda, direita), 
    o custo é atualizado se o novo caminho for mais barato. A célula de destino é retornada assim que alcançada com o menor custo.
    Se não houver caminho possível, retorna -1.
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
