# -*- coding: utf-8 -*-
#    MTUOC_task
#    Copyright (C) 2025  Antoni Oliver
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


import codecs
import os
from datetime import datetime

logfile=codecs.open("taskscheduler.log","a",encoding="utf-8")
while 1:
    entrada=codecs.open("taskQueue.txt","r",encoding="utf-8")
    tasks=[]
    for linia in entrada:
        linia=linia.strip()
        tasks.append(linia)
    entrada.close()
    try:
        task=tasks.pop(0)
        sortida=codecs.open("taskQueue.txt","w",encoding="utf-8")
        for linia in tasks:
            sortida.write(linia+"\n")
        sortida.close()
        info="START\t"+str(datetime.now())+"\t"+task
        logfile.write(info+"\n")
        logfile.flush()
        print(info)
        try:
            os.system(task)
            info="END\t"+str(datetime.now())+"\t"+task
            print(info)
            logfile.write(info+"\n")
            logfile.flush()
        except:
            info="ERROR\t"+str(datetime.now())+"\t"+task
            print(info)
            logfile.write(info+"\n")
            logfile.flush()
            
        

    except:
        pass
        

