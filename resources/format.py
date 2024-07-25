import re
unformatted = open('movies.txt', mode='r', encoding ='utf-8')
formatted = open('movies.csv', mode='w', encoding = 'utf-8')

def calculate_priority(line):
    """Changes dashes to a priority number based on length

    Args:
        line (str): Line containg dash of certain length

    Returns:
        int: priority number
    """
    dashes = line.count('-')
    priority = 0
    if dashes >= 50:
        priority = 10
    elif dashes >= 45:
        priority = 10
    elif dashes >= 40:
        priority = 9
    elif dashes >= 35:
        priority = 8
    elif dashes >= 30:
        priority = 7
    elif dashes >= 25:
        priority = 6
    elif dashes >= 20:
        priority = 5
    elif dashes >= 15:
        priority = 4
    elif dashes >= 10:
        priority = 3
    elif dashes >= 5:
        priority = 2
    elif dashes > 0:
        priority = 1
    
    return priority

# Write header for csv file
formatted.write('Name,ReleaseYear,Watched,Priority,ExtraInfo\n')

for line in unformatted.readlines():
    # remove ticks and stores in true/false variable
    tick_present = line.find('✓')
    if tick_present == -1:
        tick_present = 0
    tick_present = bool(tick_present)
    line = line.replace('✓','')
    
    # Find priority of movie and remove dashes
    priority = calculate_priority(line)
    line = line.replace('!','')
    line = line.replace('-','')

    # Delete question marks
    line = line.replace('?','')

    # Extract additional info from () and delete from line
    brackopen = line.find('(')
    brackclose = line.find(')')
    info = 'NULL'
    if brackopen != -1:
        info = line[brackopen+1:brackclose]
    line = line[:brackopen]

    # Getting name from line
    name = line.strip()

    # Extract year from info
    p = re.compile('\\d{4}')
    m = p.search(info)
    year = ''
    if m != None:
        year = m.group()
        info = info.replace(year,'')



    # Make out_line into final format
    out_line = name + ',' + year + ',' + str(tick_present) + ',' + str(priority) + ',' + info +'\n'
    formatted.write(out_line)

unformatted.close()
formatted.close()
