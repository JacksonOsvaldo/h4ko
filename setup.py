from setuptools import setup, find_packages

setup(
    name='h4ko',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',        
        'SQLAlchemy',   
    ],
    package_data={
        'h4ko': ['templates/project_template/**/*'],
    },
    entry_points={
        'console_scripts': [
            'h4ko=h4ko.cli:main',
        ],
    },
    author='Jackson Osvaldo',
    description='Descrição do seu pacote RPA framework',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/JacksonOsvaldo/h4ko',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
