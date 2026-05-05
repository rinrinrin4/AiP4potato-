#1
from PIL import Image
img = Image.open("C:/Users/Admin/OneDrive/Рабочий стол/jjjjjhhhhh (25).jpg")
width, height = img.size
form= img.format
color=img.mode
img.show()
print(width, height, form, color)

#2

def process_image_92(path)
    img = Image.open(path)

    # Уменьшение в 3 раза
    new_size = (img.width // 3, img.height // 3)
    resized = img.resize(new_size, Image.Resampling.LANCZOS)
    resized.save('resized_' + path)

    # Горизонтальное зеркало
    mirror_h = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    mirror_h.save('mirror_h_' + path)

    # Вертикальное зеркало
    mirror_v = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    mirror_v.save('mirror_v_' + path)

#3

    if not os.path.exists("filtered"):
        os.mkdir("filtered")

    for i in range(1, 6):
        name = str(i) + ".jpg"

        if os.path.exists(name):
            img = Image.open(name)

            #черно-белый
            bw_img = img.convert("L")
            new_name = "filtered/filtered_" + str(i) + ".jpg"
            bw_img.save(new_name)
            print("Обработан:", name)
        else:
            print("Файл не найден:", name)

#4

if not os.path.exists("watermarked"):
    os.mkdir("watermarked")


watermark_text = "My Watermark"

for i in range(1, 6):
    name = str(i) + ".jpg"

    if os.path.exists(name):

        img = Image.open(name)
        draw = ImageDraw.Draw(img)

        draw.text((img.width - 100, img.height - 30), watermark_text, fill="white")

        new_name = "watermarked/wm_" + str(i) + ".jpg"
        img.save(new_name)