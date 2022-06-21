from pyrogram import Client

api_id = 12695478
api_hash = '68fc86f6b4ae0914f4de906fe556d964'

# Создаём программный клиент, передаём в него
# имя сессии и данные для аутентификации в Client API
app = Client('my_account', api_id, api_hash)

app.start()
# Отправляем сообщение
# Первый параметр - это id чата или имя получателя.
# Зарезервированное слово 'me' означает собственный аккаунт отправителя.
app.send_message('me', 'Привет, это я!')
app.stop()
