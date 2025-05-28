
# 💖 Renner Lover — Monitoramento de Descontos Automático

<details>
<summary>🇧🇷 - Clique aqui para ler em Português</summary>

<br>

# 💖 Renner Lover!

🎯 **Renner Lover** é um assistente automatizado que monitora os preços dos produtos adicionados ao seu carrinho na loja online da **Renner**.  
Ele utiliza **web scraping com Selenium** para acessar sua conta, verificar os itens salvos no carrinho e detectar **reduções de preço**.  
Sempre que algum produto ficar mais barato, você recebe uma notificação por **e-mail** 📩.  
As informações são armazenadas com segurança usando **SQLite** e **criptografia** 🔐.

---

## 💡 Como surgiu a ideia?

Tudo começou com a minha esposa. 💁‍♀️  
Ela adorava procurar roupas e acessórios no site da Renner, adicionava tudo ao carrinho e…  
...todos os dias voltava para **ver se o preço baixou**.  

Apesar de funcionar bem (ela conseguiu bons descontos!), era um processo **repetitivo e chato**. Então, resolvi ajudar!

Agora, ela só precisa adicionar os produtos ao carrinho.  
O resto? Deixa com o **Renner Lover**! 😉  
Se o preço cair, ela recebe um e-mail instantâneo com a novidade.

> 💬 O nome *Renner Lover* foi ideia dela — afinal, ela é uma verdadeira fã da loja! 😅

---

## 🧠 Funcionalidades principais

- 💻 Acesso automatizado ao site da Renner  
- 🔐 Login com credenciais criptografadas  
- 🛒 Navegação até o carrinho de compras  
- 📦 Extração e monitoramento dos produtos  
- 💾 Armazenamento seguro com SQLite  
- 📉 Comparação entre preços atuais e anteriores  
- 📬 Envio automático de e-mail em caso de desconto  

---

## ⚙️ Pré-requisitos

📦 Instale as dependências do projeto com:

```bash
pip install -r requirements.txt
```

🛠️ Você pode customizar algumas configurações em `config/settings.py`, como:

- Local de armazenamento do banco de dados (`DB_PATH`)
- Tempo entre verificações de preço (`SLEEP_TIME`)
- Outras opções personalizáveis

📁 Crie um arquivo `.env` com suas credenciais de e-mail:

```
SMTP_SERVER=smtp.exemplo.com
SMTP_PORT=587
EMAIL_USER=seuemail@exemplo.com
EMAIL_PASSWORD=suasenha
```

> 🧷 **Importante:** Nunca exponha seu `.env`. Certifique-se de que ele está no seu `.gitignore`.

---

## 🚀 Como usar

1. Adicione produtos ao seu carrinho no site da Renner 🛍️

2. Execute o script para criar o banco de dados:
   ```bash
   python scripts/init_db.py
   ```

3. Gere a chave secreta para criptografia de senhas:
   ```bash
   python utils/password.py
   ```

4. Cadastre um ou mais usuários com:
   ```bash
   python user_actions.py
   ```

   Durante a execução, você verá estas opções:

   ```
   1 - Cadastrar usuário
   2 - Alterar cadastro
   3 - Excluir cadastro
   4 - Listar usuários
   5 - Sair
   ```

   ⚠️ No momento do cadastro, serão solicitados:
   - Nome
   - E-mail
   - Senha da conta da Renner (armazenada com **criptografia**)

5. Com tudo pronto, execute o coração do sistema:

   ```bash
   python main.py
   ```

   Ele irá:

   - Acessar o site da Renner
   - Logar com os dados do(s) usuário(s)
   - Navegar até o carrinho
   - Obter e comparar os preços dos produtos
   - Enviar um e-mail caso algum item esteja com **desconto**

   🪄 **Tudo de forma automática!**

---

## 📈 O que vem por aí — Funcionalidades futuras

Aqui estão algumas ideias e melhorias que estão no radar para as próximas versões do projeto:

- ✅ **Testes automatizados** para garantir estabilidade e confiabilidade  
- ⭐ **Monitoramento da lista de favoritos** do usuário (além do carrinho)  
- 🛠️ Melhorias na interface CLI para tornar o uso ainda mais intuitivo  
- 🔔 Suporte a outras formas de notificação (ex: Telegram, Push Notification)

