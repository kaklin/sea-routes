# -*- coding: utf-8 -*-
"""Takes a copy paste from the PDF and spews out a nicer file"""
import re
import json

with open('PUB151_raw.txt') as f:
    raw = f.read()

def split_by_port(x):
    """makes list of raw ports"""
    p = re.compile('([A-Z]+[A-Z\ \-\(\)\’\.\,]+\n*[A-Z\ \-\(\)\’\.]+,[\ \n]*[A-Z\ \n\-\.]+[\ \n]*[A-Z\.]*\n)')
    x = p.split(x)[1:]
    x = zip(x[::2], x[1::2])
    x = [''.join(list(a)) for a in x]
    return x

ports = split_by_port(raw)

def parse_destinations(ports):
    if ports != 'Special case':
        ports = ports.replace('&', ' ')
        ports = ports.replace(',', '')
        p = re.compile('\D*\d*\s')
        ports = p.findall(ports)
        ports = [x.strip() for x in ports]
        dist_pattern = re.compile('\d+')
        name_pattern = re.compile('\D+')
        ports = [(name_pattern.search(x).group(0).strip(), dist_pattern.search(x).group(0)) for x in ports]
        ports = {x[0]:float(x[1]) for x in ports}
    return ports

def single_location_parser(loc):
    # print('----------RAW------------')
    # print(loc)
    # print('-------EXTRACTED------------')
    loc = loc.replace('\n', '&')
    p = re.compile('.*\([0-9]')
    port_name = p.match(loc).group(0)[:-2].replace('&', '')

    # print('Port name: {}'.format(port_name.title()))
    port_name = port_name.title()

    l = re.compile('\(\d.*\\"[A-Z]\.\)')
    location = l.search(loc).group()
    location = location.replace('(', '')
    location = location.replace(')', '')
    # print('location: {}'.format(location))

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
    
    junctions = parse_destinations(junctions)
    ports = parse_destinations(ports)
    return port_name, location, junctions, ports

with open("PUB151_distances.json", 'w') as out:
    a = {}
    for port in ports[:]:
        n,l,j,p = single_location_parser(port)
        a[n] = {"location":l, "junctions":j, "destinations":p}
    out.write(json.dumps(a, indent=2, encoding="utf-8", ensure_ascii=False, sort_keys=True))
