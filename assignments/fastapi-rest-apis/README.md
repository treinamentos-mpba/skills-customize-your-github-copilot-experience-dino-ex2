# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST com FastAPI para listar, criar, atualizar e remover recursos. Você vai usar rotas HTTP, modelos Pydantic para validar dados e códigos de status adequados para cada resposta.

## 📝 Tarefas

### 🛠️ Criar a Primeira Rota GET

#### Descrição
Crie uma aplicação FastAPI e uma rota `GET /items` que retorna todos os itens da lista `items` definida no arquivo inicial. Em seguida, crie a rota `GET /items/{item_id}` para retornar apenas um item pelo seu `id`.

#### Requisitos
O programa concluído deve:

- Criar um objeto `app = FastAPI()` no arquivo `starter-code.py`.
- Implementar `GET /items` retornando a lista completa de itens em formato JSON.
- Implementar `GET /items/{item_id}` retornando o item com o `id` informado.
- Retornar status `404` quando o `item_id` não existir na lista.
- Testar as rotas em `http://127.0.0.1:8000/docs`, a documentação interativa gerada pelo FastAPI.

### 🛠️ Criar Itens com Modelos Pydantic

#### Descrição
Crie um modelo Pydantic para representar um item e use-o na rota `POST /items`, que adiciona um novo item à lista. O FastAPI deve validar automaticamente os dados recebidos.

#### Requisitos
O programa concluído deve:

- Criar uma classe `Item` que herda de `BaseModel`, com os campos `name` (texto) e `price` (número).
- Implementar `POST /items` que recebe um `Item` no corpo da requisição e o adiciona à lista.
- Gerar um `id` novo para cada item criado, somando 1 ao maior `id` existente.
- Retornar o item criado com status `201`.
- Retornar erro de validação (`422`) quando `price` não for um número ou quando `name` estiver ausente.

### 🛠️ Atualizar e Remover Itens

#### Descrição
Complete a API com as operações de atualização e remoção. Cada rota deve tratar o caso em que o item não existe.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /items/{item_id}` que substitui `name` e `price` de um item existente.
- Implementar `DELETE /items/{item_id}` que remove o item da lista.
- Retornar status `404` em `PUT` e `DELETE` quando o item não existir.
- Retornar status `204` (sem conteúdo) após uma remoção bem-sucedida.
- Verificar pela documentação `/docs` que as cinco rotas aparecem e funcionam na ordem: criar, listar, atualizar, remover.
