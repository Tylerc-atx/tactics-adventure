import ex45units as units
import ex45armies as armies
import ex45engine as engine
import ex45ai as ai
# *************JANUARY 15, UNIT TESTS

# TEST IMPORT SYNTAX DEBUG
# DONE, DEBUG IS COMPLETE


#create unit objects for testing
human_infantry = units.Infantry(name="Human Infantry")
elven_archers = units.Archers(name="Elven Archers")
honorable_spearmen = units.Spearmen(name="Honorable Spearmen")
horselords = units.Cavalry(name="Horselords")

alliance_forces = armies.Army()
alliance_forces.name = "Alliance Forces"
alliance_forces.add_unit(horselords)
alliance_forces.add_unit(human_infantry)
alliance_forces.add_unit(elven_archers)
alliance_forces.add_unit(honorable_spearmen)


goblins = units.Infantry(name="Goblins")
goblins_II = units.Infantry("Goblins II")
goblin_slingerz = units.Archers(name="Goblin Slingerz")
troll_pikemen = units.Spearmen(name="Troll Pikemen")
warg_riders = units.Cavalry(name="Warg Riders")

goblins_of_gorgoth = armies.Army()
goblins_of_gorgoth.name = "Goblins of Gorgoth"
goblins_of_gorgoth.add_unit(goblins)
goblins_of_gorgoth.add_unit(goblins_II)
goblins_of_gorgoth.add_unit(goblin_slingerz)
goblins_of_gorgoth.add_unit(troll_pikemen)
goblins_of_gorgoth.add_unit(warg_riders)


# TEST INSTANTIATION
# FIXED __INIT__ TO INCLUDE PARAMETERS
# DONE
# TEST attributes
# print "\n\n\n"
# print "-" * 150
# print "TEST INSTANTIATION"
# print "-" * 150
# print "Test .name attribute: " + goblins.name
# print "Test undefined .name attribute: " + goblins_II.name
# PASSED TEST

#TEST status_down()
# print "\n\n\n"
# print "-" * 150
# print "TEST unit.status_down()"
# print "-" * 150
# print "Status Before: {status}".format(status=human_infantry.status)
# human_infantry.status_down()
# print "Status After: {status}".format(status=human_infantry.status)

#TEST status_up()
# print "\n\n\n"
# print "-" * 150
# print "TEST unit.status_up()"
# print "-" * 150
# print "Status Before: {status}".format(status=human_infantry.status)
# human_infantry.status_up()
# print "Status After: {status}".format(status=human_infantry.status)

# #TEST engage() PASS
# # TEST 2 - Test from defense to engaged PASS
# # test 3 - Test from fending_off to engaged PASS
# # test 4 - engage defending enemy PASS
# # test 5 - engage fending off enemy PASS
# # test 6 - engage engaged enemy FIXED - PASS
# # test 7 - engage under fire enemy - PASS
# print "\n\n\n"
# print "-" * 150
# print "TEST unit.engage()"
# print "-" * 150
# human_infantry.status = "idle"
# # goblins.status = "defending"
# # goblins.defending = True
# # elven_archers.engage(goblins)
# # e = elven_archers
# # goblins.under_fire = True
# print "Status: {status}".format(status=human_infantry.status)
# print "Engagement list: {}".format(human_infantry.\
#                                           engaged_with)
# # print "Elven Archers Status: {status}".format(status=e.status)
# human_infantry.engage(goblins)
# print "Status After: {status}".format(status=human_infantry.status)
# print "Defend After: {status}".format(status=human_infantry.\
#                                       defending)
# print "Engagement list: {}".format(human_infantry.\
#                                          engaged_with)
# print "Goblins Status: {status}".format(status=goblins.status)
# # print "Elven Archers Status: {status}".format(status=e.status)
#
# human_infantry.defend() #to isolate this code segment
# print "Goblins Status: {status}".format(status=goblins.status)
# # print "Elven Archers Status: {status}".format(status=e.status)

# #TEST break_engagement
# human_infantry.engage(goblins)
# print "\n\n\n"
# print "-" * 150
# print "TEST unit.break_engagement()"
# print "-" * 150
# print "Status Before: {status}".format(status=human_infantry.status)
# print "Engagement list before: {}".format(human_infantry.\
#                                           engaged_with)
# human_infantry.break_engagement()
# print "Status After: {status}".format(status=human_infantry.status)
# print "Engagement list after: {}".format(human_infantry.\
#                                          engaged_with)
# print "Goblin Status After: {status}".format(status=goblins.status)


