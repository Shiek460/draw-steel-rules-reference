# ANGRY BEEHIVE

name: "ANGRY BEEHIVE"
level: 2
roles:
  - HEXER
  - HAZARD
ev: 2 
traits:
  - name: "Description"
    desc: "A beehive full of angry bees that will swarm and attack with little provocation"
stamina: 3
size: 1S
disable: "Cannot be disabled, if the beehive is attacked or destroyed, it will unleash the swarm of bees."
effects: "
  <br />**Trigger**: A creature moves into the hive or an adjacent square without shifting. 
  <br />**Effect:**: The hive is removed and a swarm is placed on the square of the triggering creature. Any creature who begins their turn in the same space as the swarm takes 3 poison damage. At the start of each round, the swarm spreads to a random adjacent square preferring squares that contain a creature. After 3 rounds the swarm dissipates. Upgrades: angry beehive can be upgraded in the following ways. 
  <br /> Concealed Hive (+1 ev): The hive is hidden until the swarm is unleashed. 
  <br /> Killer Bees (+2 ev): The bees are a particularly aggressive and dangerous species. The hive triggers even if a creature shifts adjacent to the hive. The swarm also deals +1D6 poison damage."

# BRAMBLES

name: "BRAMBLES"
level: 1
roles:
  - DEFENDER
  - FORTIFICATION
ancestry:
ev: "1 / 10×10 thicket"
 A thicket of vines with sharp thorns
stamina: 3/square
size: 1 or more squares of difficult terrain
disable: " Only through destruction of each square of brambles."
effects: "
  <br />**Trigger**: A creature moves into a brambles square without shifting. 
  <br />**Effect:**: The triggering creature takes 1 damage per square of brambles they move through. 
  <br />**Upgrade** - Poisonous Thorns (+1 ev): The brambles are poisonous. A creature who takes damage from a square gains [[bleeding]] (save ends)."

# CORROSIVE POOL

name: "CORROSIVE POOL"
level: 2
roles:
  - HEXER
  - HAZARD
ancestry:
ev: "3 / 10×10 pool"
A shallow pool of acid or other corrosive liquid
stamina: 12
size: 1 or more squares of difficult terrain
immunities: 5 all non  -fire or non  -cold damage.
disable: " Only through destruction. "
effects: "
  <br />**Trigger**: A creature begins their turn in or moves through a square of the corrosive pool. 
  <br />**Effect:**: The creature takes 3 acid damage starting their turn in the pool and for each square of the pool they move through. 
ta:
  - name: "Explosive Reaction"
    desc: "
      <br />**Trigger**: The liquid in the pool is highly volatile. When the pool takes any fire damage the pool uses the Explosive Reaction ability and is consumed. 
      <br />**Keywords**: Area
      <br />**Distance**: 3 burst
      <br />**Target**: All creatures and objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 fire damage; M< 1 burning (save ends)
      <br />★ 12–16 6 fire damage; M< 2 burning (save ends)
      <br />✸ 17+ 9 fire damage; M< 3 burning (save ends) 
      <br />**Effect:**: A burning creature or object takes 1D6 fire damage at the start of each of their turns until the effect ends. Creatures or objects on a pool square are also targeted with a double edge. Creatures or objects with acid weakness take extra damage from this attack and burning effect as if it was acid."
traits:
  - name: "Allied Awareness"
    desc: "When you use this object, allies with weapons are equipped with torches. An ally can use a maneuver to throw a torch up to 5 squares and ignite the corrosive pool."

# FROZEN POND

name: "FROZEN POND"
level: 1
roles:
  - HEXER
  - HAZARD
ancestry:
ev: "1 / 10×10 pond" 
A shallow, frozen patch of water. The ice is thick enough that it won’t break but the surface is slick and treacherous to navigate.
stamina: 3/square
size: 1 or more squares of difficult terrain
immunities: 5 all non  -fire damage
disable: " Destroying a square of the frozen pond turns the square into icy water. "
effects: "
      <br />**Trigger**: A creature moves into a pond’s square without shifting. 
      <br />**Effect:**: The triggering creature’s movement ends and they suffer the Slippery Surface ability. Slippery Surface (Triggered) ◆
      <br />**Keywords**: Strike
      <br />**Distance**: Melee
      <br />**Target**: 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 push 1 the direction target was moving
      <br />★ 12–16 push 2 the direction target was moving; A< 1 [[slowed]] (save ends)
      <br />✸ 17+ push 3 the direction the target was moving; A< 2 [[prone]] (save ends) 
      <br />**Effect:**: If the target triggered this ability by being force moved, this ability has an edge and adds the remaining force movement distance to the push value. Forced movement from this ability does not retrigger Frozen Pond. Upgrade - Thin Ice (+1 ev): The ice covering the pond is thin and the water is a little deeper. 
      <br />**Trigger**: A creature enters a square of icy water or becomes [[prone]] on a square of frozen pond with the thin ice upgrade. 
      <br />**Keywords**: Magic, Strike
      <br />**Target**: 1 creature or object
      <br />**Distance**: Melee
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 slide 1
      <br />★ 12–16 1 cold damage; [[slowed]] (EoT)
      <br />✸ 17+ 3 cold damage; [[restrained]] (save ends)"

# LAVA

name: "LAVA"
level: 3
roles:
  - HEXER
  - HAZARD
ancestry:
ev: "4 / 10×10 patch" 
A patch of liquid hot magma welling up from a crack in the ground. Not only dangerous to those who are unfortunate enough to step into it but to anyone who gets close to it.
stamina: 12/square
size: 1 or more squares of difficult terrain
stamina: 12/square
immunities: 5 all non  -cold damage
disable: " Only through destruction of each square of Lava. 
      <br />**Trigger**: A creature begins their turn in a square of lava, adjacent to a square of lava, or moves through at least one square of lava. 
      <br />**Keywords**: Strike
      <br />**Target**: 1 creature or object
      <br />**Distance**: Melee
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 fire damage; M< 1 burning (save ends)
      <br />★ 12–16 9 fire damage; M< 2 burning (save ends)
      <br />✸ 17+ 12 fire damage; M< 3 burning (save ends) 
      <br />**Effect:**: A burning creature or object takes 1D6 fire damage at the start of each of their turns until the effect ends. This ability has a bane if the target is adjacent to a square of lava and not in or moving through lava. Upgrade   - Magma Flow (+4
ev): The lava is flowing! At the beginning of each round of combat add one square of lava adjacent to an existing square of lava

