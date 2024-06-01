## Версия питона 3.8...3.11
- Django 4.2
## Расширения в VS Code
- Python
- Pylance
- Django
- Black Formater
- Live Server
- Material Icon Theme
- IntelliSense for CSS
- CSS Peek
- Auto Rename Tag
## Запуск проекта в VS Code
1. Создать папку на диске(например dev_env) и закинуть туда папку magaz_u_lechi
2. Открыть папку dev_env в VS Code
3. В VS Code => teminal=> python -m venv venv 
- Создастся папка venv
4. terminal=>dev_env\venv\Scripts\activate
  - в терминале появится виртуальное окружение - (venv) dev_env>
- если не удается ,то
- terminal => Get-ExecutionPolicy
- если ответ Restricted , то запрещено.
- terminal => Set ExecutionPolicy RemoteSigned
- и повторить шаг №4
5. terminal=> pip install django==4.2.7
6. terminal => pip install Pillow
7. Сохранить виртуальное окружение:
  - VS Codec => open => manage.py
  - В правом нижнем углу VSCode кликнуть на версию питона <3.11.64-bit>
  - => Enter interpretator path...
  - =>find...
  - =>указать путь dev_env\venv\Scripts\python.exe
  8. terminal => python manage.py runserver
    -и кликаем по ссылке в терминале http://127.0.0.1:8000/
    - и разглядываем кнопочки магаза
