import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.stegosaurus("hello, " + sys.argv[1])

