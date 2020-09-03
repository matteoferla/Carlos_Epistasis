from waitress import serve
from pyramid.paster import get_app, setup_logging
import os, argparse

# ======================================================================================================================
# custom `app.py` due to os.environs...
parser = argparse.ArgumentParser()
parser.add_argument('--d', action='store_true', help='run in dev mode')
if parser.parse_args().d:
    print('*'*10)
    print('RUNNING IN DEV MODE')
    print('*' * 10)
    configfile = 'development.ini'
else:
    configfile = 'production.ini'

# ======================================================================================================================
setup_logging(configfile)
app = get_app(configfile, 'main', options=os.environ) # pyramid.router.Router

# ======================================================================================================================

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=6969, threads=50)