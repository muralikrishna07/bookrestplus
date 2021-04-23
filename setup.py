from setuptools import  setup

setup(
    name='book',
    packages=['book'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)