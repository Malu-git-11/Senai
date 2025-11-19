import google.generativeai as genai
import sys

API_KEY = "AIzaSyC4IELKDx3ZzWHr_GsrqXzJzIQtCGjAK7Q"

try:
    genai.configure(api_key=API_KEY)
except Exception as e:
    print(f"Error configuring API key: {e}")
    sys.exit(1)
    
print("Iniciando o modelo...")

try:
    model = genai.GenerativeModel(model_name='gemini-2.5-flash')
except Exception as e:
    print(f"Error initializing model: {e}")
    sys.exit(1)
    
print("Gerando o conteúdo...")
response = model.generate_content(input("Digite sua pergunta ou solicitação: "))

print("\n Resposta do meu assistente virtual: ")
print(response.text)
print("\n Fim da resposta.")