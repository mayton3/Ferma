from google.colab import drive
import os

# Монтируем Google Диск
drive.mount('/content/drive')

# Путь к папке на Google Диске для вашей директории
backup_folder = '/content/drive/MyDrive/GA_backup'

# Создаём папку, если её нет
os.makedirs(backup_folder, exist_ok=True)

print(f"Папка создана или уже существует: {backup_folder}")
