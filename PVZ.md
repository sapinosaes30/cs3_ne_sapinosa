Mini Plants vs. Zombies -Planning Sheet
 
Partners: Sapinosa, Elijah Brylle & Almerol, Maria Beatrice
Section: 9 - Neon
Date: September 30, 2026

COMPUTATIONAL THINKING PLANNING

Decomposition:

Class Definitions: Create two separate classes for plant and zombie with their required items.

Object Creation: create two plant objects with damage and one zombie object.

Turn Loop: Run a loop that steps through actions turn style until a win 

Plant Loop : Loop through living plants to attack the zombie, checking if the zombie's health reaches zero.

Zombie Phase: Move the zombie closer if distance is greater than 0, or attack the current front plant if distance equals 0.

Targeting & Game State: Automatically target the second plant if the first is defeated, and terminate immediately when a side wins.

Display: Print health, distance, and combat log updates every turn.

Pattern Recognition

Attacking Interaction: Reducing a target's health by subtracting damage (health - damage).

Defeat Checks: Checking if health is less than or equal to 0 after every attack to stop action or switch targets.

Movement: Subtracting 1 from the Zombie's distance each turn it is not at distance 0.

Status Updates: Outputting current health levels and zombie distance at the start and end of each turn.

Abstraction

Plant: name, health, damage .

Zombie: name , health , damage, distance.

Algorithm Design

Initialize: Create plant1 (Peashooter, HP: 20, DMG: 10), plant2 (Snow Pea, HP: 15, DMG: 5), and zombie (Buckethead Zombie, HP: 65, DMG: 10, Distance: 2).

Start Main Loop: Run while zombie.health > 0 AND (plant1.health > 0 OR plant2.health > 0).

Plant Attacks:



If plant1 is alive: plant1.attack(zombie).

If zombie is defeated (health <= 0), stop turn and declare Plants Win!

If plant2 is alive: plant2.attack(zombie).

If zombie is defeated (health <= 0), stop turn and declare Plants Win!

Zombie Action:

If zombie.distance > 0: execute zombie.move() (decrease distance by 1).

Else (distance == 0): execute zombie.attack(target).

If both plants reach health <= 0, declare Zombie Wins!

Print Turn Summary: Display current stats before proceeding to the next turn.

End Game: Stop loop and exit program.

TESTING CHECKLIST
The two plants have different damage values
Values Tested / Changes Made: Peashooter DMG: 10, Snow Pea DMG: 5
Result Observed: Confirmed. Peashooter deals 10 HP damage and Snow Pea deals 5 HP damage to the zombie per turn.

Plants defeat the Zombie
Values Tested / Changes Made: Zombie HP set to 20
Result Observed: Zombie reached 0 HP on Turn 2, loop terminated immediately, printed "THE PLANTS WIN!".

Zombie reaches distance 0 and damages a plant
Values Tested / Changes Made: Zombie starting Distance set to 2
Result Observed: Turn 1: dist=1, Turn 2: dist=0, Turn 3: Zombie attacked Peashooter for 10 damage.

Zombie targets second plant after first is defeated
Values Tested / Changes Made: Peashooter HP set to 10, Zombie DMG: 10
Result Observed: Peashooter was defeated on Turn 3 at dist 0. On Turn 4, Zombie automatically attacked Snow Pea.

Game stops when Zombie or both plants are defeated
Values Tested / Changes Made: Tested both Win conditions
Result Observed: Loop terminated instantly when Zombie hit 0 HP or when both plants hit 0 HP without continuing turns.


