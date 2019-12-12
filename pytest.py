#import


import Cipher


# assertion


assert callable(Cipher.encode_helper)
assert isinstance(Cipher.encode_helper('a','apple'),int)


# assertion


assert callable(Cipher.decode_helper)
assert isinstance(Cipher.decode_helper('a','apple'),int)

