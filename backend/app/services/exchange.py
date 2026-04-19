import requests

def convert_currency(amount: float, from_currency: str, to_currency: str):
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("Error al obtener tipo de cambio")
    
    data = response.json()
    
    return data["rates"][to_currency]