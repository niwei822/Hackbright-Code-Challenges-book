def longestCommonPrefix(words):
    """sort word alphabetical order"""
    str1, str2 = min(words), max(words)
    i = 0
    while i < len(str1):
        if str1[i] != str2[i]:
            str1 = str1[:i]
        i += 1
    return str1
            
    
   
 
print(longestCommonPrefix(["flower","flow","flight"]))
    