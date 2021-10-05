from setuptools import setup
import os


def read_file(name):
    with open(os.path.join(os.path.dirname(__file__), name)) as f:
        return f.read()


version = '0.1.dev0'
shortdesc = "Input handling for NUI applications."
longdesc = '\n\n'.join([read_file(name) for name in [
    'README.rst',
    'CHANGES.rst',
    'LICENSE.rst'
]])


setup(
    name='nuiinput',
    version=version,
    description=shortdesc,
    long_description=longdesc,
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Graphics',
        'Programming Language :: Python',
    ],
    keywords='NUI input mtdev hid touch wacom tuio',
    author='Robert Niederreiter',
    author_email='rnix@squarewave.at',
    url='https://github.com/rnixx/nuiinput',
    license='MIT',
    packages=['nuiinput'],
    zip_safe=True,
    install_requires=[
        'setuptools',
        'structlog'
    ]
)
