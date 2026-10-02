def isPalindrome(x: int) -> bool:
     num_str = str(x)
     reverse_num_str = num_str[::-1]
     if num_str == reverse_num_str :
        return True
     else:
        return False
