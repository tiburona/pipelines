import ConfigParser
import pyxnat

config = ConfigParser.RawConfigParser()
config.read('./xnat.cfg')

xnat_config = {kw:config.get('xnat', kw) for kw in ['server', 'user', 'password']}

xnat=pyxnat.Interface(**xnat_config)
