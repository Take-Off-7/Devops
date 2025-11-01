from pecan import expose, request, response

class RootController(object):
    @expose('json')
    def index(self):
        return {'message': 'Hello, World!'}
