from setuptools import setup, find_packages

setup(
    name='okra',
    version='1.2dev2',
    packages=["okra"],
    license='MIT',
    long_description=open('README.md').read(),
    python_requires=">=3.6",
    install_requires=[
        'pandas>=0.24.2',
        'protobuf>=3.6.1',
        'pyarrow>=0.13.0',
        'sqlalchemy>=1.3.0',
        'tonyg-rfc3339>=0.1',
    ],
    scripts=['bin/okra',],
    zip_safe=False,
    url='https://okrahealth.github.io/',
    project_urls={
        "Bug Tracker": "https://github.com/okrahealth/okra/issues",
        "Documentation": "https://okrahealth.github.io/okra/",
        "Source Code": "https://github.com/okrahealth/okra",
    },
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
