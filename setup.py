from setuptools import setup
# from sphinx.setup_command import BuildDoc
from os import path
#cmdclass = {'build_sphinx': BuildDoc}

# https://pypi.org/classifiers/

name = 'list_session_inhibitors'
keywords = 'inhibitors'
version = '0.9.8'
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
    include_package_data=True,
    packages=['list_session_inhibitors'],
    data_files=[
        ('share/applications', ['inhibitor-widget.desktop']),
    ],
    python_requires='>=3.6',
    install_requires=['pydbus','PyGObject>=3.40','click','pyqt5'],
    setup_requires=['pytest-runner', 'setuptools_scm'],
    entry_points={"console_scripts": ["inhibitors=list_session_inhibitors.main:main"]},
    tests_require=["pytest", ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Office/Business',
    ],
    url='https://github.com/timrichardson/gnome_inhibit_list',
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
