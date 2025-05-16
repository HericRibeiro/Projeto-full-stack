import requests
import json
from flask import Flask, request, jsonify
import base64
import pandas as pd
from io import StringIO, BytesIO
import xml.etree.ElementTree as ET

email = "hericribeiro@abrtelecom.com.br"
api_token = "https://api.aia.abrtelecom.com.br/portal/number/v1/number/search"
base_url = 'https://acesso.aia.abrtelecom.com.br'


auth_string = f"{email}:{api_token}"
auth_base64 = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')

# === ENDPOINT ===
# url = f"{base_url}/api/v1/reports"
# url = f"{base_url}/api/v1/users"
# url = f"{base_url}/api/v1/tasks"


auth_string = f"{email}:{api_token}"
auth_base64 = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')

# === ENDPOINT ===
url = f"{base_url}/api/v1/reports"

headers = {
    "Accept": "*/*",  # Aceita qualquer tipo de conteúdo
    "Authorization": f"Basic {auth_base64}"
}

params = {
    "start": 0,
    "limit": 1000,
}

# === REQUISIÇÃO ===
response = requests.get(url, headers=headers, params=params)
content_type = response.headers.get('Content-Type', '')

print(f"\n➡️ Status: {response.status_code}")
print(f"🧾 Content-Type: {content_type}\n")

# === TRATAMENTO DINÂMICO ===
if response.status_code == 200:
    if "application/json" in content_type:
        try:
            data = response.json()
            print("✅ JSON recebido:")
            print(json.dumps(data, indent=4, ensure_ascii=False))
        except json.JSONDecodeError:
            print("❌ Erro ao decodificar JSON.")
    
    elif "text/csv" in content_type:
        print("✅ CSV recebido:")
        df = pd.read_csv(StringIO(response.text))
        print(df.head())

    elif "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" in content_type or "application/vnd.ms-excel" in content_type:
        print("✅ Excel recebido:")
        df = pd.read_excel(BytesIO(response.content))
        print(df.head())

    elif "application/xml" in content_type or "text/xml" in content_type:
        print("✅ XML recebido:")
        root = ET.fromstring(response.content)
        for elem in root.iter():
            print(f"{elem.tag}: {elem.text}")
    
    else:
        print("⚠️ Tipo de conteúdo não identificado. Exibindo resposta bruta:")
        print(response.text)

else:
    print(f"❌ Erro {response.status_code} - {response.reason}")
    print(f"Detalhes: {response.text}")



# # === AUTENTICAÇÃO ===
# auth_string = f"{email}:{api_token}"
# auth_base64 = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')

# headers = {
#     "Accept": "application/json",
#     "Authorization": f"Basic {auth_base64}"
# }
# params = {
#     "start": 0,
#     "limit": 1000,
# }

# response = requests.get(url, headers=headers, params=params)
# print(response)