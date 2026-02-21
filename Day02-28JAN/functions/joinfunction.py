full_name="Sreeramoju Pravallika"
#initials="".join(full_name.split(" ")[0][0]) + " "+"".join(full_name.split(" ")[1][0])
#print(initials)

initials="".join(word[0].upper() for word in full_name.split())
print(initials)