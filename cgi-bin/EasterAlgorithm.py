#!/usr/bin/python3
import cgi, cgitb 

cgitb.enable() # displays any errors; useful for debugging
form = cgi.FieldStorage() 
year = form.getvalue('year')
date_type = form.getvalue('dateType')

def easter(y):
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32
    return f"{p}/{n}/{y}"

def get_date_text(the_year):
    if the_year.isdigit():
        return f'Date: {easter(int(the_year))}'
    else:
        return 'Year must be a positive integer to calculate the date of easter.'

date_text = get_date_text(year)

print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')
print('<head>')
print('<title>Results</title>')
print('<link rel="stylesheet" type="text/css" href="../style.css">')
print('</head>')
print('<body>')
print('<a href="../index.html"><span>Easter Algorithm</span></a>')
print('<h1>results</h1>')
print('<p>You filled in the following data:<br/>')
print('Year: %s <br/>' % year)
print('%s <br/>' % date_text)
print('Type: %s <br/>' % date_type)
print('</p>')
print('</body>')
print('</html>')