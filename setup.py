from setuptools import setup, find_packages

setup(
    name='okra',
    version='1.2dev1',
    packages=["okra", "okra/protobuf"],
    license='MIT',
    long_description=open('README.md').read(),
    python_requires=">=3.6",
    install_requires=[
        'pandas==0.24.2',
        'protobuf==3.6.1',
        'pyarrow==0.13.0',
        'sqlalchemy>=1.3.0',
        'tonyg-rfc3339==0.1',
    ],
    scripts=['bin/okra',],
    setup_requires=['pytest-runner'],
    test_requires=[
        'pytest',
        'pytype',
    ],
    test_suite='pytest',
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
