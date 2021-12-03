#!/usr/bin/python3

import sys
import os.path
import xml.etree.ElementTree as ET
import csv

def findchildren(root, childlist, tag):
    """
    findchildren recursivly checks all nodes from the root node and appends nodes of a certain tag to a list.

    :param root: root node where the search starts (if root node has the target tag it will be the only element in the list)
    :param childlist: empty list that will be filled (if the target tag exists inside the tree)
    :param tag: target tag (string)
    """ 
    for child in root:
        if child.tag == tag:
            childlist.append(child)
        else:
            findchildren(child, childlist, tag)

# Get program arguments
prog = os.path.basename(sys.argv[0])
if len(sys.argv) != 3 or sys.argv[1].startswith('-'):
    print("usage:", prog, "<input_xml> <output_csv>", file=sys.stderr)
    sys.exit(2)
input_xml = sys.argv[1]
output_csv = sys.argv[2]

# Definition mappings
columns = ['System', 'Planet', 'Planet Type' 'Habitable', 'Atmosphere', 'Temperature', 'Gravity', 'Tectonic Activity', 'Extreme Weather', 'Darkness', 'Poor Light', 'Mild Climate', 'Inimical Biosphere', 'Irradiated', 'Decivilized', 'Decivilized Subpopulation', 'Pollution', 'Meteor Impacts', 'Water-covered Surface', 'Farmland', 'Ore Deposits', 'Rare Ore Deposits', 'Organics', 'Volatiles', 'Volturnian Lobster Pens', 'Orbital Solar Array', 'Ruins', 'Miscellaneous Conditions']
print(columns)

# Read and parse xml file
tree = ET.parse(input_xml)
root = tree.getroot()

starsystems = []
findchildren(root, starsystems, 'Sstm')

# Go through all star systems and write to csv
with open(output_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(columns)
    for starsystem in starsystems:
        if 'dN' in starsystem.attrib:
            starsystem_name = starsystem.attrib['dN']
            for planet in starsystem.find('o').find('saved').findall('Plnt'):
                market = planet.find('market')
                if market != None:
                    planet_type = planet.find('type').text
                    planet_name = market.find('name').text
                    row = [starsystem.attrib['dN'], planet_name, planet_type] + ([''] * (len(columns) - 3))
                    for condition in market.find('cond').findall('st'):
                        match condition.text:
                            case 'habitable':
                                row[3] = 'Habitable'
                            case 'no_atmosphere':
                                row[4] = 'No Atmosphere'
                            case 'dense_atmosphere':
                                row[4] = 'Dense Atmosphere'
                            case 'thin_atmosphere':
                                row[4] = 'Thin Atmosphere'
                            case 'toxic_atmosphere':
                                row[4] = 'Toxic Atmosphere'
                            case 'cold':
                                row[5] = 'Cold'
                            case 'very_cold':
                                row[5] = 'Extreme Cold'
                            case 'hot':
                                row[5] = 'Hot'
                            case 'very_hot':
                                row[5] = 'Extreme Heat'
                            case 'low_gravity':
                                row[6] = 'Low Gravity'
                            case 'high_gravity':
                                row[6] = 'High Gravity'
                            case 'tectonic_activity':
                                row[7] = 'Tectonic Activity'
                            case 'extreme_tectonic_activity':
                                row[7] = 'Extreme Tectonic Activity'
                            case 'extreme_weather':
                                row[8] = 'Extreme Weather'
                            case 'dark':
                                row[9] = 'Darkness'
                            case 'poor_light':
                                row[10] = 'Poor Light'
                            case 'mild_climate':
                                row[11] = 'Mild Climate'
                            case 'inimical_biosphere':
                                row[12] = 'Inimical Biosphere'
                            case 'irradiated':
                                row[13] = 'Irradiated'
                            case 'decivilized':
                                row[14] = 'Decivilized'
                            case 'decivilized_subpop':
                                row[14] = 'Decivilized Subpopulation'
                            case 'pollution':
                                row[15] = 'Pollution'
                            case 'meteor_impacts':
                                row[16] = 'Meteor Impacts'
                            case 'water_surface':
                                row[17] = 'Water-covered Surface'
                            case 'farmland_poor':
                                row[18] = 'Poor Farmland'
                            case 'farmland_adequate':
                                row[18] = 'Adequate Farmland'
                            case 'farmland_rich':
                                row[18] = 'Rich Farmland'
                            case 'farmland_bountiful':
                                row[18] = 'Bountiful Farmland'
                            case 'ore_sparse':
                                row[19] = 'Sparse Ore Deposits'
                            case 'ore_moderate':
                                row[19] = 'Moderate Ore Deposits'
                            case 'ore_abundant':
                                row[19] = 'Abundant Ore Deposits'
                            case 'ore_rich':
                                row[19] = 'Rich Ore Deposits'
                            case 'ore_ultrarich':
                                row[19] = 'Ultrarich Ore Deposits'
                            case 'rare_ore_sparse':
                                row[20] = 'Sparse Rare Ore Deposits'
                            case 'rare_ore_moderate':
                                row[20] = 'Moderate Rare Ore Deposits'
                            case 'rare_ore_abundant':
                                row[20] = 'Abundant Rare Ore Deposits'
                            case 'rare_ore_rich':
                                row[20] = 'Rich Rare Ore Deposits'
                            case 'rare_ore_ultrarich':
                                row[20] = 'Ultrarich Rare Ore Deposits'
                            case 'organics_trace':
                                row[21] = 'Trace Organics'
                            case 'organics_common':
                                row[21] = 'Common Organics'
                            case 'organics_abundant':
                                row[21] = 'Abundant Organics'
                            case 'organics_plentiful':
                                row[21] = 'Plentiful Organics'
                            case 'volatiles_trace':
                                row[22] = 'Trace Volatiles'
                            case 'volatiles_diffuse':
                                row[22] = 'Diffuse Volatiles'
                            case 'volatiles_abundant':
                                row[22] = 'Abundant Volatiles'
                            case 'volatiles_plentiful':
                                row[22] = 'Plentiful Volatiles'
                            case 'volturnian_lobster_pens':
                                row[23] = 'Volturnian Lobster Pens'
                            case 'solar_array':
                                row[24] = 'Orbital Solar Array'
                            case 'ruins_scattered':
                                row[25] = 'Scattered Ruins'
                            case 'ruins_widespread':
                                row[25] = 'Widespread Ruins'
                            case 'ruins_extensive':
                                row[25] = 'Extensive Ruins'
                            case 'ruins_vast':
                                row[25] = 'Vast Ruins'
                            case _:
                                row[26] = condition.text
                    print(row)
                    csvwriter.writerow(row)