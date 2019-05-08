from setuptools import setup, find_packages

setup(
    name='okra',
    version='1.1dev0',
    packages=["okra", "okra/protobuf"],
    license='MIT',
    long_description=open('README.md').read(),
    scripts=['bin/okra', ],
    setup_requires=['pytest-runner'],
    test_requires=[
        'pytest',
        'pytype',
    ],
    test_suite='pytest',
    zip_safe=False
)
