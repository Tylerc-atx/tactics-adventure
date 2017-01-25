# tactics-adventure
**v0.10a** of the revolutionary text-based strategy game that simulates battles without using any numbers

---

##CURRENT DEVELOPMENT NOTES

* DEV NOTES: FIX THE GAME BREAKING DEFENSE STALEMATE ISSUE
* Use dictionary.get(key, None) to retrieve things from dictionaries to avoid all the pointless if statements for allyflank and other
similar things. ex47 has a great structure for overworld 'move' commands where the move command and room objects are located in each room

---


### HOW TO MAKE A FULL GAME
(To make just a battle, follow steps 1 and 4)


#### 0. __main__ needs to import modules

   ```python
   import units as units  
   import armies as armies  
   import engine as engine  
   import ai as ai  
   import locations as locations  
   ```

#### 1. HOW TO MAKE A **UNIT AND ARMY** `(Player army in __main__)`

   Make a unit:  
   ```python
   unit_object = units.UnitClass("Name")
   ```

   Unit classes are in `units.py` and are Infantry, Cavalry, Archers, and Spearmen

   Create an Army:  
   ```python
   army_name = armies.Army("Army name")
   ```

   Add units to army:   
   ```python
   army_name.add_unit(unit_object)
   ```

   _ONLY A PLAYER ARMY IS NEEDED TO START CAMPAIGN, ENEMY ARMIES WILL BE MADE BY LOCATIONS_

#### To create an AI Commander (non-player army only)  
   Create a new Commander object  
   ```python
   new_commander = CommanderClass()
   ```

   Register an AI to the army with  
   ```python
   army_name.register_ai(new_commander)
   ```

   Ai will automatically populate army attributes

   (optional) Create a new AI decision priority list:  
   * Make a new commander class in `ai.py`  
     For the unit TYPE you would like to edit the decision-making tree for a type by editing the attribute list.  
   * Edit the preferred_list actions  
     Enter `['action', 'enemytype']` in the order that you want the AI to take actions as they are available.


####2. HOW TO MAKE A LOCATION

   Create a new Location class in `locations.py`.  
   Give it a `enter()` method that returns the string key of the next location

   Unit instances and a battle object can be within the location  
   (See below on how to start a battle)


####3. HOW TO USE THE LOCATION ENGINE AND LOCATIONS

   Create a dictionary map of `{"string keys": location objects}`

   Instantiate LocationEngine in `engine.py` module with `(map, player_army)` as parameters

   Run `locationengine` with `.start("Start_location_key")` to begin the program



####4. HOW TO INSTANTIATE A BATTLE

   Create a new battle object
   ```python
   battle_object = engine.BattleEngine(player_army, enemy_army)
   outcome = battle_object.battle_commence()
   outcome contains the 'who lost' string that location if-statements
   ```

   Can utilize the returned outcome to determine which location to load next

####  (Optional) Add Battle Triggers:  
   Triggers occur after player turn, and enemy turn. They can use the in-built turn_counter or any condition specified that uses the self.ea object (enemy army) or self.pa object (player).

   Triggers are written in a custom `BattleEngine` class that has a modified method `player_triggers` or `enemy_triggers`. See the campaign battle subclasses for examples
