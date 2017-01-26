#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


setup(
    name='wazo-confgend-driver-followme',
    version='0.1',
    description='Wazo Configuration Generator for Follow ME',
    author='Sylvain Boily',
    author_email='sylvainboilydroid@gmail.com',
    url='http://www.wazo.community/',
    license='GPLv3',
    packages=find_packages(),
    entry_points={
        'xivo_confgend.asterisk.followme.conf': [
            'wazo = wazo_confgend_driver_followme.followme_conf:FollowMeConfGenerator'
        ],
    },
)
