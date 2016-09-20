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

# This file implements a rpmsg_multiept.ko wrapper for
# python applications.
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
#
#  Important Notice:
#     This wrapper supposes that only single channel is used in the
#     system and that there is not a udev rule changing the default name
#     of the created endpoints.

import os
import sys
import stat
import time


# Private class for enum

class _Enum(set):

    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError


def channel_name_to_id(name):
    files = os.listdir(RpmsgEndpoint.RPMSG_ROOT)
    files = filter(lambda k: 'channel_' in k, files)
    for fil in files:
        fd = os.open('%s/%s/name' % (RpmsgEndpoint.RPMSG_ROOT, fil),
                     os.O_RDONLY, stat.S_IREAD)
        if fd is None:
            return -1
        readname = os.read(fd, 128)
        if name.strip() == readname.strip():
            id = fil.split('channel_')
            return int(id[1])
    return -1


# Endpoint class

class RpmsgEndpoint:

    Types = _Enum(['STREAM', 'DATAGRAM'])
    LOCAL_DEFAULT_ADDRESS = -1
    REMOTE_DEFAULT_ADDRESS = -1
    RPMSG_ROOT = '/sys/class/rpmsg'
    rpmsg_openamp_channel = 'rpmsg-openamp-demo-channel'
    RPMSG_MAX_DATAGRAM_SIZE = 2 ** 20

    # constructor

    def __init__(
        self, chnl, new_addr, type=Types.DATAGRAM,
        remote_addr=REMOTE_DEFAULT_ADDRESS
    ):

        self.type = type
        self.id = channel_name_to_id(chnl)
        self.addr = new_addr
        self.remote = remote_addr
        self.current_dst = None
        self.fd = None
        ret = -1

        if self.id == -1:
            raise Exception()

        # Get the channel specific default endpoint address

        if new_addr == RpmsgEndpoint.LOCAL_DEFAULT_ADDRESS:
            fd = os.open('%s/channel_%d/local_addr'
                         % (RpmsgEndpoint.RPMSG_ROOT, self.id),
                         os.O_RDONLY, stat.S_IREAD)
            if fd is None:
                raise Exception()
            local_addr = os.read(fd, 16)
            new_addr = int(local_addr)
            self.addr = new_addr
            os.close(fd)

        # Create the new endpoint

        fd = os.open('%s/channel_%d/ept_new'
                     % (RpmsgEndpoint.RPMSG_ROOT, self.id),
                     os.O_WRONLY, stat.S_IWRITE)
        if fd is None:
            raise Exception()
        if type == RpmsgEndpoint.Types.STREAM:
            ret = os.write(fd, '%d,S' % int(new_addr))
        elif type == RpmsgEndpoint.Types.DATAGRAM:
            ret = os.write(fd, '%d,D' % int(new_addr))
        else:
            raise Exception()

        os.close(fd)
        if ret <= 0:
            raise Exception()

        if type == RpmsgEndpoint.Types.STREAM:

            # Get the channel specific default endpoint address

            if remote_addr == RpmsgEndpoint.REMOTE_DEFAULT_ADDRESS:
                fd = os.open('%s/channel_%d/remote_addr'
                             % (RpmsgEndpoint.RPMSG_ROOT, self.id),
                             os.O_RDONLY, stat.S_IREAD)
                if fd is None:
                    raise Exception()
                remote_addr = os.read(fd, 16)
                remote_addr = int(remote_addr)
                self.remote = remote_addr
                os.close(fd)

            fd = os.open(
                '%s/channel_%d/rpmsg_ept%d.%d/src'
                % (RpmsgEndpoint.RPMSG_ROOT, self.id, int(new_addr), self.id),
                os.O_WRONLY, stat.S_IWRITE
            )
            if fd is None:
                raise Exception()
            ret = os.write(fd, '%d' % int(remote_addr))

            os.close(fd)
            if ret <= 0:
                raise Exception()

            fd = os.open(
                '%s/channel_%d/rpmsg_ept%d.%d/dst'
                % (RpmsgEndpoint.RPMSG_ROOT, self.id, int(new_addr), self.id),
                os.O_WRONLY, stat.S_IWRITE
            )
            if fd is None:
                raise Exception()
            ret = os.write(fd, '%d' % int(remote_addr))

            os.close(fd)
            if ret <= 0:
                raise Exception()

            path = '/dev/rpmsg_ept%d.%d' % (int(new_addr), self.id)
        else:  # Types.DATAGRAM
            path = '/dev/rpmsg_ept%d.%d' % (int(new_addr), self.id)

        fd = os.open(path, os.O_RDWR, stat.S_IWRITE | stat.S_IREAD)
        if fd is None:
            raise Exception()
        self.fd = fd

    # destructor

    def __del__(self):

        # Close the opened endpoint

        os.close(self.fd)

        # Deinit the endpoint in the rpmsg internals

        fd = os.open('%s/channel_%d/ept_delete'
                     % (RpmsgEndpoint.RPMSG_ROOT, self.id),
                     os.O_WRONLY, stat.S_IWRITE)
        if fd is None:
            raise Exception()
        os.write(fd, '%d' % int(self.addr))

    # Receive function

    def recv(self, maxlen=-1):
        if self.type == RpmsgEndpoint.Types.STREAM:
            if maxlen <= 0:
                return None
            try:
                buffer = os.read(self.fd, maxlen)
            except OSError:

                            # Nothing to be read

                return ''
            else:
                return buffer
        else:  # DATAGRAM

            if maxlen == 0:
                return (None, None)
            try:
                if maxlen == -1:
                    buffer = os.read(
                        self.fd,
                        RpmsgEndpoint.RPMSG_MAX_DATAGRAM_SIZE
                    )
                else:
                    buffer = os.read(self.fd, maxlen)
            except OSError:

                            # Nothing to be read

                return (None, '')
            else:
                fd = os.open(
                    '%s/channel_%d/rpmsg_ept%d.%d/src'
                    % (
                        RpmsgEndpoint.RPMSG_ROOT,
                        self.id,
                        int(self.addr),
                        self.id
                    ),
                    os.O_RDONLY,
                    stat.S_IREAD)
                if fd is None:
                    return (None, None)
                source = os.read(fd, 16)

                os.close(fd)
                return (int(source), buffer)

    def getRemoteAddress(self):
        if self.remote == RpmsgEndpoint.REMOTE_DEFAULT_ADDRESS:
            fd = os.open('%s/channel_%d/remote_addr'
                         % (RpmsgEndpoint.RPMSG_ROOT, self.id),
                         os.O_RDONLY, stat.S_IREAD)
            if fd is None:
                raise Exception()
            remote_addr = os.read(fd, 16)
            remote_addr = int(remote_addr)
            os.close(fd)
            return remote_addr
        else:
            return self.remote

    def getLocalAddress(self):
        return self.addr

    # Send function

    def send(self, buffer, dst=REMOTE_DEFAULT_ADDRESS):
        if buffer is None:
            return -1

        if self.type == RpmsgEndpoint.Types.STREAM:
            ret = os.write(self.fd, buffer)
            if ret >= 0:
                return 0
            else:
                return -1

        else:   # DATAGRAM

            if self.current_dst != dst:
                _dst = dst

                # Get the channel specific default endpoint address

                if dst == RpmsgEndpoint.REMOTE_DEFAULT_ADDRESS:
                    fd = os.open('%s/channel_%d/remote_addr'
                                 % (RpmsgEndpoint.RPMSG_ROOT, self.id),
                                 os.O_RDONLY, stat.S_IREAD)
                    if fd is None:
                        return None
                    dst = os.read(fd, 16)
                    dst = int(dst)
                    os.close(fd)

                fd = os.open(
                    '%s/channel_%d/rpmsg_ept%d.%d/dst'
                    % (
                        RpmsgEndpoint.RPMSG_ROOT,
                        self.id,
                        int(self.addr),
                        self.id
                    ),
                    os.O_WRONLY,
                    stat.S_IWRITE
                )
                if fd is None:
                    return -1
                ret = os.write(fd, '%d' % int(dst))
                os.close(fd)
                if ret <= 0:
                    return -1
                self.current_dst = _dst

            ret = os.write(self.fd, buffer)
            if ret >= 0:
                return 0
            else:
                return -1


