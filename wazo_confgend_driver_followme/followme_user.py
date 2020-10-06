# -*- coding: UTF-8 -*-

# Copyright (C) 2017-2020 Sylvain Boily
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
        for row in self.dao.find_all_by():
            for line in self.format_row(row):
                yield line

    def format_row(self, row):
        section = row.uuid
        mobilephonenumber = None
        ringseconds = None

        if hasattr(row, 'mobilephonenumber'):
            mobilephonenumber = row.mobilephonenumber

        if hasattr(row, 'ringseconds'):
            ringseconds = row.ringseconds * 2

        if mobilephonenumber and section not in self.user_uuid:
            yield '[{}]'.format(section)
            self.user_uuid.append(section)
            for line in self.format_user_options(row, mobilephonenumber, ringseconds):
                yield line
            yield ''

    def format_user_options(self, row, mobilephonenumber, ringseconds):
        if hasattr(row, 'musiconhold'):
            if row.musiconhold:
                yield 'musicclass = {}'.format(row.musiconhold)
        if hasattr(row, 'lines'):
            yield 'context = {}'.format(row.lines[0].context)
        if mobilephonenumber:
            yield 'number = {},{}'.format(mobilephonenumber, ringseconds)
