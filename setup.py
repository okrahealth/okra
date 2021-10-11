from setuptools import setup, find_packages

setup(
    name='okra',
    version='2.1',
    packages=["okra", "okra/proto"],
    license='MIT',
    author="Tyler Brown",
    author_email="tylers.pile@gmail.com",
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    python_requires=">=3.7",
    install_requires=[
        'click == 7.0',
        'cython==0.29.24',
        'numpy==1.21',
        'pandas == 1.0.1',
        'protobuf == 3.11.3',
        'sqlalchemy == 1.3.13',
    ],
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
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        'console_scripts': ['okra = okra.cli:cli'],
    }
)
