# Программа для генерации HTML-страницы об Университете «Синергия»

html_content = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Университет «Синергия»</title>
    <!-- Подключаем основной шрифт (Montserrat) и 5 альтернативных из Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Roboto&family=Open+Sans&family=Lato&family=Oswald&family=Ubuntu&display=swap" rel="stylesheet">
    
    <style>
        /* ОФИЦИАЛЬНЫЙ ШРИФТ КОМПАНИИ */
        body {
            font-family: 'Montserrat', sans-serif; /* Основной шрифт */
            background-color: #f4f4f9;
            color: #333333;
            line-height: 1.6;
            margin: 0;
            padding: 40px 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .container {
            background: #ffffff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            max-width: 800px;
            width: 100%;
        }

        h1 {
            color: #E30613; /* Фирменный красный цвет Синергии */
            text-align: center;
            margin-bottom: 20px;
        }

        .info-block {
            margin-bottom: 40px;
        }

        h2 {
            border-bottom: 2px solid #E30613;
            padding-bottom: 5px;
            display: inline-block;
        }

        /* 5 АЛЬТЕРНАТИВНЫХ ВАРИАНТОВ ШРИФТОВ */
        .font-demo {
            margin-bottom: 15px;
            padding: 15px;
            background: #f8f9fa;
            border-left: 5px solid #E30613;
            border-radius: 4px;
            font-size: 16px;
        }

        .font-1 { font-family: 'Roboto', sans-serif; }
        .font-2 { font-family: 'Open Sans', sans-serif; }
        .font-3 { font-family: 'Lato', sans-serif; }
        .font-4 { font-family: 'Oswald', sans-serif; }
        .font-5 { font-family: 'Ubuntu', sans-serif; }
    </style>
</head>
<body>

    <div class="container">
        <h1>Университет «Синергия»</h1>
        
        <div class="info-block">
            <p><b>Организационно-правовая форма:</b> Автономная некоммерческая организация высшего образования (АНО ВО).</p>
            <p><b>О компании:</b> Один из крупнейших вузов России и лидер рынка EdTech. Университет реализует более 700 образовательных программ, имеет филиалы в регионах РФ и за рубежом (Дубай), а также собственную высокотехнологичную экосистему дистанционного обучения (LMS Synergy). Основной упор делается на практико-ориентированное образование и трудоустройство выпускников.</p>
        </div>

        <div class="fonts-block">
            <h2>5 дополнительных вариантов шрифтов</h2>
            <p>Ниже представлен текст, стилизованный пятью разными шрифтами для сравнения с основным корпоративным стилем:</p>
            
            <div class="font-demo font-1">
                <b>Вариант 1 (Roboto):</b> Университет «Синергия» — фундаментальные академические традиции и современные технологии.
            </div>
            <div class="font-demo font-2">
                <b>Вариант 2 (Open Sans):</b> Университет «Синергия» — фундаментальные академические традиции и современные технологии.
            </div>
            <div class="font-demo font-3">
                <b>Вариант 3 (Lato):</b> Университет «Синергия» — фундаментальные академические традиции и современные технологии.
            </div>
            <div class="font-demo font-4">
                <b>Вариант 4 (Oswald):</b> Университет «Синергия» — фундаментальные академические традиции и современные технологии.
            </div>
            <div class="font-demo font-5">
                <b>Вариант 5 (Ubuntu):</b> Университет «Синергия» — фундаментальные академические традиции и современные технологии.
            </div>
        </div>
    </div>

</body>
</html>"""

filename = "synergy_page.html"
with open(filename, "w", encoding="utf-8") as file:
    file.write(html_content)
print(f"Готово! HTML-страница успешно сгенерирована. Откройте файл {filename} в любом браузере.")
