# tactics-adventure
v0.10a of the revolutionary text-based strategy game that simulates battles without using any numbers

CURRENT DEVELOPMENT NOTES


"""This document is outdated and meant for the exercise draft only.
Read the ex45developmentdocumentation file instead.
READ TOP COMMENTS TO LEARN HOW TO MAKE ADVENTURES/UNITS/ARMIES"""

DEV NOTES: FIX THE GAME BREAKING DEFENSE STALEMATE ISSUE
Use dictionary.get(key, None) to retrieve things from dictionaries
to avoid all the pointless if statements for allyflank and other
similar things
ex47 has a great structure for overworld 'move' commands
where the move command and room objects are located in each room


-----------------------------------------------------------------
HOW TO MAKE A FULL GAME
(To make just a battle, follow steps 1 and 4)
-----------------------------------------------------------------

0. __main__ needs to import modules
import ex45units as units
import ex45armies as armies
import ex45engine as engine
import ex45ai as ai
import ex45locations as locations


1. HOW TO MAKE A UNIT AND ARMY (Player army in __main__)
Make a unit: unit_object = units.UnitClass("Name")
Unit classes are in ex45units and are Infantry, Cavalry,
  Archers, and Spearmen

Create an Army : army_name = armies.Army("Army name")
Add units to army: army_name.add_unit(unit_object)

ONLY A PLAYER ARMY IS NEEDED TO START CAMPAIGN, ENEMY
  ARMIES WILL BE MADE BY LOCATIONS

Create an AI Commander (non-player army only)
Create a new Commander object.
  new_commander = CommanderClass()
Register an AI to the army with army_name.register_ai(new_commander)
Ai will automatically populate army attributes

(optional) Create a new AI decision priority list:
Make a new commander class in ex45ai.py
For the unit TYPE you would like to edit the decision-making
  tree for a type by editing the attribute list.
Edit the preferred_list actions, entering ['action', 'enemytype']
  in the order that you want the AI to take actions as they are
  available.


2. HOW TO MAKE A LOCATIONS
Create a new Location class in ex45locations. Give it a
  enter() method that returns the string key of the next location

Unit instances and a battle object can be within the location
  (See below on how to start a battle)


3. HOW TO USE THE LOCATION ENGINE AND LOCATIONS
Create a dictionary map of {"string keys": location objects}

Instantiate LocationEngine in ex45engine.py module
  with (map, player_army) as parameters

Run locationengine with .start("Start_location_key")
  to begin the program



4. HOW TO INSTANTIATE A BATTLE
Create a new battle object
battle_object = engine.BattleEngine(player_army, enemy_army)
outcome = battle_object.battle_commence()
outcome contains the 'who lost' string that location if-statements
  can utilize to determine which location to load next

(Optional) Add Battle Triggers:
Triggers occur after player turn, and enemy turn
They can use the in-built turn_counter or any condition specified
that uses the self.ea object (enemy army) or self.pa object (player)
Triggers are written in a custom BattleEngine class that has
a modified method player_triggers or enemy_triggers.
See the campaign battle subclasses for examples















-------------------------------------------------------------
## OUTDATED - DO NOT READ BELOW
-------------------------------------------------------------

# *** FROM THE EXERCISE IN BOOK *** GUIDELINES
I Different type of game
II Use more than one file. This can be simply for putting the rooms
on another file. Enemy module. Action module. TRY a inside-class
__import__ function. (not in __init__)
III One Class per room. Easy enough, the 'rooms' will be cities
forts, and battlefield subclasses
IV Engine Class and Map "runner" class
Strategic overview class for player army and resources and abilities

__DESCRIPTION__ (correct dunder?)"Tactics Adventure:Therevolutionary
new game that simulates RPG-style battles withoutusing any numerical
values.

from sys import exit
Start program by importing locations. Locations will import enemy
army module

Engine
instantiates or loads player army
instantiates or loads map as a parameter
play() method


Map Class
contains location list and a method to return the next location
location list is loaded in def load_locations(**kwargs)
**kwargs will be a dictionary
list parameter must be entered into object method with **
Can use __import__ here for location module
 __init__ for start location
attribute: Contains a list of location type class objects
map.next_location(location_name)
next_location_obj = location_list[location_name]... returns object
constructors



Location Class (seperate module)
Built for subclasses for each location
description attribute
occupying enemy army object attribute

Location Subclasses
won method (contains win text and adds items/units to player army)
	returns next location name string
lost method
  Contains Exit


PlayerArmy Class
Contains unit instances and attributes of player army
Unit instances - Stored in a list. List can be looped through
by the engine. for unit in units[] list: unit.name, availableactions
give each unit an order at start of turn (loops through units). You
can use the .format to include "string {unit.name} ipsum".format
(unit = self.unit) to return attributes (not methods!)
playerarmy.addunit(unit object constructor)
playerarmy.unit.remove (index and remove list functions)
playerarmy.turn() method goes through each unit in unit list and
prints actions, then takes inputs, then passes inputs to unit.action
playerarmy.exists() method checks if the unitlist length is 0
the engine will end the turn in loss at this point

EnemyArmy Class (Seperate module)
Main enemy army type
Contains unit instances
Defeated True/False
unit list attribute
action method with list of pre-defined actions that it iterates
through with a counter that resets when it reaches end of list
Uses a for loop to iterate through list of units, with pauses after
each action
ai methods >
.ai(units[i].name or .type) would have the preferred action from
available a, incrementers,
and if statements for which targets, etc targetlist can be a list
of favored targets, it iterates through them until it finds one
that exists, then selects the first list action on the sequence,
increments it, then returns the self.action(target) method.
can use if statements for the
ai method can have a dictionary with unit names that goto ai methods
the ai methods return the appropriate unit.action(target)

Unit Class
Main format for unit creation. Contains info all units will have
Status: Idle, Engaged, Routed
Name: String name of unit
Description: Description of Unit

Unit Subclasses
type: Infantry, archer, seige, cavalry, building, spearmen
Available actions list
available actions temp list (for during multi-turn action) that is
conditional based on special status attribute (charging, and
continue action increments charge turns counter)
action methods: attack, stand ground, charge, spear shield
take action method (index number) that runs an action
action methods can contain a target list and input target field
