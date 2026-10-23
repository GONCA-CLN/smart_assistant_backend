"""
1. fastAPI uygulaması oluştur
2. kullanıcıdan mesaj alan post endpointi
3. sahte akıllı asistan cevabı üretilecek
4. soru ve cevabı SQLite database'ine kaydedilecek
5. tüm mesajajları listeleyen get endpointi oluşturulacak
"""

from fastapi import FastAPI
from pydantic import BaseModel

from assistant_logic import fake_smart_assistant
from database import create_table, save_message, get_all_messages

app=FastAPI()

# db başlat
create_table()

class MessageRequest(BaseModel):
    user_message: str

@app.get("/")
def home():
    return {
        "message": "Akıllı asistan API çalışıyor"
    }

@app.post("/chat")
def chat_with_assistant(request: MessageRequest):

    user_message = request.user_message

    # sahte asistan cevabı
    assistant_response = fake_smart_assistant(user_message)

    # soru ve cevabı veri tabanına kaydetme
    save_message(user_message, assistant_response)

    return{
        "user_message": user_message,
        "assistant_reponse": assistant_response
    }

@app.get("/messages")
def read_all_messages():

    messages=get_all_messages()
    
    return {"messages": messages}