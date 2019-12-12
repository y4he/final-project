

###########################################################
def encode_helper(char,word):
    num = ord(char)
    result = num-(3*len(word))
    return result



###########################################################
def encode(msg):
    org_lst = msg.split()
    com_lst = []
    # loop through every word
    for i in org_lst:
        #loop thru every letter in the every word
        lst = []
        for j in i:
            lst.append(chr(encode_helper(j,i)))
            s = ''.join(lst)
        com_lst.append(s)
    return ' '.join(com_lst)

###########################################################


def decode_helper(char,word):
    num = ord(char)
    result = num+(3*len(word))
    return result


###########################################################


def decode(msg):
    org_lst = msg.split()
    com_lst = []
    # loop through every word
    for i in org_lst:
        #loop thru every letter in the every word
        lst = []
        for j in i:
            lst.append(chr(decode_helper(j,i)))
            s = ''.join(lst)
        com_lst.append(s)
    return ' '.join(com_lst)


###########################################################




