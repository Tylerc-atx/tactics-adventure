
import random
# choice(sequence) random element. Can find a key then call
# sequence[key]
# randint(a, b): choose random int from a to b with endpoints. can
# use with a
# list of keys to select one. or a list of actions that meet a
# criteria
# from .values(). can use randint(0,len(list))

class Commander(object):
    """Default Commander class. Contains a name and description.
    Subclasses can be made with varied ai methods.
    """

    def __init__(self):
        self.name = "Default"
        self.description = "Default Description"
        self.infpreferred = [
                             ['continue_engagement', ''],
                             ['continue_fending', ''],
                             ['continue_defending', ''],
                             ['engage', 'archers'],
                             ['engage', 'infantry'],
                             ['engage', 'cavalry'],
                             ['defend', ''],
                             ]
        self.archpreferred = [
                             ['shoot', 'infantry'],
                             ['shoot', 'archers'],
                             ['shoot', 'cavalry'],
                             ['shoot', 'spearmen'],
                             ['defend', ''],
                             ['continue_defending', ''],
                             ['continue_fending', ''],
                             ]
        self.spearpreferred = [
                             ['continue_defending', ''],
                             ['defend', ''],
                             ['continue_fending', ''],
                             ]
        self.cavpreferred = [
                             ['finish_charge', 'archers'],
                             ['finish_charge', 'cavalry'],
                             ['finish_charge', 'infantry'],
                             ['finish_charge', 'spearmen'],
                             ['begin_charge', ''],
                             ['defend', ''],
                             ['continue_defending', ''],
                             ['continue_fending', ''],
                             ]

    def ai(self, actions_list, unittype, enemy_army):
        """Bound to army object and used to communicate with ai.
        actions_list parameter takes the actions list
        unittype parameter takes the unit.type"""

        actions_list = actions_list
        enemy_army = enemy_army
        unittype = unittype
        if unittype == "infantry":
            return self.Infantry(actions_list, enemy_army)
        elif unittype == "spearmen":
            return self.Spearmen(actions_list, enemy_army)
        elif unittype == "archers":
            return self.Archers(actions_list, enemy_army)
        elif unittype == "cavalry":
            return self.Cavalry(actions_list, enemy_army)
        else:
            print "DEBUG: CANNOT FIND UNIT TYPE METHOD"

    def make_ailist(self, actions_list, enemy_army):
        """Make a list of format
        [("action_string", "enemy_type_string", "dict_key"),]
        that will be parsed by the ai"""

        ailist = [[x, x, x] for x in range(0, len(actions_list))]
        i = 0

        for astr in actions_list:
            ailist[i][0] = astr.split()[0] #takes action word from key
            tarname = " ".join(astr.split()[1:]) #Gets enemyna rom key
            if tarname != '':
                ailist[i][1] = enemy_army.unitlist[tarname].type
            else:
                ailist[i][1] = ""
            #need to use enemy list to get unit type
            ailist[i][2] = astr
            i += 1

        return ailist

    def make_choice(self, ailist, preferred_list):
        """Takes the ailist and the preferred list of actions
        of a type, and returns a chosen action key"""

        actkeys = []
        #goes down the preferred action list until it finds
        #a value that matches an astr in the list
        for j in preferred_list:
            for i in ailist:
                if j == i[:2]: #list match
                    actkeys.append(i[2]) #append the matching astr
                if len(actkeys) > 0:
                    return random.choice(actkeys)

        # AI COULD NOT FIND A CHOICE
        return random.choice(ailist)[2]
        print "DEBUG: NO ACTION FOUND"


    def Infantry(self, actions_list, enemy_army):
        """Receives actions_list and enemy_army.
        Returns a key to the actions_list
        default commander likes steady-state battles
        but infantry will go for archers, then other infantry"""

        ailist = self.make_ailist(actions_list, enemy_army)
        preferred_list = self.infpreferred #loads default list

        # ENTER TYPE CONDITIONAL ACTIONS as if statements
        for unit in enemy_army.unitlist.values():
            if unit.type == "infantry" and unit.status == "idle":
                preferred_list.insert(0, ['engage', 'infantry'])
            if unit.type == "archers" and len(unit.firing_at) > 0:
                preferred_list.insert(1, ['engage', 'archers'])

        return self.make_choice(ailist, preferred_list)

    def Spearmen(self, actions_list, enemy_army):
        """Receives actions_list and enemy_army.
        Returns a key to the actions_list
        default commander likes steady-state battles
        Spearmen will play defense and phalanx during charges"""

        ailist = self.make_ailist(actions_list, enemy_army)
        preferred_list = self.spearpreferred #loads default list

        # ENTER TYPE CONDITIONAL ACTIONS as if statements
        for unit in enemy_army.unitlist.values():
            if unit.charging == True:
                preferred_list.insert(0, ['phalanx', ''])

        return self.make_choice(ailist, preferred_list)


    def Archers(self, actions_list, enemy_army):
        """Receives actions_list and enemy_army.
        Returns a key to the actions_list
        default commander likes steady-state battles
        Archers will defend, and will fire at enemy units"""

        ailist = self.make_ailist(actions_list, enemy_army)
        preferred_list = self.archpreferred #loads default list

        # ENTER TYPE CONDITIONAL ACTIONS as if statements
        for unit in enemy_army.unitlist.values():
            if unit.phalanx == True:
                preferred_list.insert(0, ['shoot', 'spearmen'])

        return self.make_choice(ailist, preferred_list)

    def Cavalry(self, actions_list, enemy_army):
        """Receives actions_list and enemy_army.
        Returns a key to the actions_list
        default commander likes steady-state battles
        Cavalry will charge archers and will cancel if phalanx"""

        ailist = self.make_ailist(actions_list, enemy_army)
        preferred_list = self.cavpreferred #loads default list

        # ENTER TYPE CONDITIONAL ACTIONS as if statements
        for unit in enemy_army.unitlist.values():
            if unit.phalanx == True:
                preferred_list.insert(0, ['cancel_charge', ''])

        return self.make_choice(ailist, preferred_list)

