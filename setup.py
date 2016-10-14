from setuptools import setup

setup(
    name='require',
    version='2.0.0',
    description="Path-based imports in Python, inspired by `require.js`",
    url='https://github.com/pcattori/require.py',
    author='Pedro Cattori',
    author_email='pcattori@gmail.com',
    license='MIT',
    packages=['require'],
    install_requires=[
        'six>=1.10.0'
    ],
    test_suite='tests'
)
