from main import db
from main.utils import validation


#
def get_image(r):

    image = validation.validate_input_image(r)

    return image