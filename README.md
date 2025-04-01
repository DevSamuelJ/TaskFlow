# 🚀 TaskFlow - Gerenciador de Tarefas

![Image](https://github.com/user-attachments/assets/10c40bdb-2f9c-4b19-81c2-9832f6a70b67)

## 📖 Visão Geral
O **TaskFlow** é um aplicativo simples e direto ao ponto, desenvolvido para auxiliar na organização de tarefas diárias. Ele permite a criação, edição, conclusão e exclusão de tarefas de maneira intuitiva.

O sistema conta com:
- **Interface gráfica:** Criada com **Flet**
- **Back-end:** Desenvolvido em **Python (Flask)**
- **Banco de Dados:** **MySQL (Workbench)**

---
## 🚀 Tecnologias Utilizadas
- **Python** (Linguagem principal)
- **Flask** (Criação da API)
- **Flet** (Interface gráfica)
- **MySQL** (Armazenamento de dados)
- **JWT** (Autenticação segura)

---
## ✨ Funcionalidades
✅ **Usuário:**
- Cadastro e login
- Recuperação de senha (opcional)
- Personalização de perfil

✅ **Gerenciamento de Tarefas:**
- Criar, editar e excluir tarefas
- Marcar tarefas como concluídas
- Filtrar e buscar tarefas

✅ **Notificações e Alertas:**
- Lembretes para tarefas próximas do vencimento
- Notificação para tarefas vencidas

✅ **API:**
- Endpoints seguros para gerenciar usuários e tarefas

---
## 🛠 Estrutura do Banco de Dados
### 📂 **Tabela Usuários**
| Campo  | Tipo         | Descrição              |
|--------|------------|----------------------|
| id     | INT (PK)   | Identificador único  |
| nome   | VARCHAR(100) | Nome do usuário  |
| email  | VARCHAR(100) | E-mail único       |
| senha  | VARCHAR(255) | Senha criptografada |

### 📂 **Tabela Tarefas**
| Campo          | Tipo       | Descrição                     |
|---------------|-----------|-----------------------------|
| id           | INT (PK)  | Identificador único       |
| usuario_id   | INT (FK)  | Relacionamento com Usuários |
| titulo       | VARCHAR(255) | Nome da tarefa |
| descricao    | TEXT      | Detalhes da tarefa |
| data_vencimento | DATE | Data de vencimento |
| prioridade   | ENUM     | Baixa, Média ou Alta |
| status       | ENUM     | Pendente, Concluído, Atrasado |

---
## 🎯 Arquitetura do Sistema
📌 **Front-end:** Flet (Interface Gráfica)  
📌 **Back-end:** Flask (API e lógica do sistema)  
📌 **Banco de Dados:** MySQL (armazenamento de dados)  
📌 **API:** CRUD para comunicação entre front-end e banco  

---
## 🔮 Melhorias Futuras
🔹 Integração com Google Calendar  
🔹 Exportação de tarefas para PDF/CSV  
🔹 Modo escuro e claro para a interface  
🔹 Compartilhamento de tarefas com outros usuários  

---
## 📌 Como Rodar o Projeto Localmente
```bash
# Clone este repositório
git clone https://github.com/seu-usuario/taskflow.git

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
Acesse em **http://127.0.0.1:5000** 🚀

---
## 📜 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e contribuir! 🎯

