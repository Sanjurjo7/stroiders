from setuptools import setup

with open ('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


setup(
    name='stroiders',
    version='0.1.0',
    description='zero grav diggy game',
    url='https://github.com/Sanjurjo7/stroiders',
    long_description=readme,
    author='Thomas Sanjurjo',
    author_email='sanjurjo7@gmail.com',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    zip_safe=False
)


