# Чат-приложение

Это простое чат-приложение, построенное с использованием FastAPI, Vue.js и Socket.io

# Технологии
- Фронтенд: Vue.js, Bootstrap, Socket.io
- Бэкенд: FastAPI, Python-Socketio

# Установка

### Бэкенд (FastAPI)
1. Установите зависимости:
   ```pip install -r backend/requirements.txt```

Запустите сервер:

```
uvicorn backend.main:app --reload
python backend/socket_server.py
```

### Фронтенд (Vue.js)
Установите зависимости:
```
npm install
```

Запустите фронтенд:
```
npm run dev
```
