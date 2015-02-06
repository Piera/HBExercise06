scores_unordered=open("scores.txt")

#print type(scores_unordered.read())

#scores ={}

# for line in scores_unordered:
#     line = line.rstrip().split(":")
#     #print line
#     #print line.split(":")
#     scores[line[0]] = line[1]

# splits = line.rstrip().split(":")
tuple_list = [(line.rstrip().split(":")[0], line.rstrip().split(":")[1]) for line in scores_unordered]
scores = {k: v for (k, v) in tuple_list}
print scores

#print sorted(scores.items())

for item, value in sorted(scores.items()):
   print "Restaurant %s is rated at %s"  %(item, value)

# for key, value in scores.items():
#     print key, value