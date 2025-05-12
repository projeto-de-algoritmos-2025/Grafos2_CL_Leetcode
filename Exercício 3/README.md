# 2360. Longest Cycle in a Graph

## Questão

A questão foi resolvida no LeetCode, onde você pode conferir o enunciado completo.

[Ver questão no LeetCode](https://leetcode.com/problems/longest-cycle-in-a-graph/description/?envType=problem-list-v2&envId=2cthq20h)  

## Gravação

A resolução dessa questão foi gravada e você pode assistir ao vídeo para ver o passo a passo da solução.

[Clique aqui para assistir]()

## Dificuldade

Difícil

## Enunciado

Você recebe um grafo direcionado de `n` nós numerados de `0` a `n - 1`, onde cada nó tem no máximo uma aresta de saída.

O grafo é representado por um dado array indexado em 0 `arestas` de tamanho `n`, indicando que há uma aresta direcionada do nó `i` ao nó `arestas[i]`. Se não houver aresta de saída do nó `i`, então `arestas[i] == -1`.

Retorna o comprimento do ciclo mais longo do grafo. Se não houver ciclo, retorna `-1`.

Um ciclo é um caminho que começa e termina no mesmo nó.

## Exemplos

### Exemplo 1

![image](https://github.com/user-attachments/assets/526df431-2999-4562-a934-8f66566de10a)

>**Input**: edges = [3,3,4,2,3]<br>
>**Output**: 3<br>
>**Explicação**: O ciclo mais longo no gráfico é o ciclo: 2 -> 4 -> 3 -> 2.
O comprimento deste ciclo é 3, então 3 é retornado.

### Exemplo 2

![image](https://github.com/user-attachments/assets/ff285e0a-ad66-4750-ba60-fe1310be85c8)

>**Input**: edges = [2,-1,3,1]<br>
>**Output**: -1<br>
>**Explicação**: Não há ciclos neste gráfico.

## Restrições

- `n == edges.length`
- `2 <= n <= 105`
- `-1 <= edges[i] < n`
- `edges[i] != i`

## Submissões
