import requests

# Dados da sua conta da Nexmo
NEXMO_API_KEY = "ce9f1f15"
NEXMO_API_SECRET = "sRSeARGzTNaA3iXM"
NEXMO_PHONE_NUMBER = "14157386102"

# Função para enviar uma mensagem usando a API da Nexmo
def send_message(to_number, message):
    url = f"https://rest.nexmo.com/sms/json?api_key={NEXMO_API_KEY}&api_secret={NEXMO_API_SECRET}&from={NEXMO_PHONE_NUMBER}&to={to_number}&text={message}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False

# Pedir as informações do usuário
to_number = input("Digite o número de telefone do destinatário (no formato internacional): ")
message = input("Digite a mensagem que deseja enviar: ")

# Enviar a mensagem
if send_message(to_number, message):
    print("Mensagem enviada com sucesso!")
else:
    print("Ocorreu um erro ao enviar a mensagem.")
