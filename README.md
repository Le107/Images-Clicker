Автокликер по изображениям
===
Автокликер с распознаванием изображений. Ищет совпадения(точность 80%, можно изменить в коде: confidence=0.8) на экране с изображениями в папке Images в алфавитном порядке. Здесь(Images) пример игры Beneath Oresa.

Как использовать
===
Установите зависимости, перечисленные в файле requirements.txt:
```bash
pip install -r requirements.txt
```
Запустите сценарий 
```bash
python main.py 
```
или 
```bash
start.bat 
```
Горячие клавиши: Пробел - старт; x - пауза; Esc - стоп(см. также в коде).
Если не работает(в играх): python.exe -> Свойства -> Совместимость -> Запускать эту программу от имени администратора. Также для PyCharm.
