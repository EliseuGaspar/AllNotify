# **All Notify**

**Status**: Em Desenvolvimento.

Este é um sistema de agregação de notificações que permite que os usuários se conectem a suas plataformas de redes sociais (Facebook, Instagram, WhatsApp, Gmail) e recebam todas as suas notificações em um único local. O usuário pode selecionar quais notificações deseja receber, visualizar mensagens e realizar buscas por conversas e emails.

---

## **Tecnologias Utilizadas**

- **Backend**: Django
- **Banco de Dados**:
  - SQLite (Por Agora!)
- **Fila Assíncrona**: Celery (para processar notificações e tarefas em segundo plano)
- **API de Autenticação**: Django Rest Framework JWT
- **Notificações**: Integração com APIs de plataformas (Facebook, Gmail, WhatsApp, etc.)
- **Envio de Notificações em Tempo Real**: WebHooks

---

## **Visão Geral**

O objetivo desse sistema é proporcionar um painel único para que o usuário consiga integrar suas contas de redes sociais e serviços de mensagens (como Facebook, Gmail, WhatsApp) e centralizar as notificações de todos esses serviços em uma interface simples e intuitiva. O usuário pode:

- **Conectar suas plataformas**: Facebook, Instagram, WhatsApp, Gmail
- **Receber notificações** de novas mensagens e alertas de todas as plataformas conectadas
- **Selecionar quais notificações deseja receber**
- **Buscar conversas e e-mails específicos**
- **Marcar notificações como lidas**

---

## **Funcionalidades**

- **Cadastro e Login de Usuário**
  - Cadastro de usuário com e-mail e senha
  - Login utilizando e-mail e senha com autenticação JWT
  - Conectar contas de redes sociais (Facebook, Gmail, WhatsApp)
  
- **Notificações em tempo real**
  - Receber notificações de plataformas conectadas
  - Filtrar as notificações por plataforma, data ou status (lida/não lida)

- **Pesquisa de Conversas e E-mails**
  - Buscar por conversas no WhatsApp ou e-mails no Gmail
  - Resultados exibidos com base nos critérios fornecidos pelo usuário

---

## **Estrutura do Projeto**

### **Django Models**

- **User**: Modelo de usuário com campos para e-mail, uername e senha.
- **Platform**: Modelo para representar as plataformas conectadas pelo usuário (Facebook, Gmail, WhatsApp, Instagram).
- **Notification**: Modelo para armazenar as notificações recebidas de cada plataforma.

### **Diretórios Principais**

- **users/**: Contém toda a lógica relacionada à autenticação de usuários (login, cadastro, etc.).
- **platforms/**: Contém as lógicas de integração com APIs externas (Facebook, Gmail, WhatsApp).
- **notifications/**: Gerencia as notificações recebidas, incluindo busca, status de leitura, e filtragem.
- **services/**: Contém funções auxiliares para interação com as APIs externas.
- **tasks/**: Implementa tarefas assíncronas com Celery para processar notificações em segundo plano.

---

## **Como Rodar o Projeto Localmente**

### **Pré-requisitos**
Certifique-se de que você tenha o seguinte instalado em seu computador:

- **Python** (recomenda-se a versão 3.9 ou superior)
- **Django** (instalado via `pip`)
- **Redis** (necessário para o Celery, se for usar tarefas assíncronas)

### **Passos para rodar o projeto**

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/EliseuGaspar/AllNotify.git
   cd AllNotify

2. **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```

3. **Crie as migrações e aplique-as**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Inicie o servidor**
    ```bash
    python manage.py runserver
    ```
---

### **Como Contribuir**

1. Faça um fork deste repositório.
2. Crie uma branch para a sua feature (git checkout -b feature/nome-da-feature).
3. Realize as alterações e faça commit (git commit -am 'Adiciona nova feature').
4. Faça o push da sua branch (git push origin feature/nome-da-feature).
5. Crie um pull request.
---

### **Licença**

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](./LICENCE) para mais detalhes.