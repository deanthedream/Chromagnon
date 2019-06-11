#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012, Jean-Rémy Bancel <jean-remy.bancel@telecom-paristech.org>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the Chromagon Project nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Jean-Rémy Bancel BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys

import chromagnon.SNSSParse
import chromagnon.sessionParse

def main():
    snss = chromagnon.SNSSParse.parse(sys.argv[1])
    sessionCommand = chromagnon.sessionParse.parse(snss)
    for command in sessionCommand:
        print command

def runMain(fullFilePath):
    """Simply takes in a full file path to the 
    Current Session file and returns a list
    Args:
        fullFilePath (string) - the full file path to the Current Session File
    Returns:
        cmds (list) - the full unaltered list of files and such
    """
    snss = chromagnon.SNSSParse.parse(fullFilePath)
    sessionCommand = chromagnon.sessionParse.parse(snss)
    cmds = list()
    for command in sessionCommand:
        cmds.append(str(command))
    return cmds

def parseCMDS(cmds):
    """ This parses each string of cmds (from runMain)
    Args:
        cmds (list) -  list of commands and stuff
    Returns:
        htmlList (list) - list of html Strings
    """
    htmlList = list()
    for cmd in cmds:
        if 'Url: ' in cmd: #aha! we have an element with a URL in it
            sInd = cmd.find('Url: ')
            htmlList.append(cmd[sInd+5:])
        else:
            print(cmd)
            pass

    return htmlList

def printHTMLlistToFile(htmlList):
    """
    """
    with open('/home/dean/SavedSession.txt', 'w') as f:
        for line in htmlList:
            f.write("%s\n" % line )


if __name__ == "__main__":
    main()
