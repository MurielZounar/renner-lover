# 🛍️ Monitor de Preços - Carrinho Renner

Este programa automatiza o monitoramento de preços de produtos adicionados ao carrinho na loja online da **Renner**.  
Ele utiliza **web scraping com Selenium** para acessar o carrinho de compras do usuário, extrair os dados dos produtos e verificar alterações de preço.  
Quando um produto tem o preço reduzido, o programa envia uma notificação por **e-mail** para o usuário.

As informações dos produtos são armazenadas e gerenciadas em tempo real usando o **Firebase Realtime Database**.

---

## 🧠 Funcionalidades principais

- 💻 Acesso automatizado ao site da Renner e login via Selenium  
- 🛒 Navegação até o carrinho de compras e extração dos produtos  
- 💾 Armazenamento de informações no Firebase  
- 📉 Comparação de preços atual x anterior  
- 📬 Envio de e-mail ao usuário quando há redução de preço em algum item do carrinho  

---

## 🗂️ Estrutura de arquivos

```
Carrinho Renner_/
│
├── main.py                       # Script principal: executa a lógica de login, checagem e envio de e-mails
├── requirements.txt             # Dependências do projeto
└── modules/
    ├── renner.py                # Lida com o scraping e automação do site da Renner
    ├── database.py              # Interface com o Firebase Realtime Database
    └── password.py              # (presumivelmente lida com criptografia ou armazenamento seguro de senhas)
```

---

## ⚙️ Requisitos

Instale as dependências com:

```bash
pip install -r requirements.txt
```

Você também vai precisar de:

- Um arquivo `.env` com as seguintes variáveis:
  ```
  URL_RENNER=https://www.lojasrenner.com.br/
  URL_CART=https://www.lojasrenner.com.br/carrinho
  EMAIL_USER=seuemail@exemplo.com
  EMAIL_PASSWORD=suasenha
  SMTP_SERVER=smtp.exemplo.com
  SMTP_PORT=587
  ```
- Um arquivo de credenciais do Firebase (formato `.json`)

---

## 🚀 Como usar

1. Adicione produtos ao seu carrinho logado no site da Renner.
2. Rode o script `main.py`:
   ```bash
   python main.py
   ```
3. O script irá:
   - Logar na sua conta Renner.
   - Acessar seu carrinho.
   - Verificar os preços dos produtos.
   - Comparar com os dados salvos anteriormente.
   - Enviar um e-mail caso algum preço tenha caído.

---

## 🛡️ Observações de segurança

- Evite colocar senhas diretamente no código.
- Use o `.env` para armazenar informações sensíveis.
- Certifique-se de que o arquivo `.env` e as credenciais do Firebase estejam no `.gitignore`.

---