#
# Makefile for Wazo confgend followme driver
# Copyright (C) 2017, Sylvain Boily
#
# This program is free software, distributed under the terms of
# the GNU General Public License Version 3. See the LICENSE file
# at the top of the source tree.
#

install:
	python setup.py install
	cp etc/asterisk/followme.conf /etc/asterisk/
	cp etc/xivo-confgend/conf.d/* /etc/xivo-confgend/conf.d/
	chown asterisk.www-data /etc/asterisk/followme.conf
	chmod 660 /etc/asterisk/followme.conf
	cp etc/asterisk/extensions_extra.d/followme.conf /etc/asterisk/extensions_extra.d/
	chown asterisk.www-data /etc/asterisk/extensions_extra.d/followme.conf
	chmod 660 /etc/asterisk/extensions_extra.d/followme.conf
	sed -i '/\(^noload.*followme.so\)/s/^/;/' /etc/asterisk/modules.conf
	systemctl restart xivo-confgend
	systemctl restart asterisk
	systemctl restart xivo-ctid
