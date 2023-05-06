from flask_restx import Namespace, fields


# 문의 DTO(for save)
class InquiryDto:
    api = Namespace('inquiry', description='문의 관련 API')

    inquiry = api.model('inquiry', {
        'email_to': fields.String(required=True, description='요청할 기관/단체 이메일'),
        'email_from': fields.String(required=True, description='요청인 이메일'),
        'name': fields.String(required=True, description='요청인 이름'),
        'title': fields.String(required=False, description='요청 제목'),
        'content': fields.String(required=False, description='요청 내용')
    })

    inquiry_id = api.model('inquiry_id', {
        'inquiry_id': fields.Integer(required=True, description='삭제할 문의 번호 ')
    })



