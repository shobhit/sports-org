''' sync a directory with another directory '''

import getopt, sys, re
from xml.etree import ElementTree as ET
from org.models import *

org_re = re.compile('org.')

def get_model(s, t):
    c = s.attrib[t]
    return c[org_re.search(c).end():].capitalize()

def get_display(klass, field, val):
    d = eval('dir(' + klass + ')')
    f = 'get_' + field + '_display' 
    if f in d:
        k = eval(klass + '(' + field + "='" + val + "')")
        rval = "'" + eval('k.' + f + '()') + "'"
    else:
        rval = "'" + val + "'"
    return rval

def to_date_array(s, delim):
    return ','.join([str(int(a)) for a in s.split(delim)])

def do_field(s, model):
    if 'type' in s.attrib:
        typ = s.attrib['type']
        delim = "'"
        if typ == 'IntegerField':
            t = s.text
        elif typ == 'TextField':
            t = "'" + s.text.replace('\n', '\\n') + "'"
        elif typ == 'CharField':
            t = get_display(model, s.attrib['name'], s.text)
        elif typ == 'DateField':
            t = 'datetime.date(' + to_date_array(s.text, '-') + ')'
        elif typ == 'DateTimeField':
            (d, t) = s.text.split()
            t = 'datetime.datetime(' + to_date_array(d, '-') + ',' + to_date_array(t, ':') + ')'
        else:
            t = "'" + s.text + "'"
        rval = s.attrib['name'] + '=' + t
    elif 'to' in s.attrib:
        model = get_model(s, 'to')
        rval = s.attrib['name'] + '=' + model + s.text
    return rval

def is_valid_field(f):
    if f.text == None:
        return 0
    g = f.getchildren()
    if len(g) == 1:
        if g[0].tag == 'None':
            return 0
    return 1

address_re = re.compile("(?<=address1=').+?'")
city_re = re.compile("(?<=city=').+?'")
state_re = re.compile("(?<=state=').+?'")
def do_address(line):
    m1 = address_re.search(line)
    if m1 == None:
        return line
    l = []
    l.append(m1.group(0)[:-1])
    m = city_re.search(line)
    l.append(m.group(0)[:-1])
    m = state_re.search(line)
    st = m.group(0)
    l.append(st)
    e =  line[re.search(st, line).end():]
    return line[:m1.start()] + ', '.join(l) + e
    
def main(argv):
    try:
        opts, args = getopt.getopt(argv[1:], "f:t:r:s:", ["from=","to=","re=","sub=", "help"])
    except getopt.error:
        usage()
        sys.exit(2)

    fromp = "/u/ballen/p"
    to = "/u/ballen/p"
    ex = ""
    sub = ""

    for o, a in opts:
        if (o in ("-f", "--from")):
            fromp = a
        if (o in ("-t", "--to")):
            to = a

    tree = ET.parse(fromp)
    outf = open(to, "w")
    lines = {}
    for p in tree.findall('object'):
        pk = p.attrib['pk']
        model = get_model(p, 'model')
        if model == 'Venueavailability':
            model = 'VenueAvailability'
        key = model + pk
        line = key + '=' + model + '(' + \
              ','.join([do_field(field, model) for field in p if is_valid_field(field)]) + ')'
        line = do_address(line)
        if model in lines:
            l = lines[model]
            l.append((key, line))
        else:
            l = [(key, line)]
            lines[model] = l

    outf.write('import datetime\n')
    outf.write('from org.models import *\n')
    
    for p in ['Announcement','Org','Person','League','Division','Team',\
              'Team_player','Team_coach','Venue','VenueAvailability','Event']:
        for (name,l) in lines[p]:
            outf.write(l + '\n')
            outf.write(name + '.save()\n')
        
	
if __name__ == '__main__':
    sys.exit(main(sys.argv))
