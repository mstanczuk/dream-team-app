from setuptools import setup

setup(
    name='flask-app',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)