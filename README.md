# PixelPath CRM 📸

Um CRM completo para fotógrafos gerenciarem seus clientes, projetos, faturas e tarefas. Este projeto foi construído com o objetivo de demonstrar uma arquitetura de aplicação web moderna e robusta.

## ✨ Features

-   Gerenciamento de Clientes
-   Controle de Projetos (Ensaios)
-   Emissão e Controle de Faturas
-   Sistema de Tarefas por Projeto
-   Autenticação de Usuários com diferentes papéis (Admin, Fotógrafo)

## 🛠️ Tech Stack

-   **Frontend:** React, Next.js, Tailwind CSS
-   **Backend:** Python, Django, Django REST Framework
-   **Banco de Dados:** PostgreSQL
-   **DevOps:** Docker, Docker Compose

## 🚀 Rodando o Projeto Localmente

**Pré-requisitos:** Docker e Docker Compose instalados.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/pixelpath-crm.git](https://github.com/seu-usuario/pixelpath-crm.git)
    cd pixelpath-crm
    ```

2.  **Configure as variáveis de ambiente:**
    ```bash
    # Crie uma cópia do arquivo de exemplo
    cp .env.example .env
    ```
    *Depois, edite o arquivo `.env` com suas configurações (principalmente a `SECRET_KEY`).*

3.  **Suba os contêineres:**
    ```bash
    docker-compose up -d --build
    ```

4.  **Execute as migrações do banco de dados:**
    ```bash
    docker-compose exec backend python manage.py migrate
    ```

5.  **Acesse a aplicação:**
    -   Backend API: `http://localhost:8000`
    -   Frontend: `http://localhost:3000` (quando estiver pronto)