class ArchersCommander(Commander):
    """Commander for an army with many archers who is typically
    very defensive"""

    def __init__(self):
        super(ArchersCommander, self).__init__()
        self.description = ("Commander for an army with many archers"
                           + "who is typically very defensive")

    def Infantry(self, actions_list, enemy_army):
        raise NotImplemented

    def Spearmen(self, actions_list, enemy_army):
        raise NotImplemented

    def Archers(self, actions_list, enemy_army):
        raise NotImplemented

    def Cavalry(self, actions_list, enemy_army):
        raise NotImplemented #POSSIBLY WOULD INHERIT THIS METHOD


class AmbushCommander(Commander):
    """Used in the campaign"""

    def __init__(self):
        super(AmbushCommander, self).__init__()
        self.infpreferred =  [
                             ['continue_engagement', ''],
                             ['continue_fending', ''],
                             ['continue_defending', ''],
                             ['defend', ''],
                             ['engage', 'archers'],
                             ['engage', 'infantry'],
                             ['engage', 'cavalry'],
                             ]
        self.archpreferred = [
                             ['shoot', 'infantry'],
                             ['shoot', 'archers'],
                             ['shoot', 'cavalry'],
                             ['shoot', 'spearmen'],
                             ['continue_engagement', ''],
                             ['continue_fending', ''],
                             ['defend', ''],
                             ['continue_defending', ''],
                             ['continue_fending', ''],
                             ]

    def Infantry(self, actions_list, enemy_army):
        """Receives actions_list and enemy_army.
        Returns a key to the actions_list
        default commander likes steady-state battles
        but infantry will go for archers, then other infantry"""

        ailist = self.make_ailist(actions_list, enemy_army)
        preferred_list = self.infpreferred #loads default list

        # ENTER TYPE CONDITIONAL ACTIONS as if statements
        for unit in enemy_army.unitlist.values():
            if "Rangers" in enemy_army.unitlist:
                preferred_list.insert(0, ['engage', 'infantry'])
                preferred_list.insert(0, ['engage', 'infantry'])
            if unit.type == "archers" and len(unit.firing_at) > 0:
                preferred_list.insert(0, ['engage', 'archers'])

        return self.make_choice(ailist, preferred_list)

    def Archers(self, actions_list, enemy_army):
        """Receives actions_list and enemy_army.
        Returns a key to the actions_list
        default commander likes steady-state battles
        Archers will defend, and will fire at enemy units"""

        ailist = self.make_ailist(actions_list, enemy_army)
        preferred_list = self.archpreferred #loads default list

        # ENTER TYPE CONDITIONAL ACTIONS as if statements
        for unit in enemy_army.unitlist.values():
            if unit.phalanx == True:
                preferred_list.insert(0, ['shoot', 'spearmen'])

        return self.make_choice(ailist, preferred_list)



### NEED TO SOMEHOW TRANSFER A TARGET LIST WITH AVAILABLE
### ACTIONS TO THE ENGINE AND ADD IT AS A PARAMETER HERE
### CAN BE AN AI STYLE TARGET LIST. KEY IS ACTION type
### KEY = shoot, engage, defend, etc.
### VALUE = target.

### SOLUTION!! CAN PARSE THE DICT KEYS AND ENEMY ARMY UNITLIST
### TO DETERMINE WHAT EACH KEY MEANS AS FAR AS THE AI needs
### CAN USE split() as long as unit names do not contain spaces

### USE AI IF STATEMENTS TO GO DOWN LIST OF PREFERRED ACTIONS
### BEST ACTION LIST
### PRIORITY 1, ENGAGE PHALANX
###     IF ENGAGE IN KEY AND TARGETS[KEY].PHALANX == TRUE:
###     RETURN ENGAGE TARGET
### PRIORITY 2, SHOOT INFANTRY, etc
### PRIORITY 3, CHARGE DEFENDERS, ETC
