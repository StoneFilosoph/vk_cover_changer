from vk_api import upload
# метод открытия файла для передачи фото
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

# метод закрытия файла для передачи фото
def close_files(files):
    for f in files:
        f[1][1].close()
# метод для загрузки обложки сообщества
def group_cover(session, photo, group_id=None, crop_x=None, crop_y=None, crop_width=None):
    values = {}

    if group_id:
        values['group_id'] = group_id

    crop_params = {}

    if crop_x is not None and crop_y is not None and crop_width is not None:
        crop_params['_square_crop'] = '{},{},{}'.format(
            crop_x, crop_y, crop_width
        )

    response = session.vk.method('photos.getOwnerCoverPhotoUploadServer', values)
    url = response['upload_url']

    photo_files = open_files(photo, key_format='file')
    response = session.vk.http.post(url, data=crop_params, files=photo_files)
    close_files(photo_files)

    response = session.vk.method('photos.getOwnerCoverPhotoUploadServer', response.json())

    return response

def get_last_subscriber(session, group_id, sort='time_desc', offset=0,count=1, fields='photo_50'):
    values ={}
    values['group_id'] = group_id
    values['sort'] = sort
    values['offset'] = offset
    values['count'] = count
    values['fields'] = fields
    response = session.vk.method('groups.getMembers', values)
    print(response)