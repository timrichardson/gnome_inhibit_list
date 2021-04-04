from setuptools import setup
# from sphinx.setup_command import BuildDoc
from os import path
#cmdclass = {'build_sphinx': BuildDoc}

# https://pypi.org/classifiers/

name = 'list_session_inhibitors'
keywords = 'inhibitors'
version = '0.9.5'
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=name,
    keywords=keywords,
    version=version,
    author='Tim Richardson',
    author_email='tim@growthpath.com.au',
    description='command line utility to list session power inhibitors for Linux Gnome desktop users',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['list_session_inhibitors'],
    python_requires='>=3.6',
    install_requires=['pydbus','PyGObject>=3.40','click'],
    setup_requires=['pytest-runner', ],
    entry_points={"console_scripts": ["inhibitors=list_session_inhibitors.inhibitors:main"]},
    tests_require=["pytest", ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Office/Business',
    ],
    url='https://github.com/timrichardson/zoho_analytics_connector',
    license='LGPLv3',

    #cmdclass=cmdclass,
    # these are optional and override conf.py settings
    # command_options={
    #     'build_sphinx': {
    #         'project': ('setup.py', name),
    #         'version': ('setup.py', version),
    #         'release': ('setup.py', version),
    #         'source_dir': ('setup.py', 'docs')}},

)
