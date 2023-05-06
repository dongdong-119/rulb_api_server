from flask_restx import abort


# 500
def sendInternalServerError():
    abort(500, '서버에러가 발생했습니다.')


# 400 - 1) FileFormat
def sendBadRequestFileFormatError():
    abort(400, '파일이 없거나, 지원하지 않는 파일 형식입니다.')


# 404 - 1) Inquiry Not Found
def sendInquiryNotFoundError():
    abort(404, '존재하지 않는 문의입니다.')