def main():

    print 'Datagram endpoint Test:'

    try:
        MyEndpoint = RpmsgEndpoint(RpmsgEndpoint.rpmsg_openamp_channel,
                                   RpmsgEndpoint.LOCAL_DEFAULT_ADDRESS,
                                   RpmsgEndpoint.Types.DATAGRAM)
    except OSError:

                    # Nothing to be read

        print 'Could not create endpoint!'
        return -1

    message = 'Hello world'

    # Transmit some messages

    retval = MyEndpoint.send(message,
                             RpmsgEndpoint.REMOTE_DEFAULT_ADDRESS)
    print(
        'TX - Status: %d, Destination: %d, Message: %s, Length: %d'
        % (retval, 0, message, len(message))
    )
    retval = MyEndpoint.send(message,
                             RpmsgEndpoint.REMOTE_DEFAULT_ADDRESS)
    print(
        'TX - Status: %d, Destination: %d, Message: %s, Length: %d'
        % (retval, 0, message, len(message))
    )
    retval = MyEndpoint.send(message,
                             RpmsgEndpoint.REMOTE_DEFAULT_ADDRESS)
    print(
        'TX - Status: %d, Destination: %d, Message: %s, Length: %d'
        % (retval, 0, message, len(message))
    )
    # Wait some time for the other core to generate the response

    time.sleep(1)

    # Receive some messages

    r = MyEndpoint.recv(128)
    print(
        'RX - Source: %d, Message: %s, Length: %d'
        % (retval[0], retval[1], len(retval[1]))
    )
    retval = MyEndpoint.recv(128)
    print(
        'RX - Source: %d, Message: %s, Length: %d'
        % (retval[0], retval[1], len(retval[1]))
    )
    retval = MyEndpoint.recv(128)
    print(
        'RX - Source: %d, Message: %s, Length: %d'
        % (retval[0], retval[1], len(retval[1]))
    )
    retval = MyEndpoint.recv(128)
    print(
        'RX - Source: %d, Message: %s, Length: %d'
        % (retval[0], retval[1], len(retval[1]))
    )

    del MyEndpoint

    return 0


if __name__ == '__main__':
    sys.exit(main())