#TEST unit.defend()
# Test 2. Test engaged to defense stance
# goblins.engage(human_infantry)
# print "\n\n\n"
# print "-" * 150
# print "TEST unit.defend()"
# print "-" * 150
# print "Status Before: {status}".format(status=human_infantry.status)
# print "Engagement list before: {}".format(human_infantry.\
#                                           engaged_with)
# print ("Defense Before: {defending}\nStatus Before: {status}").\
#        format(status=human_infantry.status,
#               defending=human_infantry.defending)
# human_infantry.defend()
# print ("Defense After: {defending}\nStatus After: {status}").\
#       format(status=human_infantry.status,
#              defending=human_infantry.defending)
# print "Engagement list After: {}".format(human_infantry.\
#                                          engaged_with)

# # TEST defend
# # TEST 1 Defend > Fending_off > surrounded chain - PASS
# # TEST 2 Defend > Fending Off > engage another enemy PASS
# # TEST 3 Defend > Fending Off > engage the enemy attacking PASS
# # and works amazingly
# # TEST 4 Defend > Fending Off > Allied unit engages attacker
# # PASS, fixed some defense verbiage that didn't make sense
# # TEST 5 Surrounded, allied unit engages one attacker - FAIL
# # Needs to update engagements for all units that are connected
# # Started by editing break_engagement conditions
# # TEST 6
# h = human_infantry
# g = goblins
# gs = goblin_slingerz
# hs = honorable_spearmen
# print "\n\n\n"
# print "-" * 150
# print "TEST unit.defend()"
# print "-" * 150
# h.defend()
# g.engage(h)
# hs.engage(g)
# print "Status: {}\nDefending: {}".format(h.status, h.defending)
# print "Engaged with: {}".format(h.engaged_with)

# break_engagement. Unfortunately is not an isolated method and
# relies alot on calling methods. So it is tested as part of other
# tests.

# # TEST CONTINUE engagement, continue fending off, continue defending
# # and continue surrounded
# # FIXED, ADDED CONTINUE SURROUNDED, CHANGED VERBIAGE AND TIGHTED
# # SOME
# # UNNECESSARILY COMPLEX CODE.
# # PASS
# h = human_infantry
# g = goblins
# gs = goblin_slingerz
# hs = honorable_spearmen
# print "\n\n\n"
# print "-" * 150
# print "TEST unit.continue...()"
# print "-" * 150
# h.defend()
# h.continue_defending()
# print "Status: {}\nDefending: {}".format(h.status, h.defending)
# print "Engaged with: {}".format(h.engaged_with)

# # TEST route
# # Test in defend (which makes no sense)
# # test in engaged. (only actions will break engagement)
# # test in under_fire
# # PASS
# h = human_infantry
# g = goblins
# gs = goblin_slingerz
# hs = honorable_spearmen
# print "\n\n\n"
# print "-" * 150
# print "TEST unit.route()"
# print "-" * 150
# h.under_fire = True
# h.route()
# print "Status: {}\nDefending: {}".format(h.status, h.defending)
# print "Engaged with: {}".format(h.engaged_with)

# SKIP TESTS
# status_up and status_down tests are part of break_engagement and
# the engage suite of tests

# # TEST shoot
# # Test shooting from idle, defending, and fending off
# # test shooting in the rain
# # Test shooting IDLE unit under fire and not under fire
# # Test shooting fending_off unit and engaged unit
# # Test shooting defending unit and also defending unit under fire
# # test shooting defending unit, then having someone attack it
# # test shooting idle unit, then having someone attack it
# # ALL TESTS PASS WITH MINOR COSMETIC ISSUES
# h = human_infantry
# g = goblins
# gs = goblin_slingerz
# hs = honorable_spearmen
# ea = elven_archers
# print "\n\n\n"
# print "-" * 150
# print "TEST unit.shoot()"
# print "-" * 150
# # ea.loc_conditions = "rain"
# # ea.defend()
# # gs.engage(ea)
# # g.under_fire = False
# # g.defend()
# # hs.engage(g)
# ea.shoot(g)
# hs.engage(g)
# print "Name: {}".format(ea.name)
# print "Status: {}\nDefending: {}".format(ea.status, ea.defending)
# print "Engaged with: {}".format(ea.engaged_with)
# print "Firing at: {}".format(ea.firing_at)
# print "GOBLINS under fire: {}".format(g.under_fire)
# print "Name: {}".format(hs.name)
# print "Status: {}\nDefending: {}".format(hs.status, hs.defending)
# print "Engaged with: {}".format(hs.engaged_with)

