import json

from main import db
from main.models import Inquiry
from main.utils import errors, mail


# 문의 저장
def save_new_inquiry(data, image):

    # data(str) -> dict
    data = json.loads(data)

    title = data['title'] if data['title'] else '업로드하신 사진에 대한 교체 요청입니다.'

    content = data['content'] if data['content'] else '업로드하신 사진에 대한 교체를 요청합니다.'

    new_inquiry = Inquiry(
        email_to=data['email_to'],
        email_from=data['email_from'],
        name=data['name'],
        title=title,
        content=content
    )

    # 문의 발송
    converted_image = image.stream.read()

    mail.send_mail(title, content, data['email_to'], converted_image)

    # 문의 저장
    save_change(new_inquiry)

    success_response = {
        'message': '문의가 성공적으로 전송 및 등록되었습니다.'
    }

    return success_response, 201


# 문의 삭제
def delete_inquiry(data):

    id = data['inquiry_id']

    find_inquiry = Inquiry.query.filter_by(id=id).first()

    if find_inquiry:
        db.session.delete(find_inquiry)
        db.session.commit()

        success_response = {
            'message': '문의가 성공적으로 삭제되었습니다.'
        }

        return success_response, 200

    else:
        return errors.sendInquiryNotFoundError()


def save_change(data):
    db.session.add(data)
    db.session.commit()