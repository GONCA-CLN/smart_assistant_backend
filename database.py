"""
1) mesajları saklamak için tablo oluştur
2) kaydet: kullanıcı mesajı ve asistan cevabı
3) listele: kayıtlı tüm mesajları listele
"""

import sqlite3

DB_NAME= "assistant.db"

def create_table():
    """
    Mesajları saklayan tablo oluşturulacak
    """
    conn=sqlite3.connect(DB_NAME)
    cursor=conn.cursor()

    cursor.execute(
        """
            CREATE TABLE IF NOt EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_message TEXT NOT NULL,
                assistant_response TEXT NOT NULL            
            )
        """
    )

    conn.commit()
    conn.close()

def save_message(user_message: str, assistant_response: str):
    """
    Kuulanıcı mesajı ve asistan cevabı veri tabanına kaydedilir
    """

    conn=sqlite3.connect(DB_NAME)
    cursor=conn.cursor()

    cursor.execute(
        """
            INSERT INTO messages (user_message, assistant_response)
            VALUES (?,?)
            
        """, (user_message,assistant_response)
    )

    conn.commit()
    conn.close()

def get_all_messages():
    """
    veri tabanındaki tüm mesajları getirir
    """
    conn=sqlite3.connect(DB_NAME)
    cursor=conn.cursor()

    cursor.execute(
        """
            SELECT id, user_message, assistant_response
            FROM messages
            ORDER BY id ASC 
        """
    )

    rows = cursor.fetchall()
    conn.close()

    messages = []
    for row in rows:
        messages.append(
            {
                "id": row[0],
                "user_message": row[1],
                "assistant_response": row[2]
            }
        )
    
    return messages

if __name__ == "__main__":

    create_table()

    save_message(

        "merhaba nasılsın",
        "merhaba, size nasıl yardımcı olabilirim"
    )

    all_messages= get_all_messages()

    print(all_messages)

