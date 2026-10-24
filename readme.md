Sahte akıllı asistan fonksiyonunun geliştirilmesi
SQLite ile database işlemleri 
FastAPI ile endpoint oluşturma
    Sanal ortam:
        python -m venv venv
        .\venv\Scripts\activate
    Kurulum:
        pip install fastapi uvicorn
    çalıştırma:
        uvicorn main:app --reload
        swagger test
Backend uygulamasını Docker ile test et
    requirements.txt
    image oluştırmak için:
        Dockerfile
        Docker desktop çalıştır
        docker build -t smart_assitant_api .
    image çalıştırmak için
        docker run -d -p 8000:8000 --name smart_assitant_container smart_assitant_api
        http://localhost:8000/docs

Backendi github'a yükle ve Render ile canlıya al
    .gitignore
    repo: smart_assistant_backend

    git init
    git add .
    git commit -m "gnc first commit"
    git branch -M main
    git remote add origin https://github.com/GONCA-CLN/smart_assistant_backend.git
    git push -u origin main

    Render URL:
    https://smart-assistant-backend-ziz7.onrender.com