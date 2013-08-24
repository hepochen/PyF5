#coding:utf-8
import sys
from setuptools import setup
from settings import VERSION

try:
    import py2exe
except:
    pass

kwargs_py2exe = dict(
    console=[
        {
            "script": 'f5.py',
            'icon_resources': [(0, 'assets/app.ico')]
        }
    ],
    options={
        'py2exe': {
            'bundle_files': 1,
            'excludes': [
                'pyreadline', 'difflib', 'doctest', 'optparse',
                'pickle', 'pdb', 'unittest',
            ],
            'compressed': True,
            'dll_excludes': ['msvcr71.dll'],
        }
    },
    zipfile=None,
)


kwargs_py2app = dict(
    setup_requires = ['py2app'],
    app = ['f5.py'],
    options = {
        'py2app': {
        'optimize': 2,
        'argv_emulation': True,
        'iconfile': 'assets/app.icns',
        'site_packages': False,
        'resources': ['pyf5/_'],
        'plist': {
        	'NSHumanReadableCopyright': 'WeiJu. inc',
            'CFBundleVersion': VERSION,
            'CFBundleSignature': 'getf5',
        },
    }
    },
)

if sys.platform == 'darwin':
    setup(
        name='F5',
        **kwargs_py2app
    )
else:
    if sys.argv[1] and sys.argv[1].lower() == 'py2exe':
        setup(**kwargs_py2exe)