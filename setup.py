from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='sqlitetocsv',
    version='0.1.1',
    description='Useful package to export all the tables from sqlite db to csv files',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Kaushik Sangem',
    author_email='Kaushik.Sangem@mulliongroup.com',
    keywords=['Sqlite', 'CSV', 'sqlite to csv', 'Python 3'],
    url='https://github.com/MullionGroup/sqlitetocsv',
    download_url='https://pypi.org/project/elastictools/'
)

install_requires = [
    'pandas'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
