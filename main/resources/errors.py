from flask_restx import abort

# 500
def sendInternalServerError():
    abort(500, "서버에러가 발생했습니다.")


# 400 - 1) FileFormat
def sendBadRequestFileFormat():
    abort(400, "Bad Request - 파일이 없거나, 지원하지 않는 파일 형식입니다.")

# 