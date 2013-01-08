import cherrypy
import urllib
import urllib2
import json
from stream import Stream
from settings import *
import englishessay
from essaylib.saplugin import SAEnginePlugin, SATool
from essaylib.mysqlsession import MySQLSession
import random

# Jinja templating engine
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

user = None

class KhanAcademyMini(object):
    def __init__(self):
        self.stream = Stream()
        
    def getUser(self):
        return cherrypy.session.get('username', None)
  

    @cherrypy.expose
    def login(self, username=None,pm=0, **args):
        global user
        if username == None:
            user = None
            tmpl = env.get_template('login.html')
            return tmpl.render({})
        tmpl = env.get_template('landing.html')
        cherrypy.session['username'] = username;
        if int(pm) == 1:
           raise cherrypy.HTTPRedirect("/englishessay/index")
        else:   
            return tmpl.render()   

    @cherrypy.expose
    def khan(self):
        #user = username
        user = cherrypy.session['username']
        tmpl = env.get_template('postlogin.html')
        data = {
            'username' : user,
            'post_url' : "%s/_ah/login" % KHAN_BASE_URL,
            'base_url' : KHAN_MINI_BASE_URL
        }
        return tmpl.render(data)
        
    @cherrypy.expose    
    def index(self, topic='root'):
        user = self.getUser()
        if user == None:
            return self.login()
        
        url = "%s/api/v1/topic/%s" % (KHAN_BASE_URL, topic)
        response = urllib2.urlopen(url).read()
        data = json.loads(response)
        data['topic'] = topic
        data['login'] = "Logout %s" % user
        tmpl = env.get_template('index.html')
        return tmpl.render(data)
        
    @cherrypy.expose    
    def video(self, vid_id='root', topic='root'):
        url = "%s/api/v1/videos/%s" % (KHAN_BASE_URL, vid_id)
        response = urllib2.urlopen(url).read()
        data = json.loads(response)
        data['khan_base_url'] = KHAN_BASE_URL
        data['topic'] = topic
        tmpl = env.get_template('video.html')
        return tmpl.render(data)

    @cherrypy.expose    
    def exercise(self, exercise_id='root', topic='root'):
        url = "%s/api/v1/exercises/%s" % (KHAN_BASE_URL, exercise_id)
        response = urllib2.urlopen(url).read()
        data = json.loads(response)
        data['khan_base_url'] = KHAN_BASE_URL
        data['topic'] = topic
        
        url = "%s/api/v1/exercises/%s/followup_exercises" % (KHAN_BASE_URL, exercise_id)
        response = urllib2.urlopen(url).read()
        followup = json.loads(response)
        data['followup'] = followup
        
        tmpl = env.get_template('exercise.html')
        return tmpl.render(data)

# load config for global and application
cherrypy.config.update(khanconf)
cherrypy.tree.mount(KhanAcademyMini(), '/', config=khanconf)


SAEnginePlugin(cherrypy.engine,ESSAY_DB).subscribe()
cherrypy.tools.db = SATool()
cherrypy.tree.mount(englishessay.EnglishEssay(), '/englishessay', config=enlishessayconf)

cherrypy.engine.start()
cherrypy.engine.block()
