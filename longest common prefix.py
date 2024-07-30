strings=["flower","flow","flight"]
def longest_cp(strings):
    if not strings:
        return ""
prefix="fl"
for i in range(len(min(strings))):
    if all(s[i]==strings[0][i] for s in strings):
        prefix=prefix+strings[0][i]
    else:
        break
    
