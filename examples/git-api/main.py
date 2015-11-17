# -*- coding: utf- -*-

import commands
import json
import requests
from requests.auth import HTTPBasicAuth


def get_lib_info(name):
    info = commands.getstatusoutput('pypi info %s' % name)[1].split('\n')
    output = {}
    for line in info:
        if line:
            output['project_name'] = name
            line = line.split(':')
            if line[0] == 'Home Page':
                output['project_url'] = ':'.join(line[1:3])
            elif line[0] == 'License':
                output['license_name'] = line[1].strip()
    return output


names = [
    'execnet', 'pil', 'docutils', 'south', 'pytz', 'tox', 'pytest-cache', 'anyjson',
    'py-ipaddress', 'coverage', 'devpi', 'flake', 'apipkg', 'pytest-pep', 'pygments', 'polib',
    'django-mptt-tree-editor', 'alembic', 'django-coverage', 'wheel', 'pkginfo', 'django-coverage',
    'django-celery', 'six',
]

data = []
data_bad =  []
license_urls = {
    'bsd--clause': 'https://opensourceorg/licenses/BSD--Clause',
    'mit': 'https://opensourceorg/licenses/MIT',
    'lgpl-': 'https://opensourceorg/licenses/lgpl-license',
    'apache-': 'https://opensourceorg/licenses/Apache-',
    'bsd--clause': 'https://opensourceorg/licenses/BSD--Clause',
    'gpl-2.0': 'https://opensource.org/licenses/GPL-2.0'
}
urls = ('https://githubcom/ekalinin/nodeenv',
        'https://github.com/mbostock/d3',
        'https://githubcom/jquery/jquery-mousewheel',
        'https://githubcom/components/jqueryui',
        'https://githubcom/medialize/URIjs',
        'https://githubcom/gf/moment-range',
        'https://githubcom/gilbitron/carouFredSel',
        'https://githubcom/moment/moment',
        'https://githubcom/jashkenas/underscore',
        'https://githubcom/jquery/jquery',
        'https://githubcom/jashkenas/backbone',
        'https://githubcom/aFarkas/htmlshiv',
        'https://githubcom/jbr/jQueryhighlightRegex',
        'https://githubcom/scottjehl/Respond',
        'https://githubcom/SlexAxton/Jed',
        'https://githubcom/carhartl/jquery-cookie',
        'https://githubcom/gruntjs/grunt-contrib-uglify',
        'https://githubcom/gruntjs/grunt-contrib-copy',
        'https://githubcom/gruntjs/grunt-contrib-concat',
        'https://githubcom/gruntjs/grunt-contrib-clean',
        'https://githubcom/azproduction/grunt-lmd',
        'https://githubcom/gruntjs/grunt-contrib-requirejs',
        'https://githubcom/jdavis/grunt-rename',
        'https://githubcom/gruntjs/grunt-contrib-sass',
        'https://githubcom/nDmitry/grunt-autoprefixer',
        'https://githubcom/gruntjs/grunt-contrib-cssmin',
        'https://githubcom/dbushell/grunt-svgpng',
        'https://githubcom/gruntjs/grunt-contrib-nodeunit',
        'https://githubcom/yatskevich/grunt-bower-task',
        'https://githubcom/tschaub/grunt-newer',
        'https://githubcom/gruntjs/grunt-contrib-jshint',
        'https://githubcom/gruntjs/grunt-contrib-watch',
        'https://githubcom/localhos    t/jquery-fieldselection',
        'https://githubcom/malihu/malihu-custom-scrollbar-plugin',
        'https://githubcom/tcr/selectionjs',
        'https://githubcom/bmihelac/django-import-export'
        'https://githubcom/django-mptt/django-mptt',
        'https://githubcom/Julian/jsonschema',
        'https://githubcom/bitprophet/alabaster',
        'https://githubcom/simplejson/simplejson',
        'https://githubcom/shibukawa/snowball_py',
        'https://githubcom/rbarrois/factory_boy',
        'https://githubcom/schlamar/pytest-cov',
        'https://githubcom/mitsuhiko/markupsafe',
        'https://githubcom/getsentry/raven-python',
        'https://githubcom/inconshreveable/sqltap',
        'https://githubcom/dobarkod/django-queryinspect',
        'https://githubcom/matthewwithanm/pilkit/',
        'https://githubcom/graingert/django-babel/',
        'https://githubcom/mitsuhiko/flask/',
        'https://githubcom/mrjoes/flask-admin/',
        'https://githubcom/mumrah/kafka-python',
        'https://githubcom/pyflakes/pyflakes',
        'https://githubcom/gabrielfalcao/httpretty',
        'https://githubcom/jmcantrell/python-dateutils',
        'https://githubcom/aljosa/django-tinymce',
        'https://githubcom/celery/py-amqp',
        'https://githubcom/mgedmin/check-manifest',
        'https://githubcom/flintwork/mccabe',
        'https://githubcom/schlamar/cov-core',
        'https://githubcom/kvesteri/sqlalchemy-utils',
        'https://githubcom/dbtsai/python-mimeparse',
        'https://githubcom/JetBrains/teamcity-python',
        'https://githubcom/celery/billiard',
        'https://githubcom/celery/celery',
        'https://githubcom/openid/python-openid',
        'https://githubcom/snide/sphinx_rtd_theme',
        'https://githubcom/mitsuhiko/itsdangerous',
        'https://githubcom/bower/bower',
        'https://githubcom/fgnass/spinjs',
        'https://githubcom/DmitryBaranovskiy/raphael/',
        'https://githubcom/rubenv/grunt-git',
        'https://githubcom/smashingboxes/OwlCarousel',
        'https://githubcom/mitsuhiko/jinja',
        'https://githubcom/lxml/lxml/',
        'https://githubcom/pypa/virtualenv',
        'https://githubcom/django-admin-tools/django-admin-tools',
        'https://github.com/obviel/pojson',
        'https://github.com/django/django',
        'https://github.com/shazow/urllib3',
        'https://github.com/pika/pika/tree/0.10.0',
        'https://github.com/django-import-export/django-import-export',
        'https://github.com/celery/kombu',
        'https://github.com/unbit/uwsgi',
        'https://github.com/mitsuhiko/click',
        'https://github.com/SimonSapin/cssselect/',
        'https://github.com/pyinvoke/invoke',
        'https://github.com/pytest-dev/pytest/',
        'https://github.com/cython/cython',
        'https://github.com/jek/blinker',
        'https://github.com/rbarrois/factory_boy',
        'https://github.com/wtforms/wtforms',
        'https://github.com/falconry/falcon',
        'https://github.com/nose-devs/nose/',
        'https://github.com/python-babel/babel',
        'https://github.com/tomchristie/django-rest-framework',
        'https://github.com/kennethreitz/tablib',
        'https://github.com/linsomniac/python-memcached',
        'https://github.com/msgpack/msgpack-python',
        'https://github.com/PyCQA/pep8'
        )
