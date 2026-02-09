# Write a program to fill in a letter template given below with name and date
# Letter = '''
#             Dear <|Name|>,
#             You are selected!
#             <|Date|>
#             '''

Letter = """
Dear <|Name|>,
You are selected!
<|Date|>
"""
print(Letter.replace("<|Name|>","Akash kr singh").replace("<|Date|>","03 January"))