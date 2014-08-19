from os.path import dirname
from tamu.coa.settings.ldap import *
from tamu.coa.settings.general.settings import *
from tamu.coa.templates.settings import *

BUILDOUT_PATH = dirname(dirname(__file__))
PROJECT_PATH = dirname(__file__)
SECRET_KEY = 'v(h5hem5d+bad1vt-test.tamu.edu 20=&nj^s=@d5^31giykcgd_bxs@#xotp6'
CMS_CACHE_PREFIX = 'test.tamu.edu'
SITE_ID = 20

general_location_specific(globals())
