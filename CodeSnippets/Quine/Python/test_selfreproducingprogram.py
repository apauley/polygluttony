#!/usr/bin/env python

import sys, subprocess

usage = "%s <interpreter> <filename>" % sys.argv[0]
try:
    selfrepInterpreter = sys.argv[1]
    selfrepProgram = sys.argv[2]
    selfrepSourceFromFile = file(selfrepProgram, 'r').read()
except IndexError:
    print usage
    sys.exit(1)

def outputOfSelfReproducingProgram(selfrepSource):
    p = subprocess.Popen([selfrepInterpreter],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    out, err = p.communicate(selfrepSource)
    if err:
        raise RuntimeError("Error when interpreting source")
    return out

def sourceMatchesOutput(selfrepSource, selfrepOutput):
    return outputOfSelfReproducingProgram(selfrepSource) == selfrepOutput

print 'Checking that program is not empty... ',
if not (selfrepSourceFromFile.strip() == ''):
    print 'passed.'
else:
    print 'failed.'

print 'Checking that program does not reference its own filename... ',
if not (selfrepProgram in selfrepSourceFromFile):
    print 'passed.'
else:
    print 'failed.'

print 'Checking that source matches output... ',
selfrepOutput = outputOfSelfReproducingProgram(selfrepSourceFromFile)
if sourceMatchesOutput(selfrepSourceFromFile, selfrepOutput):
    print 'passed.'
else:
    print 'failed.'

print 'Checking the output of the output... ',
if sourceMatchesOutput(selfrepOutput, outputOfSelfReproducingProgram(selfrepOutput)):
    print 'passed.'
else:
    print 'failed.'
