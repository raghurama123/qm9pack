from setuptools import setup, find_packages

setup(
    name='qm9pack',
    version='1.0.3',
    packages=find_packages(),
    package_data={'qm9pack': ['data/*']},
    author='Raghunathan Ramakrishnan',
    author_email='raghu.rama.chem@gmail.com',
    include_package_data=True,
    url='https://github.com/raghurama123/qm9pack',
    license='MIT License',
    description='A python module for data-mining the qm9 database',
    long_desc_type="text/markdown",
    install_requires=[ 'pandas', 'numpy' ],
)
