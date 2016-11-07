from setuptools import setup

setup(
    name='require.py',
    version='2.0.1',
    description="Path-based imports in Python, inspired by `require.js`",
    url='https://github.com/pcattori/require.py',
    author='Pedro Cattori',
    author_email='pcattori@gmail.com',
    license='MIT',
    packages=['require'],
    install_requires=[
        'six>=1.10.0'
    ],
    test_suite='tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5'
    ]
)
