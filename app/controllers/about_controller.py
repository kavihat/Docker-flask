'''
Controller to render about.html
'''
from flask import render_template
# don't change this import or it can't find the module controller
from .controller import ControllerBase


class AboutController(ControllerBase):
    '''
    To define about controller class  for get
    '''
    @staticmethod
    def get():
        '''
        To define static method for get
        '''
        name = "Kavitha Kannanunny"
        return render_template('about.html', name=name)
