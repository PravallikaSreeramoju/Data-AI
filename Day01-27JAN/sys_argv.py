import sys
#var=sys.argv[1]
#print(var)
print("prog name:" , sys.argv[0])
if len(sys.argv) > 3:
    for i in range(1, len(sys.argv)):
        print(f"arg {i}:",sys.argv[i])