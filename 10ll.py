from PIL import Image

img = Image.open("postcard.jpg")
cropped = img.crop((50, 50, 350, 350))
cropped.save("cropped.jpg")


#2

holidays = {
    "новый год": "new_year.jpg",
    "8 марта": "march8.jpg",
    "день рождения": "birthday.jpg"
}


question = "К какому празднику нужна открытка? (новый год, 8 марта, день рождения): "
user_input = input(question)

if user_input in holidays:
    filename = holidays[user_input]
    img = Image.open(filename)
    img.show()


    #3

    from PIL import Image, ImageDraw, ImageFont

    # Словарь с праздниками и файлами
    holidays = {
        "новый год": "new_year.jpg",
        "8 марта": "march8.jpg",
        "день рождения": "birthday.jpg"
    }


    user_holiday = input("К какому празднику? (новый год, 8 марта, день рождения): ")

    if user_holiday in holidays:
        filename = holidays[user_holiday]
        img = Image.open(filename)

        name = input("Введите имя: ")
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except:
            font = ImageFont.load_default()


        text = name + ", поздравляю!"

        if user_holiday == "новый год":
            color = "red"
        elif user_holiday == "8 марта":
            color = "pink"
        else:
            color = "blue"

        # Рисуем текст в верхней части по центру
        # Вычисляем позицию для центрирования
        text_width = len(text) * 20  # Примерная ширина
        x = (img.width - text_width) // 2
        y = 50

        draw.text((x, y), text, fill=color, font=font)

        new_filename = name + "_" + user_holiday + ".png"
        img.save(new_filename)
        print("Сохранено как:", new_filename)

        img.show()
    else:
        print("Праздник не найден")