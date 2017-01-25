

# unitlist attribute... uses unit.name as keys, and unit() objects as
# value
# DONE

# Every enemy army will have an ai.description that describes the
# commanders and their personality during the 'location' phase
# this will give hints about the ai's choices as well as the
# enemy army composition
# DONE

# player and enemy armies defined here. Enemy armies will have the "AI
# method that returns an action after taking an enemy type, and player
# army object (so it can count units existing and their status)
# for instance, to set phalanx up if player cav is charging
# DONE

# Need a army.remove(unit) method and army.add(unit) method
# for add/remove, be sure to mention which unit is being added or
# removed prior to displaying the verbose unitlist.
#DONE

# Need an army.return_verbose_unitlist that returns a long string
# with list of units and their descriptions. to be used at beginning
# of battles and when a unit is removed or added
# DONE

# Need an army.printengagements that prints all engaged enemies and
# friendly units in a formated list, similar to
# ENEMY ROUTED
# ENEMY CHARGING
# ENEMY DEFENSE	Enemy7, Enemy8
# ENEMY PHALANX
# ENEMY UNDER FIRE
# ENEMY IDLE	Enemy5, Enemy 6
# 		Enemy1			Enemy2 Enemy3			Enemy4
#		Unit1			Unit2					Unit3
# IDLE	Unit4, Unit5
# UNDER FIRE
# PHALANX
# DEFENSE Unit6, Unit7
# CHARGING
# ENEMY ROUTED

# can cycle through
# enemy_line = [" ".join(unit.engaged_with) for unit in \
# 	playerarmy.unitlist if len(unit.engaged_with) > 0]
# player_line = [unit for unit in playerarmy.unitlist \
# 	if len(unit.engaged_with) > 0]
# Find ideal field width and number of fields (probably 4)
# Create function to print multi-line engagements IF NEEDED Can
# 	use slices to handle lists to print lists that may have partial
# 	# of fields per line. for item in enemy_line[4:8]
#	slices will not return an error if the list only goes to item 7
# DONE
# army.statuscheck runs after EVERY move
# need to add a 'surrounded' attribute for army that is part of the
# engine's routine army.status checks
# DONE
# army.status also needs a special trigger for certain scenarios where
# "it starts raining when unitlist length is at 3..." and you are told
# to anticipate a rainstorm at the start of the battle and should
# not focus on routing enemy archers
# DONE
# army.loc_conditions(conditions) argument that allows 'rain' and
# 'mud' and 'clear' to be passed to it by the status checks
# DONE
#army.refresh that will set all units to defending status, not chrging
# and no phalanx. clear conditions, etc. Cleans any arrow units out
# DONE
# army.statuscheck will route units that are surrounded, and similar
# DONE