# QUICKSAND

name: "QUICKSAND"
level: 3
roles:
  - HEXER
  - HAZARD
ancestry:
ev: "3 / 10×10 patch" 
A patch of sand saturated by water. It appears to be a normal patch of sand until it is stepped on.
stamina: N/A
size: 1 or more squares of terrain
disable: " May not be disabled. 
      <br />**Trigger**: A creature moves through a square of quicksand or begins their turn in a square of quicksand. 
      <br />**Keywords**: Strike
      <br />**Target**: 1 creature or object
      <br />**Distance**: Melee
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 M< 0 [[slowed]] (save ends)
      <br />★ 12–16 M< 1 [[restrained]] (save ends)
      <br />✸ 17+ M< 2 [[restrained]] (save ends) 
      <br />**Effect:**: This ability has a bane if the target triggered it by shifting into a square of quicksand. A character who started their turn [[restrained]] in a quicksand square begins to suffocate. You can hold your breath for a number of rounds equal to your Might score (minimum 1 round). At the end of each round after that, you take 1d6 damage while holding your breath. Hidden The quicksand begins the encounter hidden.

# TOXIC PLANTS

name: "TOXIC PLANTS"
level: 2
roles:
  - HEXER
  - HAZARD
ancestry:
ev: "2 / 10×10 field" 
A field of colorful mushrooms or lovely flowering plants that releases a cloud of spores when they are disturbed. Breathing in the spores will cause the victim to fall into a deep slumber.
stamina: 3/square
size: 1 or more squares of terrain
disable: " Only through destruction of each square of sleep spores. 
      <br />**Trigger**: A creature begins their turn in a square of toxic plants, or moves into at least one square of toxic plants without shifting. 
      <br />**Keywords**: Magic, Strike
      <br />**Target**: 1 creature
      <br />**Distance**: Melee
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 M< 0 [[dazed]] (save ends)
      <br />★ 12–16 M< 1 [[dazed]] (save ends)
      <br />✸ 17+ M< 2 [[dazed]] (save ends) 
      <br />**Effect:**: The spores begin to put the target into a deep slumber. A target who starts their turn [[dazed]] in a toxic plants square gets sluggish and drowsier and becomes [[prone]] while [[dazed]] and cannot stand until the [[dazed]] effect ends. Upgrades: Sleep spores can upgrade in the following ways. 
      <br /> Poisonous Spores (+2 ev): The spores are also poisonous. Creatures that begin their turn [[dazed]] by this hazard take 1d6 poison damage. 
      <br /> Carnivorous Plants (+2 ev): The plants are carnivorous and will try to slowly digest anyone who was unfortunate enough to lay among them. Anyone who is [[prone]] in a toxic plants square will take 4 acid damage at the beginning of their turn. FIELDWORKS These represent temporary field fortifications that give the defenders an edge in an encounter. ARCHER’S

# STAKES

name: "STAKES"
level: 1
roles:
  - DEFENDER
  - FORTIFICATION
ancestry:
ev: "2" 
A series of sharp stakes have been placed into a palisade to protect defenders against charges and other attacks. The stakes point in one direction, towards the front of the object.
stamina: 3/square
size: 1 or more squares of difficult terrain, generally 4x1 Direction: a specific side of the stakes are defined as the front
disable: " Only through destruction of each square of stakes. 
      <br />**Trigger**: A creature moves into a square of stakes. 
      <br />**Effect:**: The triggering creature takes 2 damage per square of stakes they move through and an additional 3 damage the movement is forced movement. Upgrades: Stakes can upgrade in the following ways. 
      <br /> Poison (+2 ev): The tips of the stakes have poison applied to them. A creature who takes damage from a square will become poisoned (save ends). A poisoned creature will take 1d6 poison damage at the beginning of their turn until the effect ends. 
      <br />**Keywords**: Weapon, Strike
      <br />**Target**: 1 creature or object
      <br />**Distance**: Melee
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 no effect
      <br />★ 12–16 A< 1 [[slowed]] (EoT)
      <br />✸ 17+ A< 2 [[restrained]] (EoT) Allied Awareness Allies of this object ignore the difficult terrain, damaging effects unless force moved, and benefit from cover in a square of archer’s stakes.

# BEAR TRAP

name: "BEAR TRAP"
level: 1
roles:
  - AMBUSHER
  - TRAP
ancestry:
ev: "2" 
Steel jaws attached to the ground by a chain. They will snap shut when stepped on, dealing damage and restraining the target.
stamina: 6
size: 1 square of terrain
disable: " Make a medium Might test when you are adjacent to the bear trap. On a success the trap is jammed and will not trigger when a creature steps on it. Failure with a consequence means you slide 1 into a trap square and trigger it. Success with a consequence means the trap is jammed, but you are [[slowed]] (EoT). 
      <br />**Trigger**: The defenders calibrate the trap for a size: at emplacement that triggers the trap. For example, goblins and kobolds typically calibrate these traps for size: 1M. When a creature of the correct size: or greater moves onto the trap, it triggers. 
      <br />**Keywords**: Weapon, Strike
      <br />**Target**: 1 creature or object
      <br />**Distance**: Melee
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 shift 1 to closest non trap square
      <br />★ 12–16 3 damage; A< 1 [[slowed]] (save ends)
      <br />✸ 17+ 5 damage; A< 2 [[slowed]] (save ends) Upgrades   - Chain (+1EV): The bear trap is attached to the ground by a steel chain. The target becomes [[restrained]] instead of [[slowed]]. Hidden The bear trap begins the encounter hidden.

# FLAMMABLE OIL

name: "FLAMMABLE OIL"
level: 1
roles:
  - AMBUSHER
  - TRAP
ancestry:
ev: "2 / 10x10 patch" 
A patch of flammable oil or pitch on the ground.
stamina: N/A
size: 1 or more squares of terrain
disable: " A character with appropriate knowledge, such as a College of Caustic Alchemy Shadow with the Alchemy skill, can attempt to disable an adjacent patch of flammable oil as a medium Might test. Failure with a consequence means that you slide 1 onto the closest flammable oil square which ignites. Success with a consequence means the patch is disabled but you take 3 fire damage; burning (save ends). A burning creature or object takes 1D6 fire damage at the start of each of their turns until the effect ends. 
      <br />**Trigger**: A creature or object in a square of oil takes fire damage or a creature or object enters a square of burning oil or begins their turn in a square of burning oil. 
      <br />**Effect:**: Each creature and object in a square of oil immediately takes 3 fire damage; burning (save ends). A burning creature or object takes 1D6 fire damage at the start of each of their turns until the effect ends. Upgrade (Concealed; +1
ev): The oil is concealed. Allied Awareness When you use this object, allies with weapons are equipped with torches. An ally can use a maneuver to throw a torch up to 5 squares and ignite the flammable oil. HIDEY  -

