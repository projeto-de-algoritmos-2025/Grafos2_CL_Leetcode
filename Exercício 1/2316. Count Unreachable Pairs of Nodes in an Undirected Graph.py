class Solution:
    """
    Conta o número de pares de nós que não são alcançáveis um do outro em um grafo não direcionado.

    Parâmetros:
    - n: Número total de nós no grafo.
    - edges: Lista de arestas, onde cada aresta é representada como [a, b], indicando
      que existe uma aresta não direcionada entre os nós 'a' e 'b'.

    Retorna:
    - O número de pares de nós que não são alcançáveis um do outro.
    """    
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict

        # Criação do grafo utilizando um dicionário de listas (lista de adjacência)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Função para realizar busca em profundidade (DFS) e encontrar o tamanho do componente conectado ao nó dado.
        def dfs(node, visited):
            stack = [node]  # Pilha para explorar os nós
            size = 0  # Tamanho do componente conectado
            while stack:
                curr = stack.pop()  # Retira um nó da pilha
                if curr not in visited:  # Verifica se já foi visitado
                    visited.add(curr)  # Marca o nó como visitado
                    size += 1  # Aumenta o contador de nós no componente
                    # Adiciona vizinhos não visitados à pilha
                    for neighbor in graph[curr]:
                        if neighbor not in visited:
                            stack.append(neighbor)
            return size

        visited = set()  # Conjunto para manter os nós visitados
        component_sizes = []  # Lista para armazenar os tamanhos dos componentes

        # Encontrando componentes conectados percorrendo todos os nós
        for i in range(n):
            if i not in visited:
                size = dfs(i, visited)  # Calcula o tamanho do componente
                component_sizes.append(size)  # Armazena o tamanho do componente

        # Calcular o número total de pares possíveis de nós
        total_pairs = n * (n - 1) // 2

        # Calcular o número de pares alcançáveis dentro de cada componente conectado
        reachable_pairs = sum(size * (size - 1) // 2 for size in component_sizes)

        # O número de pares não alcançáveis é a diferença entre os pares totais e os pares alcançáveis dentro dos componentes conectados
        return total_pairs - reachable_pairs
