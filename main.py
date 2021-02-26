#!/usr/bin/env python3

import hashlib

hash = hashlib.sha256("hello, world".encode()).hexdigest()

print(hash)