# HOLE

name: "HOLE"
level: 1
roles:
  - AMBUSHER
  - TRAP
ancestry:
ev: "1" 
A hidden cavity in a floor, wall, or ceiling of the environment
stamina: N/A
size: 1 square of terrain
disable: " Make a medium Might test when you are adjacent to the hidey  -hole. Sabotage will generally apply. On a success the hidey  -hole collapses and can no longer be used during combat. Failure with a consequence means you are [[restrained]] (EoT). Success with a consequence means the hidey  -hole collapses, but you are [[slowed]] (EoT). 
      <br />**Trigger**: A creature begins the encounter in a square or ends their turn in a square of the hidey  -hole. 
      <br />**Effect:**: The triggering creature can hide as a free triggered action. Upgrade to Network (+1 ev per hidey-hole): The hidey-hole is connected to a tunnel network. A creature familiar with the network can move to any square adjacent to another connected hidey-hole if they have movement available equal to the straight-line distance to that square. Creatures unfamiliar with the network can use a maneuver to make a hard Might test to discover a connected hidey-hole.

# PAVISE SHIELD

name: "PAVISE SHIELD"
level: 1
roles:
  - DEFENDER
  - FORTIFICATION
ancestry:
ev: "1" 
A reinforced metal shield embedded in the terrain that acts as mobile cover and can be repositioned with a lot of effort.
stamina: 9
size: 1M
disable: " As a maneuver, make a hard Might test when you are adjacent to the pavise shield in use by another creature. On success you take control of the shield. On failure with a consequence the creature using the shield makes an opportunity attack against you. 
      <br />**Trigger**: A creature uses a maneuver to grab the pavise. 
      <br />**Effect:**: While a creature has the pavise [[grabbed]] they have cover and take half damage from attacks that trace [[Draw Steel Rules#LINE OF EFFECT|line of effect]] through it. The pavise takes the other half of the damage. Movement: While you have a pavise [[grabbed]] your movement is halved and you move it like a [[grabbed]] creature

# SNARE TRAP

name: "SNARE TRAP"
level: 1
roles:
  - AMBUSHER
  - TRAP
ancestry:
ev: "1" 
A rope snare that will grab a target, leaving them hanging upside down.
stamina: 1
size: 1 square of terrain
disable: " As a maneuver, make a medium Might test when you are adjacent to the snare trap. On a success the trap is jammed and will not trigger when a creature steps on it. Failure with a consequence means you slide 1 into a trap square and trigger it. Success with a consequence means the trap is jammed, but you are [[slowed]] (EoT). 
      <br />**Trigger**: The defenders calibrate the trap for a size: at emplacement that triggers the trap. For example, goblins and kobolds typically calibrate these traps for size: 1M. When a creature of the correct size: or greater moves onto the trap, it triggers. 
      <br />**Keywords**: Weapon, Strike
      <br />**Target**: 1 creature or object
      <br />**Distance**: Melee
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 shift 1 to closest non trap square
      <br />★ 12–16 1 damage; A< 1 [[restrained]] (save ends)
      <br />✸ 17+ 3 damage; A< 2 [[restrained]] (save ends) 
      <br />**Effect:**: A creature [[restrained]] by this ability is vertically pulled 2 and suspended in the air by the snare line until they save. When they save they will fall. Upgrade   - Net trap (+1EV): Upgrade the snare to a net. Increase the stamina to 3 and the size: to 2x2, the Snare attack gains the area keyword, when triggered, it will attack anyone in the trap area. Any creature who makes their save to end the [[restrained]] effect will end it for all affected creatures. Hidden The snare trap begins the encounter hidden.

# SPIKE TRAP

name: "SPIKE TRAP"
level: 2
roles:
  - AMBUSHER
  - TRAP
ancestry:
ev: "3" 
A pit dug out of the terrain, filled with spikes, and camouflaged to avoid detection.
stamina: 6
size: 2x2
disable: " As a maneuver, make a medium Might test when you are adjacent to the spike trap. On a success the trap is jammed and will not trigger when a creature steps on it. Failure with a consequence means you slide 1 into a trap square and trigger it. Success with a consequence means the trap is jammed, but you are [[slowed]] (EoT). 
      <br />**Trigger**: The defenders calibrate the trap for a size: at emplacement that triggers the trap. For example, goblins and kobolds typically calibrate these traps for size: 1M. When a creature of the correct size: or greater moves onto the trap, it triggers. 
      <br />**Keywords**: Weapon, Area Type: Triggered (Free)
      <br />**Distance**: Melee
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage; shift 1 to the closest open non trap square
      <br />★ 12–16 5 damage; A< 0 [[prone]]
      <br />✸ 17+ 8 damage; A< 1 [[prone]], [[restrained]] (EoT) 
      <br />**Effect:**: Once the trap has been triggered, any creature that moves into a trap square ends their movement and triggers the Spike Trap ability. The open pit is 2 square deep. Hidden The spike trap begins the encounter hidden. MECHANISMS These represent more intricate construction projects that can impact the battlefield. Mechanisms need to be linked to another triggering mechanism for activation. Some creatures have the ability to trigger mechanisms on their turn.

# COLUMN OF BLADES

name: "COLUMN OF BLADES"
level: 3
roles:
  - DEFENDER
  - FORTIFICATION
ancestry:
ev: "3" 
A spinning wooden column affixed with sharp blades
stamina: 5
size: 1L
disable: " Direct damage only. 
      <br />**Trigger**: A creature enters a square adjacent to the column of blades. 
      <br />**Keywords**: Weapon, Strike
      <br />**Target**: 1 creature or object
      <br />**Distance**: Melee
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 6 damage; M< 2 [[bleeding]] (save ends)
      <br />✸ 17+ 9 damage; M< 3 [[bleeding]] (save ends) Upgrades: Column of Blades can be upgraded in the following ways. 
      <br /> Stone Column (+1EV): Upgrade the column to stone. Increase the stamina to 8. 
      <br /> Metal Column (+1EV): Upgrade the column to metal. Increase the stamina to 11. 
      <br /> Concealed (+1 ev): The column is motionless and the blades are concealed inside of the column until it is triggered at which point it becomes revealed. 
      <br />**Keywords**: Weapon, Strike
      <br />**Target**: 1 creature or object
      <br />**Distance**: Melee
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 8 damage; M< 2 daze (save ends)
      <br />✸ 17+ 11 damage; M< 3 daze (save ends) Allied Awareness Allies of this object can shift through triggering squares and avoid the fortification’s effects. A creature observing this can make a Hard Might test and try to shift through triggering squares. On a success they avoid the fortification’s effects. On a failure they suffer the ability. On a failure with a consequence they suffer the ability with an edge.

# DART TRAP

name: "DART TRAP"
level: 1
roles:
  - AMBUSHER
  - TRAP
ancestry:
ev: "1" 
A concealed short ranged dart thrower
stamina: 3
size: 1S, can be placed in a wall Direction: the dart trap has a direction its ability faces
disable: " Make a medium Might test when you are adjacent to the object. On a success the object is jammed and will not trigger when a creature steps on it. Failure with a consequence means you slide 1 into a square the object can target and trigger it. Success with a consequence means the object is jammed, but you are [[slowed]] (EoT). 
      <br />**Trigger**: A creature enters a square in a 1x5 line the dart trap is facing. 
      <br />**Keywords**: Weapon, Ranged, Strike
      <br />**Target**: 1 creature or object
      <br />**Distance**: Ranged 5
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage
      <br />★ 12–16 2 damage
      <br />✸ 17+ 3 damage Upgrades: Dart Trap can be upgraded in the following ways. 
      <br /> Poison Darts (+2EV): The darts are poisoned. A creature who takes damage from a dart will become poisoned (save ends). A poisoned creature will take 1d6 poison damage at the beginning of their turn until the effect ends. 
      <br /> Large Darts (+1EV): The darts are slightly larger and add push 1 / push 2/ push 3 to the power roll. 
      <br /> Gatling Darts (+4 ev): The dart trap is equipped with multiple barrels capable of launching darts at a high rate of fire. The Dart ability becomes Area 5x1 within 1 line instead of a Strike and does +1d6 damage. Hidden The dart trap begins the encounter hidden.

# HIDDEN PORTCULLIS

name: "HIDDEN PORTCULLIS"
level: 3
roles:
  - AMBUSHER
  - TRAP
ancestry:
ev: "4" 
A portcullis is hidden in the ceiling of a passage or chokepoint that drops when activated.
stamina: 9/square
size: 2x1 up to 4x1 squares
disable: " Make a medium Might test when you are adjacent to the object. On a success the object is jammed and will not trigger when a creature steps on it. Failure with a consequence means you slide 1 into an object square and trigger it. Success with a consequence means the object is jammed, but you are [[slowed]] (EoT). 
      <br />**Trigger**: A creature is standing on a portcullis square when it is activated by another mechanism, such as a pressure plate. 
      <br />**Keywords**: Weapon, Area
      <br />**Target**: All creatures and objects
      <br />**Distance**: Squares under the mechanism
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage; slide 1 (ignores stability)
      <br />★ 12–16 7 damage; [[restrained]] (EoT)
      <br />✸ 17+ 10 damage; [[restrained]] (save ends) 
      <br />**Effect:**: The portcullis blocks movement through its squares. There is a 50% chance that a slid target winds up on either side of the portcullis. When the [[restrained]] condition ends for a creature, the creature shifts 1 out of the hidden portcullis squares. Hidden The hidden portcullis begins the encounter hidden.

# PILLAR

name: "PILLAR"
level: 2
roles:
  - HEXER
  - HAZARD
ancestry:
ev: "3"
A stone pillar that can be toppled with the right amount of damage or from a well-engineered trigger
stamina: 6
size: 1 square breakaway
disable: " Direct damage only. 
      <br />**Trigger**: The pillar is destroyed or a linked trigger is activated 
      <br />**Effect:**: The pillar topples in the direction opposite of the creature that destroyed it or, if triggered, in a direction defined when the pillar was placed in the encounter. The Toppling Pillar ability activates in the direction the pillar toppled. Toppling Pillar (Triggered) 2D10+2
      <br />**Keywords**: Area
      <br />**Target**: All creatures and objects.
      <br />**Distance**: 4 x 1 line within 1
      <br />`dice: 2d10 +
      <br />✦ ≤11 4 damage
      <br />★ 12–16 6 damage; M< 1 [[restrained]] (EoT)
      <br />✸ 17+ 9 damage; M< 2 [[restrained]] (save ends) 
      <br />**Effect:**: The squares affected become difficult terrain Upgrades: Pillars can be upgraded in the following ways. 
      <br /> Sturdier Materials (+1EV): Upgrade the pillar to metal. Increase the stamina to 9 and deal 1d6 extra damage when toppling on a creature. 
      <br /> Falling Wall (+0EV): Multiple pillars can be bought together to represent a larger toppling object, like a wall. All pillars need to be destroyed before it falls if this is the case, and toppling direction is predefined when the objects are placed.

# PRESSURE PLATE

name: "PRESSURE PLATE"
level: 1
roles:
  - SUPPORT
  - TRIGGER
ancestry:
ev: "2" 
This mechanism acts as a trigger for another linked mechanism. It begins the encounter concealed from enemies.
stamina: N/A
size: 1x1 up to 4x4 squares of terrain Link A pressure plate is linked to another mechanism that it activates when triggered
disable: " Make a medium Might test when you are adjacent to the object. On a success the object is jammed and will not trigger when a creature steps on it. Failure with a consequence means you slide 1 into an object square and trigger it. Success with a consequence means the object is jammed, but you are [[slowed]] (EoT). 
      <br />**Effect:**: The pressure plate is set for a specific triggering size:, usually 1S or 1M. When a creature of that size: or larger moves onto a pressure plate square, the linked mechanism activates. Upgrades: Tripwires can be upgraded in the following ways. 
      <br /> Tripwire (  -1EV): The pressure plate is a tripwire, which only triggers once. It is still concealed, but can be discovered with an easy test. Hidden The pressure plate begins the encounter hidden.

# PULLEY

name: "PULLEY"
level: 1
roles:
  - SUPPORT
  - TRIGGER
ancestry:
ev: "1" 
This is a simple rope and pulley system that may be used to quickly ascend to the top of another structure such as a wall, scaffolding, or tower.
stamina: 1
size: 1S, attached to a structure of some sort such as a wall, tower or scaffolding
disable: " Make a medium Might test when you are adjacent to the object. On a success the object is jammed and will not trigger when a creature tries to activate it. Failure with a consequence means you slide 1 into an object square and trigger it. Success with a consequence means the object is jammed, but you are [[slowed]] (EoT). 
      <br />**Trigger**: A creature adjacent to the pulley uses a maneuver to cut the rope 
      <br />**Effect:**: The triggering creature is sent to the top of the structure the pulley is attached to. Once used in this manner the pulley is disabled and may not be used again. Upgrade   - Chain (+1EV): Instead of a rope and pulley the system uses a chain. The pulley is not disabled after use. Cimbable A creature adjacent to the pulley may make a climb test and use it to climb to the top of the structure it’s attached to.

# RAM

name: "RAM"
level: 2
roles:
  - AMBUSHER
  - TRAP
ancestry:
ev: "3" 
A heavy wooden ram that drops or swings into the encounter area. Multiple rams can be bought together to represent larger mechanisms, such as a stack of tumbling logs.
stamina: 3/square
size: Up to 4 squares (2x2, 1x3, 1x4) breakaway Direction: The ram has a defined facing it moves into
disable: " Make a medium Might test when you are adjacent to the object. Sabotage will generally apply. On a success the object is jammed and will not trigger when a creature steps on it. Failure with a consequence means you slide 1 into an object square and trigger it. Success with a consequence means the object is jammed, but you are [[slowed]] (EoT). 
      <br />**Trigger**: Activated by a linked mechanism. 
      <br />**Keywords**: Weapon, Area
      <br />**Target**: All creatures and objects
      <br />**Distance**: Squares the ram moves into
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage; slide 1 (ignores stability)
      <br />★ 12–16 6 damage; push 3
      <br />✸ 17+ 9 damage; push 5 
      <br />**Effect:**: There is a 50% chance that a slid target winds up on either side of the ram. Upgrades: Rams can be upgraded in the following ways. 
      <br /> Stone (+1ev): Increase the stamina per square to 6. Do an extra 1d3 damage. 
      <br /> Metal (+2ev): Increase the stamina per square to 9. Do an extra 1d6 damage. 
      <br /> Chompers (+1ev): The ram can be upgraded to be a repeating mechanism. The ram re-triggers at the beginning of every round. 
      <br /> Rapid Chompers (+3ev): The ram can be upgraded to a rapid repeating mechanism. The ram re-triggers at the beginning of every turn. 
      <br /> Ceiling (+1ev): The ram can be mounted in the ceiling and ram the squares below it when it is triggered. Creatures are pushed away by the ram’s squares. This can be used to create chain reactions with other terrain objects that trigger when creatures are moved into them. For example, when a ceiling ram drops onto a creature in a spike trap the spike trap ability is triggered again. Hidden The ram plate begins the encounter hidden.

# SWITCH

name: "SWITCH"
level: 1
roles:
  - SUPPORT
  - TRIGGER
ancestry:
ev: "1" 
This mechanism acts as a trigger for another linked mechanism. You can place this mechanism on a floor or wall.
stamina: 3 Squares: 1T built into a floor or a wall Link A switch is linked to another mechanism that it activates when triggered
disable: " Make a medium Might test when you are adjacent to the object. Sabotage will generally apply. On a success the object is jammed and will not trigger when a creature steps on it. Failure with a consequence means you slide 1 into an object square and trigger it. Success with a consequence means the object is jammed, but you are [[slowed]] (EoT). 
      <br />**Trigger**: A creature uses a maneuver while adjacent to the switch or the switch is destroyed. 
      <br />**Effect:**: The linked mechanism is activated. Upgrade   - Hidden (+1 ev): The switch is hidden, requiring a hard Might test to find before it can be attacked or used.

# ARROW LAUNCHER

name: "ARROW LAUNCHER"
level: 2
roles:
  - ARTILLERY
  - SIEGE
  - ENGINE
ancestry:
ev: "8" 
A small wooden cart that uses rockets to launch up to 100 arrows at one time. While it is inaccurate it makes up for it by spreading a large volume of projectiles over a wide area.
size: 1L
stamina: 30
disable: " Make a medium Might test when you are adjacent to the object. On a success the object is jammed and will not trigger when a creature steps on it. Failure with a consequence means the object attacks you, if it is loaded. Success with a consequence means the object is disabled, but you are [[slowed]] (EoT). Arrow Storm (Adjacent Creature Action) ◆ 2D10
      <br />**Keywords**: Area, Weapon
      <br />**Target**: All creatures and objects
      <br />**Distance**: 5 cube within 20
      <br />`dice: 2d10 +
      <br />✦ ≤11 5 damage
      <br />★ 12–16 8 damage
      <br />✸ 17+ 11 damage 
      <br />**Effect:**: Arrow Storm cannot be used again until the object is reloaded. Reload (Adjacent Creature Action)
      <br />**Keywords**:   -  -
      <br />**Target**: this object
      <br />**Distance**: Melee 1 
      <br />**Effect:**: The object is reloaded, allowing Arrow Storm to be used again. Spot (Adjacent Creature Action)
      <br />**Keywords**:   -  -
      <br />**Target**: this object
      <br />**Distance**: Melee 1 
      <br />**Effect:**: The next use of Arrow Storm has an edge and +10 range Move (Adjacent Creature Action)
      <br />**Keywords**:   -  -
      <br />**Target**: this object
      <br />**Distance**: Melee 1 
      <br />**Effect:**: This object moves 3 and the adjacent creature using their action moves 3 as long as they end their move adjacent to this object. Upgrades: An arrow launcher can be upgraded in the following ways: 
      <br /> Flaming arrows (+1ev): The arrows now deal fire damage and will ignite flammable objects in the area of effect. 
      <br /> Screamers (+3ev): The rockets are designed to make a distinct high pitched screaming noise as they are fired and descend onto their targets. The arrow launcher ability has the Screamers ability instead of Arrow Storm. Screamers (Adjacent Creature Action) 2D10
      <br />**Keywords**: Area, Weapon
      <br />**Target**: All creatures and objects
      <br />**Distance**: 5 cube within 20
      <br />`dice: 2d10 +
      <br />✦ ≤11 5 damage; R< 0 [[dazed]] (save ends)
      <br />★ 12–16 8 damage; R< 1 [[dazed]] (save ends)
      <br />✸ 17+ 11 damage; R< 1 [[frightened]] (save ends) 
      <br />**Effect:**: Screamers cannot be uses again until the object is reloaded.

# BOILING OIL CAULDRON

name: "BOILING OIL CAULDRON"
level: 3
roles:
  - DEFENDER
  - FORTIFICATION
ancestry:
ev: "10" 
A large cauldron of boiling oil that can be poured onto an enemy. Ideally placed above an area to gain an edge on attack rolls.
stamina: 50
size: 1L
      <br />**Keywords**: Area, Weapon
      <br />**Target**: All creatures and objects
      <br />**Distance**: 3 cube within 1
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 fire damage; M< 1 burning (save ends)
      <br />★ 12–16 9 fire damage; M< 2 burning (save ends)
      <br />✸ 17+ 12 fire damage; M< 3 burning (save ends) 
      <br />**Effect:**: A burning creature or object takes 1D6 fire damage at the start of each of their turns until the effect ends. Boiling Oil cannot be used again until the object is reloaded Reload (Adjacent Creature Action)
      <br />**Keywords**:   -  -
      <br />**Target**: this object
      <br />**Distance**: Melee 1 
      <br />**Effect:**: The object is reloaded, allowing the Boiling Oil action to be used again.

# CATAPULT

name: "CATAPULT"
level: 3
roles:
  - ARTILLERY
  - SIEGE
  - ENGINE
ancestry:
ev: "10" 
A large weapon that throws a projectile in an arc. A catapult can attack without line of sight as long as an ally has line of sight to the target square and there is a path above the target.
stamina: 50
size: 2
      <br />**Keywords**: Area, Weapon
      <br />**Target**: All creatures and objects
      <br />**Distance**: 3 cube within 20
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 9 damage; A< 0 push 1
      <br />✸ 17+ 12 damage; A< 1 push 2 
      <br />**Effect:**: Arcing Shot cannot be used again until the object is reloaded. Reload (Adjacent Creature Action)
      <br />**Keywords**:   -  -
      <br />**Target**: this object
      <br />**Distance**: Melee 1 
      <br />**Effect:**: The object is reloaded, allowing Arcing Shot to be used again. Spot (Adjacent Creature Action)
      <br />**Keywords**:   -  -
      <br />**Target**: this object
      <br />**Distance**: Melee 1 
      <br />**Effect:**: The next use of Arcing Shot has an edge and +10 range Move (Adjacent Creature Action)
      <br />**Keywords**:   -  -
      <br />**Target**: this object
      <br />**Distance**: Melee 1 
      <br />**Effect:**: This object moves 2 and the adjacent creature using their action moves 2 as long as they end their move adjacent to this object. Upgrades: A catapult can be upgraded in the following ways: 
      <br /> Fire Me Boy! (+2ev): The side fielding the catapult has trained their forces to safely use the catapult to deliver an assault across the battlefield. Instead of attacking, a creature can use the catapult to vertical push 10 any ally within 2 squares of the catapult of size: 1L or less. If the tossed ally lands in an empty square, they take no damage. 
      <br /> I Love it Here, it’s so Flammable (+2ev): The arcing shot does fire damage. Any squares targeted by the arcing shot are burning until the end of the encounter. When a creature begins their turn in a square or first enters a square that’s burning on a turn, they take 2 fire damage.

# EXPLODING MILL WHEEL

name: "EXPLODING MILL WHEEL"
level: 3
roles:
  - ARTILLERY
  - SIEGE
  - ENGINE
ancestry:
ev: "10" 
A massive wooden wheel loaded with explosives. During sieges it is rolled towards fortifications where it will explode, causing massive damage.
stamina: 25
size: 2
disable: " Before the wheel is rolling you may make a medium Might test when you are adjacent to the object. On a success the object is jammed and will not trigger when a creature steps on it. Failure with a consequence means the object attacks you, if it is loaded. Success with a consequence means the object is disabled, but you are [[slowed]] (EoT). Once the wheel is rolling, the only thing that can disable it is it exploding due to hitting a size: 3 or larger object, being triggered with the spot action, or being destroyed by damage. Roll the Wheel (Adjacent Creature Action)
      <br />**Keywords**:   -  -
      <br />**Target**: this object
      <br />**Distance**: Melee 1 
      <br />**Keywords**: Area, Weapon
      <br />**Target**: All creatures and objects
      <br />**Distance**: Self
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; push 1
      <br />★ 12–16 9 damage; push 2
      <br />✸ 17+ 12 damage; push 3 
      <br />**Effect:**: Make one power roll against every square the exploding mill wheel enters. Massive Explosion (Free Triggered Action) 2D10+2
      <br />**Keywords**: Area, Ranged
      <br />**Target**: All creatures and objects
      <br />**Distance**: 5 burst 
      <br />**Trigger**: The exploding mill wheel attempts to move into an object or creature that is size: 3 or larger or is reduced to 0 stamina
      <br />`dice: 2d10 +
      <br />✦ ≤11 5 damage; push 1; M< 0 burning (save ends)
      <br />★ 12–16 9 damage; push 2 M< 1 burning (save ends)
      <br />✸ 17+ 12 damage; push 3 M< 2 burning (save ends) 
      <br />**Effect:**: The exploding mill wheel is destroyed Upgrade - Piloted (+4 ev): The wheel has been fitted with a control mechanism and a pilot’s seat for an ally of size: 1M or smaller. This allows the wheel to be turned in any direction while it is moving. At any time during its movement, the pilot may take an action to eject out of the wheel landing in an adjacent space while the wheel continues moving in a straight line. Piloting the wheel takes knowledge and some skill but a player could figure it out and pilot it with a hard reason test. On a success the character may pilot the wheel. Failure with a consequence means the wheel immediately explodes. Success with a reward means that the player has even figured out how to disarm the explosives and may disable that aspect of the wheel.

# FIELD BALLISTA

name: "FIELD BALLISTA"
level: 2
roles:
  - SIEGE
  - ENGINE,
  - ARTILLERY
ancestry:
ev: "8" 
A large weapon that uses a mechanism similar to a crossbow. Attacking with a ballista releases a large bolt.
stamina: 40
size: 2
      <br />**Keywords**: Strike, Ranged, Weapon
      <br />**Target**: 1 creature or object
      <br />**Distance**: Ranged 20
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 8 damage; M< 1 push 1
      <br />✸ 17+ 11 damage; M< 2 push 2 
      <br />**Effect:**: Release Bolt cannot be used again until the object is reloaded. Reload (Adjacent Creature Action)
      <br />**Keywords**:   -  -
      <br />**Target**: this object
      <br />**Distance**: Melee 1 
      <br />**Effect:**: The object is reloaded, allowing Release Bolt or Chain Bolt to be used again. Spot (Adjacent Creature Action)
      <br />**Keywords**:   -  -
      <br />**Target**: this object
      <br />**Distance**: Melee 1 
      <br />**Effect:**: The next use of Release Bolt or Chain Bolt has an edge and +10 range Move (Adjacent Creature Action)
      <br />**Keywords**:   -  -
      <br />**Target**: this object
      <br />**Distance**: Melee 1 
      <br />**Effect:**: This object moves 3 and the adjacent creature using their action moves 3 as long as they end their move adjacent to this object. Upgrades: A field ballista can be upgraded in the following ways. 
      <br /> Penetrating Bolt (+2ev): The field ballista is outfitted with penetrating bolts. The ballista targets 2 additional creatures or objects in a straight line behind the initial target. This affects any creatures, including allies, and must affect the first two creatures or objects in range. 
      <br />**Keywords**: Strike, Ranged, Weapon
      <br />**Target**: 1 creature or object
      <br />**Distance**: Ranged 20
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 7 damage; M< 1 [[slowed]] (save ends)
      <br />✸ 17+ 10 damage; M< 2 [[slowed]] (save ends) 
      <br />**Keywords**: Strike, Ranged, Weapon
      <br />**Target**: 1 creature [[slowed]] by the field ballista
      <br />**Distance**: 20
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 pull 1
      <br />★ 12–16 pull 3
      <br />✸ 17+ pull 5 
      <br />**Effect:**: This forced movement will trigger opportunity attacks.

# IRON DRAGON

name: "IRON DRAGON"
level: 4
roles:
  - ARTILLERY
  - SIEGE
  - ENGINE
ancestry:
ev: "12" 
A large metal device that uses a bellows system and liquid fuel to shoot out a gout of flame
stamina: 60
size: 2
disable: " Make a medium Might test when you are adjacent to the object. Sabotage will generally apply. On a success the object is jammed and will not trigger when a creature steps on it. Failure with a consequence means the object attacks you, if it is loaded. Success with a consequence means the object is disabled, but you are [[slowed]] (EoT). Gout of Flame
      <br />**Keywords**: Area, Ranged
      <br />**Target**: All creatures and objects
      <br />**Distance**: 8x2 within 1
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage; A< 0 burning (save ends)
      <br />★ 12–16 10 damage; A< 1 burning (save ends)
      <br />✸ 17+ 13 damage; A< 2 burning (save ends) 
      <br />**Effect:**: A burning creature or object takes 1D6 fire damage at the start of each of their turns until the effect ends. Gout of Flame cannot be used until the object is reloaded Reload (Adjacent Creature Action)
      <br />**Keywords**:   -  -
      <br />**Target**: this object
      <br />**Distance**: Melee 1 
      <br />**Effect:**: The object is reloaded, allowing Gout of Glame to be used again. Spot (Adjacent Creature Action)
      <br />**Keywords**:   -  -
      <br />**Target**: this object
      <br />**Distance**: Melee 1 
      <br />**Effect:**: The next use of Gout of Glame has an edge and +10 range Move (Adjacent Creature Action)
      <br />**Keywords**:   -  -
      <br />**Target**: this object
      <br />**Distance**: Melee 1 
      <br />**Effect:**: This object moves 23 and the adjacent creature using their action moves 2 as long as they end their move adjacent to this object.

# WATCHTOWER

name: "WATCHTOWER"
level: 2
roles:
  - DEFENDER
  - FORTIFICATION
ancestry:
ev: "8" 
A sturdy wooden tower that provides cover and high ground. The tower is accessed by a set of ladders or stairs leading up to the top.
stamina: 50
size: 3
disable: " Direct damage only. High Ground: The watchtower is accessible by ladders and acts as high ground and cover for creatures inside of it Upgrades: A watchtower can be upgraded in the following ways: 
      <br /> Ballista Emplacement (+12ev): The watchtower is equipped with a ballista emplacement. The Ballista emplacement follows all rules for the Field Ballista. 
      <br /> Boiling Oil Cauldron (+17+ev): The watchtower is equipped with a boiling oil cauldron which follows all the normal rules for the boiling oil cauldron. 
      <br /> Spyglass (+2ev): A creature in the watchtower may use a spot action to make a search for hidden creatures gaining an edge on the roll and increasing the range to 15. 
      <br /> Stone Tower (+2ev): The watchtower is reinforced with stone. Increase stamina to 50. 
      <br /> Iron Tower (+4ev): The watchtower is reinforced with stone and iron. Increase stamina to 100.

# THE BLACK OBELISK

name: "THE BLACK OBELISK"
level: 3
roles:
  - RELIC,
  - CONTROLLER
ancestry:
ev: "20" 
A foreboding black obelisk that knows more about you than you would like.
stamina: 100
size: 2
disable: " Make a hard Might test when you are adjacent to the object. Magic will generally apply. On a success the object is disabled for the rest of the encounter. Failure with a consequence means you immediately trigger Your Fears Become Manifest with a bane. Success with a consequence means the object is disabled, but you are [[slowed]] (save ends). 
      <br />**Trigger**: A round begins 
      <br />**Keywords**: Area, Magic, Object
      <br />**Target**: All enemies
      <br />**Distance**: Burst 10
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 P< 1 [[slowed]] (EoT)
      <br />★ 12–16 P< 2 [[slowed]] (EoT), [[weakened]] (EoT)
      <br />✸ 17+ P< 3 [[slowed]] (EoT), [[weakened]] (EoT), [[frightened]] (EoT) 
      <br />**Effect:**: The target is pushed 2.

# THE CHRONAL HYPERCUBE

name: "THE CHRONAL HYPERCUBE"
level: 3
roles:
  - RELIC,
  - CONTROLLER
ancestry:
ev: "20" 
A shape that is impossible for most creatures to understand.
stamina: 80
size: 1M
disable: " Only a creature trained in Psionics can attempt to disable the Chronal Hypercube. Make a hard Might test when within 10 of the Hypercube. On a success, the Hypercube teleports adjacent to your square at the start of the next round and becomes your ally. On a failure with a consequence you take 1d6 psychic damage. Dimensional Flicker At the start of the round, roll 1d10. On a 7+ the Hypercube teleports to a square of your choice within 10 and is hidden. A creature with the Psionics skill can use those skills to attempt to find it. Chronal Superhighway Allies within 10 squares of the Hypercube can teleport in place of any normal movement they take, using the same distance as the normal movement. They have an edge on any attacks they make after teleporting.

# THE THRONE OF A’AN

name: "THE THRONE OF A’AN"
level: 4
roles:
  - RELIC,
  - CONTROLLER
ancestry:
ev: "24" 
A’An was the Sun God of the Antical Protectorate in what was now Vanigar. She was slain along with the other Nine Star Gods, ending the Age of Suns, plunging the region into eternal winter.
stamina: 140
size: 2
disable: " The Throne can only be disabled by attuning to it, casting out the current occupant, and sitting in it, becoming the new Hierophant of A’An. The Hierophant can make a hard Might test with a bane to disable the Throne. Failure with a consequence triggers Nova. Light of the Northern Sun In the Age of Suns there was no darkness and no night. Even among the many suns of that time, the light of A’An was the brightest. The Throne manifests the Sun powers of A’An, even when no one is seated in it. The following effects occur within 10 squares of the Throne: 
      <br /> The Throne casts a bright light, preventing any form of concealment or darkness from existing or manifesting, even from a god. 
      <br /> No creature can hide. 
      <br /> Any creature with cold immunity gains fire weakness 10. 
      <br /> Any creature that uses an ability that does cold damage takes 11 fire damage. Sitting on the Throne “Awaken me! The Sun must shine again!” Only a creature attuned to the throne can sit in it. A creature can attune to the throne as an action, if adjacent to the Throne, by succeeding at a hard Might test. Failing this test with a consequence inflicts 11 fire damage. A creature seated in the throne becomes the Hierophant of A’An and gains the following benefits: 
      <br /> The Hierophant, and their allies within 10 squares, gain fire immunity 10 
      <br /> The Hierophant, and their allies within 10 squares, can choose to do fire damage instead of their normal damage 
      <br /> You gain +5 stability and all attacks against you suffer a bane, unless the attacker is also attuned to the Throne. 
      <br />**Keywords**: Magic, Strike, Ranged
      <br />**Target**: 1 creature or object
      <br />**Distance**: Ranged 20
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 fire damage
      <br />★ 12–16 11 fire damage
      <br />✸ 17+ 14 fire damage 
      <br />**Effect:**: The target gains fire weakness 10 until the beginning of the Hierophant’s next turn. Solar Accretion (Free Triggered) “To return the Sun must feed on life and fire!”
      <br />**Keywords**: Magic
      <br />**Target**: 1 creature
      <br />**Distance**: Ranged 10 
      <br />**Trigger**: A target within distance is [[winded]] or reduced to 0 stamina by fire damage. 
      <br />**Effect:**: If the Hierophant is a hero, they gain 3 heroic resources. If Hierophant is a villain, the Director gains 3 malice. Nova (Free Triggered) “No! I will return!”
      <br />**Keywords**: Magic
      <br />**Target**: All creatures and objects
      <br />**Distance**: 10 Burst 
      <br />**Trigger**: The Throne is destroyed or the Hierophant fails with a consequence when disabling it. 
      <br />**Effect:**: Targets take 14 fire damage. The Hierophant gains the Incubator of A’An complication. If there is no Hierophant, a creature within 10 squares of the Throne, and chosen by the Director, gains the Incubator of A’An complication.
INCUBATOR OF A’AN A shard of the formerly dead Sun God A’An is incubating inside of your body, guiding you so she can be resurrected to her true glory by earning 100 followers. Benefit: You gain all the Sun domain abilities as if you were a conduit of your"
level:. You gain fire immunity 5. If you succeed in resurrecting A’An you will become a Saint of A’An. Drawback: You gain cold weakness 5. When a respite ends, and you have not recruited a new follower of A’An, make a hard Might test. On a failure you lose a Recovery. On a failure with a consequence A’An possesses your body until your next respite. You now must roleplay A’An trapped in your form, prioritizing earning new followers.

# PSIONIC SHARD

name: "PSIONIC SHARD"
level: 5
roles:
  - DEFENDER
  - FORTIFICATION
ancestry:
ev: "7" 
A massive crystal that hums and makes the air feel thick.
stamina: 40
size: 2
disable: " Direct damage only. 
      <br />**Trigger**: The shard is destroyed 
      <br />**Effect:**: The shard releases a shockwave that briefly tightens the barrier around each creature affected by Psionic Barrier, inflicting [[dazed]] (EoT). Psionic Barrier While at least one psionic shard is intact, the damage dealt to each ally creature is halved.

# HOLY IDOL

name: "HOLY IDOL"
level: 5
roles:
  - SUPPORT
  - RELIC
ancestry:
ev: "7" 
An empowering monument to the higher power that enables the villain’s machinations.
stamina: 35
size: 2
disable: " Direct damage only. Empowered Will At the start of each round while the holy idol is intact, the Director gains a d6 that lasts until the end of the round. When an ally creature deals or takes damage, the Director can roll the d6 to increase the damage the creature deals or reduce the damage the creature takes by an amount equal to the result (to a minimum of 2). Only one d6 can be applied to any one instance of damage.

# TREE OF MIGHT

name: "TREE OF MIGHT"
level: 5
roles:
  - HEXER
  - HAZARD
ancestry:
ev: "14" 
A gnarled tree with unearthed roots that writhe and curl.
stamina: 60
size: 3
immunities: 5 all non  -fire or corruption damage
disable: " Direct damage only. Tree’s Nourishment At the start of each round while at least one tree of might is intact, each enemy touching the ground takes M< 0 10 corruption damage and the tree of might grows a fruit. The potency increases by 1 each subsequent round. Mighty Fruit Once per round, an adjacent creature can take some fruit from the tree of might and eat it as a free action. The creature gains 10 temporary stamina and has their Might score increased by 1 (to a maximum of 6) until the end of the encounter.
