import os

# Настройки для тестирования API
base_url = "https://web-agr.chitai-gorod.ru"
token = os.getenv("bearer_token")
headers = {
    "Authorization": f"Bearer {token}"
}

# Настройки для тестирования UI
ui_url = "https://www.chitai-gorod.ru/"
