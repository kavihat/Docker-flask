'''
Controller to render index.html
'''
from flask import render_template
# don't change this import or it can't find the module controller
from .controller import ControllerBase


class IndexController(ControllerBase):
    '''
    class to render index.html
    '''
    @staticmethod
    def get():
        '''
        static method to render index.html
        '''
        name = "Kavitha Kannanunny"
        return render_template('index.html', name=name)