for url in urls:
    url = 'https://api.github.com/repos' + url.replace('https://github.com', '')
    result = requests.request('GET', url, headers={'Accept': 'application/vnd.github.drax-preview'},
                              auth=HTTPBasicAuth('adolgikh', 'trinitas333'))
    result_json = json.loads(result.content)
    try:
        if result_json.get('license') is None:
            data.append({
                'project_name': result_json['name'],
                'project_url': result_json['html_url'],
                'license_name': 'Unknown',
                'license_url': 'Unknown',
                'license_key': 'Unknown',
            })
        else:
            data.append({
                'project_name': result_json['name'],
                'project_url': result_json['html_url'],
                'license_name': result_json['license']['name'],
                'license_url': result_json['license']['url'],
                'license_key': result_json['license']['key']
            })
    except (KeyError, TypeError):
        data_bad.append(url)

with open('libs.mk', 'wt') as flat:
    flat.write('||Имя библиотеки||Где используется||Лицензия||Copyright||\n')
    for item in data:
        try:
            key = item['license_key']
            license_url = license_urls.get(key) or 'https://opensource.org/licenses'
            flat.write('|[%s|%s]|WGCC FE|[%s|%s]|None|\n' % (item['project_name'], item['project_url'], item['license_name'], license_url))
        except TypeError:
            pass
    for name in names:
        lib_info = get_lib_info(name)
        try:
            flat.write('|[%s|%s]|WGCC BE|%s|None|\n' % (lib_info['project_name'], lib_info['project_url'], lib_info['license_name']))
        except TypeError:
            data_bad.append(name)

    flat.write('|[mock|http://www.voidspace.org.uk/python/mock/]|WGCC BE, WGCC FE|[BSD License|http://www.voidspace.org.uk/python/license.shtml]|None]|\n')
    flat.write('|[google-diff-match-patch|https://code.google.com/p/google-diff-match-patch/]|WGCC BE, WGCC FE|[Apache License 2.0|http://www.apache.org/licenses/LICENSE-2.0]|None]|\n')
    # flat.write('[py-amqplib|https://code.google.com/p/py-amqplib/]|WGCC BE, WGCC FE|[GNU Lesser GPL|http://www.gnu.org/licenses/lgpl.html]|None]|\n')
    flat.write('|[svgweb|https://code.google.com/p/svgweb/]|WGCC FE|[Apache License 2.0|http://www.apache.org/licenses/LICENSE-2.0]|None]|\n')
    flat.write('|[django-mptt|https://github.com/django-mptt/django-mptt/]|WGCC BE|[Other|https://opensource.org/licenses]|None]|\n')
    flat.write('|[pilkit|https://github.com/matthewwithanm/pilkit]|WGCC BE|[BSD License|https://opensource.org/licenses]|None]|\n')
    flat.write('|[django-babel|https://github.com/python-babel/django-babel]|WGCC FE|[BSD License|https://opensource.org/licenses]|None]|\n')
    flat.write('|[flask|https://github.com/mitsuhiko/flask]|WGCC BE|[BSD 3-clause "New" or "Revised" License|https://opensource.org/licenses/BSD-3-Clause]|None]|\n')
    flat.write('|[flask-admin|https://github.com/flask-admin/flask-admin]|WGCC BE|[Apache License 2.0|https://opensource.org/licenses/Apache-2.0]|None]|\n')
    flat.write('|[python-daemon|https://pypi.python.org/pypi/python-daemon/]|WGCC BE|[Apache License 2.0|https://opensource.org/licenses/Apache-2.0]|None]|\n')
    flat.write('|[raphael|https://github.com/DmitryBaranovskiy/raphael/]|WGCC FE|[MIT License|https://opensource.org/licenses/MIT]|None]|\n')
    flat.write('|[lxml|https://github.com/lxml/lxml/]|WGCC FE|[BSD License, Elementtree License, GPL License, ZopePublicLicense|https://github.com/lxml/lxml/tree/master/doc/licenses]|None]|\n')
    flat.write('|[sphinx_rtd_theme|https://pypi.python.org/pypi/sphinx_rtd_theme/]|WGCC FE, WGCC BE|[MIT License|https://opensource.org/licenses/MIT]|None]|\n')
    flat.write('|[pluggy|https://pypi.python.org/pypi/pluggy]|WGCC FE, WGCC BE|[MIT License|https://opensource.org/licenses/MIT]|None]|\n')
    flat.write('|[sqlalchemy|https://bitbucket.org/zzzeek/sqlalchemy]|WGCC BE|[MIT License|https://opensource.org/licenses/MIT]|None]|\n')
    flat.write('|[flake8|https://gitlab.com/pycqa/flake8]|WGCC BE|[MIT License|https://opensource.org/licenses/MIT]|None]|\n')
    flat.write('|[py-amqplib|https://code.google.com/p/py-amqplib/]|WGCC FE|[GNU Lesser General Public License v2.1|https://opensource.org/licenses/lgpl-license]|None]|\n')