# # TEST SITREP
# # Test sitrep after shooting.
# # test while engaged
# # test while idle
# # test while fending off
# # test while surrounded
# # test while routed
# # test while charging. Fixed engagement condition to 'len'
# # test while phalanx
# # Changed some formatting
# # TESTS PASS
# h = human_infantry
# g = goblins
# gs = goblin_slingerz
# hs = honorable_spearmen
# ea = elven_archers
# print "\n\n\n"
# print "-" * 150
# print "TEST unit.sitrep()"
# print "-" * 150
# # ea.loc_conditions = "rain"
# # ea.defend()
# # gs.engage(ea)
# # g.under_fire = False
# # g.defend()
# # hs.engage(g)
# # ea.shoot(g)
# # hs.engage(ea)
# # g.engage(ea)
# # horselords.begin_charge()
# hs.form_phalanx()
# hs.sitrep()
# print "Name: {}".format(ea.name)
# print "Status: {}\nDefending: {}".format(ea.status, ea.defending)
# print "Engaged with: {}".format(ea.engaged_with)
# print "Firing at: {}".format(ea.firing_at)

# # TEST charge and form_phalanx
# # test in mud
# # test cancel
# # test from idle, fending_off and defense
# # test landing on defense, fending off, engaged, and idle enemies
# # test with phalanx active # FIXED CODE. FORGOT THE ELSE:
# # PART OF THE IF STATEMENT. Added some phalanx-break sentences
# h = human_infantry
# g = goblins
# gs = goblin_slingerz
# hs = honorable_spearmen
# ea = elven_archers
# hl = horselords
# tp = troll_pikemen
# print "\n\n\n"
# print "-" * 150
# print "TEST unit.charge() and phalanx()"
# print "-" * 150
# # hl.loc_conditions = "mud"
# hs.defend()
# g.engage(hs)
# # hl.defend()
# tp.defend()
# h.engage(tp)
# hl.begin_charge()
# tp.form_phalanx()
# h.engage(tp)
# # hl.cancel_charge()
# # hl.cancel_charge()
# hl.finish_charge(g)
# hl.sitrep()
# print "Name: {}".format(hl.name)
# print "Status: {}\nDefending: {}".format(hl.status, hl.defending)
# print "Engaged with: {}".format(hl.engaged_with)
# print "Charging: {}".format(hl.charging)
# print "-" * 40
# print "Name: {}".format(tp.name)
# print "Status: {}\nDefending: {}".format(tp.status, tp.defending)
# print "Engaged with: {}".format(tp.engaged_with)
# print "Phalanx: {}".format(tp.phalanx)
# print "-" * 40
# print "Name: {}".format(hs.name)
# print "Status: {}\nDefending: {}".format(hs.status, hs.defending)
# print "Engaged with: {}".format(hs.engaged_with)
# print "Phalanx: {}".format(hs.phalanx)


#--------------------------------------------------------------------
# ARMY TESTS
#--------------------------------------------------------------------



# # TEST ADD AND REMOVE UNIT - PASS
# print "-" * 150
# print "TEST add remove units"
# print "-" * 150
# print alliance_forces.unitlist
# print alliance_forces.unitlist["Human Infantry"]
# print alliance_forces.unitorder
# print horselords.army
# alliance_forces.remove_unit(horselords)
# print "REMOVE HORSELORDS"
# print alliance_forces.unitlist
# print alliance_forces.unitlist["Human Infantry"]
# print alliance_forces.unitorder
# print horselords.army

# TEST sort_units
# FIXED that unitlist was not declared as self.
# FIXED that list was storing objects, not names.
# PASS
# print "-" * 150
# print "TEST sort units"
# print "-" * 150
# print alliance_forces.unitorder
# print "SORT"
# alliance_forces.sort_units()
# print alliance_forces.unitorder

# # TEST status_check and refresh and loc_conditions
# # test who will have next move. Seems to work
# # test if army routed
# # test if surrounded
# # Fixed surrounded and routed returns
# # Fixed global variable issue in refresh for loop
# # Fixed self parameter in loc. as well as global variable in loop
#
# alliance_forces = armies.Army()
# alliance_forces.name = "Alliance Forces"
# alliance_forces.add_unit(horselords)
# alliance_forces.add_unit(human_infantry)
# # alliance_forces.add_unit(elven_archers)
# # alliance_forces.add_unit(honorable_spearmen)
#
# af = alliance_forces
# print "-" * 150
# print "TEST status_check() and refresh() and loc_conditions()"
# print "-" * 150
# alliance_forces.sort_units()
# print "current move: " + af.unitorder[af.next_move]
# human_infantry.status = "routed"
# horselords.status = "routed"
# af.refresh()
# af.loc_conditions("rain")
# af.status_check()
# print "current move: " + af.unitorder[af.next_move]
# print "horselords loc conditions: " + horselords.loc_conditions


