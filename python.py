import vk_api


def main():
    """ Пример загрузки фото """

    login, password = 'login', 'pass'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    """ В VkUpload реализованы методы загрузки файлов в ВК
    """

    # upload = vk_api.VkUpload(vk_session)
    #
    # photo = upload.photo(  # Подставьте свои данные
    #     'gurren.jpg',
    #     album_id=98457962
    # )
    #
    # vk_photo_url = 'https://vk.com/photo{}_{}'.format(
    #     photo[0]['owner_id'], photo[0]['id']
    # )
    # print(photo, '\nLink: ', vk_photo_url)
    request = {'group_id': 58907644, 'crop_x': 0, 'crop_y': 0, 'crop_x2':795, 'crop_y2':200, 'v':5.65}
    # 'access_token': None, 'captcha_sid': None, 'captcha_key': None
    address = vk_api.VkApi.method(vk_session,'photos.getOwnerCoverPhotoUploadServer',request)
    print (address)
    upload = vk_api.VkUpload(vk_session)

    # photo = upload.photo_profile( 'gurren.jpg',-58907644)
    crop_params = {}
    crop_params['_square_crop'] = '{},{},{}'.format(0, 0, 790)

    def open_files(paths, key_format='file{}'):
        if not isinstance(paths, list):
            paths = [paths]

        files = []

        for x, file in enumerate(paths):
            if hasattr(file, 'read'):
                f = file

                if hasattr(file, 'name'):
                    filename = file.name
                else:
                    filename = '.jpg'
            else:
                filename = file
                f = open(filename, 'rb')

            ext = filename.split('.')[-1]
            files.append(
                (key_format.format(x), ('file{}.{}'.format(x, ext), f))
            )

        return files
    def close_files(files):
        for f in files:
            f[1][1].close()

    photo_file = open_files('gurren.jpg', key_format='file')
    response = upload.vk.http.post(address['upload_url'], data=crop_params, files=photo_file)
    print (response)
    close_files(photo_file)


if __name__ == '__main__':
    main()