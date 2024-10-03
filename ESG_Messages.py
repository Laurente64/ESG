import smtplib                         # Biblioteca para enviar mensagens no WhatsApp e e-mails (Simple Mail Transfer Protocol)
import ssl                             # Biblioteca para encriptografar as menssagens (Secure Sockets Layer)
from email.message import EmailMessage # Biblioteca para enviar e-mails


email_sender   = 'joaoscam.0@gmail.com'      # Define o email sender, quem envia o e-mail
email_password = 'senha'                     # Define a senha do e-mail do emissor da mensagem
email_receiver = 'pietrodalmedico@gmail.com' # Defininfo o receiver, quem vai receber a mensagem
 
# Criando variáveis para armazenar o subject, título/assunto, e o body, corpo/conteúdo, do e-mail
subject = "Agora eu posso mandar e-mails usando Python!"
body    = "Eu fiz isso usando a biblioteca smtplib!"

em            = EmailMessage() # Criando um objeto (variável com outras várias e funções já inclusas)
em['From']    = email_sender   # Definindo quem vai enviar a mensagem
em['To']      = email_receiver # Definindo quem deve receber a mensagem
em['Subject'] = subject        # Definindo o título/assunto da mensagem
em.set_content(body)           # Definindo o conteúdo da mensagem
 

# Adicionando o  SSL, camada de segurança
context = ssl.create_default_context()

# Estabelece conexão com o SMTP, especificando informações de acesso e segurança 
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    # Fazendo o login com a conta, passando o e-mail e a senha emissor da mensagem
    smtp.login(email_sender, email_password)

    # Eviando o e-mail, passando o emissor, o destinatário e 
    smtp.sendmail(email_sender, email_receiver, em.as_string())