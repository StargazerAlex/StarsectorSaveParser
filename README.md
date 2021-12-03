# StarsectorSaveParser

## General info
This project is a simple python script that parses save files of the popular space sim [Starsector](https://fractalsoftworks.com/) from Fractal Softworks, extracts useful information and writes them into a csv file.

## Technologies
* Python: 3.10 or higher

## Features
* Extracts all planets and their respective conditions
	
## Run
```
$ python3 StarsectorSaveParser.py <input_xml> <output_csv>
```

## Example output
```
System,Planet,Planet TypeHabitable,Atmosphere,Temperature,Gravity,Tectonic Activity,Extreme Weather,Darkness,Poor Light,Mild Climate,Inimical Biosphere,Irradiated,Decivilized,Decivilized Subpopulation,Pollution,Meteor Impacts,Water-covered Surface,Farmland,Ore Deposits,Rare Ore Deposits,Organics,Volatiles,Volturnian Lobster Pens,Orbital Solar Array,Ruins,Miscellaneous Conditions
Alpha New Guan Star System,Alpha New Guan I,gas_giant,,,,High Gravity,,Extreme Weather,,,,,,,,,,,,,,Diffuse Volatiles,,,Widespread Ruins,US_floating
Alpha New Guan Star System,Alpha New Guan I-A,US_desertB,,Thin Atmosphere,,Low Gravity,,,,,,,,,,,,,Moderate Ore Deposits,,,,,,,
Alpha New Guan Star System,Alpha New Guan I-B,barren-bombarded,,No Atmosphere,,,,,,,,,,,,,,,Moderate Ore Deposits,,,,,,,
Alpha New Guan Star System,Alpha New Guan I-L4,US_azure,,No Atmosphere,,Low Gravity,,,,,,,,,,,,,Sparse Ore Deposits,,,,,,,
Beta New Guan Star System,Beta New Guan I,irradiated,,,Extreme Heat,,,,,,,,Irradiated,,,,,,Abundant Ore Deposits,Rich Rare Ore Deposits,,,,,,
Beta New Guan Star System,Beta New Guan II,desert1,Habitable,,Hot,,,Extreme Weather,,,,,,,,,,,Moderate Ore Deposits,,,,,,,
Beta New Guan Star System,Beta New Guan III,US_lifeless,Habitable,,,High Gravity,,,,,,,,,,,,Bountiful Farmland,Moderate Ore Deposits,Abundant Rare Ore Deposits,Common Organics,,,,,
Beta New Guan Star System,Beta New Guan III-L5,US_redWind,,Thin Atmosphere,,Low Gravity,,,,,,,,,,,,,Moderate Ore Deposits,,,,,,,
Gamma New Guan Star System,Gamma New Guan I,US_acid,,Toxic Atmosphere,Extreme Heat,,,Extreme Weather,,,,,,,,,,,Moderate Ore Deposits,Abundant Rare Ore Deposits,,Trace Volatiles,,,,
Gamma New Guan Star System,Gamma New Guan II,lava,,Toxic Atmosphere,Extreme Heat,,Extreme Tectonic Activity,,,,,,,,,,,,Rich Ore Deposits,Ultrarich Rare Ore Deposits,,,,,,
Gamma New Guan Star System,Gamma New Guan III,lava,,Toxic Atmosphere,Extreme Heat,,Extreme Tectonic Activity,,,,,,,,,,,,Ultrarich Ore Deposits,Rich Rare Ore Deposits,,,,,,
Gamma New Guan Star System,Gamma New Guan IV,US_barrenD,,No Atmosphere,Extreme Heat,,,,,,,,,,,,,,Moderate Ore Deposits,Rich Rare Ore Deposits,,,,,Widespread Ruins,
...
```