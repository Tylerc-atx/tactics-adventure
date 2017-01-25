"""Script used for instantiating and playing.
Some classes instantiate objects themselves
Most of this will be done when scenarios are made...
the main army will be instantiated in the first location"""


import ex45units as units
import ex45armies as armies
import ex45engine as engine
import ex45ai as ai
import ex45locations as locations

# INSTANTIATE UNITS
human_infantryXII = units.Infantry(name="Regiment XII")
human_infantryXV = units.Infantry(name="Regiment XV")
# elven_archers = units.Archers(name="Elven Archers")
# honorable_spearmen = units.Spearmen(name="Honorable Spearmen")
# horselords = units.Cavalry(name="Horselords")

# INSTANTIATE ARMY AND POPULATE
alliance_forces = armies.Army()
alliance_forces.name = "Alliance Forces"
alliance_forces.add_unit(human_infantryXII)
alliance_forces.add_unit(human_infantryXV)

# Create map with location objects. Can enter key as INSTANTIATION
# argument for the locatons
the_map = {"Plains of Gorgoth": locations.PlainsofGorgoth(),
           "Mountains of Gorgoth": locations.MountainsofGorgoth(),
           "Mountain Ridge": locations.MountainRidge()}

# Instantiate location engine
campaign = engine.LocationEngine(the_map, alliance_forces)

campaign.start("Plains of Gorgoth")
