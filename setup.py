from setuptools import setup, find_packages

version = '1.1.0'

setup(
    name='cmsplugin-fbgallery',
    version=version,
    description='facebook gallery plugin for django-cms',
    author='Vinit Kumar',
    license='MIT',
    author_email='vinit.kumar@changer.nl',
    url='https://github.com/changer/cmsplugin-fbgallery.git',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
)
