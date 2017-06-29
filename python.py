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

    ''' ссылка на метод для получения последнего подписчика https://vk.com/dev/groups.getMembers'''

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
    """"
    Pastes another image into this image. The box argument is either a 2-tuple giving the upper left corner, a 4-tuple 
    defining the left, upper, right, and lower pixel coordinate, or None (same as (0, 0)). If a 4-tuple is given, the 
    size of the pasted image must match the size of the region.

If the modes don’t match, the pasted image is converted to the mode of this image (see the convert() method for details).

Instead of an image, the source can be a integer or tuple containing pixel values. The method then fills the region with
 the given color. When creating RGB images, you can also use color strings as supported by the ImageColor module.

If a mask is given, this method updates only the regions indicated by the mask. You can use either “1”, “L” or “RGBA”
 images (in the latter case, the alpha band is used as mask). Where the mask is 255, the given image is copied as is. 
 Where the mask is 0, the current value is preserved. Intermediate values will mix the two images together, including 
 their alpha channels if they have them.

See alpha_composite() if you want to combine images with respect to their alpha channels.

Parameters:	
im – Source image or pixel value (integer or tuple).
box –
An optional 4-tuple giving the region to paste into. If a 2-tuple is used instead, it’s treated as the upper left corner.
 If omitted or None, the source is pasted into the upper left corner.

If an image is given as the second argument and there is no third, the box defaults to (0, 0), and the second argument 
is interpreted as a mask image.

mask – An optional mask image."""


if __name__ == '__main__':
    image_processor()
    # main()

pass