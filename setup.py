from setuptools import find_packages, setup

setup(
    name='graphene-sqlalchemy',
    version='2.0.dev2017072601',

    description='Graphene SQLAlchemy integration',
    long_description=open('README.rst').read(),

    url='https://github.com/graphql-python/graphene-sqlalchemy',

    author='Syrus Akbary',
    author_email='me@syrusakbary.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    keywords='api graphql protocol rest relay graphene',

    packages=find_packages(exclude=['tests']),

    install_requires=[
        'six>=1.10.0',
        'graphene>=2.0.dev',
        'SQLAlchemy',
        'singledispatch>=3.4.0.3',
        'iso8601',
    ],
    tests_require=[
        'pytest>=2.7.2',
        'mock',
        'sqlalchemy_utils',
    ],
)
