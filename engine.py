from sys import exit

import ex45armies as armies #imports units into itself
import ex45units as units





class BattleEngine(object):
	"""Engine() instance will instantiate Battle as an object that
	it manipulates when battles commence."""

	def __init__(self, player_army, enemy_army):
		"""Place two army objects in the init parameters"""
		self.pa = player_army
		self.ea = enemy_army

	def pre_battle(self):
		"""Runs army refresh and sort routines"""

		self.pa.refresh()
		self.ea.refresh()

	def change_conditions(self, newconditions='clear'):
		"""Changes location conditions. Current possibilities
		include "mud" and "rain" """

		self.pa.loc_conditions(newconditions)
		self.ea.loc_conditions(newconditions)

	def player_triggers(self, turn_counter):
		"""Runs after every player turn and can trigger changes
		in the battle.
		turn_counter counts how many turns have passed in the battle.
		You can call self.ea and self.pa to get battle status info
		from the armies"""

	def enemy_triggers(self, turn_counter):
		"""See above description"""

	def battle_commence(self):
		"""Begins the battle sequence for the battle object
		Returns "player routed", "player surrounded",
		"enemy routed", "enemy surrounded" """

		ai = self.ea.ai #ai method to be called

		self.pre_battle()

		statuspa = "ok"
		statusea = "ok"
		turn_counter = 0

		while statuspa == "ok" and statusea == "ok":

			nextpa = self.pa.unitorder[self.pa.next_move] #key nextpa
			nextea = self.ea.unitorder[self.ea.next_move]
			paunit = self.pa.unitlist[nextpa] # object next unit
			eaunit = self.ea.unitlist[nextea] # PRIOR to increment

			self.pa.print_engagements()
			self.ea.print_enemy_reserves()

			# PLAYER BLOCK
			paunit.sitrep()
			aactions = paunit.available_actions(self.ea) #printretlist
			if aactions != []:
				player_choice = raw_input("Enter Choice $")
				while player_choice not in aactions:
					player_choice = raw_input("Re-input $")
				paunit.take_action(player_choice, self.ea) #action
			estatus = self.ea.status_check()
			if estatus == "routed" or estatus == "surrounded":
				print "YOU WIN"
				return ("enemy " + estatus)
			self.player_triggers(turn_counter)

			# ENEMY BLOCK
			eaunit.sitrep()
			aactions = eaunit.available_actions(self.pa)
			raw_input("Enemy Choice $")
			if aactions != []:
				ai_choice = ai(aactions,
							   eaunit.type,
							   self.pa,
							  )
				if ai_choice not in aactions:
					print "DEBUG: AI CHOICE NOT IN KEYS"
				eaunit.take_action(ai_choice, self.pa)
			pstatus = self.pa.status_check()
			if pstatus == "routed" or pstatus == "surrounded":
				print "YOU LOSE"
				return ("player " + estatus)
			self.enemy_triggers(turn_counter)
			turn_counter += 1


class LocationEngine(object):
	"""Used to move from location to location.
	map: a dictionary of location names and location objects
	player_army: player controlled army"""
	def __init__(self, map, player_army):
		self.map = map
		self.player_army = player_army

	def start(self, start_location):
		""" begins location engine, given a start location string"""

		current_loc = start_location

		while True:
			next_loc = self.next_location(current_loc)
			current_loc = next_loc

	def next_location(self, location_name):
		return self.map[location_name].enter(self.player_army)



# CUSTOM BATTLE TRIGGER CLASSES BELOW

class PGBattleEngine(BattleEngine):
	"""Used in the campaign for Plains of Gorgoth tutorials"""

	def __init__(self, player_army, enemy_army):
		super(PGBattleEngine, self).__init__(player_army,\
		 										   enemy_army)

	def player_triggers(self, turn_counter):
		"""Tutorial for Plains of Gorgoth"""

		if turn_counter == 0:
			print """
			--------------TUTORIAL------------------------------------
			At the top of each turn the "Engagement List" is printed

			The left column contains player units
			The middle column contains player unit engagement status
			The right column contains enemy units that are engaged
			by friendly units, or are elsewhere on the battlefield

			Sometimes, units that are under fire, or have other
			special status affects, will have an indicator.
			One of these indicators is the NEXT MOVE indicator.

			Below the engagement list is the 'turn' UI.
			A units status and engagement situation will be printed.
			A list of possible actions is provided.
			The player or AI make their move using this list.

			Player will move first, then the AI will move.
			"""

	        #CHEATS TO SPEED UP DEBUG
			print "DEBUG CHEAT ENABLED. SKIPPING BATTLE."
	        self.ea.unitlist["Red Goblins"].status = "routed"
	        self.ea.unitlist["Green Goblins"].status = "routed"
	        #CHEATS TO SPEED UP DEBUG


		if turn_counter == 1:
			print """
			--------------TUTORIAL------------------------------------
			How Engagements Work:

			A Unit can 'engage' another unit, attacking it.
			Any given unit can only engage one unit.

			If two units engage a single unit, it will route...
			Although not always! (see defending)

			While engaged, a unit can only retreat to a defensive
			position, or continue the engagement.
			"""

		if turn_counter == 2:

			print """
			--------------TUTORIAL------------------------------------

			Defending:

			If a unit is in 'defend' mode, it has priviledges that
			a non-defending unit does not have, but will LOSE
			it's defensive status if it chooses to engage
			another unit.

			When engaged by an enemy, a defending unit will
			enter 'fending_off' status instead of 'engaged'.

			Fending_off is special because a unit can take actions
			OTHER than defend/continue. It can break the engagement
			and attack another unit, although it will lose its
			defending status.

			However, when it is engaged by two units it will become
			"surrounded", and will be unable to act. This is
			still preferable to routing.

			When the unit is no longer surrounded, it will be able
			to act again.

			If all your armies units are surrounded or routed, the
			battle will be lost!
			"""

		if turn_counter == 3:
			print """
			--------------TUTORIAL------------------------------------

			Engaging - in Summary

			Engagement Status:
			"""
			print "{:^22}|{:^22}|{:^22}".format("Not Engaged",
								   "Engaged", "Engaged by Two Units")
			print "\n Non-Defensive:"
			print "{:^22}|{:^22}|{:^22}".format("IDLE",
								   "ENGAGED", "ROUTED")
			print "\n Defensive:"
			print "{:^22}|{:^22}|{:^22}".format("DEFENDING",
								   "FENDING_OFF", "SURROUNDED")

			print """
			These rules apply to all units.
			However, units will special abilities will be introduced
			as the campaign progresses.
			Some of these special abilities can bend the basic
			engagement rules!
			"""

	def enemy_triggers(self, turn_counter):
		"""Tutorial for Plains of Gorgoth"""

