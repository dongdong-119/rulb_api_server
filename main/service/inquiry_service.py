from main import db
from main.models import Inquiry
from main.utils import validation, errors


# 문의 저장
def save_new_inquiry(data):

    title = data['title'] if data['title'] else '무제'
    content = data['content'] if data['content'] else '내용 없음'

    new_inquiry = Inquiry(
        email_to=data['email_to'],
        email_from=data['email_from'],
        name=data['name'],
        title=title,
        content=content
    )

    save_change(new_inquiry)

    success_msg = {
        'message': '문의가 성공적으로 등록되었습니다.'
    }

    return success_msg, 201


# 문의 삭제
def delete_inquiry(data):

    id = data['inquiry_id']

    find_inquiry = Inquiry.query.filter_by(id=id).first()

    if find_inquiry:
        db.session.delete(find_inquiry)
        db.session.commit()

        success_msg = {
            'message': '문의가 성공적으로 삭제되었습니다.'
        }

        return success_msg, 200

    else:
        return errors.sendInquiryNotFoundError()


def save_change(data):
    db.session.add(data)
    db.session.commit()