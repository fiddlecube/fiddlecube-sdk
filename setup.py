from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'soothsayer',
    version = '0.0.1',
    author = 'Kaushik Srinivasan',
    author_email = 'kaushik@fiddlecube.ai',
    license = '<the license you chose>',
    description = 'A tool to generate synthetic tabular data',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/devpod/soothsayer',
    py_modules = ['soothsayer', 'app'],
    packages = find_packages(exclude=['data', 'output', 'sooth']),
    install_requires = [requirements],
    python_requires='>=3.9',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        soothsayer=soothsayer:cli
    '''
)