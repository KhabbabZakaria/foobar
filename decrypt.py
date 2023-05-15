import base64
from itertools import cycle

encrypted="AUYYFBEKBBhdQk5dR10GGQQTHUZHDkINCAsWBAoGBwxGSxRFSQIUDgQODBcNRkcOQgsBARUTHxJV\nSVtLCQwABBUfBQIDHgxGRw5CDwQPEwQdBB8MDx8JRVRHQA8PBw4RAgQPCUlOQBUbAwkIBhpGSxRF\nSRQGHARMTVJOBwRBQk5dR10WAg9TThw="

key = bytes('zakariak.engg', "utf8")

print(bytes(a ^ b for a, b in zip(base64.b64decode(encrypted), cycle(key))))