class Army(object):
    """Army base class. Stores units in the army and has commands to
    manipulate the data and print information about army status.
    Dictionary unitlist contains the string name and object of
    each unit in the army"""

    def __init__(self):
        self.name = "Default Army"
        self.description = "default army description"
        self.unitlist = {}
        self.unitorder = []
        self.status = None
        self.next_move = 0
        self.commander = None #Assign a commander object
        self.ai = None #Assign a commander.ai object unbound method
        self.commander_name = None #commander.name

    def register_ai(self, aicommander):
        """Registers the AI commander object into
        this armies attributes. Easier than doing it
        manually and less error-prone"""

        self.commander = aicommander
        self.ai = aicommander.ai
        self.commander_name = aicommander.name

    def add_unit(self, unit):
        """Adds a unit to the army. The unit.army attribute will
        be set to the army object name. Remember, units must be
        instantiated prior to adding them."""

        self.unitlist[unit.name] = unit
        self.unitlist[unit.name].army = self
        self.unitorder.append(unit.name)
        print "{} have been added to {}".format(unit.name, self.name)

    def remove_unit(self, unit):
        """Removes a unit from the army. The unit.army attribute
        will be set to None. Remember, units remain instantiated
        after removing them."""


        del self.unitlist[unit.name]
        unit.army = None
        self.unitorder.remove(unit.name)
        print "{} have been removed from {}".format(unit.name,\
                                                   self.name)


    def sort_units(self):
        """Sorts the unitorder list, which contains all unit names.
        Type order: archers, infantry, spearmen, cavalry"""

        self.unitorder = []

        archers = [unit.name for unit in self.unitlist.values()\
                   if unit.type == "archers"]
        infantry = [unit.name for unit in self.unitlist.values()\
                   if unit.type == "infantry"]
        spearmen = [unit.name for unit in self.unitlist.values()\
                   if unit.type == "spearmen"]
        cavalry = [unit.name for unit in self.unitlist.values()\
                   if unit.type == "cavalry"]

        self.unitorder = archers + infantry + spearmen + cavalry

    def status_check(self):
        """Use AFTER each turn due to next_move counter.
        Checks if army is routed or surrounded. Checks if the last
        unit in the unitorder just moved using nextmove. The engine
        needs to run this immediately after friendly and enemy actions
        are taken. Increments the next_move attribute.
        Refreshes unit lists. returns 'ok', 'routed',
         or 'surrounded'"""

        self.routedlist = [unit for unit in self.unitlist.values() \
                           if unit.status == "routed"]
        self.charginglist = [unit for unit in self.unitlist.values() \
                           if unit.charging == True]
        self.defendinglist = [unit for unit in self.unitlist.values()\
                           if unit.defending == True]
        self.phalanxlist = [unit for unit in self.unitlist.values() \
                           if unit.phalanx == True]
        self.under_firelist = [unit for unit in self.unitlist.\
                               values() if unit.under_fire == True]
        self.engagedlist = [unit for unit in self.unitlist.values() \
                           if unit.status == "engaged" \
                           or unit.status == "fending_off"]
        self.surroundedlist = [unit for unit in self.unitlist\
                               .values() if unit.status ==\
                                "surrounded"]
        self.firing_atlist = [unit.firing_at.values()[0] for unit \
                             in self.unitlist.values() \
                             if len(unit.firing_at) > 0]

        if len(self.unitorder) == (self.next_move + 1):
            self.next_move = 0
            self.sort_units()
        else:
            self.next_move += 1

        if len(self.routedlist) + len(self.surroundedlist)\
           == len(self.unitlist):
            if len(self.surroundedlist) > 0: #last units surrounded
                print "{thisarmy.name} are surrounded".format(
                      thisarmy=self)
                return "surrounded"
            else:
                print "{thisarmy.name} are routed".format(
                      thisarmy=self)
                return "routed"
        else:
            return "ok"

    def refresh(self):
        """Used at beginning of battles or afterwards by the location
        engine. Refreshes unit status"""

        self.next_move = 0
        self.sort_units()

        for unit in self.unitlist.values():
            unit.army = self
            unit.status = "idle"
            unit.engaged_with = {}
            unit.defending = False
            unit.loc_conditions = 'clear'
            unit.charging = False
            unit.phalanx = False
            unit.under_fire = False
            unit.firing_at = {}

    def loc_conditions(self, conditions='clear'):
        """Specify new location conditions in the parameter, otherwise
        defaults to 'clear'
        Other implemented conditions include 'mud' and 'rain'"""

        for unit in self.unitlist.values():
            unit.loc_conditions = conditions

    def print_engagements(self, fwidth = 120):
        """Prints a list of all actively engaged units. fwidth
        parameter specifies field width of full table"""

        # rlist. right list that contains enemy units
        # llist. left list that contains allied units
        llist = {}
        clist = {}
        rlist = {}
        r = 0 #row number
        # NOT IMPLEMENTED- ARCHER ISSUE surround_participant = []

        for name in self.unitorder:
            unit = self.unitlist[name]

            #ensures units already printed in surround actions aren't
            #printed twice NOT IMPLEMENTED DUE TO ARCHER ISSUE
            #if unit in surround_participant:
             #   continue

            if len(unit.firing_at) > 0:
                llist[r] = unit.name
                clist[r] = "are firing at"
                rlist[r] = unit.firing_at.keys()[0]
                r += 1


            if unit.status == "surrounded":
                llist[r] = unit.name
                clist[r] = "are surrounded by"
                rlist[r] = (unit.engaged_with.keys()[0] + ", "
                           + unit.engaged_with.keys()[1])
            elif unit.status == "engaged":
                enemy = unit.engaged_with.values()[0]
                if enemy.status == "surrounded":
                    if unit.name == enemy.engaged_with.\
                                    keys()[0]:
                        allyname = enemy.engaged_with.\
                                    keys()[1]
                    else:
                        allyname = enemy.engaged_with.\
                                   keys()[0]
                    llist[r] = (unit.name
                               + " (with "
                               + allyname + ")")
                    clist[r] = "are surrounding"
                    rlist[r] = enemy.name
                    # ally1 = enemy.engaged_with.values()[0]
                    # ally2 = enemy.engaged_with.values()[1]
                    # surround_participant.append(ally1)
                    # surround_participant.append(ally2)
                else:
                    llist[r] = unit.name
                    clist[r] = "are engaged to"
                    rlist[r] = unit.engaged_with.keys()[0]
            elif unit.status == "fending_off":
                enemy = unit.engaged_with.values()[0]
                # if enemy.status == "surrounded":
                #     llist[r] = (enemy.engaged_with.keys()[0]
                #                + " (with "
                #                + enemy.engaged_with.keys()[1] + ")")
                #     clist[r] = "are surrounding"
                #     rlist[r] = enemy.name
                    #IF code may be impossible in practice
                    # ally1 = enemy.engaged_with.values()[0]
                    # ally2 = enemy.engaged_with.values()[1]
                    # surround_participant.append(ally1)
                    # surround_participant.append(ally2)
                # else:
                llist[r] = unit.name
                clist[r] = "are fending off"
                rlist[r] = unit.engaged_with.keys()[0]
            elif unit.status == "routed":
                llist[r] = unit.name
                clist[r] = "are routed"
                rlist[r] = " "
            elif unit.status == "idle":
                llist[r] = unit.name
                rlist[r] = " "
                if unit.phalanx == True:
                    clist[r] = "are in idle phalanx"
                elif unit.charging == True:
                    clist[r] = "are charging"
                else:
                    clist[r] = "are idle"
            elif unit.status == "defending":
                llist[r] = unit.name
                if unit.phalanx == True:
                    clist[r] = "are in defending phalanx"
                else:
                    clist[r] = "are defending"
                rlist[r] = " "

            if self.unitorder[self.next_move] == unit.name:
                llist[r] = "NEXT MOVE " + llist[r]

            if unit.under_fire == True:
                llist[r] = "(UNDER FIRE) " + llist[r]

            r += 1

        # Print Columns Out
        table_width = fwidth
        header_width = fwidth + 4
        center_width = fwidth / 3
        side_width = center_width
        #left: right aligned, center: center
        # right column, left aligned
        print "\n"
        print "{ue:-^{hw}}".format(ue="UNIT ENGAGEMENT SUMMARY",\
                                 hw=header_width)
        print "-" * header_width
        for row in llist:
            print ("|{l:>{sw}}|{c:^{cw}}|"
                  + "{r:<{sw}}|").format(l=llist[row],
                  c=clist[row], r=rlist[row], cw=center_width,
                  sw=side_width)
        # Table is left open so enemy reserves list can be printed


    def print_enemy_reserves(self, fwidth=120):
        """Prints, PHALANX, CHARGING, IDLE (Nonphalanx, non-charging),
        DEFENDING, and ROUTED units.
        This method is used primarily to print enemy units that
        do not show up in print_engagements.
        Needs to print in the same format, but with the first two
        columns completely empty.
        The battle engine can call this method on the enemy army.
        Although, both armies have the method"""

        # rlist. right list that contains enemy units
        # llist. left list that contains allied units
        llist = {}
        clist = {}
        rlist = {}
        r = 0 #row number

        for name in self.unitorder:
            unit = self.unitlist[name]

            # if self.unitorder[self.next_move] == unit.name:
            #     llist[r] = " "
            #     clist[r] = " "
            #     rlist[r] = "NEXT MOVE"
            #     r += 1
            # Does not work due to shifting enemy list

            if unit.phalanx == True:
                llist[r] = " "
                clist[r] = " "
                if unit.defending == True:
                    rlist[r] = unit.name +\
                               " are in defending phalanx"
                else:
                    rlist[r] = unit.name +\
                               " are in idle phalanx"
            elif unit.charging == True:
                llist[r] = " "
                clist[r] = " "
                rlist[r] = unit.name + " are charging"
            elif unit.status == "idle":
                llist[r] = " "
                clist[r] = " "
                rlist[r] = unit.name + " are idle"
            elif unit.status == "defending":
                llist[r] = " "
                clist[r] = " "
                rlist[r] = unit.name + " are defending"
            elif unit.status == "routed":
                llist[r] = " "
                clist[r] = " "
                rlist[r] = unit.name + " are routed"

            if ((unit.status == "defending" or
               unit.status == "idle" or
               unit.status == "routed") and
               self.unitorder[self.next_move] == unit.name):
                rlist[r] = rlist[r] + " NEXT MOVE"
                if unit.under_fire == True:
                    rlist[r] = rlist[r] + " (Under fire)"

            r += 1

        # Print Columns Out
        table_width = fwidth
        header_width = fwidth + 4
        center_width = fwidth / 3
        side_width = center_width
         #left: right aligned, center: center
        # right column, left aligned
        for row in llist:
            print ("|{l:>{sw}}|{c:^{cw}}|"
                  + "{r:<{sw}}|").format(l=llist[row],
                  c=clist[row], r=rlist[row], cw=center_width,
                  sw = side_width)
        print "-" * header_width
