"""
Amaç: 
    - gerçek bir yapay zeka modli kullanmadan, sabit cevaplar arasından rastgele seçim yapan basit bir akıllı asistan geliştirme

"""
import random

def fake_smart_assistant(user_message: str) -> str:
    """
    Kllanıcıdan gelen mesaj ne olursa olsun,
    hazır cevaplar arasından rastgele birtanesini dödürür    
    """
    # ... buraya ai gelmeli

    responses = [
        "Merhaba size nasıl yardımcı olabilirim?",
        "Tabii, bu konuda size destek olmaya çalışayım",
        "Anladım, isterseniz bunu birlikte inceleyebiliriz",
        "Elbette, size yardımcı olmak için buradayım"
    ]

    return random.choice(responses)

if __name__ == "__main__":
    
    user_text = input("Bir mesaj yazın: ")
    answer = fake_smart_assistant(user_text)
    print(f"Asistan cevabı: {answer}")
