# 2290. Minimum Obstacle Removal to Reach Corner

## Questão

A questão foi resolvida no LeetCode, onde você pode conferir o enunciado completo.

[Ver questão no LeetCode](https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/description/?envType=problem-list-v2&envId=2cthq20h)  

## Gravação

A resolução dessa questão foi gravada e você pode assistir ao vídeo para ver o passo a passo da solução.

[Clique aqui para assistir]()

## Dificuldade

Difícil

## Enunciado

Você recebe uma grade de matriz de inteiros bidimensional com índice 0 e tamanho m x n. Cada célula possui um de dois valores:

0 representa uma célula vazia,
1 representa um obstáculo que pode ser removido.
Você pode mover para cima, para baixo, para a esquerda ou para a direita a partir de e para uma célula vazia.

Retorne o número mínimo de obstáculos a serem removidos para que você possa mover do canto superior esquerdo (0, 0) para o canto inferior direito (m - 1, n - 1).

## Exemplos

### Exemplo 1

![image](https://github.com/user-attachments/assets/3348a823-a412-44e7-b294-84a165dbacf7)

>**Input**: grid = [[0,1,1],[1,1,0],[1,1,0]]<br>
>**Output**: 2<br>
>**Explicação**: Podemos remover os obstáculos em (0, 1) e (0, 2) para criar um caminho de (0, 0) a (2, 2).
Pode-se demonstrar que precisamos remover pelo menos 2 obstáculos, então retornamos 2.
Observe que pode haver outras maneiras de remover 2 obstáculos para criar um caminho.

### Exemplo 2

![image](https://github.com/user-attachments/assets/0fa07aaa-1d84-4de8-8c31-c7654d6be384)

>**Input**: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]<br>
>**Output**: 0<br>
>**Explicação**: Podemos passar de (0, 0) para (2, 4) sem remover nenhum obstáculo, então retornamos 0.

## Restrições

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 105
- 2 <= m * n <= 105
- grid[i][j] is either 0 or 1.
- grid[0][0] == grid[m - 1][n - 1] == 0

## Submissões
