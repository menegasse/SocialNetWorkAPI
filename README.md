# GraphQL-Graphene-Python

<p>Projeto com o intuito de aprender mais sobre GraphQL com a tecnologia Python utilizando a biblioteca Graphene. Foi desenvolvida uma API simulando algumas funcionalidades de uma rede social, podendo realizar as seguintes queries e mutations:</p>

### 1. Cadastro na API (Register)
#### <em>Endpoint: /user</em>
```json
mutation {
  register(name: "UserName", email: "useremail@graphene.com", password: "12345678") {
    success
    errorMessage
  }
}
```
---
### 2. Efetuar Login 
#### <em>Endpoint: /user</em>
```json
mutation{
  login (email:"useremail@graphene.com", password:"12345678") {
    token 
    errorMessage 
  }
}
```
<em>Obs*: Após o login é necessário configurar o token para todas as próximas requisições</em>

---
### 3. Começar seguir um usuário (Follow)
#### <em>Endpoint: /follow</em>
```json
mutation {
  follow (id: 2) {
    success 
    errorMessage 
  }
}
```

---
### 4. Deixar de seguir um usuário (Unfollow)
#### <em>Endpoint: /follow</em>
```json
mutation {
  unfollow(id: 1) {
    success 
    errorMessage 
  }
}
```

---
### 5. Obtém a lista de todos os usuários que o usuário autenticado está seguindo (Following)
#### <em>Endpoint: /follow</em>
```json
query {
  following {
    id
    name
    followsCount 
    followersCount 
  }
}
```

---
### 6. Obtém a lista de todos os usuários que estão seguindo o usuário autenticado (FollowMe)
#### <em>Endpoint: /follow</em>
```json
query {
  followsMe { 
    id
    name
    followsCount 
    followersCount
  }
}
```

---
### 7. Posta uma mensagem no feed do usuário autenticado (PostMesage)
#### <em>Endpoint: /post</em>
```json
mutation {
  postMessage (text: "I'm learned GraphQL in Python with Graphene lib!"){
    success 
    errorMessage 
    message { 
      id
      text
      postedAt
      postedBy {
        id
        name
        followsCount
        followersCount
      }
    }
  }
}
```

---
### 8. Obtém uma lista paginada de todas as postagens dos usuários em que o usuário autenticadoa marcou que segue (MessagePage)
#### <em>Endpoint: /post</em>
```json
query {
  feed (limit: 2 offset: 0) {
    pageInfo {
      totalPages 
      page 
    }
    messages { 
      id
      text
      postedAt
      postedBy {
        id
        name
        followsCount
        followersCount
      }
    }
  }
}
```

<p>Caso queria apenas executar as queries e mutations de modo mais fácil, basta importar o arquivo <em>Insomnia_workspace.json</em> no aplicativo Insomnia que já terá todo o Workspace configurado.</p>
<p>
    <em>Obs*: lembre de trocar a variável de ambiente      _token toda vez que realizar o login para realizar as requisições que necessitam de autenticação</em>
</p>




---

## Dependências 

Todas as bibliotecas e dependências do projetos estão listadas no arquivo <em>requirements.txt</em>, contudo as principais utilizadas foram:

- **Graphene (v3.0)**: para o desenvolvimento da interface da api GrapheQL.

- **Framework Django (v3.0)**: para o desenvolvimento das funcionalidades da API, como tratamento dos dados, comunicação com o banco de dados (SQLite3) e autenticação de usuário utilizando token (método JWT).

<em> Obs*: A versão do Python utilizada é a 3.8.10</em>

---

## Banco de Dados

O banco de dados desse projeto está sendo representado pelo arquivo do tipo SQLite3 na raiz do projeto, que está sendo criado automaticamente ao executar os migrations do Framework Django.

---

## Scripts

Na pasta scripts possui 2 arquivos para facilitar a instalação das dependências do projeto (<em>install-project.sh</em>) e outro para iniciar o servidor (<em>start.sh</em>). Os scripts devem ser executados a partir do próprio diretório <em>(/scripts)</em> para que não haja nenhum problema.

