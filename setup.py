from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Name',
  version='0.0.1',
  description='Descrizione',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Autore',
  author_email='email',
  license='MIT', 
  classifiers=classifiers,
  keywords='parole', 
  packages=find_packages(),
  install_requires=[''] 
)
