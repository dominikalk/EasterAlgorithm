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
    if the_year and the_year.isdigit():
        return f'{easter(int(the_year))}'
    else:
        return None

date_text = get_date_text(year)

print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html lang="en">')
print('    <head>')
print('        <meta charset="utf-8">')
print('        <title>Easter Algorithm</title>')
print('        <link rel="stylesheet" type="text/css" href="../style.css">')
print('        <style>')
print('            @import url("https://fonts.googleapis.com/css2?family=Inika&display=swap");')
print('        </style>')
print('        <meta name="viewport" content="width=device-width, initial-scale=1.0" />')
print('    </head>')
print('    <body>')
print('        <main>')
print('            <h1>Easter Algorithm</h1>')
if date_text == None:
    print('        <p class="return-text">')
    print('             The date inputed must be a positive whole number. Try again.<br/>')
    print('        </p>')
elif date_type not in ['numerically', 'verbosely', 'both']:
    print('        <p class="return-text">')
    print('             The date type inputed was not one of the options. <br/>Try again.<br/>')
    print('        </p>')
else:
    print('        <p class="return-text">')
    print('             The date of easter on the year <b>%s</b> is:<br/>' % year)
    print('             <b>%s</b> </br>' % date_text)
    print('        </p>')
print('            <a href="../index.html">')
print('                <div class="button"><p>Go back</p></div>')
print('            </a>')
print('        </main>')
print('    </body>')
print('</html>')