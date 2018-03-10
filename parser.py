# -*- coding: utf-8 -*-
"""Takes a copy paste from the PDF and spews out a nice file"""
import re

with open('all.txt') as f:
    raw = f.read()

def split_by_port(x):
    """makes list of ports"""
    p = re.compile('([A-Z]+[A-Z\ \-\(\)\’\.\,]+\n*[A-Z\ \-\(\)\’\.]+,[\ \n]*[A-Z\ \n\-\.]+[\ \n]*[A-Z\.]*\n)')
    x = p.split(x)[1:]
    x = zip(x[::2], x[1::2])
    x = [''.join(list(a)) for a in x]
    return x

ports = split_by_port(raw)

# print(ports[3])

# print(''.join(big[1:3]))
# print(''.join(big[103:105]))

with open("ports/AAIUN,  WESTERN SAHARA") as f:
    aauin = f.read()

def parse_destinations(ports):
    if isinstance(ports, list):
        ports = ports.replace('&', ' ')
        ports = ports.replace(',', '')
        p = re.compile('\D*\d*\s')
        ports = p.findall(ports)
        ports = [x.strip() for x in ports]
        dist_pattern = re.compile('\d+')
        name_pattern = re.compile('\D+')
        ports = [(name_pattern.search(x).group(0).strip(), dist_pattern.search(x).group(0)) for x in ports]
    return ports

def single_location_parser(loc):
    # print('----------RAW------------')
    # print(loc)
    # print('-------EXTRACTED------------')
    loc = loc.replace('\n', '&')
    p = re.compile('.*\([0-9]')
    port_name = p.match(loc).group(0)[:-2].replace('&', '')
    # port_name = loc.split('\n')[0]

    print('Port name: {}'.format(port_name.title()))

    l = re.compile('\(\d.*\\"[A-Z]\.\)')
    location = l.search(loc).group()
    location = location.replace('(', '')
    location = location.replace(')', '')
    print('location: {}'.format(location))


    try:
        junctions = loc[loc.index("Junction Points*")+len("Junction Points* "):loc.index("Ports")]
    except ValueError as e:
        # print('Special case with no Junction points?')
        junctions = 'Special case'
        pass
    try:
        ports = loc[loc.index("Ports")+len("Ports "):]
    except Exception as e:
        # print('Special case?')
        ports = 'Special case'
        pass
    
    parse_destinations(junctions)
    parse_destinations(ports)
    
    return

# single_location_parser(ports[2])

for p in ports[:]:
    single_location_parser(p)




