import re 

# text="python is powerful"
# result=re.search("python", text)
# if result:
#     print("Match found:", result.group())
    
# text="my number is 8328540984 or 9573349532"
# numbers=re.findall("\d{10}", text)
# print("Phone numbers found:", numbers)

# for match in re.finditer("\d{10}", text):
#     print("Match at index:", match.start(), "-", match.end())

text="my phone number is 8328540984"
masked=re.sub("\\d{6}","XXXXXX", text)
print("Masked text:", masked)