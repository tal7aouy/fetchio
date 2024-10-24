from setuptools import setup, find_packages

setup(
    name='fetchio',
    version='1.0.0',
    author='Mhammed Talhaouy',
    author_email='tal7apuy@gmail.com',
    description='A simple HTTP library in Python similar to JavaScript fetch.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tal7aouy/fetchio',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    install_requires=[
        'requests',
    ],
)
