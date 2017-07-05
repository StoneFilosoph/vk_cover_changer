import vk_api
from PIL import Image, ImageOps, ImageDraw
from additional_api_methods import group_cover, get_last_subscriber, download_image
import config


def main():
    # задаём логин и пароль для нашей сессии
    login, password = config.login, config.password
    vk_session = vk_api.VkApi(login, password)
    #пробуем авторизоваться
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    # готовим наш объект api_use чтобы передавать его в методы для использования api
    api_use = vk_api.VkUpload(vk_session)

    # получаем последнего подписчика группы
    response = get_last_subscriber(api_use, 58907644)
    # выдергиваем фото_50 из последнего субскрайбера
    photo_of_last_subscriber = response['items'][0]['photo_100']
    first_name_subscriber = response['items'][0]['first_name']
    last_name_subscriber = response['items'][0]['last_name']
    print(first_name_subscriber, last_name_subscriber)
    download_image(photo_of_last_subscriber)
    # готовим картинку компонуем полученную картинку и заготовленную
    output_cover = image_processor(500, 50, 'cover_image.jpg', 'avatar.jpg')
    # загружаем готовую картинку в сообщество
    # cover = group_cover(api_use, output_cover, 58907644)

def image_processor(x, y, base_image, embedded_image):
    size = (100, 100)  #размер аватарки
    bigsize = (900, 900)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(size, Image.ANTIALIAS)

    image1 = Image.open(base_image)
    image2 = Image.open(embedded_image)

    image2 = ImageOps.fit(image2, mask.size, centering=(0.5, 0.5))
    result_image = image1.copy()
    result_image.paste(image2, (x, y), mask=mask)
    result_image.show()
    result_image.save('output_cover.jpg')
    return result_image

if __name__ == '__main__':
    # image_processor()
    main()