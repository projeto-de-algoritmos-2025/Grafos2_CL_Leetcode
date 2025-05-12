# 2316. Count Unreachable Pairs of Nodes in an Undirected Graph

## Questão

A questão foi resolvida no LeetCode, onde você pode conferir o enunciado completo.

[Ver questão no LeetCode](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/?envType=problem-list-v2&envId=2cthq20h)    

## Gravação

A resolução dessa questão foi gravada e você pode assistir ao vídeo para ver o passo a passo da solução.

[Clique aqui para assistir](https://youtu.be/x45eKyT45RI)

## Dificuldade

Média

## Enunciado

Você recebe um inteiro `n`. Há um grafo não direcionado com `n` nós, numerados de `0` a `n - 1`. Você recebe um array de inteiros 2D `arestas`, onde `arestas[i] = [ai, bi]` denota que existe uma aresta não direcionada conectando os nós `ai` e `bi`.

Retorna o número de pares de nós diferentes que são inalcançáveis ​​entre si.

## Exemplos

### Exemplo 1

![image](https://github.com/user-attachments/assets/e03c9343-3307-45b0-b598-77efcc508f08)

>**Input**: n = 3, edges = [[0,1],[0,2],[1,2]]<br>
>**Output**: 0<br>
>**Explicação**: Não há pares de nós inacessíveis entre si. Portanto, retornamos 0.

### Exemplo 2

![image](https://github.com/user-attachments/assets/9f731a34-78c3-42e2-9e53-fd9a47b35182)

>**Input**: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]<br>
>**Output**: 14<br>
>**Explicação**: Existem 14 pares de nós que são inacessíveis entre si:
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
Therefore, we return 14.

## Restrições

- `1 <= n <= 105`
- `0 <= edges.length <= 2 * 105`
- `edges[i].length == 2`
- `0 <= ai, bi < n`
- `ai != bi`
- Não há arestas repetidas.

## Submissões

![image](https://github.com/user-attachments/assets/8e0dcdd1-385e-4b21-9479-f4f9c3e30c37)

![image](https://github.com/user-attachments/assets/60cf67cc-5509-4d84-8780-a401b1e617ae)
