from setuptools import setup, find_packages

setup(
    name='FlaskTDC',
    version='0.1',
    description='Landing Page com Flask no TDC',
    author='Lays Rodrigues',
    author_email='laysrodriguessilva@gmail.com',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'Flask==0.12.1',
        'gunicorn==19.6.0',
    ],
)
