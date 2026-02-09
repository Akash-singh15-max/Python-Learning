# Write a python function to remove a given word from a list and strip it
# at the same time


# # only to remove a word
# def rem(l, word):
#     for item in l:
#         l.remove(word)
#         return l
    
# l = ["Akash","Varsha","Vishal","Lucky"]
# print(rem(l,"Varsha"))

def rem(l,word):
    n = []
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l = ["Akash", "Varsha", "Vikaash", "sh"]
print(rem(l,"sh"))