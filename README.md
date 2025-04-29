# 🚀 TaskFlow - Gerenciador de Tarefas

![TaskFlow Logo](logo.png)

## 📖 Visão Geral

O **TaskFlow** é um aplicativo simples e direto ao ponto, desenvolvido para auxiliar na organização de tarefas diárias. Ele permite a criação, edição, conclusão e exclusão de tarefas de maneira intuitiva.

O sistema conta com:

- **Interface gráfica (front-end):** Desenvolvida com **HTML, CSS e JavaScript**
- **Back-end:** Desenvolvido em **Python (Flask)**
- **Banco de Dados:** **MySQL (Workbench)**

> ✨ Este projeto está aberto para melhorias e futuras atualizações, como a transformação em um aplicativo mobile usando **React Native** ou outras tecnologias.

---

## 🚀 Tecnologias Utilizadas

- **Python** (Linguagem principal)
- **Flask** (Criação da API)
- **HTML, CSS e JavaScript** (Interface Web)
- **MySQL** (Armazenamento de dados)

---

## ✨ Funcionalidades

✅ **Gerenciamento de Tarefas:**

- Criar, editar e excluir tarefas
- Marcar tarefas como concluídas
- Filtrar e buscar tarefas

✅ **Notificações e Alertas:**

- Lembretes para tarefas próximas do vencimento
- Notificação para tarefas vencidas

✅ **API:**

- Endpoints para gerenciar tarefas

✅ **Sistema de Usuários:**

- Cadastro de usuários
- Login com autenticação
- Sessões seguras por token ou cookie

---

## 🛠 Estrutura do Banco de Dados

### 📂 **Tabela Tarefas**

| Campo            | Tipo         | Descrição                     |
| ---------------- | ------------ | ----------------------------- |
| id               | INT (PK)     | Identificador único           |
| titulo           | VARCHAR(255) | Nome da tarefa                |
| descricao        | TEXT         | Detalhes da tarefa            |
| data\_vencimento | DATE         | Data de vencimento            |
| prioridade       | ENUM         | Baixa, Média ou Alta          |
| status           | ENUM         | Pendente, Concluído, Atrasado |
| usuario_id       | INT (FK)     | ID do usuário proprietário    |

### 📂 **Tabela Usuários**

| Campo      | Tipo         | Descrição                   |
| ---------- | ------------ | --------------------------- |
| id         | INT (PK)     | Identificador do usuário    |
| nome       | VARCHAR(255) | Nome completo               |
| email      | VARCHAR(255) | E-mail único                |
| senha_hash | VARCHAR(255) | Senha criptografada         |

---

## 🎯 Arquitetura do Sistema

📌 **Front-end:** HTML + CSS + JS (Interface Web)  
📌 **Back-end:** Flask (API e lógica do sistema)  
📌 **Banco de Dados:** MySQL (armazenamento de dados)  
📌 **API:** CRUD para comunicação entre front-end e banco
📌 **Autenticação:** Gerenciamento de usuários e sessões

> ✨ Futuramente, este projeto poderá ganhar uma versão mobile com **React Native** ou framework similar!

---

## 🔮 Melhorias Futuras

🔹 Integração com Google Calendar  
🔹 Exportação de tarefas para PDF/CSV  
🔹 Modo escuro e claro para a interface  
🔹 Compartilhamento de tarefas com outros usuários  
🔹 Aplicativo Mobile (React Native, Flutter, etc.)

---

## 📌 Como Rodar o Projeto Localmente

```bash
# Clone este repositório
git clone https://github.com/devsamuelj/taskflow.git

# Entre no diretório
cd taskflow

# Crie um ambiente virtual e ative
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python app.py
```

Acesse em [**http://127.0.0.1:5000**](http://127.0.0.1:5000) 🚀

---

## 📜 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e contribuir! 🎯

