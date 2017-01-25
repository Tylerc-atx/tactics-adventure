


# --------------------------------------------------------------------
# NEXT IMPLEMENTATION
# --------------------------------------------------------------------
# 1. Locations/scenarios and map engine.
#       # Rain scenario
#       # Mud scenario
#       # Scenarios where units are added mid-battle
#       # World map add/remove units during campaign
# 2. Add Unit descriptions, pre-made unit and army classes. Redo
#    and add to battle verbage.
# 3. Add more AI classes
# 4. Battle classes with status_check triggers. These are typically
#    scenario-dependent, but will check conditions after each turns
#    and modify the playing field when triggered.

# --------------------------------------------------------------------
# ORIGINAL DRAFT DOCUMENT - outdated
# --------------------------------------------------------------------
## GUIDELINES
# I Different type of game
# II Use more than one file. This can be simply for putting the rooms
# on another file. Enemy module. Action module. TRY a inside-class
# __import__ function. (not in __init__)
# III One Class per room. Easy enough, the 'rooms' will be cities
# forts, and battlefield subclasses
# IV Engine Class and Map "runner" class
# Strategic overview class for player army and resources and abilities

# __DESCRIPTION__ (correct dunder?)"Tactics Adventure: The revolutionary
# new game that simulates RPG-style battles without using any numerical
# values.

# from sys import exit
# Start program by importing locations. Locations will import enemy
# army module

# Engine
# instantiates or loads player army
# instantiates or loads map as a parameter
# play() method


# Map Class
# contains location list and a method to return the next location
# location list is loaded in def load_locations(**kwargs)
# **kwargs will be a dictionary
# list parameter must be entered into object method with **
# Can use __import__ here for location module
#  __init__ for start location
# attribute: Contains a list of location type class objects
# map.next_location(location_name)
# next_location_obj = location_list[location_name]... returns object
# constructors
#
#

# Location Class (seperate module)
# Built for subclasses for each location
# description attribute
# occupying enemy army object attribute
#
# Location Subclasses
# won method (contains win text and adds items/units to player army)
#	returns next location name string
# lost method
#   Contains Exit


# PlayerArmy Class
# Contains unit instances and attributes of player army
# Unit instances - Stored in a list. List can be looped through
# by the engine. for unit in units[] list: unit.name, unit.availableactions
# give each unit an order at start of turn (loops through units). You
# can use the .format to include "string {unit.name} ipsum".format(unit
# = self.unit) to return attributes (not methods!)
# playerarmy.addunit(unit object constructor)
# playerarmy.unit.remove (index and remove list functions)
# playerarmy.turn() method goes through each unit in unit list and
# prints actions, then takes inputs, then passes inputs to unit.action
# playerarmy.exists() method checks if the unitlist length is 0
# the engine will end the turn in loss at this point

# EnemyArmy Class (Seperate module)
# Main enemy army type
# Contains unit instances
# Defeated True/False
# unit list attribute
# action method with list of pre-defined actions that it iterates
# through with a counter that resets when it reaches end of list
# Uses a for loop to iterate through list of units, with pauses after
# each action
# ai methods >
# .ai(units[i].name or .type) would have the preferred action from available a, incrementers,
# and if statements for which targets, etc targetlist can be a type list
# of favored targets, it iterates through them until it finds one
# that exists, then selects the first list action on the sequence,
# increments it, then returns the self.action(target) method.
# can use if statements for the
# ai method can have a dictionary with unit names that goto ai methods
# the ai methods return the appropriate unit.action(target)

# Unit Class
# Main format for unit creation. Contains info all units will have
# Status: Idle, Engaged, Routed
# Name: String name of unit
# Description: Description of Unit

# Unit Subclasses
# type: Infantry, archer, seige, cavalry, building, spearmen
# Available actions list
# available actions temp list (for during multi-turn action) that is
# conditional based on special status attribute (charging, and
# continue action increments charge turns counter)
# action methods: attack, stand ground, charge, spear shield
# take action method (index number) that runs an action
# action methods can contain a target list and input target field
