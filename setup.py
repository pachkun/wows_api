from setuptools import setup
import wows_api

setup(
    name='wows_api',
    version=wows_api.__version__,
    packages=['wows_api'],
    install_requires=['requests'],
    url='https://github.com/pachkun/wows_api',
    author='pachkun',
    author_email='pachkunishka@gmail.com',
    description='Работа с api world of warship',
    python_requires='>=3.6'
)
