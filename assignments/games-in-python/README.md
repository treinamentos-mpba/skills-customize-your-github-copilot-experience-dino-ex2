# 📘 Atividade: Jogo da Forca em Python

## 🎯 Objetivo

Construa um jogo da Forca em Python para praticar manipulação de strings, listas, condicionais e loops. O jogador tentará descobrir uma palavra secreta antes de esgotar o número de tentativas.

## 📝 Tarefas

### 🛠️ Preparar a Palavra e o Progresso do Jogo

#### Descrição
Crie a estrutura inicial do jogo: selecione uma palavra secreta de uma lista e prepare a representação que será exibida ao jogador.

#### Requisitos
O programa concluído deve:

- Manter uma lista predefinida com pelo menos cinco palavras.
- Selecionar aleatoriamente uma palavra da lista.
- Exibir cada letra ainda não descoberta como `_`, preservando as posições das letras já acertadas.
- Inicializar e acompanhar um limite de tentativas incorretas.

### 🛠️ Implementar os Palpites e o Encerramento

#### Descrição
Permita que o jogador tente adivinhar letras, atualize o progresso a cada palpite e encerre a partida quando a palavra for descoberta ou as tentativas acabarem.

#### Requisitos
O programa concluído deve:

- Solicitar um palpite de uma letra por rodada e informar se ela está na palavra.
- Atualizar as letras reveladas quando o palpite estiver correto.
- Reduzir as tentativas restantes quando o palpite estiver incorreto.
- Continuar até que todas as letras sejam descobertas ou não restem tentativas.
- Exibir uma mensagem de vitória ou derrota e revelar a palavra secreta ao final.
