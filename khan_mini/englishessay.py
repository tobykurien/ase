import cherrypy
from settings import *
import essaylib.db
import hashlib


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
        return "Hallo world" + username

    @cherrypy.expose    
    def admin(self, password=None, bsubmit=None):
        result = ''
        conn = essaylib.db.makeConnection(ESSAY_DB)
        if password == None:
            result = env.get_template('adminlogin.html').render()
        elif hashlib.sha224(password).hexdigest() == essaylib.db.getPasswordHash(conn):
            cherrypy.session['admin'] = True
            rows = essaylib.db.listAssignments(conn)
            cols = ['Id','Title','Description','State','Date','Action']
            result = env.get_template('adminassignments.html').render({'rows':rows,'cols':cols})
        else:
            result = env.get_template('adminlogin.html').render()
        return result
    

if __name__=="__main__":
    # load config for global and application
    cherrypy.config.update(khanconf)
    cherrypy.tree.mount(EnglishEssay(), '/englishessay', config=enlishessayconf)

    cherrypy.engine.start()
    cherrypy.engine.block()