---

## 🤖 Tecnologias utilizadas

- 🐍 Python  
- 🌐 Selenium  
- 🛡️ Cryptography  
- 🗃️ SQLite  

---

## 🔐 Dicas de segurança

- ❌ **Nunca** coloque senhas diretamente no código  
- ✅ Use arquivos `.env` para armazenar informações sensíveis  
- 📁 Garanta que `.env` está no seu `.gitignore`  

---

</details>

<details>
<summary>🇺🇸 - Click here to read in English</summary>

<br>

# 💖 Renner Lover!

🎯 **Renner Lover** is an automated assistant that monitors the prices of products added to your shopping cart on **Renner**'s online store.  
It uses **web scraping with Selenium** to access your account, check the items saved in your cart, and detect **price drops**.  
Whenever a product gets cheaper, you receive an **email notification** 📩.  
All data is securely stored using **SQLite** and **encryption** 🔐.

---

## 💡 How the Idea Was Born

It all started with my wife. 💁‍♀️  
She loved browsing for clothes and accessories on Renner's website, added everything to her cart, and…  
...checked every day to **see if the price had dropped**.

Although it worked well (she got some great deals!), it was a **tedious and repetitive** process. So I decided to help!

Now, she just adds products to the cart.  
The rest? Leave it to **Renner Lover**! 😉  
If a price drops, she gets an instant email alert.

> 💬 The name *Renner Lover* was her idea — after all, she’s a real fan of the store! 😅

---

## 🧠 Key Features

- 💻 Automated access to Renner’s website  
- 🔐 Login with encrypted credentials  
- 🛒 Navigation to the shopping cart  
- 📦 Product data extraction and monitoring  
- 💾 Secure storage using SQLite  
- 📉 Price comparison (current vs. previous)  
- 📬 Automatic email notifications when discounts are detected  

---

## ⚙️ Prerequisites

📦 Install project dependencies with:

```bash
pip install -r requirements.txt
```

🛠️ You can customize some settings in `config/settings.py`, such as:

- Database file path (`DB_PATH`)
- Delay between price checks (`SLEEP_TIME`)
- Other tweakable options

📁 Create a `.env` file with your email credentials:

```
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
EMAIL_USER=youremail@example.com
EMAIL_PASSWORD=yourpassword
```

> 🧷 **Important:** Never expose your `.env` file. Make sure it’s listed in `.gitignore`.

---

## 🚀 How to Use

1. Add products to your cart on the Renner website 🛍️

2. Run the script to create the database:
   ```bash
   python scripts/init_db.py
   ```

3. Generate the secret key for password encryption:
   ```bash
   python utils/password.py
   ```

4. Register one or more users with:
   ```bash
   python user_actions.py
   ```

   You’ll see these options during execution:

   ```
   1 - Register user
   2 - Edit user
   3 - Delete user
   4 - List users
   5 - Exit
   ```

   ⚠️ During registration, you’ll be asked for:
   - Name
   - Email
   - Renner account password (stored **encrypted**)

5. Once ready, run the core system:

   ```bash
   python main.py
   ```

   It will:

   - Access Renner’s website
   - Log in with each user’s credentials
   - Visit the shopping cart
   - Fetch and compare product prices
   - Send an email if any product has **dropped in price**

   🪄 **All fully automated!**

---

## 📈 What’s Coming — Future Features

Here are some ideas and improvements planned for future versions:

- ✅ **Automated tests** to ensure stability and reliability  
- ⭐ **Monitor the user's favorite list** (not just the cart)  
- 🛠️ Improved CLI interface for an even more intuitive experience  
- 🔔 Support for other notification channels (e.g. Telegram, Push Notification)

---

## 🤖 Tech Stack

- 🐍 Python  
- 🌐 Selenium  
- 🛡️ Cryptography  
- 🗃️ SQLite  

---

## 🔐 Security Tips

- ❌ **Never** hardcode passwords  
- ✅ Use `.env` files for sensitive information  
- 📁 Ensure `.env` is listed in `.gitignore`  

---

</details>
