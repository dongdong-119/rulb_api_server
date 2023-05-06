from flask import request, jsonify
from flask_restx import Resource, Namespace

from main.service import inquiry_service
from main.dtos import InquiryDto

""" 
    [문의(Contact) 관련 API] : /contact 
    
    1. 문의 생성(POST)
    2. 문의 삭제(DELETE)
    3. 
    
    """

api = InquiryDto.api
_inquiry = InquiryDto.inquiry
_inquiry_id = InquiryDto.inquiry_id


@api.route('/')
class InquiryManager(Resource):

    @api.response(201, '문의가 성공적으로 등록되었습니다.')
    @api.expect(_inquiry, validate=False)
    def post(self):

        """Create new Inquiry"""

        data = request.json

        return inquiry_service.save_new_inquiry(data)


    @api.expect(_inquiry_id, validate=False)
    @api.response(200, '문의가 성공적으로 삭제되었습니다.')
    @api.response(404, '존재하지 않는 문의입니다.')
    def delete(self):

        """Delete Inquiry with inquiry_id"""

        data = request.json

        return inquiry_service.delete_inquiry(data)