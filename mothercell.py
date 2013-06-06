#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mothercell.py
#  
#  Copyright 2013 Alberto Lorente <JerryMrSlime@JERRYMRSLIME-PC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import shutil
import os
import datetime

def main():
	if not os.path.isdir("cells"):
		os.mkdir("cells")
	while:
		now = datetime.datetime.now()
		cell = "cells/cell_"+str((now.microsecond / now.second)*now.minute)+".py"
		cellexec = "python cells/cell_"+str((now.microsecond / now.second)*now.minute)+".py"
		shutil.copy("mothercell.py", cell)
		os.system(cellexec)
	return 0

if __name__ == '__main__':
	main()

