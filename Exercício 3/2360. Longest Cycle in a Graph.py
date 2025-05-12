class Solution:
    """
    Encontra o comprimento do ciclo mais longo em um grafo direcionado.

    Parâmetros:
    - n: Número de nós no grafo.
    - edges: Lista de arestas direcionadas, onde edges[i] indica que existe uma
      aresta direcionada do nó 'i' para o nó 'edges[i]'. Se edges[i] == -1, o nó 'i'
      não tem aresta de saída.

    Retorna:
    - O comprimento do ciclo mais longo no grafo. Se não houver ciclo, retorna -1.
    """
    def longestCycle(self, edges: List[int]) -> int:
        visited = [False] * len(edges)  # Marca nós já visitados para evitar repetição
        max_cycle_length = -1  # Comprimento máximo do ciclo encontrado

        # Função para explorar o ciclo a partir de um nó
        def explore(node):
            dist = {}  # Armazena a distância do nó atual desde o início da exploração
            current = node
            length = 0

            # Percorre o caminho enquanto o nó não for visitado e existir uma aresta
            while current != -1 and current not in dist:
                dist[current] = length
                length += 1
                current = edges[current]

            # Verifica se um ciclo foi encontrado
            if current != -1 and current in dist:
                return length - dist[current]
            return -1

        # Percorre cada nó para encontrar o ciclo mais longo
        for i in range(len(edges)):
            if not visited[i]:  # Evita reexploração de componentes já visitados
                current = i
                dist = {}  # Mapa para armazenar distâncias locais na exploração

                # Caminha enquanto o nó não for visitado e existir uma aresta
                while current != -1 and current not in dist:
                    dist[current] = len(dist)
                    visited[current] = True
                    current = edges[current]

                # Se encontrar um ciclo, calcula o comprimento
                if current != -1 and current in dist:
                    cycle_length = len(dist) - dist[current]
                    max_cycle_length = max(max_cycle_length, cycle_length)

        return max_cycle_length
