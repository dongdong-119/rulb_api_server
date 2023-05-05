from flask import request, jsonify
from flask_restx import Resource, Namespace
from werkzeug.utils import secure_filename

from main import db
from main.utils import validation


"""
    [사진 관련 API] : /picture
    
    1. /upload (post)
    : 업로드된 사진 -> ai 모델 -> 결과 반환
    
    2. 
    
    
"""


Picture = Namespace(
    name='picture',
    description='사진 관련 API'
)


# 사진 업로드 api
@Picture.route('/upload')
class PicturePost(Resource):

    def get(self):

        # 1. 데이터 검증
        image = validation.validate_input_image(request)

        image_name = secure_filename(str(image.filename))

        # image.save(secure_filename(image_name))

        # 2. ai 모델에 넣어서 pred 받아옴
        # >> Return : pred(사각형 좌표, 가로 세로 길이)


        # 3. DTO 형식으로 jsonify해서 반환
        # >> Return : 2의 결과(dict) /

        result = dict()

        # 얼굴 인식 완료
        if result:
            return jsonify(result)
        # 얼굴 인식 불가능
        else:
            return 0


# 사진 올려서 -> 결과 값 받는데 post? get?
#

# @Picture.route('/')