import string
import random
import qrcode
from django.conf import settings
from PIL import Image

class UrlShortener:
    def __init__(self, url_to_short=None):
        self.url_to_short = url_to_short

    @staticmethod
    def short_url_free(host_url):
        url = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        return [url, host_url + url]
    

class GenerateQR(UrlShortener):
    
    @staticmethod
    def generate_qr_free(host_url):
        generated_url = 'QR' + ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        path_to_qr = f'media/qr/{generated_url}.png'
            
        # открываем наше лого 
        # будет помещено в центре QR кода
        Logo_link = f'media/qr_logos/default_logo.jpg'
    
        logo = Image.open(Logo_link)
    
        # Устанавливаем базовую ширину
        basewidth = 100
    
        # Подстраиваем размер изображения
        wpercent = (basewidth/float(logo.size[0]))
        hsize = int((float(logo.size[1])*float(wpercent)))
        logo = logo.resize((basewidth, hsize), Image.LANCZOS)
        QRcode = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H
        )
 
        # добавляем ссылку на QR-код
        QRcode.add_data(host_url + generated_url)
 
        # генерируем QR-код
        QRcode.make()
 
        # устанавливаем основной цвет
        QRcolor = 'Green'
    
        # добавляем основной цвет к QR-коду
        QRimg = QRcode.make_image(
            fill_color=QRcolor, back_color="white").convert('RGB')
 
        # задаем размер QR-кода
        pos = ((QRimg.size[0] - logo.size[0]) // 2,
               (QRimg.size[1] - logo.size[1]) // 2)
        QRimg.paste(logo, pos)
    
        # сохраняем QR-код по пути указанному в начале метода
        QRimg.save(path_to_qr)

        return [path_to_qr, generated_url]