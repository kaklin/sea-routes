sea-routes
==========

## Reformatted data from [Distances Between Ports](https://maddenmaritime.files.wordpress.com/2015/01/pub151-distances-btw-ports.pdf)

### From [Wiki Article](https://en.wikipedia.org/wiki/Distances_Between_Ports)
Distances Between Ports (PUB 151) is a publication that lists the distances between major ports. Reciprocal distances between two ports may differ due to the different routes of currents and climatic conditions chosen. To reduce the number of listings needed, junction points along major routes are used to consolidate routes converging from different directions.

The positions listed for ports are central positions that most represent each port. The distances are between positions shown for each port and are generally over routes that afford the safest passage. Most of the distances represent the shortest navigable routes, but in some cases, longer routes, that take advantage of favorable currents, have been used. In other cases, increased distances result from routes selected to avoid ice or other dangers to navigation, or to follow required separation schemes.

### Map
![pub151 ports](/all_ports.png)


### Repo includes
* Junction points with their longitude and latitude
* All ports with their locations, the distances to junction points, and distances to other ports
* `parser.py` which takes `PUB151_raw.txt` and spews out a JSON format

### Notes
Some ports are considered special cases, that is when they dont have a list of junction points and ports. See below for an explanation of the difference:

#### Typical format

```
ABENRA, DENMARK
(55°01'36"N., 9°25'50"E.) to:
Junction Points*
Nord-Ostsee-Kanal (East
Entrance), Germany, 207
Skagens Odde, Denmark, 87
Ports
Aarhus, Denmark, 114
Helsinki, Finland, 666
Kobenhavn, Denmark, 196
Lubeck, Germany, 138
Lulea, Sweden, 914
Riga, Latvia, 588
Sankt-Peterburg, Russia, 811
Tallinn, Estonia, 646
Umea, Sweden, 792
```
#### Special case
```
ABADAN, IRAN
(30°19'48"N., 48°16'30"E.)
Subtract 30 miles from Al Basrah
distances.
```

The special cases do not have a list of junction points or ports.

## TODO
- [ ] Treat the special cases better - apply the corrections mentioned
- [ ] Unify the formatting of junction point names between the `junction_points.json` and `PUB151_distances.json`
