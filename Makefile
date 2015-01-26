#                            Package   : omniEvents
# Makefile                   Created   : 2003/10/31
#                            Author    : Alex Tingle
#
#    Copyright (C) 2003 Alex Tingle.
#
#    This file is part of the omniEvents application.
#
#    omniEvents is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    omniEvents is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

all:
	$(MAKE) -C idl $@
	$(MAKE) -C src $@
	$(MAKE) -C tools $@
	$(MAKE) -C examples $@

install:
	$(MAKE) -C idl $@
	$(MAKE) -C src $@
	$(MAKE) -C tools $@
	$(MAKE) -C contrib $@

uninstall:
	$(MAKE) -C idl $@
	$(MAKE) -C src $@
	$(MAKE) -C tools $@
	$(MAKE) -C contrib $@

clean:
	$(MAKE) -C idl $@
	$(MAKE) -C src $@
	$(MAKE) -C tools $@
	$(MAKE) -C examples $@

.PHONY: all install uninstall clean
