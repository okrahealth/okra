from setuptools import setup, find_packages

setup(
    name='okra',
    version='1.1dev0',
    packages=["okra", "okra/protobuf"],
    license='MIT',
    long_description=open('README.md').read(),
<<<<<<< HEAD
    python_requires=">=3.6",
    install_requires=[
        'pandas==0.24.2',
        'protobuf==3.6.1',
        'pyarrow==0.13.0',
        'sqlalchemy>=1.3.0',
        'tonyg-rfc3339==0.1',
    ],
    scripts=['bin/okra',],
=======
    scripts=['bin/okra', ],
>>>>>>> devel
    setup_requires=['pytest-runner'],
    test_requires=[
        'pytest',
        'pytype',
    ],
    test_suite='pytest',
    zip_safe=False
)