class MountainBattleEngine(BattleEngine):
	"""Used in the campaign to create rain mid-battle"""

	def __init__(self, player_army, enemy_army):
		super(MountainBattleEngine, self).__init__(player_army,\
		 										   enemy_army)

	def enemy_triggers(self, turn_counter):
		"""Triggers the rain"""

		if turn_counter == 1:
			print """
			--------------TUTORIAL------------------------------------
			Archers:

			Archers are units that can attack without
			becoming engaged themselves by using the SHOOT
			ability.

			Archers can shoot from the following situations:
			DEFENDING, FENDING_OFF, and IDLE

			A unit that is shot by an archer will recieve an
			UNDER_FIRE flag until either:
			The archer is routed
			The archer's next turn arrives

			If an engaged/fending_off unit is shot, it will route
			immediately!

			When a unit is UNDER_FIRE it will be routed when engaged!
			This includes units that are defensive stances!

			However, a unit that is UNDER_FIRE can still engage
			enemies without being routed. It only panics and 'breaks'
			if it is being hit by arrows and also attacked.

			It is important to watch the NEXT_TURN indicator to
			engage archers before they can shoot.
			"""

		if turn_counter == 2:
			goblin_throwers = units.Archers("Goblin Throwers")
			self.ea.add_unit(goblin_throwers)

			print """
			--------------TUTORIAL------------------------------------
			Reinforcements:

			Sometimes reinforcements will appear during a battle.
			These are often important to the scenario. So
			pay attention to the scenario details.

			Reinforcements will move last in the unit turn order"""

		if turn_counter == 5:
			goblin_throwers = units.Archers("Goblin Throwers")
			self.ea.add_unit(goblin_throwers)

		if turn_counter == 7:
			print "A team of mountain rangers arrives to help!"
			print "They have been tracking the goblins for weeks and"
			print "want to join your expeditionary force"
			rangers = units.Archers("Rangers")
			self.pa.add_unit(rangers)

		if turn_counter == 6:
			self.ea.loc_conditions("rain")
			self.pa.loc_conditions("rain")

			print """
			--------------TUTORIAL------------------------------------
			Rain:

			Rain will make arrow fire impossible. This greatly
			reduces the usefulness of the SHOOT ability.

			Archers can still engage just as effectively as any other
			unit, however.

			UNDER_FIRE flags will not disappear until the Archers
			next turn, so give the rain storm a few minutes to take
			effect.
			"""

			print "A RAINSTORM BEGINS"















#don't forget 'captured' condition if all units in army are captured.
# the condition can pass to the location instance for the scenario
# DONE

# a battle(army, army) class will be needed
# This need to include an 'available actions list parse' type method
# that reads the second returned value from action functions
# DONE

# play_player_army = ex45armies.####(###)
# play_map = Map()
# play_map.load("ex45locations.py") #should include location dictionay
#
# engine_object = Engine(play_map, play_player_army)

#BATTLE CLASS
# use list comprehensions for unit order if needed
#DONE

# An battle.sort__turn_order() method will be needed when units
# are added or removed. Will still maintain 'unit.tookturn' for the
# current turn. (0 or 1) The turn_order return string can have a
# sequence with the unitlist dict keys
# Turn order is type: archer, infantry, spearmen, cavalry
#DONE

# START: ARMY REFRESH > SORT UNITS >
# > PLAYERARMY.PRINT_ENGAGEMENTS
# > ENEMYARMY.PRINT_ENEMY_RESERVES

# AFTER BATTLE STARTS:
# PLAYERUNIT SITREP > PLAYERUNIT ACTIONLIST > INPUT ACTION >
#  > ENEMYARMY.STATUS_CHECK
# ENEMYUNIT SITREP > ENEMYUNIT ACTIONLIST > AI ACTION >
# > PLAYERARMY.STATUS_CHECK
# > PLAYERARMY.PRINT_ENGAGEMENTS
# > ENEMYARMY.PRINT_ENEMY_RESERVES
# > PLAYERUNIT SITREP.......... >>>>>
# Call on next unit by unitlist[unitorder[next_move]]
# Call on enemyarmy.ai by using its type argument
# enemyarmy.ai(actiondict, enemyunit.type)

# engine.battle.status is run after every turn. It checks the
# army statuses, and also resets the .tookturn counters to
# 1 if all units have .tookturn == 0. The '0, 1' rather than
# true false is simply for extensibility in case another
# unit type is implemented that gets more than 1 turn.
