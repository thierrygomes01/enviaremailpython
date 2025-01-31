import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#dados de conexão
username = "seu_email@gmail.com" #Digite seu email
senha = "sua_senha_de_app" #Digite sua senha

#informações do email para enviar
dest = "destinatario@exemplo.com" #Digite o email do destinatário
assunto = "" #Digite o assunto do email
corpo = "" #Digite o corpo do email a ser enviado

#configurar a mensagem
mensagem = MIMEMultipart()
mensagem['From'] = username
mensagem['to'] = dest
mensagem['Subject'] = assunto
mensagem.attach( MIMEText(corpo, 'plain') )

try:
  with smtplib.SMTP('smtp.gmail.com', 587) as server :
    server.starttls()
    server.login(username, senha)
    server.sendmail(username, dest, mensagem.as_string() )
  print("E-mail enviado com sucesso!")
except Exception as e :
  print("Erro ao enviar o email!" + e)