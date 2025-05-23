import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config.settings import EMAIL_PASSWORD, EMAIL_USER, SMTP_PORT, SMTP_SERVER


def notify_user(cheaper_items, user_email):
    print("Enviando e-mail")

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)

            subdject = "🛒 Carrinho Renner - ⚠️ Alerta de Redução de Preço ⚠️"
            message = get_html(cheaper_items)

            email_msg = MIMEMultipart()
            email_msg["From"] = EMAIL_USER
            email_msg["To"] = user_email
            email_msg["Subject"] = subdject
            email_msg.attach(MIMEText(message, "html"))

            server.send_message(email_msg)
            print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")


def get_html(items):
    items_list = ""

    for item in items:
        last_price = f"{float(item['last_price']):.2f}".replace(".", ",")
        current_price = f"{float(item['current_price']):.2f}".replace(".", ",")
        items_list += (
            "<tr>"
            '    <td align="center" style="padding-bottom: 1.5em;">'
            '        <table width="100%" cellpadding="0" cellspacing="0" border="0" style="border: 1px solid #000; border-radius: 0.6em; font-family: '
            + "Poppins"
            + ', sans-serif; padding: 0.8em;">'
            "            <tr>"
            '                <td width="30%" align="center" style="padding: 0.6em;">'
            f'                    <a href="{item['product_link']}" target="_blank">'
            f'                        <img src="{item['product_image']}" width="100" style="border-radius: 0.6em;" alt="Produto">'
            "                    </a>"
            "                </td>"
            '                <td style="padding: 0.6em;">'
            f'                    <a href="{item['product_link']}" target="_blank" style="text-decoration: none; color: black; font-size: 1rem; font-weight: bold; font-family: '
            + "Poppins"
            + ', sans-serif;">'
            f"                        {item['name']}"
            "                    </a><br>"
            '                    <span style="font-family: '
            + "Poppins"
            + ', sans-serif; font-size: 0.7rem;">'
            f"                        Cor | Tamanho: {item['variant']}"
            "                    </span><br><br>"
            f'                    <span style="color: #555555; text-decoration: line-through; font-size: 0.8rem;">R${last_price}</span><br>'
            f'                    <span style="font-weight: bold; font-size: 1rem; color: black;">R${current_price}</span><br><br>'
            '                    <a href="https://www.lojasrenner.com.br/sacola#" target="_blank"'
            '                    style="background-color: #da2e34; color: white; padding: 1em 2em; border-radius: 0.6em; text-decoration: none; font-family: '
            + "Poppins"
            + ', sans-serif; font-weight: 700; font-size: 0.7rem;" margin-botton: 0.3em;>'
            "                        Ver na Sacola"
            "                    </a>"
            "                </td>"
            "            </tr>"
            "        </table>"
            "    </td>"
            "</tr>"
        )

    html = (
        "<!DOCTYPE html>"
        '<html lang="pt-br">'
        "<head>"
        '    <meta charset="UTF-8">'
        "    <title>Redução de Preço</title>"
        '    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">'
        "</head>"
        '<body style="margin: 0; padding: 0; background-color: #ffffff; font-family: '
        + "Poppins"
        + ', sans-serif;">'
        '    <table width="100%" cellpadding="0" cellspacing="0" border="0" align="center">'
        "        <tr>"
        '            <td align="center" style="padding: 1.2em;">'
        '                <table width="100%" cellpadding="0" cellspacing="0" border="0" style="font-family: '
        + "Poppins"
        + ', sans-serif;">'
        "                    <tr>"
        '                        <td style="font-size: 1.5rem; font-weight: bold; text-align: center; padding-bottom: 0.5em;">'
        "                            Chegou uma ótima notícia pra você 🤩!"
        "                        </td>"
        "                    </tr>"
        "                    <tr>"
        '                        <td style="font-size: 1.2rem; font-weight: bold; text-align: center; padding-bottom: 1.5em;">'
        "                            Estes produtos do seu carrinho Renner tiveram redução de preço 💸:"
        "                        </td>"
        "                    </tr>"
        f"                    {items_list}"
        "                </table>"
        "            </td>"
        "        </tr>"
        "    </table>"
        "</body>"
        "</html>"
    )
    return html
