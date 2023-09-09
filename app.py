import yara

# compile rules

rules = yara.compile(filepath='/foo/bar/myrules')

# The default argument is filepath, so you don't need to explicitly specify its name:

rules = yara.compile('/foo/bar/myrules')

# You can also compile your rules from a file object:

fh = open('/foo/bar/myrules')
rules = yara.compile(file=fh)
fh.close()

# Or you can compile them directly from a Python string:
rules = yara.compile(source='rule dummy { condition: true }')