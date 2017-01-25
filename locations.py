

# plains of gorgoth - 2 infantry regiments against 2 goblin regiments
# something of a tutorial. Also includes reinforcements at endpoints
# AI - likes to continue engagement, and engage idle/defending units
# typcially not a dangerous AI
#
# mountains of gorgoth - recieve an archer 'mountain ranger' type
# unit. Ambushed by 3 enemy archer units. The archer units will
# AI goes shoot (any non-under fire units) > then
# Rain scenario
# mud scenario
# endless reinforcement 'kill the king' scenario
# surround all spearmen scenario where you have temporary
#  cavalry reinforcements
# 	but the ai keeps spearmen on constant defense > phalanx
# (When charging)
# 	forces are balanced but when an enemy unit defends you can
# free up
#   one cavalry to start routing them.

import sys
import ex45armies as armies
import ex45units as units
import ex45ai as ai
import ex45engine as engine

class Location(object):
    """Object that contains the location name attribute and
    a function to enter the location"""

    def __init__(self, name="location"):
        self.name = name

    def enter(self, player_army):
        """player army enters the location. can instantiate
        enemy armies here"""
        # print "You enter the location"
        # print "This will be different for every location"

        # enemy = armies.Army()

        # outcome = battle() engine info here

        # if outcome == "enemy routed" or outcome ==
        # "enemy surrounded":
        #     print 'you win'
        #     return "next location"

class PlainsofGorgoth(Location):

    def __init__(self, name="Plains of Gorgoth"):
        super(PlainsofGorgoth, self).__init__(name)

    def enter(self, player_army):
        """Entry method for plains of gorgoth"""

        pa = player_army

        print "-" * 100
        print "{:-^100}".format(
              "TACTICS ADVENTURE")
        print "{:-^100}".format(
              "Welcome to Tactics Adventure, the strategy game that"
               + " doesn't use numbers")
        print "{:-^100}".format(
              "Units can only be routed or surrounded, so nobody"
              + " ever dies either!")
        print "-" * 100
        print """
        Tactics adventure is designed to be played slowly,
        weighing each decision much like a chess game.
        A wrong move can quickly route a unit.
        Watch the NEXT MOVE indicator and try to anticipate
        the enemy reaction before entering a command!"""

        print "\n\nEnter plains of Gorgoth\n"
        raw_input(">")
        print """
        You are the leader of the {}. You enter the Plains of
        Gorgoth to investigate incursions by a local goblin tribe.
        The tribe is led by a fearsome goblin chieftan named Cesar.
        Cesar has raided many villages, taking gold and goods
        from the villagers "As a deposit" that is never returned.
        """.format(player_army.name)
        raw_input(">")
        print """
        A host of goblins approaches, you spot two goblin
        infantry units. They are led by a pretty dumb looking chief
        goblin. Is it Cesar? You engage them to find out."""
        raw_input(">")

        # INSTANTIATE UNITS
        goblins = units.Infantry(name="Red Goblins")
        goblins_II = units.Infantry("Green Goblins")

        # INSTANTIATE ARMY AND POPULATE
        goblins_of_gorgoth = armies.Army()
        goblins_of_gorgoth.name = "Goblins of Gorgoth"
        goblins_of_gorgoth.add_unit(goblins)
        goblins_of_gorgoth.add_unit(goblins_II)

        # INSTANTIATE AI COMMANDER
        goblin_commander = ai.Commander()
        goblins_of_gorgoth.register_ai(goblin_commander)

        # INSTANTIATE BATTLE
        battle_for_the_plains_of_gorgoth = engine.PGBattleEngine(
                                           player_army,
                                           goblins_of_gorgoth
                                           )
        battlegorgoth = battle_for_the_plains_of_gorgoth

        print "The Battle for the Plains of Gorgoth begins!"
        raw_input(">")

        # BATTLE METHOD WITH OUTCOME
        outcome = battlegorgoth.battle_commence()

        if outcome == "enemy routed" or outcome == "enemy surrounded":
            print outcome
            print """
            The goblins have been defeated. They flee to the
            mountains on the edge of the plain."""
            raw_input(">")
            print """
            You interrogate the chief goblin, and determine
            that the main goblin army has left, towards the Gorgoth
            Mountain range. Interrogations reveal that the primary
            goblin force is significantly larger. You send a rider
            to town to request reinforcements, but continue onwards
            to catch Cesar before he can escape."""
            raw_input(">")
            return "Mountains of Gorgoth"
        else:
            print "You lost, game over. exit"
            sys.exit()

class MountainsofGorgoth(Location):

    def __init__(self, name="Mountains of Gorgoth"):
        super(MountainsofGorgoth, self).__init__(name)

    def enter(self, player_army):
        """Entry method for mountains of gorgoth"""

        print ("Enter Mountains of Gorgoth")
        raw_input(">")
        print """
        Your forces move through the narrow passes of
        the mountain range. No sign of the goblins is visible.
        Rainclouds form in the sky, it will begin to pour any time
        now."""
        raw_input(">")
        print """
        Suddenly, a rain of stones falls on your forces!
        A goblin ambush is sprung!

        Fortunately, the goblins appear uneasy and
        and do not engage. You will need to fight defensively
        to survive until help arrives or the rain starts!

        The infantry units are unwilling to attack, but arrow fire
        will route your units if they are engaged!

        """
        raw_input(">")

        goblins = units.Infantry("Goblins")
        goblin_slingerz = units.Archers("Goblin Slingerz")
        goblin_slingerz_II = units.Archers("Goblin Slingerz II")


        mountain_ambushers = armies.Army()
        mountain_ambushers.name = "Mountain Ambushers"
        mountain_ambushers.add_unit(goblins)
        mountain_ambushers.add_unit(goblin_slingerz)
        mountain_ambushers.add_unit(goblin_slingerz_II)

        ambush_commander = ai.AmbushCommander()
        mountain_ambushers.register_ai(ambush_commander)

        ambushmountains = engine.MountainBattleEngine(player_army,\
                                        mountain_ambushers)
        outcome = ambushmountains.battle_commence()

        if outcome == "enemy surrounded" or outcome == "enemy routed":
            print """
            The Goblins have been captured or routed. You
            interrogate their commander to discover that the mountain
            clans routed Cesar recently.
            Regiment XV is dispatched to speak to the mountain clans.
            You press forward into the mountains to find Cesar
            and return the deposits to their rightful owners"""
            raw_input(">")
            player_army.remove(human_infantryXV)
            return "Mountain Ridge"
        else:
            print """
            You are defeated, the deposits will never
            be returned"""
            sys.exit()

class MountainRidge(Location):

    def __init__(self, name="Mountains of Gorgoth"):
        super(MountainRidge, self).__init__(name)

    def enter(self, player_army):
        """Entry method for mountain ridge"""

        print "Enter Mountain Ridge"
        print """
        You camp on a large mountain ridge. The slopes
        offer some safety if an attack is mounted.
        Late at night, the reinforcements arrive from the villages.
        The new reinforcements are escorted by a team of mounted
        Knights from a nearby castle who have also come looking
        for Cesar, claiming that he killed their lord.
        "His life was a deposit" Cesar claimed, before fleeing.
        The knights will join temporarily but must leave by
        the next morning to defend the castle."""
        raw_input(">")

        spears = units.Spearmen("Levy Pikemen")
        spearsnoble = units.Spearmen("Noble Spearmen")
        knights = units.Cavalry("Knights of Stoneybrook")
        player_army.add_unit(spears)
        player_army.add_unit(spearsnoble)
        player_army.add_unit(knights)
