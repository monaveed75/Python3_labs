line = "root:x:0:0:The Super User:/root:/bin/ksh"

fields = line.split(":")
fields[4] = "The Administrator"
fields[6] = "/bin/bash"

line = ":".join(fields)
print(line)