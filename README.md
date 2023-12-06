# Projeto Django para Estudo de Queries

Este projeto Django foi desenvolvido com o objetivo de proporcionar um ambiente prático para o estudo e a prática de queries no Django ORM. Ele inclui uma série de modelos representativos e dados iniciais para permitir a experimentação com diferentes tipos de consultas e relacionamentos de banco de dados.

## Modelos Incluídos

O projeto inclui os seguintes modelos:

- `Author`: Representa autores de livros.
- `Book`: Representa livros, com uma relação "um-para-muitos" com `Author` e uma relação "muitos-para-muitos" com `Tag`.
- `Tag`: Representa etiquetas ou categorias para livros.
- `Profile`: Representa perfis de usuários, com uma relação "um-para-um" com o modelo de usuário padrão do Django.
- `Review`: Representa revisões de livros, com uma relação "um-para-muitos" com `Book`.

## Instalação e Configuração

Siga os passos abaixo para configurar o projeto em seu ambiente local:


1. **Configuração do Ambiente Virtual:**

- **Windows:**
  ```
  python -m venv venv
  venv\Scripts\activate
  ```

- **Linux:**
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

2. **Instalando Dependências:**
  ```
   pip install -r requirements.txt
  ```

