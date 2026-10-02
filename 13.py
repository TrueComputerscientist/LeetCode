def romanToInt( s: str) -> int:
    roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000 }
    som = 0
    for i,teken in enumerate(s):
        if i + 1 < len(s) and roman[teken] < roman[s[i + 1]]:
            som -= roman[teken]
        else:
            som += roman[teken]
    return som
