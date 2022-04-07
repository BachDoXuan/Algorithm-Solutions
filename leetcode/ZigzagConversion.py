def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    res = ""
    for i in range(0, len(s), 2 * numRows - 2):
        res += s[i]
    if numRows > 2:
        for r in range(1, numRows-1):
            for i in range (r, len(s), 2 * numRows - 2):
                res += s[i]
                if  i + (numRows - 1 - r) * 2 < len(s):
                    res += s[i + (numRows - 1 - r) * 2]
    
    for i in range(numRows-1, len(s), 2 * numRows - 2):
        res += s[i]
    return res

print(convert("PAYPALISHIRING", 3))

print(convert("PAYPALISHIRING", 4))

print(convert("A", 1))