from setuptools import setup, find_packages

setup(
    name="data_analysis",
    version="0.0.1",
    url="https://github.com/Lycan47/data-analysis",
    author="Hamza Shaikh",
    packages=find_packages,
    install_requires=['PyQt5', 'pandas', 'sqlalchemy', 'nltk', 'numpy', 'jupyter', 'python-twitter'],
    entry_points={},
    extra_require={}

)