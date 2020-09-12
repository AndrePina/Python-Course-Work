# The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted. For example: 640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----" 755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x" Fill in the blanks to make the code convert a permission in octal format into a string format.


def octal_to_string(octal):
    octal = str(octal)
    result = ""
    result0 = ""
    result1 = ""
    result2 = ""
    result3 = ""
    result4 = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    n = 0
    for x in range(len(octal)):
        # result = result + octal[n]
        # print(x)
        # print(len(octal))
        if octal[0] >= str(7):
            result0 = "rwx"
        elif octal[0] <= str(6):
            result0 = "rw-"
            
        if octal[1] == str(5):
            result1 = "r-x"
        elif octal[1] == str(4):
            result1 = "r--"
        elif octal[1] == str(0):
            result1 = "---"

        if octal[2] == str(5):
            result2 ="r-x"
        elif octal[2] == str(4):
            result2 = "r--"
        elif octal[2] <= str(0):
            result2 = "---"

    
    result = result0+result1+result2
    # x = x + 1

    return result 

        
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------