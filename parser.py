# -*- coding: utf-8 -*-
"""Takes a copy paste from the PDF and spews out a nice file"""
import re

with open('all.txt') as f:
    big = f.read()

def remove_footers(x):
    x = x.replace('* JUNCTION POINT.—See Preface for use of junction points\n', '')
    return x

big = remove_footers(big)

print(big)

def split_by_port():
    return

with open("ports/AAIUN,  WESTERN SAHARA") as f:
    aauin = f.read()

def parse_ports(ports):
    ports = ports.replace('\n', ' ')
    ports = ports.replace(',', '')
    p = re.compile('\D*\d*\s')
    ports = p.findall(ports)
    ports = [x.strip() for x in ports]
    dist_pattern = re.compile('\d+')
    name_pattern = re.compile('\D+')
    ports = [(name_pattern.search(x).group(0).strip(), dist_pattern.search(x).group(0)) for x in ports]
    return ports

def single_location_parser(loc):
    # print(whole_file)
    port_name = loc.split('\n')[0]

    print('Port name: {}'.format(port_name.title()))

    location = loc.split('\n')[1]
    location = location.replace('\xcc\x8a', '')
    location = location.replace('(', '')
    location = location.replace(')', '')
    location = location.replace('"', '\\"')
    print('location: {}'.format(location[0:location.index(' to:')]))

    junctions = loc[loc.index("Junction Points*")+len("Junction Points* "):loc.index("Ports")]
    ports = loc[loc.index("Ports")+len("Ports "):]
    
    print(parse_ports(junctions))
    print(parse_ports(ports))
    
    return

single_location_parser(aauin)




