#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2015-2016 Freescale Semiconductor, Inc.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# o Redistributions of source code must retain the above copyright notice, this list
#   of conditions and the following disclaimer.
#
# o Redistributions in binary form must reproduce the above copyright notice, this
#   list of conditions and the following disclaimer in the documentation and/or
#   other materials provided with the distribution.
#
# o Neither the name of Freescale Semiconductor, Inc. nor the names of its
#   contributors may be used to endorse or promote products derived from this
#   software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# This file implements a demo using RPMsg Python wrapper.
# Execute directly this script for STREAM and DATAGRAM
# mode usage demonstration.
# If the other core just echoes the received data,
# you should see only one receive to success in STREAM
# mode, but in DATAGRAM mode, the received data are 
# fragmented into 'frames', so both read attemps succeed.
# Example Output:
# Stream endpoint Test:
#  TX - Status: 0, Destination: 0, Message: Hello world, Length: 11
#  TX - Status: 0, Destination: 0, Message: Hello world, Length: 11
#  TX - Status: 0, Destination: 0, Message: Hello world, Length: 11
#  RX - Source: 0, Message: Hello worldHello worldHello world, Length: 33
#  RX - Source: -1, Message: , Length: 0
#  Datagram endpoint Test:
#  TX - Status: 0, Destination: 0, Message: Hello world, Length: 11
#  TX - Status: 0, Destination: 0, Message: Hello world, Length: 11
#  TX - Status: 0, Destination: 0, Message: Hello world, Length: 11
#  RX - Source: 0, Message: Hello world, Length: 11
#  RX - Source: 0, Message: Hello world, Length: 11

try:
    from rpmsg.sysfs import RpmsgEndpoint
except ImportError:
    print("Could not import RPMsg.\r\nPlease install it first by running \"middleware\rpmsg-python\setup.py\" script.")
    sys.exit()

import sys
import time

def main():

    print "Datagram endpoint Test:"


    try:
        MyEndpoint = RpmsgEndpoint(
            RpmsgEndpoint.rpmsg_openamp_channel,
            RpmsgEndpoint.LOCAL_DEFAULT_ADDRESS,
            RpmsgEndpoint.Types.DATAGRAM)
    except OSError: # Nothing to be read
        print "Could not create endpoint!"
        return -1

    message = "Hello world"


    # Transmit some messages
    retval = MyEndpoint.send(message, RpmsgEndpoint.REMOTE_DEFAULT_ADDRESS)
    print "TX - Status: %d, Destination: %d, Message: %s, Length: %d" % \
        (retval, 0, message, len(message))
    retval = MyEndpoint.send(message, RpmsgEndpoint.REMOTE_DEFAULT_ADDRESS)
    print "TX - Status: %d, Destination: %d, Message: %s, Length: %d" % \
        (retval, 0, message, len(message))
    retval = MyEndpoint.send(message, RpmsgEndpoint.REMOTE_DEFAULT_ADDRESS)
    print "TX - Status: %d, Destination: %d, Message: %s, Length: %d" % \
        (retval, 0, message, len(message))

    # Wait some time for the other core to generate the response
    time.sleep(1)

    # Receive some messages
    retval = MyEndpoint.recv(128)
    print "RX - Source: %d, Message: %s, Length: %d" % \
     (retval[0], retval[1], len(retval[1]))
    retval = MyEndpoint.recv(128)
    print "RX - Source: %d, Message: %s, Length: %d" % \
     (retval[0], retval[1], len(retval[1]))
    retval = MyEndpoint.recv(128)
    print "RX - Source: %d, Message: %s, Length: %d" % \
     (retval[0], retval[1], len(retval[1]))
    retval = MyEndpoint.recv(128)
    print "RX - Source: %d, Message: %s, Length: %d" % \
     (retval[0], retval[1], len(retval[1]))

    del MyEndpoint

    return 0

if __name__ == '__main__':
    sys.exit(main())
