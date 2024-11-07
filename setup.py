from setuptools import setup, find_packages

setup(
    name='h4ko',
    author='Jackson Osvaldo',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'SQLAlchemy',
    ],
    package_data={
        'h4ko': ['templates/project_template/*'],
    },
    entry_points={
        'console_scripts': [
            'h4ko=h4ko.cli:main',
        ],
    },
)