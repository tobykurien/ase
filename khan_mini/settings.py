import os

KHAN_BASE_URL = "http://ase:8080"       # instance used by khan mini to access API
KHAN_MINI_BASE_URL = "http://ase:8081"
KHAN_BASE_URL2 = "http://ase"           # excluding port, which will be randomly assigned from below
KHAN_INSTANCES = [8082,8083,8084,8085,8086,8087,8088,8089,8090]

khanconf = os.path.join(os.path.dirname(__file__), 'khanmini.conf')
enlishessayconf = os.path.join(os.path.dirname(__file__), 'englishessay.conf')
current_dir = os.path.dirname(os.path.abspath(__file__))

ESSAY_DB = "mysql://ase:asep4s5@localhost/ase"
