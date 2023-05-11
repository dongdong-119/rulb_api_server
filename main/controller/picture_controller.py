from flask import request, jsonify
from flask_restx import Resource, Namespace
from werkzeug.utils import secure_filename

from main.service import picture_service
from main.yolov5 import detect
import cv2
import os
import shutil

"""
    [사진 관련 API] : /picture
    
    1. /upload 사진 업로드
    : 업로드된 사진 -> ai 모델 -> 결과 반환
    2. 
    
    
"""

api = Namespace(
    name='picture',
    description='사진 관련 API'
)


# 사진 업로드 api
@api.route('/upload')
class PicturePost(Resource):

    @api.response(200, '얼굴인식이 성공적으로 완료되었습니다.')
    @api.response(400, '파일이 없거나, 지원하지 않는 파일 형식입니다.')
    def get(self):

        # 1. 데이터 검증
        image = picture_service.get_image(request)
        RESULT = './main/yolov5/runs/detect/exp'
        FILE = image.filename
        IMG = FILE.split('.')[0]
        
        image.save(secure_filename(FILE))
        img = cv2.imread(FILE)
        height, width, _ = img.shape

        # 2. ai 모델에 넣어서 pred 받아옴
        # >> Return : pred(사각형 좌표, 가로 세로 길이)
        detect.run(weights='best.pt', source='./', save_txt=True)

        boxes,faceCnt = [],0
        try:
            with open(f'{RESULT}/labels/{IMG}.txt','r') as f:
                while True:
                    tmp = f.readline()
                    if not tmp:
                        break
                    tmp = list(map(float,tmp.rstrip().split()))[1:]
                    x, y, w, h = tmp
                    x, w = x*width, w*width
                    x -= w/2
                    y, h = y*height, y*height
                    y -= h/2
                    boxes.append({'x':x, 'y':y, 'width':w, 'height':h})
                    faceCnt += 1
        except:
            print('결과 반환 실패')
            pass

        if os.path.exists(FILE):
            os.remove(FILE)
            print('이미지 삭제 완료')
        if os.path.exists(RESULT):
            shutil.rmtree(RESULT)
            print('삭제완료')

        return jsonify(boxes)


# @Picture.route('/')