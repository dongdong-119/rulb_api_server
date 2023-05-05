from flask import request
from main.resources import errors

"""
    검증 함수
    
    1. validate_input_image  
    2. 

"""


def validate_input_image(request):

    files = request.files

    # 이미지 개수
    if not files or len(files) >= 2:
        errors.sendBadRequestFileFormat()

    # 'image' 이름의 파일 / 파일 형식
    if 'image' not in files or files['image'].content_type is None:
        errors.sendBadRequestFileFormat()

    image = files['image']
    c_type = image.content_type.split('/')[0]

    if c_type != 'image':
        errors.sendBadRequestFileFormat()

    return image
