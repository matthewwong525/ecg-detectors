#!/usr/bin/python3

from setuptools import setup

setup(
    name='ecgdetectors',
    version='0.9.0',
    description="Seven ECG heartbeat detection algorithms and heartrate variability analysis",
    long_description="Seven ECG heartbeat detection algorithms and heartrate variability analysis",
    author='Luis Howell and Bernd Porr',
    author_email='luisbhowell@gmail.com',
    py_modules=['ecgdetectors','hrv'],
    include_package_data=True,
    install_requires=['numpy','PyWavelets','pathlib','scipy','biosppy','gatspy'],
    zip_safe=False,
    url='https://github.com/luishowell/ecg-detectors',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Medical',
    ],
)
