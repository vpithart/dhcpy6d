# DHCPy6d DHCPv6 Daemon
#
# Copyright (C) 2009-2020 Henri Wahl <h.wahl@ifw-dresden.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

from binascii import hexlify
from socket import (AF_INET6,
                    inet_pton)

from dhcpy6d.config import cfg
from dhcpy6d.options import OptionTemplate


class Option(OptionTemplate):
    """
    Option 12 Server Unicast Option
    """
    def build(self, **kwargs):
        response_string_part = self.convert_to_string(self.number, hexlify(inet_pton(AF_INET6, cfg.ADDRESS)).decode())
        return response_string_part, self.number
