from flask import request, jsonify
from flask_restx import Resource, Api, Namespace
from main import db
from main.models import Person

"""
    [사진 관련 API]
    
"""


picture_list = dict()
count = 1


Picture = Namespace(
    name='picture',
    description='사진 관련'
)


# 사진 저장
@Picture.route('/')
class PicturePost(Resource):
    def post(self):
        global count, picture_list

        idx = count
        count += 1
        picture_list[idx] = request.json.get('data')

        person = Person('test-name', 'red')
        db.session.add(person)
        db.session.commit()

        return {
            'picture_id': idx,
            'question_list': picture_list
        }

