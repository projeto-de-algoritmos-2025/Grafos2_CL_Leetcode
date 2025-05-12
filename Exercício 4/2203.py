from collections import defaultdict
from math import inf

class Solution:
    def minimumWeight(self, n: int, edges: list[list[int]], src1: int, src2: int, dest: int) -> int:
        # funcao para empurrar um elemento na heap
        def push_heap(heap, item):
            heap.append(item)
            _sift_up(heap, len(heap) - 1)
            
        # funcao para retirar o menor elemento da heap
        def pop_heap(heap):
            if len(heap) == 1:
                return heap.pop()
            smallest = heap[0]
            heap[0] = heap.pop()
            _sift_down(heap, 0)
            return smallest
            
        # funcao para subir um elemento na heap
        def _sift_up(heap, idx):
            parent = (idx - 1) // 2
            while idx > 0 and heap[idx][0] < heap[parent][0]:
                heap[idx], heap[parent] = heap[parent], heap[idx]
                idx = parent
                parent = (idx - 1) // 2
        # funcao para descer um elemento na heap
        def _sift_down(heap, idx):
            smallest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2

            if left < len(heap) and heap[left][0] < heap[smallest][0]:
                smallest = left
            if right < len(heap) and heap[right][0] < heap[smallest][0]:
                smallest = right

            if smallest != idx:
                heap[idx], heap[smallest] = heap[smallest], heap[idx]
                _sift_down(heap, smallest)
                
        # funcao dijkstra para calcular distancias minimas
        def dijkstra(start: int, graph: dict) -> list[int]:
            dist = [inf] * n
            dist[start] = 0
            heap = []
            push_heap(heap, (0, start)) # (distancia, no)
            while heap:
                current_dist, u = pop_heap(heap)
                if current_dist > dist[u]:
                    continue # ignora nos ja processados
                for v, weight in graph[u]:
                    if dist[v] > dist[u] + weight:
                        dist[v] = dist[u] + weight
                        push_heap(heap, (dist[v], v))
            return dist

        # construir o grafo e o grafo invertido
        graph = defaultdict(list)
        reversed_graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            reversed_graph[v].append((u, w))

        # calcular distancias minimas
        dist_from_src1 = dijkstra(src1, graph)
        dist_from_src2 = dijkstra(src2, graph)
        dist_to_dest = dijkstra(dest, reversed_graph)

        # encontrar o peso minimo total
        min_total = inf
        for i in range(n):
            total = dist_from_src1[i] + dist_from_src2[i] + dist_to_dest[i]
            if total < min_total:
                min_total = total

        return min_total if min_total != inf else -1
