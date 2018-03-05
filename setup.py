from setuptools import setuptools

setup(name='textanalysis',
	version='1.0',
	url='https://github.com/alisonhowland/text-analysis)',
	author='Alison Howland',
	author_email='alisonhowland@gmail.com',
	license='none',
	packages=['textaanalysis'],
	install_requires=[
		'nltk',
		'string',
		'terminaltables',
		'sys'
	]
	zip_safe=False)