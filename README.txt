📧 Automação de Envio de E-mail com Python
Este script permite o envio automatizado de e-mails utilizando Python e o servidor SMTP do Gmail.

🚀 Funcionalidades
✅ Envio de e-mails com assunto e corpo personalizados.
✅ Suporte para múltiplos destinatários.
✅ Conexão segura via SMTP (TLS).

🛠 Pré-requisitos
Antes de utilizar o código, você precisa:

Ter uma conta no Gmail.
Ativar a autenticação por senha de app no Gmail (https://support.google.com/mail/answer/185833).
Ter o Python instalado (versão 3.x recomendada).
📌 Configuração e Uso
1️⃣ Instale os pacotes necessários
O código utiliza a biblioteca padrão do Python, então não é necessário instalar pacotes adicionais.

2️⃣ Configure suas credenciais
Antes de rodar o script, edite as seguintes variáveis no código:

```python
# Dados de conexão
username = "seu_email@gmail.com"  # Substitua pelo seu e-mail
senha = "sua_senha_de_app"  # Substitua pela senha de app gerada no Gmail

# Informações do e-mail
dest = "destinatario@exemplo.com"  # Substitua pelo e-mail do destinatário
assunto = "Assunto do E-mail"  # Digite o assunto
corpo = "Olá, este é um e-mail enviado automaticamente!"  # Corpo do e-mail


# Informações do e-mail
dest = "destinatario@exemplo.com"  # Substitua pelo e-mail do destinatário
assunto = "Assunto do E-mail"  # Digite o assunto
corpo = "Olá, este é um e-mail enviado automaticamente!"  # Corpo do e-mail
3️⃣ Execute o código
Salve o arquivo como enviar_email.py e execute no terminal:

```sh
python enviar_email.py


🔍 Possíveis Erros e Soluções
Erro de autenticação (SMTPAuthenticationError)

Verifique se o e-mail e a senha de app estão corretos.
Certifique-se de que a autenticação por senha de app está ativada.
Erro de conexão (SMTPConnectError)

Verifique sua conexão com a internet.
O Gmail pode estar bloqueando acessos suspeitos. Tente desbloquear através do e-mail de alerta recebido.