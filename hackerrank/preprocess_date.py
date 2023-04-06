
#
# Complete the 'preprocessDate' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY dates as parameter.
#
"""
Facts/Assumptions
- INPUT: STRING 
- Day: number + st, nd, rd, st, th
    - 1st, 2nd, 31st
- Month: first three letters
    - Jan, Feb
- Year: 1900-2100
- OUTPUT: YYYY-MM-DD

Edge Cases
- No Edge cases

Pseudocode


"""

def preprocessDate(dates):
    converted = []
    months = {
        'Jan': '01',
        'Feb': '02', 
        'Mar': '03',
        'Apr': '04',
        'May': '05', 
        'Jun': '06',
        'Jul': '07',
        'Aug': '08',
        'Sep': '09',
        'Oct': '10',
        'Nov': '11',
        'Dec': '12'
    }
    for date in dates:
        x = date.split()
        x[0] = x[0][0:-2]
        if len(x[0]) == 1:
            x[0] = '0' + x[0]
        x[1] = months[x[1]]
        z = f'{x[2]}-{x[1]}-{x[0]}'
        converted.append(z)
    return converted