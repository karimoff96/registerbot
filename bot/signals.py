import requests
from environs import Env

env = Env()
env.read_env()


def send_appointment_to_doctor(message: dict, to: str = "well_admin"):
    text = f"""Yangi qabul!\nTartib raqami: {message['id']}\nBe'mor ismi: {message['patient']['first_name']}\nBe'mor familiyasi: {message['patient']['last_name']}\nQabul kuni: {message['appointment']['day']}\nQabul soati: {message['appointment']['time']}\nYaratilgan vaqti: {message['appointment']['created_at']}\n{f'Qo`shimcha: {message["patient"]["complaint"]}' if len(message['patient']['complaint'])>0 else 'Qo`shimcha: Admin panel orqali ariza yaratildi'} """
    url = f"""https://api.telegram.org/bot{env.str("BOT_TOKEN")}/sendMessage?chat_id={to}&text={text}"""
    try:
        _ = requests.get(url)
    except:
        pass
