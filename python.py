import vk_api
from PIL import Image


def main():



    login, password = 'login', 'pass'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    """ В VkUpload реализованы методы загрузки файлов в ВК
    """
    upload = vk_api.VkUpload(vk_session)
    cover = upload.group_cover('gurren.jpg', 58907644)


    """group cover changer  method for vk_api class VkUpload"""
    # def group_cover(self, photo, group_id=None, crop_x=None, crop_y=None, crop_width=None):
    #     values = {}
    #
    #     if group_id:
    #         values['group_id'] = group_id
    #
    #     crop_params = {}
    #
    #     if crop_x is not None and crop_y is not None and crop_width is not None:
    #         crop_params['_square_crop'] = '{},{},{}'.format(
    #             crop_x, crop_y, crop_width
    #         )
    #
    #     response = self.vk.method('photos.getOwnerCoverPhotoUploadServer', values)
    #     url = response['upload_url']
    #
    #     photo_files = open_files(photo, key_format='file')
    #     response = self.vk.http.post(url, data=crop_params, files=photo_files)
    #     close_files(photo_files)
    #
    #     response = self.vk.method('photos.getOwnerCoverPhotoUploadServer', response.json())
    #
    #     return response


def image_processor():
    image1 = Image.new('RGB',(500, 500))
    image2 = Image.new('RGB', (100, 100), 156)
    image1.paste(image2)
    image1.show()


if __name__ == '__main__':
    image_processor()
    # main()