# # Test print_engagements and print_enemy_reserves
# # fixed non-global variables in functions
# # fixed variables in header specifications to be in format
# # fixed row + 1 needed to be added to end of if statements
# # added next_move to 0 and sort units to army.refresh
# # set both for loops to loop off unitorder instead of list
# # added next move to enemy unitlist
# # TEST with some units engaged, surrounded, defending,
# # fending off shooting at others,
# # charging, phalanx, routed. Enemies surrounded, enemies shooting
# # at us,
# # enemy phalanx.
# # Added under fire to unit descriptions
# # Removed next_move from enemy list
# # Fixed issue with if statements where friendly's surrounding
# # enemies only showed as engaged. Fixed conditional to include .status
# #
# # print "-" * 150
# # print "TEST print_engagements() and print_enemy_reserves()"
# # print "-" * 150
# alliance_forces.refresh()
# goblins_of_gorgoth.refresh()
# # alliance_forces.next_move = 2
# # print "next move: " + str(alliance_forces.next_move)
# # print alliance_forces.unitlist
# # goblins_of_gorgoth.next_move = 0
# horselords.defend()
# goblins.engage(horselords)
#
#
# goblins_II.defend()
# human_infantry.engage(goblins_II)
# elven_archers.defend()
# warg_riders.engage(elven_archers)
# honorable_spearmen.defend()
# honorable_spearmen.form_phalanx()
# horselords.begin_charge()
# troll_pikemen.form_phalanx()
#
# alliance_forces.print_engagements()
# goblins_of_gorgoth.print_enemy_reserves()


# TEST available_actions
# May use previous battle progress to test it
# Test on surrounded unit GOOD
# Test on idle, engaged, routing, defending, fending off,
# charging, phalanx, shooting
# Archer that is fending off
# Rewrote entire system to utilized strings in a list instead
# of dictionary types
# Also fixed logic in cavalry options
# added a take_action method for the engine
# print "-" * 150
# print "TEST available actions"
# print "-" * 150

# elven_archers.sitrep()
# aactions = elven_archers.available_actions(goblins_of_gorgoth)


# TEST take_action
# Debugged issues with cavalry.
# took several available action scripts and ran the actions
# elven_archers.take_action("shoot Warg Riders",\
# goblins_of_gorgoth)

# # QUICK SUBTEST ABOUT METHODS
# DONE - Learned you cannot pass an active method...
# class Class1(object):
#     def __init__(self):
#         pass
#     def method1(self, string):
#         print "method1 print: " + string
#
# obj = Class1()
# dict = {}
# dict['key1'] = obj.method1("a string")




# Test AI
# 1 Test register_ai - PASSED
# 2 test putting an action list into AI and getting answer
# fixed issue with tuples as sub-list in makeailist for loop
# for makeailist. need to account for instance where there is no
# target and fill in row 1 as ''
# Fixed issue with tuples in the preferred list. The issue with
# tuples is that you cannot call them.
# fixed issue with for-loop logic in make_choice where I was using
# the for loop keys like indices rather than values
# incremented the if len(actkeys) condition to run after each
# ailist value is checked
# fixed issue where phalanx doesn't break if you issue defense stance
# although it won't happen in practice due to breaking when
# available actions are printed.
# 3 Testing feeding into take_action
# ALL PASS. Ready for battle class trials
# alliance_commander = ai.Commander()
# alliance_forces.register_ai(alliance_commander)
# print goblins_of_gorgoth.commander
# print goblins_of_gorgoth.ai
# print goblins_of_gorgoth.commander_name

# aactions = horselords.available_actions(goblins_of_gorgoth)
# print alliance_forces.ai(aactions,
#                     horselords.type,
#                     goblins_of_gorgoth)
# ai_choice = alliance_forces.ai(aactions,
#                     horselords.type,
#                     goblins_of_gorgoth)
# horselords.take_action(ai_choice, goblins_of_gorgoth)


# TEST Battle Class!!!
# TEST import for syntax. Small errors fixed (Documentation)
# and string with missing quotes

goblin_commander = ai.Commander()
goblins_of_gorgoth.register_ai(goblin_commander)
battle_for_the_plains_of_gorgoth = engine.BattleEngine(
                                   alliance_forces,
                                   goblins_of_gorgoth
                                   )
battlegorgoth = battle_for_the_plains_of_gorgoth
battlegorgoth.battle_commence()

# test 1
# fixed self.eaunit/paunit in the engine. These aren't classwide
# variables.
# fixed the issue where enemy block was calling army.available_actions
# instead of unit
# added 'self.'pa and self.ea where needed...
# removed aactions.keys() line from legacy dictionary actionlist
# changed take_action[ai_choice] to take_action(ai_choice)... it's
# not a list, it's a function
# added self.pa as an argument for take choice
# This engine is ripe with syntax and bugs!!
# Fixed print engagements issue where under fire units that engaged
# enemy targets were no longer marked as under fire (game logic
# that I didn't realize)
# fix issue where routed archer leaves its mark under fire
