"""The Joshua file storage backend."""

import os
import sys
import uuid


DIRECTORY = '/tmp/joshua'
MODE = os.R_OK | os.W_OK


path = lambda *a: os.path.join(DIRECTORY, *a)


if not os.path.isdir(DIRECTORY):
    os.mkdir(DIRECTORY)

if not os.access(DIRECTORY, MODE):
    try:
        os.chmod(DIRECTORY, MODE)
    except IOError:
        print 'Could not chmod %s!' % DIRECTORY
        sys.exit(1)


class DoesNotExist(Exception):
    """File/object does not exist."""


class Overwrite(Exception):
    """Attempting to overwrite an existing file."""


class StoredObject(object):
    def __init__(self, name=None, extension=None):
        self.fp = None  # Open this lazily.
        if name is not None:
            self.new = False
            self.name = name
        else:
            self.new = True
            self.name = str(uuid.uuid4())
        self.extension = extension or 'txt'
        self.path = u'.'.join([path(self.name), self.extension])
        if not self.new and not os.path.isfile(self.path):
            raise DoesNotExist

    def __del__(self):
        if self.fp is not None and not self.fp.closed:
            self.fp.close()

    def write(self, data):
        if not self.new:
            raise Overwrite

        if self.fp is None or self.fp.closed:
            self.fp = open(self.path, 'wb')

        self.fp.write(data)
        self.fp.close()
        self.fp = None
        self.new = False

    def read(self):
        if self.new:
            raise DoesNotExist

        if self.fp is None or self.fp.closed:
            self.fp = open(self.path, 'rb')

        data = self.fp.read()
        self.fp.close()
        self.fp = None
        return data

    def delete(self):
        if self.new:
            raise DoesNotExist

        os.unlink(self.path)

    def size(self):
        if self.new:
            raise DoesNotExist
        return os.lstat(self.path).st_size
