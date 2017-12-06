# related data generator for python 2.7
# > generates 4 files:
# * primary key-ed data (ordered)
# * secondary key-ed data (ordered)
# * primary key-ed data (unordered)
# * secondary key-ed data (unordered)
# > all files have the same size, and each line has a fixed size
# > all relations are 1-1

import string
from random import choice
from random import shuffle

output_prefix = "data"
output_ext = "dat"
field_delimiter = "|"
record_size = 2048
size = 10000

print "Generating keys..."

# generate the primary keys for the primary key-ed files
first_keys = range(size)

# generate the primary keys for the second key-ed files
second_keys = range(size,2*size)

print "Generating relations..."

# generate the key relationships (the first keys act as foreign keys for the secondary key-ed registers)
key_relations = {}
scp = second_keys
for k1 in first_keys:
    key_relations[k1] = scp.pop(scp.index(choice(scp)))

print "Generating primary records..."

# generate the registers for the primary key-ed data
first_data = []
for k1 in first_keys:
    rec = str(k1)
    rec += field_delimiter
    rec += ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(record_size - len(rec)))
    first_data.append(rec)

print "Generating secondary records..."

# now for the second dataset
second_data = []
for k1 in first_keys:
    rec = str(key_relations[k1])
    rec += field_delimiter
    rec += str(k1)
    rec += field_delimiter
    rec += ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(record_size - len(rec)))
    second_data.append(rec)

# lets start generating the final files, starting by the ordered primary key-ed data
output_filename = output_prefix + "_ordered_primary." + output_ext
print "Generating file " + output_filename
with open(output_filename, "w") as f:
    for rec in first_data:
        f.write(rec + "\n")
    
# now the ordered secondary data file
output_filename = output_prefix + "_ordered_secondary." + output_ext
print "Generating file " + output_filename
with open(output_filename, "w") as f:
    for rec in second_data:
        f.write(rec + "\n")

# the unordered primary
shuffle(first_data)
output_filename = output_prefix + "_unordered_primary." + output_ext
print "Generating file " + output_filename
with open(output_filename, "w") as f:
    for rec in first_data:
        f.write(rec + "\n")

# finally the last one, the unordered secondary dataset
shuffle(second_data)
output_filename = output_prefix + "_unordered_secondary." + output_ext
print "Generating file " + output_filename
with open(output_filename, "w") as f:
    for rec in second_data:
        f.write(rec + "\n")

print "All Done!"