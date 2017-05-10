# -*- coding: UTF-8 -*-

# Copyright (C) 2017 Sylvain Boily
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from __future__ import unicode_literals
import logging

logger = logging.getLogger(__name__)

class FollowMeUserGenerator(object):

    def __init__(self, dao):
        self.dao = dao
        self.user_uuid = []

    def generate(self):
        for row in self.dao.find_sip_user_settings():
            for line in self.format_row(row):
                yield line

    def format_row(self, row):
        section = row.user_id
        mobilephonenumber = None
        ringseconds = None

        try:
            mobilephonenumber = row.UserSIP.line.users[0].mobilephonenumber
        except:
            pass

        try:
            ringseconds = row.UserSIP.line.users[0].ringseconds * 2
        except:
            pass

        if mobilephonenumber and section not in self.user_uuid:
            yield '[{}]'.format(section)
            self.user_uuid.append(section)
            for line in self.format_user_options(row, mobilephonenumber, ringseconds):
                yield line
            yield ''

    def format_user_options(self, row, mobilephonenumber, ringseconds):
        if row.mohsuggest:
            yield 'music = {}'.format(row.mohsuggest)
        if row.context:
            yield 'context = {}'.format(row.context)
        if mobilephonenumber:
            yield 'number = {},{}'.format(mobilephonenumber, ringseconds)
