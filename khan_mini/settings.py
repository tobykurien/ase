import os
KHAN_BASE_URL = "http://192.168.1.2:8080"
KHAN_MINI_BASE_URL = "http://192.168.1.2:8081"

khanconf = os.path.join(os.path.dirname(__file__), 'khanmini.conf')
enlishessayconf = os.path.join(os.path.dirname(__file__), 'englishessay.conf')
current_dir = os.path.dirname(os.path.abspath(__file__))

ESSAY_DB = "mysql://ase:asep4s5@localhost/ase"
