from flask import request, jsonify
from flask_restx import Resource, Namespace

from main import db
from main.utils import validation

""" 
    [문의(Contact) 관련 API] : /contact 

    
    
    """

Contact = Namespace(
    name='contact',
    description='문의 관련 API'
)


@Contact.route('/')
class ContactManager(Resource):

    def post(self):

        return 1

    def get(self):

        return 2

