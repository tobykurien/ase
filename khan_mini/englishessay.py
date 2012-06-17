import cherrypy
from settings import *

# Jinja templating engine
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

class EnglishEssay(object):
                
    @cherrypy.expose    
    def index(self, username=None):
        if username == None:
            username = cherrypy.session.get('username', None)
            if username == None:
                raise cherrypy.HTTPRedirect("/login")                
        return "Hallo world"

if __name__=="__main__":
    # load config for global and application
    cherrypy.config.update(khanconf)
    cherrypy.tree.mount(EnglishEssay(), '/englishessay', config=enlishessayconf)

    cherrypy.engine.start()
    cherrypy.engine.block()
