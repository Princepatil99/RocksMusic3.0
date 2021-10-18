# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit

from os import listdir
from os import mkdir

if 'raw_files' not in listdir():
    mkdir('raw_files')

from RocksMusicv3.services.converter.converter import convert

__all__ = ["convert"]
