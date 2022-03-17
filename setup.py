from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pandasxml',
    packages=['pandasxml'],
    version='0.01.1',
    license='MIT',
    description='PandasXML is a Python package that imports data from remote XML files into Pandas dataframes, so they can be manipulated or exported to other file formats, such as CSV. ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Matt Clarke',
    author_email='matt@practicaldatascience.co.uk',
    url='https://github.com/practical-data-science/PandasXML',
    download_url='https://github.com/practical-data-science/PandasXML/archive/master.zip',
    keywords=['python', 'pandas', 'xml'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=['pandas', 'bs4', 'lxml'],
    include_package_data=True
)
