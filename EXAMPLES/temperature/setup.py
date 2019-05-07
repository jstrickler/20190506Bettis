from setuptools import setup, find_packages

setup(
    name='temperature',
    version='1.2',
    description='Class for converting temperatures',
    long_description='Long description here....',
    author='John Strickler',
    author_email='jstrick@mindspring.com',
    license='MIT',
    url='http://www.cja-tech.com/temperature',
    packages=find_packages(exclude=['contrib', 'doc', 'tests']),
)
