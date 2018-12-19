import configparser as cp


inifile = cp.SafeConfigParser()
inifile.read('../config.ini')

inifile.get('settings', 'host')

def file