print data_bad
packages_be = ['alembic', 'blinker', 'click', 'cov-core', 'coverage', 'Cython', 'dateutils', 'docutils', 'execnet',
               'factory-boy', 'falcon', 'flake', 'Flask', 'Flask-Admin', 'invoke', 'ipaddress', 'ipython',
               'itsdangerous', 'Jinja2', 'jsonschema',
               'kafka-python', 'lockfile', 'lxml', 'Mako', 'MarkupSafe', 'mccabe', 'mock', 'msgpack-python', 'nose',
               'pep',
               'pika', 'psycopg', 'py', 'py-ipaddress', 'pyflakes', 'Pygments', 'pytest', 'pytest-cache', 'pytest-cov',
               'pytest-pep', 'python-daemon', 'python-dateutil', 'python-mimeparse', 'pytz', 'raven',
               'requests', 'simplejson', 'six', 'Sphinx', 'SQLAlchemy', 'SQLAlchemy-Utils', 'sqltap', 'statsd',
               'teamcity-messages', 'uWSGI', 'Werkzeug', 'wgnc-client', 'WTForms']

packages_fe = ['amqp', 'amqplib', 'anyjson', 'Babel', 'billiard', 'celery', 'check-manifest', 'click', 'coverage',
               'cssselect', 'devpi-client',
               'devpi-common', 'diff-match-patch', 'Django', 'django-admin-tools', 'django-babel', 'django-celery',
               'django-coverage', 'django-import-export',
               'django-mptt', 'django-mptt-tree-editor', 'django-queryinspect', 'django-tinymce', 'django-wg-bwdata',
               'django-wg-clansapiclient', 'django-wg-clanwars-api',
               'django-wg-clanwarsdata', 'django-wg-wgccfe-l10n', 'django-wgcw-gamedata', 'django-wgcwx-i18n',
               'django-wgext', 'django-wginternal', 'djangorestframework', 'docutils',
               'httpretty', 'Jinja2', 'jsonschema', 'kombu', 'lxml', 'MarkupSafe', 'mock', 'msgpack-python', 'nodeenv',
               'notifier-client', 'pilkit', 'Pillow', 'pkginfo', 'psycopg2', 'py', 'Pygments',
               'python-dateutil', 'python-memcached', 'python-wglog', 'pytz', 'raven', 'requests', 'six', 'South',
               'Sphinx', 'tablib', 'teamcity-messages', 'tox', 'urllib3',
               'virtualenv', 'wgccfe-wowp-data', 'wgcms', 'wgnc-client', 'wot-bw-lib', 'wot-game-data']

common_packages = set(packages_fe).intersection(set(packages_be))
be_only_packages = set(packages_be).difference(set(packages_fe))
fe_only_packages = set(packages_fe).difference(set(packages_be))
print fe_only_packages