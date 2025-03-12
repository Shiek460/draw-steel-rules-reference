# ANIMAL

name: "ANIMAL"
level: 1
roles:
  - TROOP
  - HARRIER
ancestry:
  - Animal
ev: 12
stamina: 60
speed: 6
size: 1M /
stability: 0
free_strike: 4
characteristics:
  - +0
  - +2
  - -2
  - +1
  - -2
actions:
  - name: "Natural Weapon"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 9 damage
      <br />✸ 17+ 12 damage 
      <br />**Effect:** The animal can shift 2 between striking the first and second target."
maneuvers:
  - name: "Rush"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The animal moves up to their speed."
traits:
  - name: "Nature Calls"
    desc: 
      "The animal ignores 1 bane on their abilities while in an encounter outside or in a natural environment."

# BIG ANIMAL A

name: "BIG ANIMAL A"
level: 1
roles:
  - TROOP
  - MOUNT
ancestry:
  - Animal
ev: 12
stamina: 60
speed: 6
size: 2 /
stability: 1
free_strike: 4
characteristics:
  - +1
  - +2
  - -2
  - +1
  - -2
actions:
  - name: "Natural Weapon"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 9 damage; A< 1 3 damage
      <br />✸ 17+ 12 damage; A< 2 3 damage Toss (Maneuver)
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object 
      <br />**Effect:** Vertical slide 3. If the target is an ally, they can make a free strike and then fall without taking damage."
ta:
  - name: "Juke"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The animal is targeted by an area ability. 
      <br />**Effect:** The animal shifts 2 before the ability activates."
traits:
  - name: "Nature Calls"
    desc: "The beast ignores 1 bane on their abilities while in an encounter outside or in a natural environment."


# BIG ANIMAL B

name: "BIG ANIMAL B"
level: 2
roles:
  - TROOP
  - MOUNT
ancestry:
  - Animal
ev: 16
stamina: 80
speed: 6
size: 3 /
stability: 3
free_strike: 5
characteristics:
  - +2
  - +1
  - -1
  - +1
  - +0
actions:
  - name: "Natural Weapon"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 10 damage; push 1
      <br />✸ 17+ 13 damage; push 2 Trundle (Maneuver)
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The beast moves up to their speed. The beast can make a free strike on each creature that makes an opportunity attack against them during this movement."
ta:
  - name: "Animal Rally"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** An ally within [[Draw Steel Rules#LINE OF EFFECT|line of effect]] is knocked [[prone]]. 
      <br />**Effect:** The beast moves up to their speed. If they end their turn adjacent to the triggering ally, they can pick the ally up and allow them to climb on top of the beast."
traits:
  - name: "Beast of Burden"
    desc: "Two of the beast’s  1 allies can occupy the same space while riding the beast."
  - name: "Nature Calls"
    desc: "The beast ignores 1 bane on their abilities while in an encounter outside or in a natural environment."

# SWARM

name: "SWARM"
level: 1
roles:
  - TROOP
  - HEXER
ancestry:
  - Animal
  - Swarm
ev: 16
stamina: 40
speed: 5
size: 2 /
stability: 1
free_strike: 4
characteristics:
  - -2
  - +1
  - -3
  - +2
  - -3
actions:
  - name: "Flurry"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 9 damage; pull 1
      <br />✸ 17+ 12 damage; pull 2 
      <br />**Effect:** The target can be pulled into the swarm without inflicting damage."
maneuvers:
  - name: "Impede"
    desc: "
      <br />**Keywords** —
      <br />**Distance** 1 aura
      <br />**Target** Special 
      <br />**Effect:** The swarm forces themselves in the way of their foes. The affected area is considered difficult terrain for enemies until the start of the swarm’s next turn."
traits:
  - name: "Swarm"
    desc: "The swarm can move through squares as if they were size -1M, and can occupy other creatures’ spaces. At the start of the swarm’s turn, they can make a free strike against each creature they share a square with."
  - name: "Nature Calls"
    desc: "The swarm ignores 1 bane on their abilities while in an encounter outside or in a natural environment."

# PREDATOR A

name: "PREDATOR A"
level: 1
roles:
  - TROOP
  - BRUTE
ancestry:
  - Animal
ev: 16
stamina: 80
speed: 5
size: 2 /
stability: 0
free_strike: 5
characteristics:
  - +1
  - +2
  - -2
  - +1
  - +1
actions:
  - name: "Natural Weapon"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 10 damage; M< 1 [[prone]]
      <br />✸ 17+ 13 damage; M< 2 [[prone]] Ready to Strike (Maneuver)
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The predator assesses their environment or lets loose a battle cry and gives themself an edge on their next strike."
ta:
  - name: "Quick Strike"
    desc: "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Triggering creature or object 
      <br />**Trigger** A creature or object comes within distance. 
      <br />**Effect:** The predator makes a free strike against the target. The predator deals an additional 3 damage if they were hidden from the target."
traits:
  - name: "Nature Calls"
    desc: "The predator ignores 1 bane on their abilities while in an encounter outside or in a natural environment."

# PREDATOR B

name: "PREDATOR B"
level: 2
roles:
  - TROOP
  - BRUTE
ancestry:
  - Animal
ev: 16
stamina: 100
speed: 5
size: 3 /
stability: 2
free_strike: 5
characteristics:
  - +2
  - +1
  - -1
  - +1
  - +0
actions:
  - name: "Natural Weapon"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 11 damage; push 1; M < 1 [[prone]]
      <br />✸ 17+ 14 damage; push 2; M < 2 [[prone]] 
  - name: "Wild Swing"
    desc:
      "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 1 burst
      <br />**Target** All enemies and objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 6 damage
      <br />✸ 17+ 8 damage; A < 2 [[bleeding]] (save ends) 
      <br />**Effect:** The predator uses their weapons in a wanton flurry."
ta:
  - name: "Swat"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** Triggering creature or object 
      <br />**Trigger** The predator takes damage from a creature or object within distance. 
      <br />**Effect:** Push 5. Trample The predator can move through enemies and objects at normal speed. When the predator enters a creature’s space for the first time on their turn, the creature takes 3 damage."
traits:
  - name: "Nature Calls"
    desc: "The predator ignores 1 bane on their abilities while in an encounter outside or in a natural environment."

# ANKHEG

name: "ANKHEG"
level: 1
roles:
  - SOLO
ancestry:
  - Ankheg
  - Beast
ev: 30
stamina: 200
speed: 5 (burrow)
size: 2 /
stability: 2
free_strike: 5
characteristics:
  - +3
  - +1
  - −3
  - +1
  - −4
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The ankheg takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the ankheg can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the ankheg can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Soft Underbelly"
    desc: "A [[prone]] creature gains an edge on melee strikes against the ankheg instead of taking a bane."
actions:
  - name: "Bite"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage
      <br />★ 12–16 13 damage; [[grabbed]]
      <br />✸ 17+ 16 damage; [[grabbed]] 
      <br />**Effect:** A size 1 target [[grabbed]] this way takes 3 acid damage at the start of each of their turns."
  - name: "Claws"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; A < 1 [[grabbed]]
      <br />★ 12–16 11 damage; A < 2 [[grabbed]]
      <br />✸ 17+ 14 damage; A < 3 [[grabbed]] 2 Malice The ankheg can vertical slide each target up to 5 squares."
  - name: "Spitfire"
    desc:
      "
      <br />**Keywords** Area, Ranged, Weapon
      <br />**Distance** 1 cube within 5
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 acid damage
      <br />★ 12–16 8 acid damage
      <br />✸ 17+ 11 acid damage 
      <br />**Effect:** The affected area is covered in burning acid. An enemy who enters an affected square for the first time on their turn or starts their turn there takes 2 acid damage."
  - name: "Earth Eruption"
    desc:
      "
      <br />**Keywords** Area, Melee
      <br />**Distance** 4 burst
      <br />**Target** Each enemy in the burst 
      <br />**Effect:** The ankheg burrows up to their speed, then creates the burst when they breach the surface.
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 6 damage
      <br />✸ 17+ 7 damage; push 2 Dust Cloud (Maneuver)
      <br />**Keywords** Area
      <br />**Distance** 1 burst
      <br />**Target** Special 
      <br />**Effect:** The ankheg kicks up dust into the affected area that blocks [[Draw Steel Rules#LINE OF EFFECT|line of effect]] for enemies. The ankheg then shifts or burrows up to their speed."
ta:
  - name: "Skitter"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** A creature damages the ankheg 
      <br />**Effect:** The ankheg shifts up to 3 squares."
traits:
  - name: "Earthwalk"
    desc: "Difficult terrain composed of earth or loose rock doesn’t cost the ankheg extra movement."
  - name: "Tunneler"
    desc: "When the ankheg burrows, they create a size 2 tunnel. The tunnel remains stable for one day, then collapses."
va:
  - name: "Acid Spew (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Weapon
      <br />**Distance** 10 x 1 line within 1
      <br />**Target** Each creature in the line
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 acid damage
      <br />★ 12–16 8 acid damage
      <br />✸ 17+ 11 acid damage 
      <br />**Effect:** The ground within the affected area is covered in a puddle of acid. A creature who enters an affected square for the first time on their turn or starts their turn there takes 2 acid damage."
  - name: "Sinkhole (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The ankheg shifts up to their speed by burrowing. If the ankheg ends this move underground and within 2 squares of a creature on the surface, the ankheg uses Bite against the creature."
  - name: "Acid and Claws (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 2 burst
      <br />**Target** Each creature in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 acid damage; M < 1 [[bleeding]] (save ends)
      <br />★ 12–16 8 acid damage; M < 2 [[bleeding]] (save ends)
      <br />✸ 17+ 11 acid damage; M < 3 [[bleeding]] (save ends)"

# ASHEN HOARDER

name: "ASHEN HOARDER"
level: 4
roles:
  - SOLO
ancestry:
  - Construct
  - Undead
ev: 60
stamina: 350
weaknesses: Holy 5
speed: 8 (burrow)
size: 3 /
stability: 3
free_strike: 6
characteristics:
  - +4
  - -2
  - -2
  - +0
  - -5
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The ashen hoarder takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the ashen hoarder can take one action and one maneuver per turn."
  - name: "End Effect:
    desc: "At the end of their turn, the ashen hoarder can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
actions:
  - name: "Claw and Blade"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 10 damage; one target M < 2 [[bleeding]] (save ends); other target A < 2 [[grabbed]]
      <br />★ 12–16 15 damage; one target M < 3 [[bleeding]] (save ends); other target A < 3 [[grabbed]]
      <br />✸ 17+ 18 damage; M < 4 [[bleeding]] (save ends); A < 4 [[grabbed]] 
      <br />**Effect:** The ashen hoarder can have up to two size 1 creatures [[grabbed]] at the same time."
  - name: "Corpse Bomb"
    desc:
      "
      <br />**Keywords** Area, Ranged
      <br />**Distance** 4 cube within 20
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 4 damage; A < 2 [[weakened]] (save ends)
      <br />★ 12–16 8 damage; A < 3 [[weakened]] (save ends)
      <br />✸ 17+ 11 damage; A < 4 [[weakened]] (save ends) 
      <br />**3 Malice** The ashen hoarder targets a second 4 cube within distance. 
      <br />**2 Malice** An enemy [[weakened]] by a Corpse Bomb is also [[slowed]] (save ends)"
  - name: "Impale"
    desc:
      "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 4 x 1 line within 1
      <br />**Target** All creatures in the line
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 6 corruption damage; M < 2 impaled (save ends)
      <br />★ 12–16 11 corruption damage; M < 3 impaled (save ends)
      <br />✸ 17+ 14 corruption damage; M < 4 impaled (save ends) 
      <br />**Effect:** An impaled creature is [[restrained]] and [[bleeding]] until the condition ends. Each impaled creature moves whenever the ashen hoarder moves. The ashen hoarder can have no more than 3 creatures impaled with this ability at a time. 
      <br />**2 Malice** A creature impaled by this ability can be used with the Armor of Corpses ability instead of paying Malice."
maneuvers:
  - name: "Bone Dozer"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The ashen hoarder moves up to twice their speed in a straight line. Each creature and object in the ashen hoarder’s way is either moved into the nearest unoccupied square to the side or M < 3 is pushed forward until the end of the ashen hoarder’s movement. A target that is force moved into an obstacle is [[dazed]] (save ends)."
ta:
  - name: "Armor of Corpses"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The ashen hoarder takes damage. 
      <br />**Effect:** The ashen hoarder halves the incoming damage. If an impaled creature was used in place of spending Malice on this ability, the impaled creature takes the other half of the damage."
traits:
  - name: "Unshackled Rage"
    desc: "The ashen hoarder is commanded by whoever holds its Soul Shackle. A Soul Shackle is a size 1T object with 5 stamina. If the Soul Shackle is destroyed, the ashen hoarder flies into an unshackled rage. While raging, the ashen hoarder has a double edge on their abilities, damage immunities 5, ignores all commands, and is hostile to all living creatures within [[Draw Steel Rules#LINE OF EFFECT|line of effect]]. At the start of each of their turns, the ashen hoarder takes 10 damage that can’t be reduced."
  - name: "Bladed Body"
    desc: "Whenever an enemy makes physical contact with the ashen hoarder or uses a melee ability against the ashen hoarder, they take 3 damage."
  - name: "Soul Singularity"
    desc: "When the Ashen Hoarder is reduced to 0 stamina it explodes in a swirling singularity of bone shards and soul energy. Each creature within 5 takes M< 3 11 corruption damage. If a creature is killed by this explosion, their soul is sucked into the vortex and is lost somewhere on the plane of the dead. They cannot be resurrected until their soul is recovered."
va:
  - name: "Skeletal Eruption (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 8 x 3 line within 1
      <br />**Target** All creatures in the line
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 6 damage, vertical push 2 straight upward
      <br />★ 12–16 11 damage, vertical push 3 straight upward
      <br />✸ 17+ 14 damage, vertical push 4 straight upward 
      <br />**Effect:** Each target that would normally fall [[prone]] is instead [[restrained]] (save ends)."
  - name: "Mobile Mine Field (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** 10 cube within 20
      <br />**Target** Special 
      <br />**Effect:** The Ashen Hoarder sprays out a rain of zombie mines brimming with necrotic energy. Six size 1M zombie mines appear in unoccupied squares within distance. An enemy that moves into a square adjacent to a zombie mine or starts their turn there causes the zombie mine to explode, dealing 4 corruption damage to each creature adjacent to the mine. A zombie explosion can trigger other zombie mines adjacent to it to also explode. At the start of each of the ashen hoarders’s turns, each zombie mine can be moved 2 squares."
  - name: "Ossuary Assault (Villain Action 3)"
    desc: "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The Ashen Hoarder moves up to their speed and makes a Claw and Blade attack with a double edge against a single target. On a tier-3 result, the ashen hoarder then uses Impale without spending malice."

# BASILISK

name: "BASILISK"
level: 1
roles:
  - TROOP
  - BRUTE
ancestry:
  - Basilisk
  - Beast
ev: 12
stamina: 80
immunities: Poison 4
speed: 8
size: 2 /
stability: 2
free_strike: 5
characteristics:
  - +2
  - 0
  - −3
  - −1
  - −1
actions: 
  - name: "Noxious Bite"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 poison damage
      <br />★ 12–16 10 poison damage
      <br />✸ 17+ 13 poison damage 
      <br />**Effect:** This ability has an edge against targets that the basilisk has previously dealt poison damage to."
  - name: "Poison Fumes"
    desc:
      "
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 cube within 1
      <br />**Target** All creatures in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 poison damage; M<  0 [[weakened]] (save ends)
      <br />★ 12–16 6 poison damage; M<  1 [[weakened]] and [[slowed]] (save ends)
      <br />✸ 17+ 9 poison damage; M<  2 [[weakened]] and [[slowed]] (save ends)"
maneuvers:
  - name: "Petrifying Eye Beams"
    desc: "
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 5 × 2 line within 1
      <br />**Target** Special
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 M<  0 [[restrained]] (save ends)
      <br />★ 12–16 M<  1 [[restrained]] (save ends)
      <br />✸ 17+ [[slowed]] (save ends) or M<  2 [[restrained]] (save ends) 
      <br />**Effect:** The basilisk targets the first unobstructed creature in each column of the area. An already [[slowed]] target has -1 to resisting the potency. Each target magically begins to turn to stone. A creature [[restrained]] by this ability or a creature adjacent to them can use an action to cut the encroaching stone from their body, taking 8 damage which can’t be reduced in any way and ending the effect. A target that ends two consecutive turns [[restrained]] by this ability is petrified until they are cured (see Alchemical Ingredients)."
ta:
  - name: "Lash Out"
    desc: "
      <br />**Keywords** — 
      <br />**Trigger** The basilisk takes melee damage.
      <br />**Distance** 1 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** Each target takes 5 damage and is A<  2 [[bleeding]] (save ends)."
traits:
  - name: "Calcifying"
    desc: "The area within 3 squares of the basilisk is considered difficult terrain for enemies."

# BASILISK TONGUESNAPPER

name: "BASILISK TONGUESNAPPER"
level: 1
roles:
  - TROOP
  - HEXER
ancestry:
  - Basilisk
  - Beast
ev: 12
stamina: 40
immunities: Poison 2, Acid 2
speed: 8
size: 2 /
stability: 2
free_strike: 4
characteristics:
  - +1
  - +2
  - −3
  - −1
  - −1
actions:
  - name: "Prehensile Tongue"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 acid damage; pull 1
      <br />★ 12–16 10 acid damage; pull 2
      <br />✸ 17+ 14 acid damage; pull 3 
      <br />**Effect:** This ability can pull targets [[restrained]] by Petrifying Eye Beams, ignoring stability. 
      <br />**3 Malice** The toungesnapper targets two additional creatures or objects."
  - name: "Wink"
    desc:
      "
      <br />**Keywords** Melee, Magic, Strike, Ranged
      <br />**Distance** Melee 1 or Ranged 10
      <br />**Target** 1 creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 corruption damage; R<  0 [[dazed]] (save ends)
      <br />★ 12–16 10 corruption damage; R<  1 [[dazed]] (save ends)
      <br />✸ 17+ 14 corruption damage; R<  2 [[dazed]] and [[slowed]] (save ends) 
      <br />**Effect:** A creature [[dazed]] by this ability can’t benefit from edges or surges until the condition ends. 
maneuvers:
  - name: "Petrifying Eye Beams"
    desc: "
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 5 × 2 line within 1
      <br />**Target** Special
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 A<  0 [[restrained]] (save ends)
      <br />★ 12–16 A<  1 [[restrained]] (save ends)
      <br />✸ 17+ [[slowed]] (save ends) or A<  2 [[restrained]] (save ends) 
      <br />**Effect:** The tonguesnapper targets the first unobstructed creature in each column of the area. An already [[slowed]] target has -1 to resisting the potency. Each target magically begins to turn to stone. A creature [[restrained]] by this ability or a creature adjacent to them can use an action to cut the encroaching stone from their body, taking 8 damage which can’t be reduced in any way and ending the effect. A target that ends two consecutive turns [[restrained]] by this ability is petrified until they are cured (see Alchemical Ingredients)."
ta:
  - name: "Neurotoxin Splash"
    desc: "
      <br />**Keywords** — 
      <br />**Trigger** The tonguesnapper takes melee damage.
      <br />**Distance** 2 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** Each target takes 4 acid damage and is M<  2 [[slowed]] (save ends)."
traits:
  - name: "Petrifying Fumes"
    desc: "A creature that starts their turn adjacent to the tonguesnapper is M< 1 [[slowed]] (save ends)."

# BREDBEDDLE

name: "BREDBEDDLE"
level: 3
roles:
  - SOLO
ancestry:
  - Bredbeddle
  - Giant
ev: 50
stamina: 300
speed: 5
size: 2 /
stability: 4
free_strike: 6
characteristics:
  - +3
  - 0
  - −3
  - +1
  - +2
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The bredbeddle takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the bredbeddle can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the bredbeddle can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Resilient Form"
    desc: "The bredbeddle can’t be physically transformed in any way except by their Heady or Not trait."
  - name: "Heady or Not"
    desc: "While headless, the bredbeddle can move into a space with a severed head and attach it to their neck as an action. Doing so physically transforms the bredbeddle, who takes on the size, weight, reach, and stability of the head’s original owner. These effects last until the bredbeddle is killed or beheaded, or until the head falls off after 24 hours. A head that falls off this way can no longer be attached to the bredbeddle. A creature must succeed on a hard Might test made as a maneuver to rip a head off the bredbeddle. If they fail, the bredbeddle makes a free strike against them."
actions:
  - name: "Executioner’s Swing"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 2 burst
      <br />**Target** Each enemy in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 2 damage; A<  1 [[bleeding]] (save ends)
      <br />★ 12–16 4 damage; A<  2 [[bleeding]] (save ends)
      <br />✸ 17+ 5 damage; A<  3 [[bleeding]] (save ends); M<  2 [[dazed]] (save ends) 
      <br />**3 Malice** The bredbeddle shifts up to 2 squares and can target additional enemies who come within distance of this ability during the move."
  - name: "Lop"
    desc:
      "
      <br />**Keywords** Magic, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** One creature
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage; [[bleeding]] (save ends) or M<  1 beheaded (see effect)
      <br />★ 12–16 13 damage; [[bleeding]] (save ends) or M<  2 beheaded (see effect)
      <br />✸ 17+ 16 damage; [[bleeding]] (save ends) or M<  3 beheaded (see effect) 
      <br />**Effect:** A beheaded target has their head fall into an unoccupied square adjacent to the bredbeddle, but they remain alive. While beheaded, the target is [[bleeding]] and can’t establish [[Draw Steel Rules#LINE OF EFFECT|line of effect]] beyond 1 square. The beheaded target can survive without their head for 24 hours, and can reattach their head with a maneuver by entering its square. A target who remains beheaded for 24 hours dies."
maneuvers:
  - name: "Scramble"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self (while headless)
      <br />**Target** Self 
      <br />**Effect:** The bredbeddle shifts up to their speed, and can push each creature who comes within their reach during the movement 1 square. Each square the bredbeddle exits during the movement becomes difficult terrain."
  - name: "Headway"
    desc: "
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 20
      <br />**Target** One creature or object 
      <br />**Effect:** The bredbeddle must have a head in their possession (attached to them or not), which they throw at the target. If the head was attached, the bredbeddle becomes headless.
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage; M<  1 [[dazed]] (save ends)
      <br />★ 12–16 13 damage; [[prone]]; M<  2 [[dazed]] (save ends)
      <br />✸ 17+ 16 damage; [[prone]]; M<  3 [[dazed]] (save ends)"
ta:
  - name: "Envious Imitation"
    desc: "<br />**Cost** 2 Malice
      <br />**Keywords** Magic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** A creature targets the bredbeddle with a ranged strike. 
      <br />**Effect:** The bredbeddle uses the same ability against the triggering creature, using that creature’s bonus to any power rolls they have to make."
va:
  - name: "Turn Green (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 burst
      <br />**Target** Each enemy in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 P<  1 The target turns green (save ends)
      <br />★ 12–16 P<  2 The target turns green (save ends)
      <br />✸ 17+ P<  3 The target turns green until the end of the encounter 
      <br />**Effect:** Green shadows crawl out from under the bredbeddle’s feet and attempt to turn each target green. The bredbeddle has a double edge on attacks made against targets turned green until the condition ends."
  - name: "Challenge (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 5
      <br />**Target** One enemy 
      <br />**Effect:** The bredbeddle points at the target and issues them a challenge. If the target refuses, they turn green until the end of the encounter (see Turn Green). If the target accepts, the bredbeddle shifts to a space adjacent to the target, who must make a hard Might test with no additional modifiers. On success, the target can choose to deal 40 damage to the bredbeddle or remove the bredbeddle’s head. On failure, the target is beheaded (see Lop)."
  - name: "Headlam Rampage (Villain Action 3)"
    desc: "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** Four creatures
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 damage; [[bleeding]] (save ends) or A<  1 beheaded
      <br />★ 12–16 7 damage; [[bleeding]] (save ends) or A<  2 beheaded
      <br />✸ 17+ 8 damage; [[bleeding]] (save ends) or A<  3 beheaded (see Lop)"

# BUGBEAR CHANNELER

name: "BUGBEAR CHANNELER"
level: 2
roles:
  - TROOP
  - CONTROLLER
ancestry:
- Bugbear 
- Goblin 
- Humanoid 
- Fey
ev: 16
stamina: 60
speed: 5
size: 1L /
stability: 0
free_strike: 5
characteristics:
  - +1
  - +1
  - +2
  - +2
  - +2
actions:
  - name: "Shadow Drag"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Strike, Ranged
      <br />**Distance** Ranged 8
      <br />**Target** 2 creatures or objects on the ground
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; pull 2
      <br />★ 12–16 10 damage; pull 3
      <br />✸ 17+ 13 damage; pull 4 
      <br />**Effect:** Each square that a target is pulled through becomes difficult terrain for enemies."
  - name: "Blistering Element"
    desc:
      "
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage; M<  0 [[bleeding]] (save ends)
      <br />★ 12–16 3 damage; M<  1 [[bleeding]] (save ends)
      <br />✸ 17+ 4 damage; M<  2 [[bleeding]] (save ends) 
      <br />**Effect:** The channeler chooses one of the following damage types for the damage: acid, cold, corruption, fire, or poison."
  - name: "Twist Shape"
    desc:
      "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** 1 creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 corruption damage; P<  0 [[slowed]] (save ends)
      <br />★ 12–16 8 corruption damage; P<  1 shapechanged (save ends)
      <br />✸ 17+ 11 corruption damage; P<  2 shapechanged (save ends) 
      <br />**Effect:** A shapechanged creature has their limbs violently stretched and their skin becomes paper thin. They are [[slowed]] and have fire weakness 10 while they have this effect."
maneuvers:
  - name: "Throw"
      <br />**Keywords** Attack, Melee
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object [[grabbed]] by the channeler 
      <br />**Effect:** Vertical push 3. An ally target doesn’t take damage from being force moved."
ta:
  - name: "Catcher (Free Triggered Action)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** 1 size 1 creature or object 
      <br />**Trigger** The target is force moved into a square adjacent to the channeler. 
      <br />**Effect:** The target is [[grabbed]] by the channeler."
  - name: "Shadow Veil (Triggered Action)"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** 1 ally 
      <br />**Trigger** The target takes damage. 
      <br />**Effect:** The channeler collapses the target into their shadow and halves the damage. The target can’t be targeted by strikes until they reform from the shadows at the start of their next turn."


# BUGBEAR COMMANDER

name: "BUGBEAR COMMANDER"
level: 2
roles:
  - TROOP
  - SUPPORT
ancestry:
- Bugbear 
- Goblin 
- Humanoid 
- Fey
ev: 16
stamina: 80
speed: 5
size: 1L /
stability: 0
free_strike: 5
characteristics:
  - +2
  - +1
  - +2
  - 0
  - 0
actions:
  - name: "Inspiring Swordplay"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Attack, Melee, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 10 damage
      <br />✸ 17+ 13 damage; one target is [[grabbed]] 
      <br />**Effect:** 1 ally within 5 of the commander has an edge on their next attack until the start of the commander’s next turn."
  - name: "You Next!"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 8
      <br />**Target** 1 ally 
      <br />**Effect:** The target moves up to their speed and uses a signature action."
  - name: "Fall Back!"
    desc:
      "
      <br />**Cost** 5 Malice
      <br />**Keywords** —
      <br />**Distance** Self and 5 burst
      <br />**Target** Self and all allies 
      <br />**Effect:** Each target shifts up to their speed. Each target can use the Throw maneuver if they are grabbing a creature or object."
maneuvers:
  - name: "Throw"
    desc: "
      <br />**Keywords** Attack, Melee
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object [[grabbed]] by the commander 
      <br />**Effect:** Vertical push 4. An ally target doesn’t take damage from being force moved."
ta:
  - name: "Catcher (Free Triggered Action)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** 1 size 1 creature or object 
      <br />**Trigger** The target is force moved into a square adjacent to the commander. 
      <br />**Effect:** The target is [[grabbed]] by the commander."
traits:
  - name: "The Commander’s Watching"
    desc: "While an ally has [[Draw Steel Rules#LINE OF EFFECT|line of effect]] to the commander, the ally can end one condition afflicting them at the start of their turn."


# BUGBEAR ROUGHNECK

name: "BUGBEAR ROUGHNECK"
level: 2
roles:
  - TROOP
  - BRUTE
ancestry:
- Bugbear
- Goblin 
- Humanoid 
- Fey
ev: 16
stamina: 109
speed: 6
size: 1L /
stability: 0
free_strike: 5
characteristics:
  - +2
  - +2
  - 0
  - 0
  - 0
actions:
  - name: "Haymaker"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 11 damage; one target is [[grabbed]]; one target is pushed 2
      <br />✸ 17+ 14 damage; one target is [[grabbed]]; one target is vertically pushed 3 
      <br />**5 Malice** The distance becomes 1 Burst, the Strike keyword is replaced with Area, and the roughneck targets all enemies instead."
  - name: "Leaping Fury"
    desc:
      "
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; M< 1 [[prone]]
      <br />★ 12–16 13 damage; M< 2 [[prone]]
      <br />✸ 17+ 16 damage; M< 3 [[prone]] 
      <br />**Effect:** The roughneck leaps 5 to an unoccupied space adjacent to the target before making the attack."
maneuvers:
  - name: "Drag Through Hell"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object [[grabbed]] by the roughneck 
      <br />**Effect:** The roughneck moves up to their speed, dragging the target across the ground. The target takes 2 damage for each square they were dragged through before being released [[prone]]. Each square the target was dragged through becomes difficult terrain for enemies."
  - name: "Throw"
    desc: "
      <br />**Keywords** Attack, Melee
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object [[grabbed]] by the roughneck 
      <br />**Effect:** Vertical push 5. An ally target doesn’t take damage from being force moved."
ta:
  - name: "Catcher (Free Triggered Action)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** 1 size 1 creature or object 
      <br />**Trigger** The target is force moved into a square adjacent to the roughneck. 
      <br />**Effect:** The target is [[grabbed]] by the roughneck."
  - name: "Flying Sawblade"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The roughneck is vertically moved by another creature. 
      <br />**Effect:** The roughneck uses their Haymaker ability against a creature or object at the end of the movement."


# BUGBEAR SHADOW SNEAK

name: "BUGBEAR SHADOW SNEAK"
level: 2
roles:
  - TROOP
  - AMBUSHER
ancestry:
- Bugbear 
- Goblin 
- Humanoid 
- Fey
ev: 16
stamina: 80
speed: 7
size: 1L /
stability: 0
free_strike: 5
characteristics:
  - +2
  - +2
  - 0
  - 0
  - 0
actions:
  - name: "Suckerpunch"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 damage; A<  1 [[grabbed]]
      <br />★ 12–16 13 damage; A<  2 [[grabbed]]
      <br />✸ 17+ 16 damage; [[grabbed]] 
      <br />**Effect:** The target can’t use triggered actions until the start of the next round. This ability deals an additional 4 damage if the sneak started their turn hidden from the target."
  - name: "Shadow Cloak"
    desc:
      "
      <br />**Keywords** Area
      <br />**Distance** 2 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage; I<  0 sneak is concealed from the target (save ends)
      <br />★ 12–16 3 damage; I<  1 sneak is concealed from the target (save ends)
      <br />✸ 17+ 4 damage; I<  2 sneak is concealed from the target (save ends) 
      <br />**Effect:** The sneak shifts up to their speed and hides after using this ability."
  - name: "Carving Dagger"
    desc:
      "
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 8
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; M<  0 [[bleeding]] (save ends)
      <br />★ 12–16 11 damage; M<  1 [[bleeding]] (save ends)
      <br />✸ 17+ 14 damage; M<  2 [[bleeding]] (save ends) 
      <br />**Effect:** The target can’t hide from the sneak or their allies while [[bleeding]] from this ability."
maneuvers:
  - name: "Throw"
    desc: "
      <br />**Keywords** Attack, Melee
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object [[grabbed]] by the sneak 
      <br />**Effect:** Vertical push 4. An ally target doesn’t take damage from being force moved."
ta:
  - name: "Catcher (Free Triggered Action)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** 1 size 1 creature or object 
      <br />**Trigger** The target is force moved into a square adjacent to the sneak. 
      <br />**Effect:** The target is [[grabbed]] by the sneak."
  - name: "Clever Trick"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Special
      <br />**Target** 1 enemy 
      <br />**Trigger** A target attacks the sneak. 
      <br />**Effect:** The sneak chooses an enemy within distance of the attack. The attack targets that enemy instead."


# BUGBEAR KNIGHTMARE

name: "BUGBEAR KNIGHTMARE"
level: 8
roles:
  - MINION
  - HEXER
ancestry:
- Bugbear 
- Goblin 
- Humanoid 
- Fey
ev: 10 for eight minions
stamina: 12
speed: 5
size: 1L /
stability: 2
with-captain: Edge on strikes
free_strike: 3
characteristics:
  - +4
  - +3
  - +1
  - +1
  - +4
actions:
  - name: "Corrosive Blade"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 3 corruption damage
      <br />★ 12–16 6 corruption damage; P<  3 [[bleeding]] (save ends)
      <br />✸ 17+ 8 corruption damage; [[grabbed]]; P<  4 [[bleeding]] (save ends) 
      <br />**Effect:** A target [[grabbed]] by the knightmare can be immediately vertically pushed 5."
traits:
  - name: "Bu’gathic Inspiration"
    desc: "Each ally has +1 on dice rolls for each adjacent knightmare."
  - name: "Magic Terror"
    desc: "Each enemy has -1 to dice rolls for each adjacent knightmare."


# BUGBEAR MOB

name: "BUGBEAR MOB"
level: 5
roles:
  - MINION
  - BRUTE
ancestry:
- Bugbear 
- Goblin 
- Humanoid 
- Fey 
- Swarm
ev: 7 for eight minions
stamina: 10
speed: 6
size: 3 /
stability: 2
with-captain: Strike damage +2
free_strike: 3
characteristics:
  - +3
  - -1
  - 0
  - +1
  - 0
actions:
  - name: "Mug and Tear"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 damage; pull 2
      <br />★ 12–16 6 damage; pull 3
      <br />✸ 17+ 7 damage; pull 4; [[grabbed]] 
      <br />**Effect:** The target can be pulled into the mob without inflicting damage."
traits:
  - name: "Swarm"
    desc: "The mob can move through squares as if they were size -1M, and can occupy other creatures’ spaces. At the start of the mob’s turn, they can make a free strike against each creature they share a square with."


# BUGBEAR SNARE

name: "BUGBEAR SNARE"
level: 5
roles:
  - MINION
  - AMBUSHER
ancestry:
- Bugbear 
- Goblin 
- Humanoid 
- Fey
ev: 7 for eight minions
stamina: 9
speed: 6
size: 1L /
stability: 2
with-captain:
speed: +3
free_strike: 3
characteristics:
  - +2
  - +3
  - 0
  - 0
  - +1
actions:
  - name: "Cut Em Low!"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 6 damage
      <br />✸ 17+ 7 damage; A<  3 [[slowed]] (save ends) 
      <br />**Effect:** The target is [[grabbed]] if the snare started their turn hidden from them. A target [[grabbed]] by the snare can be immediately vertically pushed 4."

# DEMON ENSNARER

name: "DEMON ENSNARER"
level: 1
roles:
  - MINION
  - BRUTE
ancestry:
  - Abyssal
  - Demon
ev: 3 for eight minions
stamina: 5
weaknesses: Holy 3
speed: 5
size: 1M/
stability: 0
with-captain: Melee distance +2
free_strike: 2
characteristics:
  - +2
  - +0
  - −1
  - −1
  - −1
actions: 
  - name: "Barbed Tongues"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage; pull 1
      <br />★ 12–16 4 damage; pull 2
      <br />✸ 17+ 5 damage; pull 3 
      <br />**Effect:** If the target is pulled adjacent to the ensnarer, the ensnarer makes a free strike against them. Soulsight Each creature within 2 of the ensnarer can’t be hidden from them."


# DEMON FRENZIED

name: "DEMON FRENZIED"
level: 1
roles:
  - MINION
  - HARRIER
ancestry:
  - Abyssal
  - Demon
ev: 3 for eight minions
stamina: 4
weaknesses: Holy 3
speed: 6
size: 1M/
stability: 0
with-captain:
speed: +2
free_strike: 1
characteristics:
  - +0
  - +2
  - −1
  - −1
  - −1
actions:
  - name: "Rip and Tear"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage
      <br />★ 12–16 2 damage
      <br />✸ 17+ 3 damage Soulsight Each creature within 2 of the frenzied can’t be hidden from them."


# DEMON PITLING

name: "DEMON PITLING"
level: 1
roles:
  - MINION
  - ARTILLERY
ancestry:
  - Abyssal
  - Demon
ev: 3 for eight minions
stamina: 3
weaknesses: Holy 3
speed: 5 (fly)
size: 1T/
stability: 0
with-captain:
speed: +2
free_strike: 2
characteristics:
  - −2
  - +2
  - −2
  - −2
  - −2
actions:
  - name: "Spit"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 poison damage
      <br />★ 12–16 4 poison damage
      <br />✸ 17+ 5 poison damage Horrid Stench Any enemy who has three or more pitlings within 2 squares of them can’t regain stamina. Soulsight Each creature within 2 of the pitling can’t be hidden from them."


# DEMON BENDRAK

name: "DEMON BENDRAK"
level: 2
roles:
  - BAND
  - HEXER
ancestry:
  - Abyssal
  - Demon
ev: 4
stamina: 15
weaknesses: Holy 3
speed: 5
size: 1S/
stability: 0
free_strike: 2
characteristics:
  - +0
  - +1
  - +0
  - +0
  - +2
actions:
  - name: "Warp Perceptions"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** One creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 psychic damage
      <br />★ 12–16 5 psychic damage; P<  1 [[weakened]] (save ends)
      <br />✸ 17+ 7 psychic damage; P<  2 [[weakened]] (save ends) 
      <br />**Effect:** If the target makes a strike while [[weakened]] this way, the bendrak can choose a second target within distance for the strike, then evenly divides any damage from the strike between the two targets. 
maneuvers:
  - name: Vanish"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** Self or one ally 
      <br />**Effect:** The target immediately becomes hidden, regardless of whether they have cover or concealment. Lethe While [[winded]], the bendrak has an edge on strikes, and strikes have an edge against them."
traits:
  - name: "Soulsight"
    desc: "Each creature within 2 of the bendrak can’t be hidden from them."


# DEMON MUCERON

name: "DEMON MUCERON"
level: 3
roles:
  - BAND
  - BRUTE
ancestry:
  - Abyssal
  - Demon
ev: 5
stamina: 30
weaknesses: Holy 3
speed: 5
size: 1M/
stability: 0
free_strike: 3
characteristics:
  - +2
  - +2
  - +0
  - +0
  - +1
actions:
  - name: "Barbed Tongues"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** One creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; pull 2
      <br />★ 12–16 7 damage; pull 3
      <br />✸ 17+ 8 damage; pull 4 
      <br />**Effect:** If the target is pulled adjacent to the muceron, the muceron either makes a free strike against them or grabs them."
maneuvers:
  - name: "Tongue Pull"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 5
      <br />**Target** Three creatures 
      <br />**Effect:** The muceron pulls each target 5 squares."
traits:
  - name: "Lethe"
    desc: "While [[winded]], the muceron has an edge on strikes, and strikes have an edge against them."
  - name: "Soulsight"
    desc: "Each creature within 2 of the muceron can’t be hidden from them."


# DEMON REMASCH

name: "DEMON REMASCH"
level: 2
roles:
  - BAND
  - AMBUSHER
ancestry:
  - Abyssal
  - Demon
ev: 4
stamina: 20
weaknesses: Holy 3
speed: 5 (teleport)
size: 1S/
stability: 0
free_strike: 3
characteristics:
  - +0
  - +2
  - +0
  - +0
  - +2
actions:
  - name: "Abyssal Strike"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; the remasch teleports 2 squares
      <br />★ 12–16 6 damage; the remasch teleports 3 squares
      <br />✸ 17+ 8 damage; the remasch teleports 5 squares 
      <br />**5 Malice** The remasch takes an adjacent creature with them when they teleport. The creature appears in an unoccupied space adjacent to the remasch’s destination."
maneuvers:
  - name: "Grasping Shadow"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** Magic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The resmach teleports 2 squares and uses Abyssal Strike."
  - name: "Lethe"
    desc: "While [[winded]], the resmach has an edge on strikes, and strikes have an edge against them."
  - name: "Soulsight"
    desc: "Each creature within 2 of the remasch can’t be hidden from them."


# DEMON RUINANT

name: "DEMON RUINANT"
level: 1
roles:
  - BAND
  - HARRIER
ancestry:
  - Abyssal
  - Demon
ev: 3
stamina: 15
weaknesses: Holy 3
speed: 6
size: 1M/
stability: 0
free_strike: 1
characteristics:
  - +0
  - +2
  - +0
  - +0
  - +1
actions:
  - name: "Bloodletting Claws"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage; M<  2 [[bleeding]] (save ends) Salt Wounds (Maneuver) ◆
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** Three creatures without full stamina
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 corruption damage
      <br />★ 12–16 2 corruption damage
      <br />✸ 17+ 3 corruption damage"
traits: 
  - name: "Lethe"
    desc: "While [[winded]], the ruinant has an edge on strikes, and strikes have an edge against them."
  - name: "Soulsight"
    desc: "Each creature within 2 of the ruinant can’t be hidden from them."


# DEMON TORLAS

name: "DEMON TORLAS"
level: 1
roles:
  - BAND
  - CONTROLLER
ancestry:
  - Abyssal
  - Demon
ev: 3
stamina: 10
weaknesses: Holy 3
speed: 5
size: 1S/
stability: 0
free_strike: 1
characteristics:
  - +0
  - +1
  - +0
  - +0
  - +2
actions:
  - name: "Floor to Flesh"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 3 cube within 10
      <br />**Target** Each enemy in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 Slide 3
      <br />★ 12–16 Slide 4
      <br />✸ 17+ Slide 5 
      <br />**Effect:** The area turns into a morass of spongy flesh before the targets are force moved. Until the start of the torlas’s next turn, the area is difficult terrain, and each creature who moves within the area takes 1 damage for each square moved."
maneuvers:
  - name: "Grasping Tendons"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** Three creatures 
      <br />**Effect:** The torlas pulls each target 3 squares."
  - name: "Lethe"
    desc: "While [[winded]], the torlas has an edge on strikes, and strikes have an edge against them."
  - name: "Soulsight"
    desc: "Each creature within 2 of the torlas can’t be hidden from them."


# DEMON CHOROGAUNT

name: "DEMON CHOROGAUNT"
level: 3
roles:
  - LEADER
ancestry:
  - Abyssal
  - Demon
ev: 20
stamina: 120
weaknesses: Holy 5
speed: 5
size: 1L/
stability: 2
free_strike: 5
characteristics:
  - +2
  - +2
  - +2
  - +2
  - +2
actions:
  - name: "Agonizing Harmony"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 5 burst
      <br />**Target** Each enemy in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 4 psychic damage; I<  1 [[slowed]] (save ends)
      <br />★ 12–16 7 psychic damage; I<  2 [[slowed]] (save ends)
      <br />✸ 17+ 10 psychic damage; I<  3 [[slowed]] (save ends) 
      <br />**Effect:** An ally within 10 squares of the chorogaunt can shift up to their speed."
maneuvers:
  - name: "Chaotic Entrancing Harmony"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 10 burst
      <br />**Target** Each enemy in the burst 
      <br />**Effect:** Each target slides 3, ignoring their stability."
ta:
  - name: "I Thrive on Pain"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** Magic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The chorogaunt is targeted by a strike. 
      <br />**Effect:** Any damage from the attack is halved, and the chorogaunt deals an additional 3 damage with their abilities until the end of their next turn."
traits:
  - name: "End Effect"
    desc: "At the end of their turn, the chorogaunt can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Lethe"
    desc: "While [[winded]], the chorogaunt has an edge on strikes, and strikes have an edge against them."
  - name: "Soulsight"
    desc: "Each creature within 2 of the chorogaunt can’t be hidden from them."
va:
  - name: "Frightening Tones (Villain Action 1)"
    desc: "
      <br />**Keywords** Ranged
      <br />**Distance** Ranged 10
      <br />**Target** Three enemies 
      <br />**Effect:** The chorogaunt allows each target to choose between taking 5 psychic damage or being [[frightened]] (save ends)."
  - name: "Bully the Weak (Villain Action 2)"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One ally 
      <br />**Effect:** The chorogaunt kills the target, and each other ally deals an additional 3 damage on attacks until the end of the round. The Director gains malice equal to the number of heroes."
  - name: "Running Cacophony (Villain Action 3)"
    desc: "
      <br />**Keywords** Magic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The chorogaunt shifts up to their speed, uses their Agonizing Harmony, shifts up to their speed, and then uses their Agonizing Harmony again."

# DEMON GRULQIN

name: "DEMON GRULQIN"
level: 4
roles:
  - MINION
  - BRUTE
ancestry:
  - Abyssal
  - Demon
ev: 6 for eight minions
stamina: 9
weaknesses: Holy 5
speed: 8
size: 1L /
stability: 1
with-captain: Strike damage +2
free_strike: 3
characteristics:
  - +3
  - +2
  - -1
  - -1
  - -1
actions:
  - name: "Spinning Bone Blade"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 5 damage
      <br />✸ 17+ 7 damage 
      <br />**Effect:** The grulqin has an edge on this ability if they moved at least 3 squares in a line during their turn."
  - name: "Soulsight"
    desc: "Each creature within 2 of the grulqin can’t be hidden from them."


# DEMON ORLIQ

name: "DEMON ORLIQ"
level: 4
roles:
  - MINION
  - HARRIER
ancestry:
  - Abyssal
  - Demon
ev: 6 for eight minions
stamina: 8
weaknesses: Holy 5
speed: 6 (fly)
size: 1T /
stability: 0
with-captain:
speed: +2
free_strike: 2
characteristics:
  - -1
  - +3
  - +1
  - +0
  - -1
actions:
  - name: "Soul Prism"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 corruption damage; slide 2
      <br />★ 12–16 4 corruption damage; vertical slide 2
      <br />✸ 17+ 6 corruption damage; vertical slide 4"
traits:
  - name: "Imposing Energy"
    desc: "A enemy who starts their turn with two or more orliqs adjacent to them is [[slowed]] (EoT)."
  - name: "Soulsight"
    desc: "Each creature within 2 of the orliq can’t be hidden from them."


# DEMON WOBALAS

name: "DEMON WOBALAS"
level: 4
roles:
  - MINION
  - ARTILLERY
ancestry:
  - Abyssal
  - Demon
ev: 6 for eight minions
stamina: 7
weaknesses: Holy 5
speed: 6
size: 1M /
stability: 0
with-captain: Strike damage +2
free_strike: 3
characteristics:
  - +1
  - +3
  - +1
  - +2
  - +1
actions:
  - name: "Despair Bolt"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike, Weapon
      <br />**Distance** Ranged 20
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 psychic damage
      <br />★ 12–16 5 psychic damage
      <br />✸ 17+ 7 psychic damage 
      <br />**Effect:** The target has a bane on their next attack. If the target is [[winded]], they have a double bane on their next attack instead."
  - name: "Soulsight"
    desc: "Each creature within 2 of the wobalas can’t be hidden from them."


# DEMON BALE EYE

name: "DEMON BALE EYE"
level: 5
roles:
  - BAND
  - HEXER
ancestry:
  - Abyssal
  - Demon
ev: 7
stamina: 30
weaknesses: Holy 5
speed: 6 (fly)
size: 4 /
stability: 2
free_strike: 3
characteristics:
  - +0
  - +0
  - +3
  - +3
  - +3
actions:
  - name: "Wilting Visions"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Strike, Ranged
      <br />**Distance** Ranged 15
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 psychic damage
      <br />★ 12–16 8 psychic damage
      <br />✸ 17+ 9 psychic damage 
      <br />**Effect:** The target has corruption weakness 5 (EoT). 
      <br />**2 Malice** The target has I<  2 corruption weakness 5 (save ends)."
  - name: "Demonwarp Tears"
    desc:
      "
      <br />**Keywords** Area, Magic
      <br />**Distance** 4 cube beneath Bale Eye within 5
      <br />**Target** All enemies
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 psychic damage; A<  1 warped (save ends)
      <br />★ 12–16 5 psychic damage; A<  2 warped (save ends)
      <br />✸ 17+ 6 psychic damage; A<  3 warped (save ends) 
      <br />**Effect:** A warped creature has all of their characteristic scores reversed. A score of +1 becomes -1, -2 becomes +2, etc."
traits:
  - name: "Lethe"
    desc: "While [[winded]], the bale eye has an edge on strikes, and strikes have an edge against them."
  - name: "Focused Soulsight"
    desc: "Each creature within 5 of the bale eye can’t be hidden from them."


# DEMON FANGLING

name: "DEMON FANGLING"
level: 4
roles:
  - BAND
  - HARRIER
ancestry:
  - Abyssal
  - Demon
ev: 6
stamina: 30
weaknesses: Holy 5
speed: 8
size: 1L /
stability: 0
free_strike: 2
characteristics:
  - +3
  - +2
  - 0
  - +0
  - 0
actions:
  - name: "Tooth! Tusk! Claw!"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 7 damage
      <br />✸ 17+ 9 damage 
      <br />**Effect:** Each enemy adjacent to the fangling takes 2 damage."
maneuvers:
  - name: "Tumbling Gore"
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 8 × 3 line within 1
      <br />**Target** All enemies
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 2 damage; pull 1; A<  1 [[bleeding]] (save ends)
      <br />★ 12–16 3 damage; pull 2; A<  2 [[bleeding]] (save ends)
      <br />✦ 17+ 4 damage; pull 3; A<  3 [[bleeding]] (save ends)"
traits:
  - name: "Made of Teeth"
    desc: "Whenever an enemy makes physical contact with the fangling or uses a melee ability against the fangling, they take 2 damage."
  - name: "Lethe"
    desc: "While [[winded]], the skitirin has an edge on strikes, and strikes have an edge against them."
  - name: "Soulsight"
    desc: "Each creature within 2 of the fangling can’t be hidden from them."


# DEMON GUNGE

name: "DEMON GUNGE"
level: 4
roles:
  - BAND
  - CONTROLLER
ancestry:
  - Abyssal
  - Demon
ev: 6
stamina: 25
weaknesses: Holy 5
speed: 6
size: 3 /
stability: 0
free_strike: 2
characteristics:
  - +3
  - +2
  - +1
  - +2
  - -1
actions:
  - name: "Bilious Expulsion"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Melee, Ranged, Weapon
      <br />**Distance** 1 burst or 3 cube within 5Target One creature or object in the area
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 acid damage; M<  1 [[slowed]] (save ends)
      <br />★ 12–16 7 acid damage; M<  2 [[slowed]] (save ends)
      <br />✸ 17+ 9 acid damage; M<  3 [[restrained]] (save ends) 
      <br />**Effect:** The affected area pools with slime. The slime is difficult terrain for enemies, and an enemy is [[bleeding]] while occupying an affected square."
ta:
  - name: "Spew Slide (Free Triggered Action)"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Area
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The gunge takes damage from a melee strike. 
      <br />**Effect:** The gunge vomits and shifts up to their speed, ignoring any additional effects from the strike. Each square they started in is covered in slime. The slime is difficult terrain for enemies, and an enemy is [[bleeding]] while occupying an affected square."
traits:
  - name: "Lethe"
    desc: "While [[winded]], the gunge has an edge on strikes, and strikes have an edge against them."
  - name: "Soulsight"
    desc: "Each creature within 2 of the gunge can’t be hidden from them."


# DEMON NIKTIN

name: "DEMON NIKTIN"
level: 5
roles:
  - BAND
  - AMBUSHER
ancestry:
  - Abyssal
  - Demon
ev: 7
stamina: 35
weaknesses: Holy 5
speed: 6
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - +2
  - +2
  - +2
  - +1
  - +3
actions:
  - name: "Violent Transformation"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 2 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 3 corruption damage
      <br />★ 12–16 6 corruption damage
      <br />✦ 17+ 7 corruption damage; I<  3 [[dazed]] (save ends) 
      <br />**Effect:** The niktin violently changes shape. The niktin deals an additional 6 damage to each target they were hidden from with their Aggressive Mimicry ability."
maneuvers:
  - name: "Aggressive Mimicry"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Magic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The niktin can become a mundane object the same size or smaller and is hidden. They can change back as a free action."
traits:
  - name: "Lethe"
    desc: "While [[winded]], the niktin has an edge on strikes, and strikes have an edge against them."
  - name: "Soulsight"
    desc: "Each creature within 2 of the niktin can’t be hidden from them."


# DEMON TORMENAUK

name: "DEMON TORMENAUK"
level: 6
roles:
  - BAND
  - BRUTE
ancestry:
  - Abyssal
  - Demon
ev: 8
stamina: 45
weaknesses: Holy 5
speed: 6
size: 1M /
stability: 2
free_strike: 4
characteristics:
  - +3
  - 0
  - 2
  - +1
  - +2
actions:
  - name: "Many Maws"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 9 damage
      <br />✸ 17+ 11 damage; [[grabbed]], target has a bane on escaping the grab 
      <br />**Effect:** While the target is [[grabbed]] by this ability, they take 4 psychic damage at the start of each of the tormenauk’s turns."
maneuvers:
  - name: "Agony Wail"
    desc: "
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 3 burst
      <br />**Target** All enemies
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 4 psychic damage; I<  1 [[dazed]] (save ends)
      <br />★ 12–16 6 psychic damage; I<  2 [[dazed]] (save ends)
      <br />✸ 17+ 8 psychic damage; I<  3 [[dazed]] (save ends) 
      <br />**Effect:** The potency increases by 1 if the target is [[grabbed]] by the tormenauk."
traits:
  - name: "Lethe"
    desc: "While [[winded]], the tormenauk has an edge on strikes, and strikes have an edge against them."
  - name: "Soulsight"
    desc: "Each creature within 2 of the tormenauk can’t be hidden from them."


# LUMBERING EGRESS

name: "LUMBERING EGRESS"
level: 6
roles:
  - LEADER
ancestry:
  - Abyssal
  - Demon
ev: 32
stamina: 180
weaknesses: Holy 5
speed: 6
size: 3 /
stability: 3
free_strike: 7
characteristics:
  - +4
  - -1
  - +1
  - +2
  - +2
actions:
  - name: "Ensnarer Cannon"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** Two creature or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 corruption damage; A<  2 [[restrained]] (save ends)
      <br />★ 12–16 16 corruption damage; A<  3 [[restrained]] (save ends)
      <br />✸ 17+ 19 corruption damage; A<  4 [[restrained]] (save ends) 
      <br />**2 Malice** An ensnarer(s) survives the launch, appearing adjacent to one of the targets. Two ensnarers appear on a tier-3 result."
maneuvers:
  - name: "Demonic Egress"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** —
      <br />**Distance** 3 burst
      <br />**Target** Special 
      <br />**Effect:** Four level 1 demon minions (ensnarer, frenzied, pitling) burst forth from the egress and appear in unoccupied squares. 
      <br />**2 Malice** A level 4 demon minion (orflig, wobalas, grulqin) also bursts forth and appears in an unoccupied square."
  - name: "Abyssal Protectors"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Magic
      <br />**Distance** 5 burst
      <br />**Target** Special 
      <br />**Trigger** The last ally minion on the encounter map dies OR the Egress falls below 25 stamina. 
      <br />**Effect:** A muceron and 2 ensnarers appear anywhere in range. 
      <br />**End Effect:** At the end of their turn, the egress can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
traits:
  - name: "Soulsight"
    desc: "Each creature within 2 of the egress can’t be hidden from them."
va:
  - name: "Frenzied Deluge (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 5 burst
      <br />**Target** All enemies
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 7 corruption damage
      <br />★ 12–16 12 corruption damage
      <br />✸ 17+ 15 corruption damage; a frenzied appears in an unoccupied square adjacent to the target"
  - name: "Fold Space (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 20
      <br />**Target** Self 
      <br />**Effect:** The egress folds into their own portal and teleports to an unoccupied space within distance. Four level 1 demon minions (ensnarer, frenzied, pitling) appear in the space the egress leaves behind."
  - name: "Blood of the Abyss (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 10 × 3 line within 1Target All enemies and objects in the line
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 5 corruption damage; R<  2 [[weakened]] (save ends)
      <br />★ 12–16 10 corruption damage; R<  3 [[weakened]] (save ends)
      <br />✸ 17+ 13 corruption damage; R<  4 [[weakened]] (save ends) 
      <br />**Effect:** The egress recalls and instantly destroys any ally minions on the encounter map. A torrent of churned up minion bodies and blood erupts from the egress, dealing an additional 2 damage for each minion destroyed this way."

# DEVIL CLERK

name: "DEVIL CLERK"
level: 5
roles:
  - MINION
  - BRUTE
ancestry:
  - Devil
  - Infernal
ev: 7 for eight minions
stamina: 10
immunities: Fire 5
speed: 6
size: 1M /
stability: 0
with-captain: Strike damage +2
free_strike: 3
characteristics:
  - +3
  - 0
  - +1
  - +1
  - +2
actions:
  - name: "Quill Pushing"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 damage; push 1
      <br />★ 12–16 6 damage; push 2
      <br />✸ 17+ 7 damage; push 3 
      <br />**Effect:** A target adjacent to 2 or more clerks is [[taunted]] (EoT)."
traits:
  - name: "True Name"
    desc: "If a creature within 10 squares of the clerk speaks the clerk's true name aloud, the clerk loses their fire immunity and the additional effects on their signature action."


# DEVIL NOTARY

name: "DEVIL NOTARY"
level: 5
roles:
  - MINION
  - HEXER
ancestry:
  - Devil
  - Infernal
ev: 7 for eight minions
stamina: 8
immunities: Fire 5
speed: 6
size: 1M /
stability: 0
with-captain: Ranged distance +5
free_strike: 3
characteristics:
  - 0
  - +1
  - +3
  - +1
  - +2
actions:
  - name: "Importunity"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 5
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 fire damage
      <br />★ 12–16 5 fire damage; R<  2 target has a bane on their next strike
      <br />✸ 17+ 6 fire damage; R<  3 target has a bane on their next strike 
      <br />**Effect:** A non  -minion devil within 5 has an edge on their next strike."
traits:
  - name: "True Name"
    desc: "If a creature within 10 squares of the notary speaks the notary's true name aloud, the notary loses their fire immunity and the additional effects on their signature action."


# DEVIL SCRIVENER

name: "DEVIL SCRIVENER"
level: 5
roles:
  - MINION
  - HARRIER
ancestry:
  - Devil
  - Infernal
ev: 7 for eight minions
stamina: 9
immunities: Fire 5
speed: 6 (fly)
size: 1M /
stability: 0
with-captain:
speed: +3
free_strike: 3
characteristics:
  - 0
  - +3
  - +1
  - +1
  - +2
actions:
  - name: "Litigation"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Magic, Melee, Strike
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 corruption damage
      <br />★ 12–16 5 corruption damage; [[slowed]] (EoT)
      <br />✸ 17+ 6 corruption damage; [[slowed]] (EoT) 
      <br />**Effect:** Shift 1."
traits:
  - name: "True Name"
    desc: "If a creature within 10 squares of the scrivener speaks the scrivener’s true name aloud, the scrivener loses their fire immunity and the additional effects on their signature action."


# DEVIL JURIST

name: "DEVIL JURIST"
level: 5
roles:
  - TROOP
  - ARTILLERY
ancestry:
  - Devil
  - Infernal
ev: 28
stamina: 120
immunities: Fire 5
speed: 6 (fly)
size: 1M /
stability: 0
free_strike: 7
characteristics:
  - 0
  - +2
  - +1
  - +1
  - +3
actions:
  - name: "Fire and Brimstone"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 12
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 fire damage
      <br />★ 12–16 15 fire damage; A<  2 burning (save ends)
      <br />✸ 17+ 18 fire damage; A<  3 burning (save ends) 
      <br />**Effect:** A burning creature or object takes 1d6 fire damage at the start of each of their turns until the condition ends.
      <br />**1 Malice** The jurist can target one additional creature or object for each malice spent."
  - name: "Dismissal with Prejudice"
    desc:
      "
      <br />**Keywords** Area, Magic
      <br />**Distance** 2 burst
      <br />**Target** Each enemy in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 damage; slide 1
      <br />★ 12–16 10 damage; slide 3
      <br />✸ 17+ 12 damage; slide 5 
      <br />**Effect:** M<  2 the target slides an additional 3 squares."
maneuvers:
  - name: "Ashes to Ashes"
    desc: "
      <br />**Keywords** Magic
      <br />**Distance** Ranged 12
      <br />**Target** 1 burning creature 
      <br />**Effect:** The target takes 6 fire damage."
ta:
  - name: "Devilish Charm (Triggered Action)"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** Magic
      <br />**Distance** Ranged 5
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature targets the jurist with a strike. 
      <br />**Effect:** The target makes a Might test.
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 The jurist chooses a new target for the strike
      <br />★ 12–16 The jurist halves the incoming damage
      <br />✦ 17+ The target is [[dazed]] (EoT)"
traits:
  - name: "Hellfire"
    desc: "Fire damage dealt by the jurist ignores immunity."
  - name: "True Name"
    desc: "If a creature within 10 squares of the jurist speaks the jurist’s true name aloud, the jurist loses their immunities, the additional effects on their signature action, and their Devilish Charm ability."


# DEVIL LEGATE

name: "DEVIL LEGATE"
level: 5
roles:
  - TROOP
  - DEFENDER
ancestry:
  - Devil
  - Infernal
ev: 28
stamina: 160
immunities: Fire 5
speed: 6
size: 1M /
stability: 2
free_strike: 6
characteristics:
  - +3
  - +1
  - 0
  - +1
  - +2
actions:
  - name: "Infernal Pike"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage
      <br />★ 12–16 14 damage; A<  2 [[slowed]] (save ends)
      <br />✸ 17+ 17+ damage; A<  3 [[slowed]] (save ends) 
      <br />**Effect:** If the targets are adjacent to each other, this ability deals an additional 3 damage."
  - name: "Writ of Execution"
    desc:
      "
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 6 damage; M<  1 [[prone]]
      <br />★ 12–16 11 damage; M<  2 [[prone]] can’t stand (save ends)
      <br />✦ 17+ 14 damage; M<  3 [[prone]] can’t stand (save ends) 
      <br />**Effect:** If the legate charges while using this ability, they ignore difficult terrain and target each creature and object they move through with the power roll (but not its additional effects)."
maneuvers:
  - name: "Law and Order"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** 1 creature 
      <br />**Effect:** The target is [[taunted]] by the legate (save ends). The legate can only have one creature [[taunted]] at a time."
ta:
  - name: "Devilish Charm"
    desc:
      <br />**Cost** 2 Malice
      <br />**Keywords** Magic
      <br />**Distance** Ranged 5
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature targets the legate with a strike. 
      <br />**Effect:** The target makes a Might test.
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 The legate chooses a new target for the strike
      <br />★ 12–16 The legate halves the incoming damage
      <br />✦ 17+ The target is [[dazed]] (EoT) Hellish Bailiff The legate has damage immunity 3 while in one of the nine Hells or within 10 squares of a non minion devil that is a higher level than them."
traits:
  - name: "True Name"
    desc: "If a creature within 10 squares of the legate speaks the legate’s true name aloud, the legate loses their immunities, the additional effects on their signature action, and their Devilish Charm ability."


# DEVIL ADJUDICATOR

name: "DEVIL ADJUDICATOR"
level: 6
roles:
  - TROOP
  - CONTROLLER
ancestry:
  - Devil
  - Infernal
ev: 32
stamina: 140
immunities: Fire 5
speed: 6 (fly)
size: 1M /
stability: 1
free_strike: 7
characteristics:
  - 0
  - +1
  - +2
  - +1
  - +3
actions:
  - name: "Infernal Injunction"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 fire damage; I<  1 [[frightened]] (save ends)
      <br />★ 12–16 15 fire damage; I<  2 [[frightened]] (save ends)
      <br />✸ 17+ 18 fire damage; I<  3 [[frightened]] (save ends) 
      <br />**Effect:** The adjudicator can slide a target [[frightened]] by this ability 2 squares."
  - name: "Adjudicator’s Interdiction"
    desc: "
      <br />**Keywords** Magic
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature 
      <br />**Effect:** The target makes a Might test.
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 [[slowed]], bane on power rolls, can’t regain stamina (save ends)
      <br />★ 12–16 [[slowed]], bane on power rolls (save ends)
      <br />✦ 17+ [[slowed]] (save ends)"
maneuvers:
  - name: "Quid Pro Quo"
    desc: "
      <br />**Keywords** Magic
      <br />**Distance** Ranged 10
      <br />**Target** 1 ally or 1 [[frightened]] creature 
      <br />**Effect:** The adjudicator switches places with the target."
ta:
  - name: "Devilish Charm"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** Magic
      <br />**Distance** Ranged 5
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature targets the adjudicator with a strike. 
      <br />**Effect:** The target makes a Might test.
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 The adjudicator chooses a new target for the strike
      <br />★ 12–16 The adjudicator halves the incoming damage
      <br />✦ 17+ The target is [[dazed]] (EoT)"
traits:
  - name: "Vexatious Litigation"
    desc: "A creature has -2 on saving throws while within 10 of the adjudicator if their Presence score is lower than the adjudicator’s."
  - name: "True Name"
    desc: "If a creature within 10 squares of the adjudicator speaks the adjudicator’s true name aloud, the adjudicator loses their immunities, the additional effects on their signature action, and their Devilish Charm ability."


# DEVIL MAGISTRATE

name: "DEVIL MAGISTRATE"
level: 6
roles:
  - TROOP
  - HARRIER
ancestry:
  - Devil
  - Infernal
ev: 32
stamina: 160
immunities: Fire 5
speed: 7
size: 1M /
stability: 0
free_strike: 7
characteristics:
  - +1
  - +3
  - 0
  - +1
  - +2
actions:
  - name: "Edge of the Law"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 damage
      <br />★ 12–16 15 damage
      <br />✸ 17+ 18 damage; R<  3 [[dazed]] (save ends) 
      <br />**Effect:** The magistrate can shift up to 3 squares before or after using this ability, or between targets."
  - name: "Verdict"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature
      <br />✸ ≤11 11 damage
      <br />★ 12–16 17+ damage
      <br />`dice: 2d10 + 3`
      <br />✦ 17+ 21 damage 
      <br />**Effect:** This ability has a double edge if the magistrate was hidden before using this ability and deals an additional 5 damage if the target is [[dazed]]."
maneuvers:
  - name: "Justice Turns Its Gaze"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The magistrate becomes hidden, even if they are being observed."
ta:
  - name: "Devilish Charm"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** Magic
      <br />**Distance** Ranged 5
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature targets the magistrate with a strike. 
      <br />**Effect:** The target makes a Might test.
      <br />✸ ≤11 The magistrate chooses a new target for the strike
      <br />★ 12–16 The magistrate halves the incoming damage
      <br />✦ 17+ The target is [[dazed]] (EoT) Leading If the magistrate moves away from an enemy who is adjacent to one of the magistrate’s allies, the movement is considered shifting."
traits:
  - name: "True Name"
    desc: "If a creature within 10 squares of the magistrate speaks the magistrate’s true name aloud, the magistrate loses their immunities, the additional effects on their signature action, and their Devilish Charm ability."


# ARCHDEVIL

name: "ARCHDEVIL"
level: 6
roles:
  - LEADER
ancestry:
  - Devil
  - Infernal
ev: 32
stamina: 181
immunities: Fire 8
speed: 7 (fly)
size: 1M /
stability: 2
free_strike: 6
characteristics:
  - +1
  - +3
  - +2
  - +1
  - +4
actions:
  - name: "Infernal Decree"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 12
      <br />**Target** Three creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 10 damage; P<  2 the target can’t hide (save ends)
      <br />★ 12–16 15 damage; P<  3 the target can’t hide (save ends)
      <br />✸ 17+ 19 damage; P<  4 the target can’t hide (save ends) 
      <br />**Cost** 2 Malice 
      <br />**EFfect** Each devil has an edge to strike a target that can’t hide."
maneuvers:
  - name: "Compel the Jury"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 12
      <br />**Target** 2 creatures
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 I< 2 charmed (save ends)
      <br />★ 12–16 I< 3 charmed (save ends)
      <br />✸ 17+ I< 4 charmed (save ends) 
      <br />**Effect:** Until the condition ends, a charmed creature considers the archdevil an ally, and the archdevil can spend 1 malice on their turn to force move a charmed creature up to 3 squares."
ta:
  - name: "Devilish Suggestion:
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** Magic
      <br />**Distance** Ranged 5
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature targets the archdevil with a strike. 
      <br />**Effect:** The target makes a Might test.
      <br />`dice: 2d10 + 4`
      <br />✸ ≤11 Charmed (save ends) (see Compel the Jury)
      <br />★ 12–16 The archdevil chooses a new target for the strike
      <br />✦ 17+ The archdevil halves the incoming damage 
traits:
  - name: "End Effect"
    desc: "At the end of their turn, the archdevil can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "True Name"
    desc: "If a creature within 10 squares of the archdevil speaks the archdevil’s true name aloud, the archdevil loses their immunities, the additional effects on their signature attack, and their Devilish Suggestion triggered action."
va:
  - name: "Welcome, Friends (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 burst
      <br />**Target** Each enemy in burst 
      <br />**Effect:** Each target makes a Might test.
      <br />`dice: 2d10 +
      <br />✦ ≤11 15 psychic damage; charmed (save ends)
      <br />★ 12–16 12 psychic damage; charmed (save ends)
      <br />✸ 17+ 7 psychic damage "
  - name: "Heed My Commands! (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self and 5 burst
      <br />**Target** Self and each allies in the burst 
      <br />**Effect:** Each target shifts up to their speed. The archdevil can force move each charmed creature up to half their speed."
  - name: "Deceptive Stratagem (Villain Action 3)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 12
      <br />**Target** 1 ally or charmed creature 
      <br />**Effect:** The archdevil swaps places with the target. Then, each ally and charmed creature within 12 of the archdevil make a free strike against a target of the archdevil’s choice."

# AEOLYXRIA THE UNCANNY

name: "AEOLYXRIA THE UNCANNY"
level: 6
roles:
  - TROOP
  - CONTROLLER
ancestry:
  - Draconian
  - Dragon
  - Humanoid
ev: 32
stamina: 140
immunities: poison 6
speed: 5 (flying)
size: 1M /
stability: 2
free_strike: 7
characteristics:
  - -1
  - +2
  - +4
  - +3
  - +1
actions:
  - name: "Spittlesplash"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** 2 enemies
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 poison damage; M< 1 [[slowed]] (save ends)
      <br />★ 12–16 15 poison damage; M< 2 [[slowed]] (save ends)
      <br />✸ 17+ 18 poison damage; M< 3 [[slowed]] (save ends)"
  - name: "Experimental Treasure"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 The target regains 10 stamina
      <br />★ 12–16 12 corruption damage; A< 2 [[weakened]] (save ends)
      <br />✸ 17+ 12 lightning damage; A< 2 [[bleeding]] (save ends) 
      <br />**Effect:** The first time in an encounter that Lydixavus rolls a result with this ability, she can choose that result instead of rolling whenever she uses this ability for the rest of the encounter. 
      <br />**2+ Malice** Aeolyxria targets an additional creature or object for every 2 malice spent."
maneuvers:
  - name: "Elevate!"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** 1 cube within 5
      <br />**Target** Special 
      <br />**Effect:** The ground is elevated by 5 squares, creating a pillar of dirt. Each creature in the affected area is lifted along with it. 
      <br />**1+ Malice** Aeolyxria creates an additional pillar for each malice spent."
ta:
  - name: "Blood For Blood"
    desc: "
      <br />**Keywords** Ranged, Weapon
      <br />**Distance** Ranged 5
      <br />**Target** One creature 
      <br />**Trigger** The target inflicts the [[bleeding]] condition on an ally.
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 poison damage; A< 2 [[bleeding]] (save ends)
      <br />★ 12–16 12 poison damage; A< 3 [[bleeding]] (save ends)
      <br />✸ 17+ 15 poison damage; [[bleeding]] (save ends)"
traits:
  - name: "That’s Our Opening!"
    desc: "The Director gains 1 malice whenever Aeolyxria inflicts a condition on an enemy."


# LOKRATIX THE MORNINGSTAR

name: "LOKRATIX THE MORNINGSTAR"
level: 6
roles:
  - TROOP
  - HARRIER
ancestry:
  - Draconian
  - Dragon
  - Humanoid
ev: 32
stamina: 160
immunities: acid 6
speed: 8 (flying)
size: 1M /
stability: 2
free_strike: 7
characteristics:
  - +1
  - +3
  - +1
  - +2
  - +2
actions:
  - name: "Skewer"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 damage
      <br />★ 12–16 15 damage; M< 1 [[slowed]] (save ends)
      <br />✸ 17+ 18 damage; M< 2 [[slowed]] (save ends) 
      <br />**Effect:** Lokratix deals 6 damage to each creature or object in a line up to two squares behind the target."
  - name: "Acidic Stun"
    desc:
      "
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 3 × 1 line within 1
      <br />**Target** All enemies in the line
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 acid damage; M< 1 [[dazed]] (save ends)
      <br />★ 12–16 12 acid damage; M< 2 [[dazed]] (save ends)
      <br />✸ 17+ 15 acid damage; M< 3 [[dazed]] (save ends) 
      <br />**Effect:** Lokratix deals an additional 6 damage on abilities targeting enemies [[dazed]] by this ability."
maneuvers:
  - name: "Takeoff"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Lokratix lifts off from the ground and flies up to her speed. All creatures adjacent to the square she took off from are A < 2 knocked [[prone]]."
ta:
  - name: "Stay Back!"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 2
      <br />**Target** One creature 
      <br />**Trigger**
      <br />**Target** enters a square within distance.
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 acid damage; A< 1 speed is 0 (EoT)
      <br />★ 12–16 12 acid damage; A< 2 speed is 0 (EoT)
      <br />✸ 17+ 15 acid damage; A< 3 speed is 0 (EoT) Flighty When Lokratix deals damage to an enemy, the enemy can’t use her as the trigger for any of their triggered actions until the start of her next turn."
traits:
  - name: "Absorbing Scales"
    desc: "When Lokratix takes damage of a type she has an immunity for, she has damage immunity 6 against the next strike made against her."


# LYDIXAVUS THE DEADEYE

name: "LYDIXAVUS THE DEADEYE"
level: 6
roles:
  - TROOP
  - ARTILLERY
ancestry:
  - Draconian
  - Dragon
  - Humanoid
ev: 32
stamina: 140
immunities: cold 6
speed: 5 (flying)
size: 1M /
stability: 2
free_strike: 7
characteristics:
  - -1
  - +3
  - +3
  - +3
  - +1
actions:
  - name: "Breathsnipe"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 15
      <br />**Target** 1 enemy
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 cold damage
      <br />★ 12–16 16 cold damage; the target has a bane on their next strike.
      <br />✸ 17+ 19 cold damage; the target has a double bane on their next strike."
  - name: "Ice Lob"
    desc:
      "
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 2 cube within 10
      <br />**Target** All enemies and objects in the cube
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 cold damage; M< 1 [[dazed]] (save ends)
      <br />★ 12–16 13 cold damage; M< 2 [[dazed]] (save ends)
      <br />✸ 17+ 16 cold damage; M< 3 [[dazed]] (save ends) Parting Gift (Maneuver)
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Lydixavus flies up to their speed, leaving a size 1S ice mine in the square they took off from. The ice mine explodes when an enemy enters a square containing it. Lydixavus rolls power for an exploding ice mine as if they used their Ice Lob ability, targeting the triggering creature and each creature and object within 1 of the ice mine."
ta:
  - name: "Wasn’t Aiming For You"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** Lydixavus gets a Tier 1 result on their signature action 
      <br />**Effect:** Lydixavus uses an additional signature action targeting a creature within 5 of the original target."
traits:
  - name: "Scorekeeping Scales"
    desc: "Lydixavus knows the location of every creature who has ever dealt damage to them and has [[Draw Steel Rules#LINE OF EFFECT|line of effect]] to each of these creatures while they’re within 20 of Lydixavus."


# MYXOVIDAN THE SINTAKER

name: "MYXOVIDAN THE SINTAKER"
level: 6
roles:
  - TROOP
  - HEXER
ancestry:
  - Draconian
  - Dragon
  - Humanoid
ev: 46
stamina: 140
immunities: corruption 6
speed: 5 (flying)
size: 1M /
stability: 2
free_strike: 7
characteristics:
  - -1
  - +3
  - +2
  - +2
  - +1
actions:
  - name: "Breaking Palm"
    desc: "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 enemies
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 damage; M< 1 [[weakened]] (save ends)
      <br />★ 12–16 15 damage; M< 2 [[weakened]] (save ends)
      <br />✸ 17+ 18 corruption damage; M< 3 [[weakened]] (save ends) 2 Malice Myxovidan regains stamina equal to half the damage dealt."
  - name: "Expunging Exhalation"
    desc: "
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 2 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 +
      <br />✦ ≤11 7 corruption damage; M< 1 condemned (save ends)
      <br />★ 12–16 12 corruption damage; M< 2 condemned (save ends)
      <br />✸ 17+ 15 corruption damage; M< 3 condemned (save ends) 
      <br />**Effect:** A condemned creature has corruption weakness 3 until the condition ends."
maneuvers:
  - name: "Step and Swap"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 3
      <br />**Target** 1 ally 
      <br />**Effect:** Myxovidan and the target shift and swap places."
ta:
  - name: "Anyone Can Do That"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** An adjacent creature damages Myxovidan 
      <br />**Effect:** Myxovidan perfectly recreates the damaging move. If the move requires a Power Roll, Myxovidan rolls power using his stats. If Myxovidan gets a higher tier on this roll than the triggering creature, the Director gains 2 Malice."
traits:
  - name: "Stench of Death"
    desc: "Whenever an enemy regains stamina while within 5 of Myxovidan, they regain 3 less stamina."


# PHRRYGALAX THE SUBDUER

name: "PHRRYGALAX THE SUBDUER"
level: 6
roles:
  - TROOP
  - BRUTE
ancestry:
  - Draconian
  - Dragon
  - Humanoid
ev: 32
stamina: 180 Immunities fire 6
speed: 5 (flying)
size: 1L /
stability: 5
free_strike: 7
characteristics:
  - +3
  - +2
  - +0
  - +0
  - +3
actions:
  - name: "Baneful Blade"
    desc: "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 damage
      <br />★ 12–16 16 damage; M< 1 [[bleeding]] (save ends)
      <br />✸ 17+ 19 damage; M< 2 3 damage, [[bleeding]] (save ends) "
  - name: "Spinning Spit"
    desc: "
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 1 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 7 fire damage
      <br />★ 12–16 13 fire damage
      <br />✸ 17+ 16 fire damage "
maneuvers:
  - name: "Heavy Landing"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Phrrygalax flies up to his speed and lands in an unoccupied space on the ground. Each creature adjacent to where he lands is A< 2 knocked [[prone]]."
ta:
  - name: "Armor of the Ancients"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** Phrrygalax takes acid, cold, corruption, fire, lightning, or poison damage. 
      <br />**Effect:** Phrrygalax absorbs the damage instead, recovering stamina equal to the damage dealt. Phrrygalax swaps his current immunity with the triggering damage type."
  - name: "STILL YOUR TONGUE! (Free Triggered Action)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** Phrrygalax hears a creature within 5 reciting the oath of Good King Omund’s Dragon Phalanx 
      <br />**Effect:** Phrrygalax shifts up to his speed and uses Baneful Blade against the enemy, dealing an additional 7 damage."
traits:
  - name: "Oathbreaker’s Vengeance"
    desc: "When Phrrygalax fails a saving throw, he deals an additional 7 damage on his next strike."

# DORZINUUTH THE BASE

name: "DORZINUUTH THE BASE"
level: 6
roles:
  - LEADER
ancestry:
  - Draconian
  - Dragon
  - Humanoid
ev: 32
stamina: 180
immunities: lightning 6
speed: 5 (flying, hover)
size: 1L /
stability: 6
free_strike: 7
characteristics:
  - +4
  - +1
  - +1
  - +2
  - +3
actions:
  - name: "Punishing Flail"
    desc: "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 damage; M< 2 [[prone]]
      <br />★ 12–16 16 damage; M< 3 [[prone]]
      <br />✸ 17+ 19 damage; M< 4 [[prone]] 2 Malice M< 4 [[bleeding]] (save ends)."
maneuvers:
  - name: "I’ll Cut A Path"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 5 × 1 line Within 1
      <br />**Target** All enemies in the line 
      <br />**Effect:** Dorzinuuth shifts to an unoccupied square adjacent to the end of the line and then rolls power.
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 12 damage; M< 3 [[prone]]
      <br />✸ 17+ 15 damage; M< 4 [[prone]] "
ta:
  - name: "Watch Your Six!"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** 1 Ally 
      <br />**Trigger** An ally within distance takes damage while Dorzinuuth isn’t flying. 
      <br />**Effect:** Dorzinuuth shields his ally with his wings, halving the damage. 
      <br />**End Effect:** At the end of his turn, Dorzinuuth can take 10 damage to end one save ends effect affecting him. This damage can’t be reduced in any way."
traits:
  - name: "Sheltering Wings"
    desc: "Strikes made against Dorzinuuth have a bane while he isn’t flying."
  - name: "Remember Your Oath"
    desc: "After Dorzinuuth hears a character recite the Dragon Phalanx oath, he has a bane on all strikes made against that character."
va:
  - name: "Roaring Gambit (Villain Action 1)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** 5 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** Dorzinuuth lets loose a powerful roar. Each target must make a Might test.
      <br />`dice: 2d10 + 4`
      <br />✸ ≤11 [[frightened]] (save ends)
      <br />★ 12–16 [[frightened]] (EoT)
      <br />✦ 17+ no effect 
      <br />**Effect:** Each ally within distance has an edge on their next attack."
  - name: "Wings of Second Wind (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self and 10 burst
      <br />**Target** Self and all allies 
      <br />**Effect:** Each target shifts or flies up to their speed and regains 10 stamina."
  - name: "Snap, Crackle, Pop (Villain Action 3)"
    desc: "
      <br />**Keywords** Magic, Melee
      <br />**Distance** 5 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Dorzinuuth covers all allies in an electrifying mesh. Whenever a target takes damage from a melee strike or ability, the attacker takes 6 lightning damage."

# THORN DRAGON

name: "THORN DRAGON"
level: 2
roles:
  - SOLO
ancestry:
  - Dragon
  - Elemental
ev: 40
stamina: 250
immunities: poison 5
speed: 8 (fly)
size: 3 /
stability: 6
free_strike: 5
characteristics:
  - +2
  - +3
  - -1
  - +1
  - +2
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The dragon takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the dragon can take one action and one maneuver per turn. "
  - name: "End Effect"
    desc: " At the end of their turn, the dragon can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Withering Wyrmscale Aura"
    desc: " The dragon’s scales emit a 2 aura barrier of withering green magic. When a creature in the affected area regains stamina, they only regain half the stamina. A [[winded]] creature who enters an affected square or starts their turn there takes 1d6 poison damage."
  - name: "Thorn Dragon’s Domain"
    desc: " If the encounter map is a location the dragon has occupied for 1 week or more, each space on the map is considered difficult terrain for all creatures except for the dragon. Each such creature who moves within the area takes 1 damage for each square they enter. A creature [[restrained]] in this area is also [[bleeding]]."
actions:
  - name: "Virulent Breath"
    desc: "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 10 x 1 line within 1
      <br />**Target** All enemies 
      <br />**Effect:** Each target makes a Might test.
      <br />`dice: 2d10 +
      <br />✸ ≤11 12 poison damage; P< 4 dragonsealed (save ends)
      <br />★ 12–16 9 poison damage; P< 3 dragonsealed (save ends)
      <br />✦ 17+ 5 poison damage; P< 2 dragonsealed (save ends) 
      <br />**Effect:** Until the condition ends, a creature dragonsealed by the dragon has their wounds overtaken by nettles and thorns, and they take an additional die of damage from conditions that deal damage, the dragon’s Wyrmscale Aura, and the dragon’s Malign Thicket Villain Action."
  - name: "Spinous Tail Swing"
    desc: "
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** Two enemies or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; push 2
      <br />★ 12–16 12 damage; push 4
      <br />✸ 17+ 15 damage; push 8 3 Malice Each target is A< 3 [[bleeding]] (save ends)."
maneuvers:
  - name: "Provoking Nettles (Free Maneuver)"
    desc: " Once per turn, the dragon shifts 5 and can move through enemies at normal speed. The first time the dragon passes through a creature’s space during this movement, the creature takes 3 damage."
  - name: "Investiture of Verdure"
    desc: "
      <br />**Cost** 5 Malice
      <br />**Keywords** Area
      <br />**Distance** 10 burst
      <br />**Target** All dragonsealed enemies 
      <br />**Effect:** Each target is pulled 5 toward the dragon. For each creature pulled, the dragon gains 5 temporary stamina."
ta:
  - name: "Prickly Situation (Triggered Action)"
    desc: "
      <br />**Keywords** Magic
      <br />**Distance** 10
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature successfully saves to end their dragonsealed condition. 
      <br />**Effect:** The target is pulled 5 toward the dragon and is [[restrained]] (EoT)."
  - name: "Thorny Scales (Free Triggered Action)"
    desc: " ◆ 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature deals damage to the dragon with a melee strike. 
      <br />**Effect:** The dragon makes a free strike against the target. The target is M < 2 [[bleeding]] (EoT)."
va:
  - name: "Briar Bindings (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 4 burst
      <br />**Target** All enemies
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 damage; A< 2 [[restrained]] (save ends)
      <br />★ 12–16 9 damage; A< 3 [[restrained]] (save ends)
      <br />✸ 17+ 12 damage; A< 4 [[restrained]] (save ends)  "
  - name: "Thorned Armor (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The dragon grows longer, sharper thorns upon their scales. A creature who targets the dragon with a melee strike takes 3 damage."
  - name: "Malign Thicket (Villain Action 3)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The dragon’s domain becomes imbued with deadly poison. A creature who takes damage from the dragon’s domain or from striking the dragon takes an additional 1d6 poison damage."

# GLOOM DRAGON

name: "GLOOM DRAGON"
level: 4
roles:
  - SOLO
ancestry:
  - Dragon
  - Elemental
ev: 60
stamina: 350
immunities: psychic 5
speed: 8 (fly, hover)
size: 4 /
stability: 4
free_strike: 6
characteristics:
  - +2
  - +4
  - +1
  - +3
  - +4
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The dragon takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the dragon can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the dragon can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Gloaming Wyrmscale Aura"
    desc: "The dragon’s scales emit a 4 aura of dark fog. An enemy who starts their turn in an affected area takes 2 psychic damage, and the dragon deals an additional 2 psychic damage on abilities per number of enemies in the aura (to a maximum of 6)."
actions:
  - name: "Breath of Brume"
    desc: "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 4 cube within 10
      <br />**Target** All enemies and objects 
      <br />**Effect:** Each target makes a Might test.
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 6 cold damage; P< 3 dragonsealed (save ends)
      <br />★ 12–16 11 cold damage; P< 4 dragonsealed (save ends)
      <br />✸ 17+ 14 cold damage; P< 5 dragonsealed (save ends) 
      <br />**Effect:** The affected area becomes an area of magical darkness. The dragon ignores concealment granted by the darkness. A creature dragonsealed by the dragon has psychic weakness 3 and cold weakness 3 until the condition ends."
  - name: "Phantom Tail Swing"
    desc: "
      <br />**Keywords** Charge, Magic, Melee, Strike
      <br />**Distance** Melee 3
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 10 psychic damage; pull 2
      <br />★ 12–16 15 psychic damage; pull 4
      <br />✸ 17+ 18 psychic damage; pull 6 
      <br />**2 Malice** The pull becomes a vertical slide. 
maneuvers:
  - name: "Shadow Skulk (Free Maneuver)"
    desc: "- Once per turn, the dragon shifts up to their speed and leaves behind a 4 cube area of magical darkness. The dragon ignores concealment granted by the darkness. An enemy that ends their turn in the affected area is I< 3 [[frightened]] of the dragon."
  - name: "Visions in the Dark"
    desc: "
      <br />**Cost** 5 Malice
      <br />**Keywords** Area, Magic
      <br />**Distance** 10 burst
      <br />**Target** All dragonsealed enemies 
      <br />**Effect:** Each target takes 3 psychic damage and is I< 3 compelled to immediately make a free strike against one of their allies within range as they hallucinate a threat."
ta:
  - name: "Shroud (Triggered Action)"
    desc: " 
      <br />**Cost** 1 Malice
      <br />**Keywords** Area, Magic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The dragon takes damage. 
      <br />**Effect:** The dragon reduces the damage by 2 for each enemy in their aura."
  - name: "Encroaching Darkness (Free Triggered Action)"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** Special 
      <br />**Trigger** A creature moves. 
      <br />**Effect:** The dragon moves two cubes of magical darkness up to 10."
  - name: "Gloom Dragon’s Domain"
    desc: "If the encounter map is a location the dragon has occupied for 1 week or more, illusory magic drenches the air such that even the scenery emanates malice. Each creature other than the dragon in the affected area has a -2 on saving throws made to end the [[frightened]] condition. A [[frightened]] enemy in the affected area takes an additional 3 psychic damage whenever they take damage."
va:
  - name: "Enveloping Umbrage (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 burst
      <br />**Target** All enemies
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 Pull 2; I< 3 [[frightened]] (EoT)
      <br />★ 12–16 Push 4; I< 4 [[frightened]] (save ends)
      <br />✸ 17+ Push 6; I< 5 [[frightened]] (save ends) Pall of Nightmares."
  - name: "(Villain Action 2)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 10 burst
      <br />**Target** All dragonsealed enemies
      <br />`dice: 2d10 +
      <br />✦ ≤11 6 psychic damage
      <br />★ 12–16 11 psychic damage
      <br />✸ 17+ 14 psychic damage 
      <br />**Effect:** The targets are I < 4 [[dazed]] as they are assaulted by their hallucinations."
  - name: "Absence of All Light (Villain Action 3)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Special
      <br />**Target** Self 
      <br />**Effect:** The dragon disappears, then reappears anywhere on the encounter map, as do three hallucinatory versions of it at other points on the encounter map (the director determines which one is real). The dragon and each hallucinatory version of it immediately uses Breath of Brume. A creature who deals damage to a hallucination of the dragon causes it to immediately dissipate."

# CRUCIBLE DRAGON

name: "CRUCIBLE DRAGON"
level: 6
roles:
  - SOLO
ancestry:
  - Dragon
  - Elemental
ev: 80
stamina: 450
immunities: fire 6
speed: 8
size: 4 /
stability: 6
free_strike: 7
characteristics:
  - +4
  - -1
  - +3
  - +3
  - +2
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The dragon takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the dragon can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the dragon can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Magnetized Wyrmscale Aura"
    desc: "The dragon’s scales emit a 3 aura of magnetism that affects metal equipment and objects A creature that enters an affected square or starts their turn there while slagged or wearing metal is pulled 2 towards the dragon and is M< 3 unable to move away."
  - name: "Crucible Dragon’s Domain"
    desc: "If the encounter map is a location the dragon has occupied for 1 week or more, melted metal and blades coat nearly every wall and column. A creature or object other than the dragon that comes into physical contact with an affected surface takes 5 damage. Whenever an enemy uses an ability that deals electric damage, they take 1d6 damage and deal half the amount of damage to each adjacent enemy and object."
actions:
  - name: "Slag Spew"
    desc: "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 10 × 2 line within 1
      <br />**Target** All creatures and objects 
      <br />**Effect:** Each target makes an Might test.
      <br />✸ ≤11 13 fire damage; A< 4 slagged (save ends)
      <br />★ 12–16 10 fire damage; A< 3 slagged (save ends)
      <br />`dice: 2d10 + 4`
      <br />✦ 17+ 6 fire damage; A< 2 slagged (save ends) 
      <br />**Effect:** Until the condition ends, a slagged target is coated in molten metal, takes 2d6 fire damage at the start of each of their turns, and is M< 3 [[restrained]] (save ends) whenever they take cold damage."
  - name: "Forge Hammer Tail Slam"
    desc: "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 damage; M< 2 [[prone]]
      <br />★ 12–16 17+ damage; M< 3 [[prone]]
      <br />✸ 17+ 20 damage; M< 4 [[prone]] 
      <br />**Effect:** The dragon makes a free strike against each slagged target knocked [[prone]] by this ability. 
      <br />**1 Malice** The hammerhead freezes, dealing 1d6 cold damage."
maneuvers:
  - name: "Thermodynamic Flight"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Area, Melee
      <br />**Distance** 2 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** The dragon expels blistering steam straight down, dealing 7 fire damage to each target. The dragon then shifts up to their speed vertically and adds the fly keyword to their movement until the end of the round."
  - name: "Heat Buffer (Free Maneuver)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self (while flying)
      <br />**Target** Self 
      <br />**Effect:** The dragon can use this ability once per round. They continue to give off steam to extend the duration of their flight for an additional round. Each creature under the dragon when they use this ability takes 7 fire damage."
ta:
  - name: "Polarize Aura"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 burst
      <br />**Target** All creatures and objects 
      <br />**Trigger** The dragon is targeted by 2 melee attacks in a single turn.
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 push 5
      <br />★ 12–16 push 7
      <br />✸ 17+ push 10 (ignores stability) "
  - name: "Hammer and Anvil (Free Triggered Action)"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The dragon starts their turn or moves while flying. 
      <br />**Effect:** The dragon plumets to the ground and uses Forge Hammer Tail. They deal an additional 4 damage for each square they fell."
va:
  - name: "Heart of the Forge (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 6 burst
      <br />**Target** All enemies
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 4 fire damage; I< 2 [[frightened]] (save ends)
      <br />★ 12–16 6 fire damage; I< 3 [[frightened]] (save ends)
      <br />✸ 17+ 8 fire damage; I< 4 [[frightened]] (save ends) 
      <br />**Effect:** The dragon roars, venting scorching air in every direction."
  - name: "Subdermal Shielding (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Shields embedded under their scales emerge, giving the dragon damage immunity 6 at the start of each round for the rest of the encounter. The dragon loses this immunity for the rest of the round if they take any damage."
  - name: "Polarity Chaos (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Magic, Melee, Ranged
      <br />**Distance** 10 burst
      <br />**Target** All creatures and objects in the burst 
      <br />**Effect:** The dragon charges their wyrmscale aura, whipping metal into a magnetized frenzy. Each target makes an Might test.
      <br />`dice: 2d10 + 4`
      <br />✸ ≤11 16 damage; M< 4 pull 10 or push 10
      <br />★ 12–16 13 damage; M< 3 pull 8 or push 8
      <br />✦ 17+ 7 damage, M< 2 pull 5 or push 5"

# DWARF AXETHROWER

name: "DWARF AXETHROWER"
level: 1
roles:
  - MINION
  - DEFENDER
ancestry:
  - Dwarf
  - Humanoid
ev: 3 for eight minions
stamina: 7
speed: 5
size: 1M /
stability: 2
with-captain: 2 temporary
stamina:
free_strike: 1
characteristics:
  - +1
  - 0
  - 0
  - +2
  - 0
actions:
  - name: "Whistling Axes"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage
      <br />★ 12–16 2 damage
      <br />✸ 17+ 3 damage; an ally adjacent to the target can make a free strike 
      <br />**Effect:** The target can’t use triggered actions until the start of the next round."


# DWARF CATCHPOLE

name: "DWARF CATCHPOLE"
level: 1
roles:
  - MINION
  - BRUTE
ancestry:
  - Dwarf
  - Humanoid
ev: 3 for eight minions
stamina: 7
speed: 5
size: 1M /
stability: 2
with-captain: 2 temporary
stamina:
free_strike: 2
characteristics:
  - +2
  - 0
  - 0
  - 0
  - 0
actions:
  - name: "Maul"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage; [[grabbed]] or [[prone]] 
      <br />**Effect:** The catchpole deals an additional 2 damage to [[restrained]] targets."

# DWARF DRIVER

name: "DWARF DRIVER"
level: 1
roles:
  - MINION
  - HARRIER
ancestry:
  - Dwarf
  - Humanoid
ev: 3 for eight minions
stamina: 6
speed: 7
size: 1M /
stability: 1
with-captain: 2 temporary
stamina:
free_strike: 1
characteristics:
  - +2
  - +1
  - 0
  - 0
  - 0
actions:
  - name: "Handaxes"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage; push 1
      <br />★ 12–16 2 damage; push 2
      <br />✸ 17+ 3 damage; push 4 
      <br />**Effect:** A target [[restrained]] by a dwarf can be pushed by this ability."


# DWARF HUNTER

name: "DWARF HUNTER"
level: 1
roles:
  - MINION
  - SUPPORT
ancestry:
  - Dwarf
  - Humanoid
ev: 3 for eight minions
stamina: 6
speed: 5
size: 1M /
stability: 1
with-captain: 2 temporary
stamina:
free_strike: 1
characteristics:
  - +1
  - +2
  - 0
  - 0
  - 0
actions:
  - name: "Snaring Javelin"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 5
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage; pull 1
      <br />★ 12–16 2 damage; pull 2
      <br />✸ 17+ 3 damage; pull 4 
      <br />**Effect:** A target [[restrained]] by a dwarf can be pulled by this ability."


# DWARF GRENADIER

name: "DWARF GRENADIER"
level: 2
roles:
  - PLATOON
  - HEXER
ancestry:
  - Dwarf
  - Humanoid
ev: 8
stamina: 39
speed: 5
size: 1M /
stability: 3
free_strike: 4
characteristics:
  - +1
  - 0
  - 0
  - +2
  - 0
actions:
  - name: "Concussive Grenade"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Ranged, Weapon
      <br />**Distance** 3 cube within 5
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage; push 1
      <br />★ 12–16 6 damage; push 3; M< 1 [[slowed]] (save ends)
      <br />✸ 17+ 8 damage; push 5; M< 2 [[slowed]] (save ends) 
      <br />**Effect:** A target [[restrained]] by a dwarf can be pushed by this ability."
  - name: "Sleep Grenade"
    desc:
      "
      <br />**Keywords** Area, Ranged
      <br />**Distance** 3 cube within 5
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 poison damage; I< 0 [[dazed]] (save ends)
      <br />★ 12–16 6 poison damage; I< 1 [[dazed]] (save ends)
      <br />✸ 17+ 8 poison damage; I< 2 [[dazed]] (save ends) 
      <br />**Effect:** A creature [[dazed]] by this ability has -1 to all characteristics while resisting potent effects until the condition ends."
traits:
  - name: "Indirect Fire"
    desc: "The grenadier ignores cover and concealment and doesn’t need to establish [[Draw Steel Rules#LINE OF EFFECT|line of effect]] for their abilities."


# DWARF GUNNER

name: "DWARF GUNNER"
level: 1
roles:
  - PLATOON
  - ARTILLERY
ancestry:
  - Dwarf
  - Humanoid
ev: 12
stamina: 26
speed: 5
size: 1M /
stability: 1
free_strike: 4
characteristics:
  - 0
  - +2
  - 0
  - +1
  - 0
actions:
  - name: "Portable Ballista"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage; push 1
      <br />★ 12–16 9 damage; push 3
      <br />✸ 17+ 12 damage; push 5 
      <br />**Effect:** If the target is adjacent to a wall or object after the power roll is resolved, they are [[restrained]] (EoT). A target [[restrained]] by a dwarf can be pushed by this ability. 
      <br />**5 Malice** If the target is pushed into another creature, both the target and the creature are [[restrained]] (EoT)."
maneuvers:
  - name: "Ensnaring Chains (Maneuver)"
    desc: "
      <br />**Cost** 5 Malice
      <br />**Keywords** Ranged, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** 1 [[restrained]], [[slowed]], or [[prone]] target 
      <br />**Effect:** The gunner makes a free strike against the target. The target loses any [[restrained]], [[slowed]] or [[prone]] conditions and gains [[restrained]] (save ends)."
traits:
  - name: "Split Shot"
    desc: "Whenever the gunner deals damage to a creature or object, a creature or object within 1 of the recipient takes 3 damage."


# DWARF REEL WINCH

name: "DWARF REEL WINCH"
level: 1
roles:
  - PLATOON
  - SUPPORT
ancestry:
  - Dwarf
  - Humanoid
ev: 13
stamina: 36
speed: 5
size: 1M /
stability: 2
free_strike: 3
characteristics:
  - 0
  - +2
  - 0
  - +1
  - 0
actions:
  - name: "Snaring Crossbow"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 7 damage
      <br />✸ 17+ 9 damage; M< 2 [[restrained]] (save ends) 
      <br />**Effect:** Pull 5. A target [[restrained]] by a dwarf, including by this ability, can be pulled this way."
maneuvers:
  - name: "Reel Them In"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** Ranged, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** 3 creatures 
      <br />**Effect:** Pull 8. A [[slowed]] or [[restrained]] target is pulled an additional 2. A target [[restrained]] by a dwarf can be pulled this way."
traits:
  - name: "We Have a Quota!"
    desc: "If the engineer applies the [[slowed]] condition to a target who is already [[slowed]] or [[grabbed]], the target becomes [[restrained]] (save ends) and the [[slowed]] or [[grabbed]] condition ends."


# DWARF SHIELDWALL

name: "DWARF SHIELDWALL"
level: 3
roles:
  - PLATOON
  - DEFENDER
ancestry:
  - Dwarf
  - Humanoid
ev: 21
stamina: 72
speed: 5
size: 1M /
stability: 4
free_strike: 5
characteristics:
  - +2
  - 0
  - +0
  - +0
  - +1
actions
  - name: "Wide Axe"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; slide 1
      <br />★ 12–16 10 damage; slide 1
      <br />✸ 17+ 13 damage; slide 1 
      <br />**Effect:** The shieldwall can shift 1 to remain adjacent to the target. A target [[restrained]] by a dwarf can be slid by this ability. 3 Malice The shieldwall targets an additional creature or object."
ta:
  - name: "Intercepting Shield"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** A creature strikes an adjacent ally. 
      <br />**Effect:** The shieldwall becomes the strike’s target and halves the damage."
traits:
  - name: "Call to the Wall"
    desc: "The shieldwall inflicts [[taunted]] (EoT) on a creature whenever they deal damage to the shieldwall or take damage from the shieldwall."


# DWARF STONEWHISPERER

name: "DWARF STONEWHISPERER"
level: 3
roles:
  - PLATOON
  - CONTROLLER
ancestry:
  - Dwarf
  - Humanoid
ev: 10
stamina: 52
speed: 5
size: 1M /
stability: 2
free_strike: 5
characteristics:
  - +1
  - 0
  - +2
  - +2
  - 0
actions:
  - name: "Tile Slide"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic
      <br />**Distance** 2 cube within 1
      <br />**Target** All creatures and objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; slide 1; M< 0 [[slowed]] (save ends)
      <br />★ 12–16 8 damage; slide 3; M< 1 [[slowed]] (save ends)
      <br />✸ 17+ 11 damage; slide 5; M< 2 [[restrained]] (save ends) 
      <br />**Effect:** A target [[restrained]] by a dwarf can be slid by this ability."
maneuvers:
  - name: "Stone Wave"
    desc: "
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 3 cube within 10
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage; push 2; R< 1 [[slowed]] (save ends)
      <br />★ 12–16 6 damage; push 3; R< 2 [[slowed]] (save ends)
      <br />✸ 17+ 9 damage; push 3; R< 3 [[slowed]] (save ends) 
      <br />**Effect:** A target [[restrained]] by a dwarf can be pushed by this ability. The affected area is considered difficult terrain for enemies."
traits:
  - name: "Stonewalker"
    desc: "The stonewhisperer can phase through 2 squares of stone as part of any movement they take. If they end their movement inside stone, they are shunted out into the square where they entered it."


# DWARF TRAPPER

name: "DWARF TRAPPER"
level: 1
roles:
  - PLATOON
  - HARRIER
ancestry:
  - Dwarf
  - Humanoid
ev: 6
stamina: 36
speed: 7
size: 1M /
stability: 2
free_strike: 3
characteristics:
  - 0
  - +2
  - 0
  - +1
  - 0
actions:
  - name: "Concussive Bolts"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; push 2
      <br />★ 12–16 7 damage; push 4
      <br />✸ 17+ 9 damage; push 6 
      <br />**Effect:** A target [[restrained]] by a dwarf can be pushed by this ability."
maneuvers:
  - name: "Steam Powered Snare"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** Area, Ranged
      <br />**Distance** 3 cube within 5
      <br />**Target** All enemies in the cube 
      <br />**Effect:** Each target makes a Might test.
      <br />`dice: 2d10 +
      <br />✸ ≤11 7 damage; [[restrained]] (EoT)
      <br />★ 12–16 5 damage; [[slowed]] (EoT)
      <br />✦ 17+ No effect 
      <br />**Effect:** The snare remains until the end of the encounter. An enemy that moves into an affected square for the first time on their turn must make the test."


# DWARF WARDEN

name: "DWARF WARDEN"
level: 2
roles:
  - PLATOON
  - BRUTE
ancestry:
  - Dwarf
  - Humanoid
ev: 8
stamina: 59
speed: 5
size: 1M /
stability: 3
free_strike: 5
characteristics:
  - +2
  - 0
  - 0
  - +1
  - 0
actions:
  - name: "Concussive Maul"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; push 1
      <br />★ 12–16 10 damage; push 3
      <br />✸ 17+ 13 damage; push 5; M< 2 [[restrained]] (save ends) 
      <br />**Effect:** A target [[restrained]] by a dwarf can be pushed by this ability."
maneuvers:
  - name: "Concussive Shockwave"
    desc: "
      <br />**Keywords** Area, Melee
      <br />**Distance** 3 cube within 1
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; push 2; A< 0 [[slowed]] (save ends)
      <br />★ 12–16 8 damage; push 4; A< 1 [[slowed]] (save ends)
      <br />✸ 17+ 11 damage; push 6; A< 2 [[dazed]] (save ends) 
      <br />**Effect:** A target [[restrained]] by a dwarf can be pushed by this ability. Escort the Prisoners Whenever the warden moves, they can carry an adjacent [[restrained]] enemy as if they were [[grabbed]]."


# DWARF MARAUDER LORD

name: "DWARF MARAUDER LORD"
level: 3
roles:
  - LEADER
ancestry:
  - Dwarf
  - Humanoid
ev: 20
stamina: 132
speed: 5
size: 1M /
stability: 4
free_strike: 5
characteristics:
  - +3
  - 0
  - +2
  - +1
  - 0
actions:
  - name: "Levitating Axes"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Psionic, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 10
      <br />**Target** Two creature or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; slide 1
      <br />★ 12–16 12 damage; slide 3
      <br />✸ 17+ 15 damage; slide 5 
      <br />**Effect:** A target [[restrained]] by a dwarf can be slid by this ability. 3 Malice A target that is force moved adjacent to an ally with this ability is [[restrained]] (EoT)."
maneuvers:
  - name: "Magnetomancy"
    desc: "
      <br />**Keywords** Psionic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object 
      <br />**Effect:** Vertical slide 5. A target [[restrained]] by a dwarf can be slid by this ability. 5 Malice This ability gains the Area keyword, its distance becomes 10 burst, and it now targets [[restrained]] creatures."
ta:
  - name: "Your Weapon is Useless"
    desc: "
      <br />**Keywords** Psionic
      <br />**Distance** Self or ranged 10
      <br />**Target** Self or 1 ally 
      <br />**Trigger** A creature makes a melee strike against the target. 
      <br />**Effect:** The target takes half damage from the attack. The attacker takes 4 damage. End 
      <br />**Effect:** At the end of their turn, the marauder lord can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
va:
  - name: "Ajax Will Pay Well for These Specimens (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Psionic, Weapon
      <br />**Distance** 5 cube within 10
      <br />**Target** All enemies in the cube 
      <br />**Effect:** The marauder lord uses Levitating Axes against each target. The marauder lord makes one power roll against all targets. "
  - name: "Don’t Let Them Escape! (Villain Action 2)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 5 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Each target shift up to their speed. The marauder lord then uses Levitating Axes."
  - name: "Test Your Metal! (Villain Action 3)"
    desc: "
      <br />**Keywords** Psionic
      <br />**Distance** Ranged 10
      <br />**Target** special 
      <br />**Effect:** The marauder lord creates three 2-square metal objects in unoccupied squares within distance. When the marauder lord uses Magnetomancy, they can additionally target one of these objects."


# SERVITOR WAR WALKER

name: "SERVITOR WAR WALKER"
level: 1
roles:
  - TROOP
  - MOUNT
ancestry:
  - Construct
  - Dwarf
ev: 12
stamina: 60
speed: 8 (climb)
size: 3 /
stability: 2
free_strike: 3
characteristics:
  - +2
  - +0
  - −2
  - 0
  - −2
actions:
  - name: "Grasping Claws"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 9 damage
      <br />✸ 17+ 12 damage; M< 2 [[restrained]] (save ends) 
      <br />**Effect:** [[restrained]] targets and targets [[restrained]] by this ability are pulled 3. A target [[restrained]] by a dwarf can be pulled by this ability."
maneuvers:
  - name: "Stunning Blast"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 3 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 2`
      <br />✸ ≤11 3 lightning damage; A< 0 [[slowed]] (save ends)
      <br />★ 12–16 6 lightning damage; A< 1 [[slowed]] (save ends)
      <br />✦ 17+ 8 lightning damage; A< 2 [[slowed]] (save ends)"
traits:
  - name: "Cupola" 
    desc: "Three of the war walker’s 1 allies can occupy the same space while riding the war walker. Riders have cover against attacks that target them."
  - name: "Mobile Prison Harness"
    desc: "[[slowed|Slowed]] or [[restrained]] creatures adjacent to the war walker become [[restrained]] (save ends) and have a bane on all power rolls. Adjacent [[restrained]] creatures are automatically moved with the war walker, ignoring stability."

# CRUX OF FIRE

name: "CRUX OF FIRE"
level: 3
roles:
  - TROOP
  - ARTILLERY
ancestry:
  - Elemental
ev: 20
stamina: 80
immunities: fire 5
speed: 6
size: 1T /
stability: 0
free_strike: 6
characteristics:
  - −1
  - +2
  - 0
  - +1
  - +2
actions:
  - name: "Spitfire"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 12
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 fire damage
      <br />★ 12–16 12 fire damage; A< 1 burning (save ends)
      <br />✸ 17+ 15 fire damage; A< 2 burning (save ends) 
      <br />**Effect:** A burning creature or object takes 1d6 fire damage at the start of each of their turns until the condition ends."
maneuvers:
  - name: "Convocation of Flames"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** Self or 1 elemental 
      <br />**Effect:** The target receives fire immunity 5 until the start of the crux’s next turn if they don’t already have it. 3 Malice The ground within 3 of the target is wreathed in fire until the end of the encounter. Whenever an enemy first enters the affected area on a turn or starts their turn within it, they take 3 fire damage."
ta:
  - name: "Flame Jet"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Magic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The crux takes damage. 
      <br />**Effect:** The crux ignores any effects associated with the damage and flies up to their speed. If the crux doesn’t end this movement on solid ground, they fall [[prone]]."
traits:
  - name: "Fickle and Free"
    desc: "The crux can’t be [[restrained]], [[slowed]], or knocked [[prone]], and they ignore difficult terrain."


# ESSENCE OF STORMS

name: "ESSENCE OF STORMS"
level: 3
roles:
  - TROOP
  - HARRIER
ancestry:
  - Elemental
ev: 20
stamina: 100
immunities: lightning 5
speed: 8 (fly)
size: 1S /
stability: 0
free_strike: 5
characteristics:
  - +1
  - +2
  - −1
  - 0
  - +2
actions:
  - name: "Bluster"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 1 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 5 damage; 4 lightning damage; push 1
      <br />✸ 17+ 5 damage; 7 lightning damage; push 3 
      <br />**Effect:** The essence shifts 3 before or after using this ability."
maneuvers:
  - name: "Convocation of Squalls"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** Self or 1 elemental 
      <br />**Effect:** The target receives lightning immunity 5 until the start of the essence’s next turn if they don’t already have it. 
      <br />**3 Malice** The target emits a 3 aura vortex until the end of the encounter. The aura is considered difficult terrain for enemies. At the end of each of the target’s turns, the target can select 1 creature within the aura to push 5."
ta:
  - name: "Thunderclap"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Magic, Melee, Ranged
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** 1 creature or object 
      <br />**Trigger** The essence takes damage from the target. 
      <br />**Effect:** The essence deals 5 lightning damage to the target."
traits:
  - name: "Fickle and Free"
    desc: "The essence can’t be [[restrained]], [[slowed]], or knocked [[prone]], and they ignore difficult terrain."


# ESSENCE OF TIDES

name: "ESSENCE OF TIDES"
level: 3
roles:
  - TROOP
  - CONTROLLER
ancestry:
  - Elemental
ev: 20
stamina: 80
immunities: cold 5
speed: 7 (swim)
size: 1M /
stability: 1
free_strike: 5
characteristics:
  - +2
  - 0
  - +1
  - −1
  - +2
actions:
  - name: "Water Wing"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Strike
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; slide 1
      <br />★ 12–16 11 damage; slide 2
      <br />✸ 17+ 14 damage; slide 3 
      <br />**Effect:** P< 2 the target’s stability is reduced to 0 and they move 2 additional squares whenever they are force moved (save ends)"
maneuvers:
  - name: "Convocation of Waves
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** Self or 1 elemental 
      <br />**Effect:** The target receives cold immunity 5 until the start of the essence’s next turn if they don’t already have it. 
      <br >**3 Malice** The target emits a 1 aura pool of water until the end of the encounter. The area beneath the aura becomes a river that trails behind the target as they move and is considered difficult terrain. An enemy that ends their turn standing in the river is M< 2 [[slowed]] (save ends)."
ta:
  - name: "Sea Salted Wounds
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Malice 1
      <br />**Target** 1 creature 
      <br />**Trigger** An ally deals damage to the target. 
      <br />**Effect:** The essence makes a free strike against the target."
traits:
  - name: "Water Glide"
    desc: "When the essence starts their turn on a space containing water, they can add the flying keyword to their movement until the end of their turn. While flying, the essence doesn’t provoke opportunity attacks."
  - name: "Fickle and Free"
    desc: "The essence can’t be [[restrained]], [[slowed]], or knocked [[prone]], and they ignore difficult terrain."


# FIELD OF GROWTH

name: "FIELD OF GROWTH"
level: 5
roles:
  - TROOP
  - CONTROLLER
ancestry:
  - Elemental
ev: 28
stamina: 120
immunities: poison 5
speed: 8 (climb)
size: 3 /
stability: 2
free_strike: 6
characteristics:
  - +2
  - 0
  - 0
  - +2
  - +2
actions:
  - name: "Hampering Roots"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 8
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 damage
      <br />★ 12–16 13 damage; R< 1 [[prone]] can’t stand (save ends)
      <br />✸ 17+ 16 damage; [[prone]] R< 2 and can’t stand (save ends) 
      <br />**Effect:** This ability inflicts [[restrained]] (save ends) on targets that are already [[prone]]. When the [[restrained]] condition ends, any can’t stand effects also end."
maneuvers:
  - name: "Convocation of Verdure"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** Self or 1 elemental 
      <br />**Effect:** The target gains 15 temporary stamina that lasts until the start of the field’s next turn. 
      <br />**3 Malice** The ground within 1 of the target is overgrown with thicket and vines until the end of the encounter. Whenever an enemy attacks the target while within [[Draw Steel Rules#LINE OF EFFECT|line of effect]] of the affected area, they are pulled 5 towards the affected area. Whenever an enemy enters the affected area on a turn or starts their turn within it, they are knocked [[prone]]."
ta:
  - name: "Rose Lash"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Magic, Melee, Ranged
      <br />**Distance** Melee 3
      <br />**Target** 1 creature or object 
      <br />**Trigger** The field takes damage from the target. 
      <br />**Effect:** The field deals 6 damage to the target and A< 2 [[bleeding]] (save ends). Roots Run Deep The field can target creatures touching the ground with abilities, even if they don’t have [[Draw Steel Rules#LINE OF EFFECT|line of effect]]. 
traits:
  - name: "Fickle and Free"
    desc: "The field can’t be [[restrained]], [[slowed]], or knocked [[prone]], and they ignore difficult terrain."


# FORCE OF EARTH

name: "FORCE OF EARTH"
level: 3
roles:
  - TROOP
  - BRUTE
ancestry:
  - Elemental
ev: 20
stamina: 132
speed: 5 (burrow)
size: 2 /
stability: 2
free_strike: 6
characteristics:
  - +2
  - −1
  - 0
  - +1
  - +2
actions:
  - name: "Slam Into Dirt"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 damage
      <br />★ 12–16 12 damage; M< 1 [[restrained]] (save ends)
      <br />✸ 17+ 15 damage; M< 2 [[restrained]] (save ends) 
      <br />**Effect:** The area beneath the target becomes difficult terrain."
maneuvers:
  - name: "Convocation of Quartz"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** Self or 1 elemental 
      <br />**Effect:** The target imposes a bane on melee strikes made against them until the start of the force’s next turn if they don’t already have it. 3 Malice The target grows a carapace of stone, increasing their stability by 3 and granting them 15 temporary stamina until the end of the encounter."
ta:
  - name: "Break Armor"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The force takes damage 
      <br />**Effect:** The force halves the damage, gains damage weakness 3, and increases their speed by 3. The damage weakness increases by 3 each time the force uses this ability in an encounter. Primordial Strength The force deals an additional 6 damage with strikes targeting objects. "
traits:
  - name: "Fickle and Free"
    desc: "The force can’t be [[restrained]], [[slowed]], or knocked [[prone]], and they ignore difficult terrain."

# ELEMENTAL MOTE

name: "ELEMENTAL MOTE"
level: 1
roles:
  - MINION
  - HEXER
ancestry:
  - Elemental
  - High
  - Elf
ev: 3 for eight minions
stamina: 3
speed: 5 (fly)
size: 1T /
stability: 0
with-captain:
speed: +2
free_strike: 1
characteristics:
  - 0
  - 0
  - 0
  - 0
  - +2
actions:
  - name: "Dweomer Plume"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Strike
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage
      <br />★ 12–16 2 damage; R< 1 Magic weakness 3 (save ends)
      <br />✸ 17+ 3 damage; R< 2 Magic weakness 3 (save ends)"
traits:
  - name: "Spark of Life"
    desc: "On their turn, the mote can choose to die to revive a dead soot crow, brambleguard, or ceramic horse within 1, returning with 3 stamina."


# HIGH ELF DAWN MAGE

name: "HIGH ELF DAWN MAGE"
level: 1
roles:
  - MINION
  - CONTROLLER
ancestry:
  - Fey
  - High
  - Elf
  - Humanoid
ev: 3 for eight minions
stamina: 3
speed: 5
size: 1M /
stability: 0
with-captain: Ranged distance +5
free_strike: 1
characteristics:
  - 0
  - 0
  - +1
  - +1
  - +1
actions:
  - name: "Bright Bolt"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 5
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 holy damage
      <br />★ 12–16 2 holy damage
      <br />✸ 17+ 3 holy damage 
      <br />**Effect:** The target can’t hide until the start of the dawn mage’s next turn."
traits:
  - name: "Otherworldly Grace"
    desc: "At the start of their turn, the dawn mage can turn the duration of one save ends effect they suffer from into EoT."


# HIGH ELF QUIVER

name: "HIGH ELF QUIVER"
level: 1
roles:
  - MINION
  - ARTILLERY
ancestry:
  - Fey
  - High
  - Elf
  - Humanoid
ev: 3 for eight minions
stamina: 3
speed: 5
size: 1M /
stability: 0
with-captain: Ranged distance +5
free_strike: 2
characteristics:
  - 0
  - +2
  - +1
  - 0
  - 0
actions:
  - name: "Heavy Arrow"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage 
      <br />**Effect:** Each ally adjacent to the target can shift 2."
traits:
  - name: "Otherworldly Grace"
    desc: "At the start of their turn, the dawn mage can turn the duration of one save ends effect they suffer from into EoT."

# SOOT CROW

name: "SOOT CROW"
level: 1
roles:
  - MINION
  - HARRIER
ancestry:
  - Elemental
  - High
  - Elf
ev: 3 for eight minions
stamina: 4
speed: 7 (fly)
size: 1T /
stability: 0
with-captain: Edge on strikes
free_strike: 1
characteristics:
  - 0
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Heckle"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage
      <br />★ 12–16 2 damage
      <br />✸ 17+ 3 damage; [[taunted]] (EoT) 
      <br />**Effect:** The soot crow ignores opportunity attacks from the target until the end of its turn."


# BRAMBLEGUARD

name: "BRAMBLEGUARD"
level: 2
roles:
  - PLATOON
  - DEFENDER
ancestry:
  - Elemental
  - High
  - Elf
ev: 8
stamina: 59
speed: 4
size: 2 /
stability: 3
free_strike: 4
characteristics:
  - +2
  - 0
  - 0
  - 0
  - +2
actions:
  - name: "Wall of Roses"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The brambleguard’s speed becomes 0 and they extend themself into a 5 wall until the start of their next turn. Each ally adjacent to the brambleguard at the start of their turn regains 5 stamina and can apply the Magic keyword to their weapon abilities until the end of their turn."
  - name: "Whip Frenzy"
    desc:
      "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 2 burst
      <br />**Target** Each enemy in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 7 damage; push 3
      <br />✸ 17+ 10 damage; push 3; A< 2 [[bleeding]] (save ends)"
traits:
  - name: "Thicket and Thorns"
    desc: "The brambleguard blocks [[Draw Steel Rules#LINE OF EFFECT|line of effect]] for enemies. An enemy that starts their turn adjacent to a brambleguard takes 4 damage."


# HIGH ELF BLOODLETTER

name: "HIGH ELF BLOODLETTER"
level: 1
roles:
  - PLATOON
  - AMBUSHER
ancestry:
  - Fey
  - High
  - Elf
  - Humanoid
ev: 6
stamina: 30
speed: 7
size: 1M /
stability: 0
free_strike: 4
characteristics:
  - 0
  - +2
  - 0
  - +1
  - 0
actions:
  - name: "Razor’s Edge"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 9 damage
      <br />✸ 17+ 12 damage; R< 2 [[bleeding]] (save ends) 
      <br />**Effect:** The bloodletter and each ally has a double edge on abilities targeting a creature or object [[bleeding]] from this ability."
maneuvers:
  - name: "Blood Haze"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 3 burst
      <br />**Target** Special 
      <br />**Effect:** The bloodletter creates a cloud of blood vapor in the area until the end of the next round. The cloud blocks [[Draw Steel Rules#LINE OF EFFECT|line of effect]] for enemies, and an enemy has Magic weakness 3 occupying an affected square. The bloodletter then shifts up to their speed, hiding if they end their movement under concealment."
traits:
  - name: "Otherworldly Grace"
    desc: "At the start of their turn, the dawn mage can turn the duration of one save ends effect they suffer from into EoT."


# HIGH ELF DEATHTOUCH

name: "HIGH ELF DEATHTOUCH"
level: 2
roles:
  - PLATOON
  - ARTILLERY
ancestry:
  - Fey
  - High
  - Elf
  - Humanoid
ev: 8
stamina: 30
speed: 5
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - +2
  - 0
  - +1
  - 0
  - +1
actions:
  - name: "Heartpiercer"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 15
      <br />**Target** 1 creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 10 damage
      <br />✸ 17+ 13 damage; R< 1 [[bleeding]] (save ends) ; I< 1 [[frightened]] (save ends) ; P< 1 [[restrained]] (save ends)
      <br />**5 Malice** The ability replaces Strike with the Area keyword, the distance becomes 3 cube within 10, and it targets all creatures in the cube."
maneuvers:
  - name: "Kiss of Death"
    desc: "
      <br />**Keywords** Magic
      <br />**Distance** Melee 1
      <br />**Target** 1 ally 
      <br />**Effect:** The target’s speed increases by 5 and they cannot get results lower than tier 3 on their power rolls. The target immediately dies at the end of their next turn."
traits:
  - name: "Otherworldly Grace"
    desc: "At the start of their turn, the dawn mage can turn the duration of one save ends effect they suffer from into EoT."


# HIGH ELF ORBWEAVER

name: "HIGH ELF ORBWEAVER"
level: 3
roles:
  - PLATOON
  - HEXER
ancestry:
  - Fey
  - High
  - Elf
  - Humanoid
ev: 10
stamina: 40
speed: 5
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - 0
  - 0
  - +2
  - +2
  - +2
actions:
  - name: "Awash"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 cube within 1
      <br />**Target** All creatures in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 cold damage; M< 0 push 3
      <br />★ 12–16 6 cold damage; M< 1 push 5 or [[prone]]
      <br />✸ 17+ 9 cold damage; M< 2 slide 5 or [[prone]]"
  - name: "Aetherweb"
    desc:
      "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 8
      <br />**Target** 2 enemies or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; R< 0 [[slowed]] (save ends)
      <br />★ 12–16 8 damage; R< 1 [[slowed]] (save ends)
      <br />✸ 17+ 11 damage; R< 2 [[restrained]] (save ends) 
      <br />**Effect:** Each enemy within 3 of a target suffers the same additional effects as the target unless they shift into an unoccupied square adjacent to them"
traits:
  - name: "Otherworldly Grace"
    desc: "At the start of their turn, the dawn mage can turn the duration of one save ends effect they suffer from into EoT."

# HIGH ELF PALINODE

name: "HIGH ELF PALINODE"
level: 1
roles:
  - PLATOON
  - SUPPORT
ancestry:
  - Fey
  - High
  - Elf
  - Humanoid
ev: 6
stamina: 30
immunities: psychic 5
speed: 5
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - 0
  - 0
  - 0
  - +2
  - +1
actions:
  - name: "Instill Regret"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 8
      <br />**Target** 1 creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 psychic damage
      <br />★ 12–16 7 psychic damage; I< 1 [[weakened]] (save ends)
      <br />✸ 17+ 9 psychic damage; I< 2 [[weakened]] (save ends) 
      <br />**2 Malice** The potency of this ability increases by 1. If the target is still [[weakened]] by this ability at the end of the encounter, they cannot take a respite activity during their next respite."
maneuvers:
  - name: "Recall"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** 2 allies 
      <br />**Effect:** Each target is teleported to an unoccupied square adjacent to the palinode. Then, the palinode and each target gain 5 temporary stamina." 
traits:
  - name: "Otherworldly Grace"
    desc: "At the start of their turn, the dawn mage can turn the duration of one save ends effect they suffer from into EoT."

# HIGH ELF WYRD

name: "HIGH ELF WYRD"
level: 3
roles:
  - PLATOON
  - CONTROLLER
ancestry:
  - Fey
  - High
  - Elf
  - Humanoid
ev: 10
stamina: 40
speed: 5
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - 0
  - +1
  - +2
  - −1
  - +2
actions:
  - name: "Twystrd"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 1 cube within 5
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 vertical push 3
      <br />★ 12–16 vertical push 5
      <br />✸ 17+ vertical push 6 
      <br />**Effect:** The area of the cube increases by 1 for each elemental mote adjacent to the wyrd."
maneuvers:
  - name: "Summon Elemental"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** Ranged 5
      <br />**Target** Special 
      <br />**Effect:** The wyrd summons 2 elemental motes or 2 soot crows into unoccupied squares within distance."
  - name: "Wyrd Warp"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 8 wall within 8
      <br />**Target** Special 
      <br />**Effect:** The wyrd shapes the land as if it were loose clay. Each wall segment takes up the entire square. A segment can also be used to push a square of the terrain further into the ground. An enemy on top of an affected square moves with the elevation of the terrain."
traits:
  - name: "Otherworldly Grace"
    desc: "At the start of their turn, the dawn mage can turn the duration of one save ends effect they suffer from into EoT."

# HIGH ELF ZEPHYR

name: "HIGH ELF ZEPHYR"
level: 1
roles:
  - PLATOON
  - HARRIER
ancestry:
  - Fey
  - High
  - Elf
  - Humanoid
ev: 6
stamina: 30
speed: 7
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - 0
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Sweeping Blade"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 7 damage
      <br />✸ 17+ 9 damage; the zephyr makes a free strike on a creature adjacent to the target; both creatures are A< 2 [[prone]] 
      <br />**Effect:** Shift 2."
maneuvers:
  - name: "Windwalk"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The zephyr moves up to their speed through the air. They must end this movement on solid ground or immediately fall [[prone]]. Like the Wind All of the zephyr’s movement is considered shifting."
traits:
  - name: "Otherworldly Grace"
    desc: "At the start of their turn, the dawn mage can turn the duration of one save ends effect they suffer from into EoT."

# HIGH ELF ORDINATOR

name: "HIGH ELF ORDINATOR"
level: 3
roles:
  - LEADER
ancestry:
  - Fey
  - High
  - Elf
  - Humanoid
ev: 20
stamina: 120
speed: 5 (fly, hover)
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - 0
  - +2
  - +3
  - +2
  - +3
actions:
  - name: "Lightning Rod"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 20
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 lightning damage; R< 1 [[dazed]] (save ends)
      <br />★ 12–16 14 lightning damage; R< 2 [[dazed]] (save ends)
      <br />✸ 17+ 17+ lightning damage; R< 3 [[dazed]] (save ends) 
      <br />**Effect:** High elves have an edge on abilities used against the target until the start of the ordinator’s next turn."
maneuvers:
  - name: "Elemental Uproar"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 10 Burst
      <br />**Target** Each elemental ally in the burst 
      <br />**Effect:** Each target moves up to their speed or makes a free strike. An elemental mote target can use their Spark of Life trait."
  - name: "Summon Elemental (Free Maneuver)"
    desc: "
      <br />**Cost** 3+ Malice
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** Special 
      <br />**Effect:** For every 3 malice spent, the ordinator summons 5 elemental motes, 3 soot crows, 1 ceramic horse, or 1 brambleguard into unoccupied squares within distance."
ta:
  - name: "Enough!"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** Triggering enemy 
      <br />**Trigger** An enemy targets the ordinator or an ally within distance with an ability. 
      <br />**Effect:** The ordinator uses Lightning Rod against the target. Otherworldly Grace At the start of their turn, the ordinator can turn the duration of one save ends effect they suffer from into EoT. Magic Beacon While using Chaincast, magic abilities that use the Ordinator’s space have a double edge (see Chaincast)."
va:
  - name: "Fountains Roar, Now Free From The Earth (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 10 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Each target glows, ending one condition on themselves and then moving up to twice their speed."
  - name: "And The Sun Forsook Her Children (Villain Action 2)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 cube within 10
      <br />**Target** All enemies in the cube 
      <br />**Effect:** Each target makes a Might test.
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 12 corruption damage; pull 5 towards center of cube
      <br />★ 12–16 9 corruption damage; pull 3 towards center of cube
      <br />✦ 17+ Pull 1 towards center of cube 
      <br />**Effect:** The affected area becomes darkened and its space warps violently in every direction."
  - name: "But We Will Change Her Mind. (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** Self and 10 burst
      <br />**Target** Self and each ally in the burst 
      <br />**Effect:** All elves radiate wisps of magic. Each target makes a free strike that has the Magic keyword and deals an additional 3 damage."


# CERAMIC HORSE

name: "CERAMIC HORSE"
level: 1
roles:
  - PLATOON
  - MOUNT
ancestry:
  - Elemental
  - High
  - Elf
ev: 6
stamina: 30
speed: 10
size: 2 /
stability: 2
free_strike: 3
characteristics:
  - +2
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Elemental Charge"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 7 fire damage
      <br />✸ 17+ 9 lightning damage; M< 2 [[prone]]"
  - name: "Stomp"
    desc:
      "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 1 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 5 damage
      <br />✸ 17+ 7 damage 
      <br />**Effect:** This attack deals an additional 2 damage to [[prone]] targets."
maneuvers: 
  - name: "Buck"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** The horse’s rider 
      <br />**Effect:** Vertical slide 3; The rider can use a ranged ability at any point during the movement and then fall without taking damage."
traits:
  - name: "Shared Otherworldly Grace"
    desc: "If the ceramic horse’s rider has the Otherworldly Grace trait, it also gains the Otherworldly Grace trait."
  - name: "Otherworldly Grace"
    desc: "At the start of their turn, the dawn mage can turn the duration of one save ends effect they suffer from into EoT."

# SHADOW ELF CLOAK

name: "SHADOW ELF CLOAK"
level: 4
roles:
  - MINION
  - HARRIER
ancestry:
  - Fey
  - Humanoid
  - Shadow
  - Elf
ev: 6 for eight minions
stamina: 8
speed: 8 (climb)
size: 1M /
stability: 0
with-captain:
speed: +2
free_strike: 2
characteristics:
  - +3
  - +1
  - +0
  - +0
  - +0
actions:
  - name: "Stick and Poke"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 6 damage 
      <br />**Effect:** Shift 2."
traits:
  - name: "Of the Umbra"
    desc: "The cloak ignores concealment granted by darkness. While the cloak is in direct sunlight, they have damage weakness 3. While the cloak is concealed, they have damage immunity 3."


# SHADOW ELF DUSK MAGE

name: "SHADOW ELF DUSK MAGE"
level: 4
roles:
  - MINION
  - HEXER
ancestry:
  - Fey
  - Humanoid
  - Shadow
  - Elf
ev: 6 for eight minions
stamina: 7
speed: 5 (climb)
size: 1M /
stability: 0
with-captain: Edge on strikes
free_strike: 2
characteristics:
  - +0
  - +3
  - +2
  - +0
  - +0
actions:
  - name: "Gloom Strike"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage; A< 2 [[slowed]] (save ends)
      <br />✸ 17+ 6 damage; A< 3 [[slowed]] (save ends)"
traits:
  - name: "Of the Umbra"
    desc: "The cloak ignores concealment granted by darkness. While the cloak is in direct sunlight, they have damage weakness 3. While the cloak is concealed, they have damage immunity 3."

# SHADOW ELF NIGHTSTRIKE

name: "SHADOW ELF NIGHTSTRIKE"
level: 4
roles:
  - MINION
  - AMBUSHER
ancestry:
  - Fey
  - Humanoid
  - Shadow
  - Elf
ev: 6 for eight minions
stamina: 8
speed: 5 (climb)
size: 1M /
stability: 0
with-captain: Edge on strikes
free_strike: 3
characteristics:
  - +1
  - +3
  - +0
  - +1
  - +0
actions:
  - name: "Vault"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 5 damage
      <br />✸ 17+ 7 damage 
      <br />**Effect:** The nightstrike leaps over the target, shifting into an unoccupied square adjacent to the target opposite from their starting position."
traits:
  - name: "Of the Umbra"
    desc: "The cloak ignores concealment granted by darkness. While the cloak is in direct sunlight, they have damage weakness 3. While the cloak is concealed, they have damage immunity 3."

# SHADOW ELF SNIPER

name: "SHADOW ELF SNIPER"
level: 4
roles:
  - MINION
  - ARTILLERY
ancestry:
  - Fey
  - Humanoid
  - Shadow
  - Elf
ev: 6 for eight minions
stamina: 7
speed: 5 (climb)
size: 1M /
stability: 0
with-captain: Strike damage +2
free_strike: 3
characteristics:
  - +1
  - +3
  - +0
  - +0
  - +0
actions:
  - name: "Neon Arrow"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 7
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 5 damage
      <br />✸ 17+ 7 damage 
      <br />**Effect:** The next strike made against the target has an edge."
traits:
  - name: "Of the Umbra"
    desc: "The cloak ignores concealment granted by darkness. While the cloak is in direct sunlight, they have damage weakness 3. While the cloak is concealed, they have damage immunity 3."

# SHADOW ELF ASSASSIN

name: "SHADOW ELF ASSASSIN"
level: 6
roles:
  - PLATOON
  - ARTILLERY
ancestry:
  - Fey
  - Humanoid
  - Shadow
  - Elf
ev: 16
stamina: 70
speed: 5 (climb)
size: 1M /
stability: 0
free_strike: 7
characteristics:
  - +0
  - +3
  - +2
  - +1
  - +1
actions:
  - name: "Neon Assault"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 15
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 damage
      <br />★ 12–16 15 damage
      <br />✸ 17+ 18 damage 
      <br />**Effect:** The next ability made against the target has a double edge. 
      <br />**5 Malice** Each ally within 5 of the target makes a free strike against them."
  - name: "Splitbow"
    desc:
      "
      <br />**Keywords** Area, Ranged, Weapon
      <br />**Distance** 1 x 4 line within 10
      <br />**Target** All enemies in the line
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 damage; I< 1 [[bleeding]] (save ends).
      <br />★ 12–16 10 damage; I< 2 [[bleeding]] (save ends).
      <br />✸ 17+ 12 damage; I< 3 [[bleeding]] (save ends). 
      <br />**Effect:** Push 4."
traits:
  - name: "Of the Umbra"
    desc: "The cloak ignores concealment granted by darkness. While the cloak is in direct sunlight, they have damage weakness 3. While the cloak is concealed, they have damage immunity 3."

# SHADOW ELF DARK KNIGHT

name: "SHADOW ELF DARK KNIGHT"
level: 4
roles:
  - PLATOON
  - DEFENDER
ancestry:
  - Fey
  - Humanoid
  - Shadow
  - Elf
ev: 12
stamina: 70
speed: 5 (climb)
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - +0
  - +2
  - +0
  - +3
  - +2
actions:
  - name: "Suffusing Strike"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 3
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 corruption damage
      <br />★ 12–16 12 corruption damage; R< 2 [[taunted]] (EoT)
      <br />✸ 17+ 15 corruption damage; R< 3 [[taunted]] (EoT) 
ta:
  - name: "Trick of the Eye"
    desc: "
      <br />**Keywords** Magic
      <br />**Distance** Melee 2
      <br />**Target** 1 ally 
      <br />**Trigger** An enemy within distance makes a strike against the target. 
      <br />**Effect:** The damage is halved. The dark knight takes the other half of the damage."
traits:
  - name: "Of the Umbra"
    desc: "The cloak ignores concealment granted by darkness. While the cloak is in direct sunlight, they have damage weakness 3. While the cloak is concealed, they have damage immunity 3."

# SHADOW ELF DUSKCALLER

name: "SHADOW ELF DUSKCALLER"
level: 5
roles:
  - PLATOON
  - CONTROLLER
ancestry:
  - Fey
  - Humanoid
  - Shadow
  - Elf
ev: 14
stamina: 60
speed: 5 (climb)
size: 1M /
stability: 0
free_strike: 6
characteristics:
  - +0
  - +3
  - +3
  - +2
  - +0
actions:
  - name: "Night Knife"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage
      <br />★ 12–16 13 damage
      <br />✸ 17+ 16 damage 
      <br />**Effect:** The duskcaller can target an additional creature or object while concealed."
maneuvers:
  - name: "Shadesong"
    desc: "
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 2 cube within 3
      <br />**Target** Special 
      <br />**Effect:** The affected area is covered in darkness and is considered concealment until the start of the duskcaller’s next turn. 
      <br />**2 Malice** The area of the cube increases by 3."
traits:
  - name: "Of the Umbra"
    desc: "The cloak ignores concealment granted by darkness. While the cloak is in direct sunlight, they have damage weakness 3. While the cloak is concealed, they have damage immunity 3."

# SHADOW ELF LUMINATOR

name: "SHADOW ELF LUMINATOR"
level: 4
roles:
  - PLATOON
  - SUPPORT
ancestry:
  - Fey
  - Humanoid
  - Shadow
  - Elf
ev: 12
stamina: 60
speed: 5 (climb)
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - +0
  - +1
  - +1
  - +3
  - +2
actions:
  - name: "Neon Mark"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 3
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 lightning damage
      <br />★ 12–16 12 lightning damage
      <br />✸ 17+ 15 lightning damage 
      <br />**Effect:** The next strike made against the target deals an additional 5 damage."
  - name: "Mourning ‘Til Dusk"
    desc:
      "
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 2 burst
      <br />**Target** All allies in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 The target regains 2 stamina
      <br />★ 12–16 The target regains 3 stamina
      <br />✸ 17+ The target regains 5 stamina; the Director gains 3 Malice 
      <br />**Effect:** Each target has an edge on their next strike."
traits:
  - name: "Of the Umbra"
    desc: "The cloak ignores concealment granted by darkness. While the cloak is in direct sunlight, they have damage weakness 3. While the cloak is concealed, they have damage immunity 3."

# SHADOW ELF MOONDANCER

name: "SHADOW ELF MOONDANCER"
level: 5
roles:
  - PLATOON
  - HARRIER
ancestry:
  - Fey
  - Humanoid
  - Shadow
  - Elf
ev: 14
stamina: 70
speed: 7 (climb)
size: 1M /
stability: 0
free_strike: 6
characteristics:
  - +1
  - +3
  - +1
  - +2
  - +0
actions:
  - name: "Crescent Sweep"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage
      <br />★ 12–16 13 damage
      <br />✸ 17+ 16 damage 
      <br />**Effect:** The moondancer ignores opportunity attacks from the target until the end of their turn."
ta:
- name: "Dissolve"
  desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Special 
      <br />**Trigger** The moondancer takes damage from a strike 
      <br />**Effect:** The moondancer teleports to a square in concealment granted by darkness within 10."
traits:
  - name: "Of the Umbra"
    desc: "The cloak ignores concealment granted by darkness. While the cloak is in direct sunlight, they have damage weakness 3. While the cloak is concealed, they have damage immunity 3."

# SHADOW ELF MOURNBLADE

name: "SHADOW ELF MOURNBLADE"
level: 6
roles:
  - PLATOON
  - AMBUSHER
ancestry:
  - Fey
  - Humanoid
  - Shadow
  - Elf
ev: 16
stamina: 80
speed: 5 (climb)
size: 1M /
stability: 0
free_strike: 7
characteristics:
  - +2
  - +3
  - +1
  - +2
  - +0
actions:
  - name: "Knife in the Dark"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 damage
      <br />★ 12–16 15 damage
      <br />✸ 17+ 18 damage 
      <br />**Effect:** The mournblade is invisible to the target until the start of their next turn."
maneuvers:
  - name: "Shadow Step"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Special 
      <br />**Effect:** If the mournblade is concealed, they can teleport to another square in concealment granted by darkness within 10."
traits:
  - name: "Of the Umbra"
    desc: "The cloak ignores concealment granted by darkness. While the cloak is in direct sunlight, they have damage weakness 3. While the cloak is concealed, they have damage immunity 3."

# SHADOW ELF NOCTIS MAGE

name: "SHADOW ELF NOCTIS MAGE"
level: 6
roles:
  - PLATOON
  - HEXER
ancestry:
  - Fey
  - Humanoid
  - Shadow
  - Elf
ev: 16
stamina: 70
speed: 5 (climb)
size: 1M /
stability: 0
free_strike: 6
characteristics:
  - +0
  - +2
  - +3
  - +1
  - +1
actions:
  - name: "Blotting Bolt"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 5
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage
      <br />★ 12–16 14 damage
      <br />✸ 17+ 17+ damage 
      <br />**Effect:** The target has a bane on their next strike. 
      <br />**3 Malice** The target has a double bane on the next signature action they use. "
  - name: "Enemies in the Dark"
    desc:
      "
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Melee 1
      <br />**Target** Two enemies
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; R< 1 the target makes a free strike against an enemy of the noctis mage’s choice.
      <br />★ 12–16 10 damage; R< 2 the target makes a free strike against an enemy of the noctis mage’s choice.
      <br />✸ 17+ 13 damage; R< 3 the target uses a signature action against an enemy of the noctis mage’s choice."
traits:
  - name: "Of the Umbra"
    desc: "The cloak ignores concealment granted by darkness. While the cloak is in direct sunlight, they have damage weakness 3. While the cloak is concealed, they have damage immunity 3."

# SHADOW ELF PANTHER

name: "SHADOW ELF PANTHER"
level: 4
roles:
  - PLATOON
  - BRUTE
ancestry:
  - Fey
  - Humanoid
  - Shadow
  - Elf
ev: 12
stamina: 70
speed: 5 (climb)
size: 1M /
stability: 0
free_strike: 6
characteristics:
  - +3
  - +2
  - -1
  - +1
  - +1
actions:
  - name: "Dusk Cleave"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage
      <br />★ 12–16 13 damage
      <br />✸ 17+ 16 damage; I< 3 [[bleeding]] (save ends) 
      <br />**Effect:** The panther makes a free strike against a creature or object adjacent to the target."
  - name: "Bladestorm"
    desc:
      "
      <br />**Keywords** Area, Ranged, Weapon
      <br />**Distance** 2 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 corruption damage
      <br />★ 12–16 8 corruption damage; I< 2 [[dazed]] (save ends)
      <br />✸ 17+ 10 corruption damage; I< 3 [[dazed]] (save ends) 
      <br />**Effect:** The panther has a double edge on strikes against targets [[dazed]] by this ability."
traits:
  - name: "Of the Umbra"
    desc: "The cloak ignores concealment granted by darkness. While the cloak is in direct sunlight, they have damage weakness 3. While the cloak is concealed, they have damage immunity 3."


# SHADOW ELF ECLIPSE

name: "SHADOW ELF ECLIPSE"
level: 6
roles:
  - LEADER
ancestry:
  - Fey
  - Shadow
  - Elf
ev: 32
stamina: 180
speed: 6 (climb)
size: 1M /
stability: 1
free_strike: 7
characteristics:
  - +4
  - +3
  - +2
  - +1
  - +2
actions:
  - name: "Manifold Blade"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 damage; I< 2 [[bleeding]] (save ends)
      <br />★ 12–16 16 damage; I< 3 [[bleeding]] (save ends)
      <br />✸ 17+ 19 damage; I< 4 [[bleeding]] (save ends) 
      <br />**2 Malice** The potency of this ability increases by 1."
maneuvers:
  - name: "Grasping Shadow"
    desc: "
      <br />**Keywords** Magic
      <br />**Distance** Ranged 5
      <br />**Target** Three creatures or objects casting a shadow
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 pull 5; I< 2 [[slowed]] (save ends)
      <br />★ 12–16 pull 7; I< 3 [[slowed]] (save ends)
      <br />✸ 17+ pull 10; I< 4 [[slowed]] (save ends) 
      <br />**Effect:** The eclipse makes a free strike against each target pulled into an adjacent square."
ta:
  - name: "PUT IT OUT!"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** Special 
      <br />**Trigger** An enemy uses an ability that emits light, such as fire. 
      <br />**Effect:** The enemy has a double bane on the ability. End 
      <br />**Effect:** At the end of their turn, the eclipse can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way. Of the Umbra The eclipse ignores concealment granted by darkness. While the eclipse is in direct sunlight, they have damage weakness 3. While the eclipse is concealed, they have damage immunity 3."
va:
  - name: "From the Shadows (Villain Action 1)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 5
      <br />**Target** All allies 
      <br />**Effect:** The eclipse calls forth one brush stalker that appears within distance. Each target then shifts up to their speed and makes a free strike."
  - name: "Cast Away All Hope (Villain Action 2)"
    desc: "
      <br />**Keywords** Magic
      <br />**Distance** 3 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** The eclipse dispels their enemies’ hard  -earned advantages, removing each target’s surges. Each ally ignores edges and additional effects of each target’s damaging abilities until the end of the round."
  - name: "Umbral Hunger (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 3 cube within 5
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 7 corruption damage
      <br />★ 12–16 12 corruption damage
      <br />✸ 17+ 15 corruption damage 
      <br />**Effect:** R< 3 speed becomes zero (save ends). The affected area is shrouded in darkness and becomes concealment. When an enemy starts their turn in an affected square, they take 5 corruption damage."


# BRUSH STALKER

name: "BRUSH STALKER"
level: 4
roles:
  - PLATOON
  - MOUNT
ancestry:
  - Animal
  - Fey
ev: 12
stamina: 60
speed: 8
size: 2 /
stability: 3
free_strike: 5
characteristics:
  - +3
  - +2
  - -1
  - +0
  - +1
actions:
  - name: "Gore"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 10 damage
      <br />✸ 17+ 13 damage"
  - name: "Reclamation"
    desc:
      "
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 2 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 4 corruption damage; M< 1 [[weakened]] (save ends)
      <br />★ 12–16 7 corruption damage; M< 2 [[weakened]] (save ends)
      <br />✸ 17+ 10 corruption damage; M< 3 [[weakened]] (save ends)"
traits:
  - name: "Suneater"
    desc: "The brush stalker sheds darkness like other creatures would shed light. Each square within 2 of the brush stalker is devoid of light and provides concealment."
  name: "Wyrd Dyr"
    desc: "Each non brush stalker creature with the Animal keyword is [[frightened]] while they have [[Draw Steel Rules#LINE OF EFFECT|line of effect]] to the brush stalker."

# WODE ELF LOOKOUT

name: "WODE ELF LOOKOUT"
level: 1
roles:
  - MINION
  - SUPPORT
ancestry:
  - Fey
  - Humanoid
  - Wode
  - Elf
ev: 3 for eight minions
stamina: 4
speed: 7
size: 1M /
stability: 0
with-captain:
speed: +2
free_strike: 1
characteristics:
  - 0
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Longbow"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 8
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage
      <br />★ 12–16 2 damage
      <br />✸ 17+ 3 damage There! A wode elf within 5 of the lookout can make a ranged strike as if occupying the lookout’s space."
traits:
  - name: "Masking Glamor"
    desc: "The lookout immediately hides at the end of their turn while in cover or concealment, even if they are observed."

# WODE ELF RUNNER

name: "WODE ELF RUNNER"
level: 1
roles:
  - MINION
  - HARRIER
ancestry:
  - Fey
  - Humanoid
  - Wode
  - Elf
ev: 3 for eight minions
stamina: 4
speed: 7
size: 1M /
stability: 0
with-captain: Edge on strikes
free_strike: 1
characteristics:
  - 0
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Spear"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage
      <br />★ 12–16 2 damage
      <br />✸ 17+ 3 damage 
      <br />**Effect:** The runner can shift 2 before charging while using this ability."
traits:
  - name: "Masking Glamor"
    desc: "The lookout immediately hides at the end of their turn while in cover or concealment, even if they are observed."

# WODE ELF SCOUT

name: "WODE ELF SCOUT"
level: 1
roles:
  - MINION
  - AMBUSHER
ancestry:
  - Fey
  - Humanoid
  - Wode
  - Elf
ev: 3 for eight minions
stamina: 4
speed: 10
size: 1M /
stability: 0
with-captain: Edge on strikes
free_strike: 2
characteristics:
  - 0
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Daggers"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage"
traits: 
  - name: "Hunter’s Glamor"
    desc: "The scout immediately hides at the end of their turn, even if they are observed."


# WODE ELF YEOMAN

name: "WODE ELF YEOMAN"
level: 1
roles:
  - MINION
  - ARTILLERY
ancestry:
  - Fey
  - Humanoid
  - Wode
  - Elf
ev: 3 for eight minions
stamina: 3
speed: 7
size: 1M /
stability: 0
with-captain: Strike damage +1
free_strike: 2
characteristics:
  - +2
  - +1
  - 0
  - 0
  - +1
actions:
  - name: "Heavy Longbow"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 12
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage; push 1
      <br />★ 12–16 4 damage; push 2
      <br />✸ 17+ 5 damage; push 3"
traits:
  - name: "Masking Glamor"
    desc: "The lookout immediately hides at the end of their turn while in cover or concealment, even if they are observed."

# WODE ELF DRUID

name: "WODE ELF DRUID"
level: 2
roles:
  - PLATOON
  - CONTROLLER
ancestry:
  - Fey
  - Humanoid
  - Wode
  - Elf
ev: 8
stamina: 30
speed: 7
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - 0
  - +1
  - 0
  - 0
  - +2
actions:
  - name: "Entangling Vines"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** 3 cube within 10
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; pull 1
      <br />★ 12–16 8 damage; pull 3; M< 1 [[slowed]] (save ends)
      <br />✸ 17+ 10 damage; pull 5; M< 2 [[slowed]] (save ends) 
      <br />**Effect:** A creature [[slowed]] by this ability can’t search for hidden creatures until the condition ends. 
      <br />**3 Malice** The area of the cube and the potency of the effect both increase by 1."
maneuvers:
  - name: "The Wode Protects Us"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** Magic
      <br />**Distance** Self and Ranged 5
      <br />**Target** Self and 3 allies 
      <br />**Effect:** Each target teleports to a square within 10 that has cover or concealment from all enemies.
traits:
  - name: "Masking Glamor"
    desc: "The elf immediately hides at the end of their turn while in cover or concealment, even if they are observed."

# WODE ELF GREEN SEER

name: "WODE ELF GREEN SEER"
level: 1
roles:
  - PLATOON
  - HEXER
ancestry:
  - Fey
  - Humanoid
  - Wode
  - Elf
ev: 6
stamina: 20
speed: 7
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - 0
  - +1
  - 0
  - +2
  - +1
actions:
  - name: "The Forest’s Embrace"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 7 damage; I< 1 [[restrained]] (save ends)
      <br />✸ 17+ 9 damage; I< 2 [[restrained]] (save ends) 
      <br />**Effect:** A creature [[restrained]] by this ability can’t search for hidden creatures until the condition ends."
maneuvers:
  - name: "The Natural Cycle"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** 2 creatures
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage; P< 1 target has a double bane on strikes (save ends)
      <br />✸ 17+ 6 damage; P< 2 [[bleeding]] (save ends), target has a double bane on strikes (save ends) 
      <br />**Effect:** The green seer causes lichen to form and encroach upon each target. "
ta:
  - name: "Foreseen Punishment (Free Triggered Action)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 5
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature uses a triggered action targeting the green seer or an ally within distance. 
      <br />**Effect:** The green seer makes a free strike against the target."
traits:
  - name: "Masking Glamor"
    desc: "The elf immediately hides at the end of their turn while in cover or concealment, even if they are observed."

# WODE ELF GREENSKEEPER

name: "WODE ELF GREENSKEEPER"
level: 1
roles:
  - PLATOON
  - DEFENDER
ancestry:
  - Fey
  - Humanoid
  - Wode
  - Elf
ev: 6
stamina: 40
speed: 7
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - 0
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Growing Longsword"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 7 damage
      <br />✸ 17+ 9 damage 
      <br />**Effect:** [[taunted]] (EoT). The greenskeeper can shift 3 after making the attack. 
      <br />**2 Malice** The distance increases to Melee 5."
maneuvers:
  - name: "Overgrowth"
      <br />**Cost** 3 Malice
      <br />**Keywords** Area, Ranged
      <br />**Distance** 3 cube within 10
      <br />**Target** Special 
      <br />**Effect:** The affected area is overgrown with heavy brush and bramble. It provides cover and concealment for the greenskeeper and all allies, and is considered difficult terrain for enemies. An enemy that starts their turn in an affected square takes 3 damage."
traits:
  - name: "Masking Glamor"
    desc: "The elf immediately hides at the end of their turn while in cover or concealment, even if they are observed."

# WODE ELF SENTRY

name: "WODE ELF SENTRY"
level: 1
roles:
  - PLATOON
  - SUPPORT
ancestry:
  - Fey
  - Humanoid
  - Wode
  - Elf
ev: 6
stamina: 30
speed: 7
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - 0
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Tracer Longbow"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 7 damage
      <br />✸ 17+ 9 damage; marked (save ends) 
      <br />**Effect:** Each ally has an edge on strikes and abilities against marked targets until the condition ends.
      <br />**3 Malice** The sentry targets two additional creatures or objects."
maneuvers:
  - name: "Death Blossom"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** Area, Weapon
      <br />**Distance** 5 burst
      <br />**Target** All marked enemies 
      <br />**Effect:** 3 damage."
traits:
  - name: "Masking Glamor"
    desc: "The elf immediately hides at the end of their turn while in cover or concealment, even if they are observed."

# WODE ELF TREE CHIRUGEON

name: "WODE ELF TREE CHIRUGEON"
level: 2
roles:
  - PLATOON
  - HARRIER
ancestry:
  - Fey
  - Humanoid
  - Wode
  - Elf
ev: 8
stamina: 40
speed: 7
size: 1M /
stability: 0
free_strike: 4
characteristics:
  - +1
  - +2
  - 0
  - 0
  - 0
actions:
  - name: "Wild Ax"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage; push 1
      <br />★ 12–16 9 damage; push 3
      <br />✸ 17+ 12 damage; push 5 
      <br />**Effect:** The tree chirugeon can make a ranged free strike before using this ability. <br />**5 Malice** The tree chirugeon uses this ability again."
maneuvers:
  - name: "The Wode Protects Us"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** Magic
      <br />**Distance** Self and Ranged 5
      <br />**Target** Self and 3 allies 
      <br />**Effect:** Each target teleports to a square within 10 that has cover or concealment from all enemies.
traits:
  - name: "Masking Glamor"
    desc: "The elf immediately hides at the end of their turn while in cover or concealment, even if they are observed."

# WODE ELF TREE GUERILLA

name: "WODE ELF TREE GUERILLA"
level: 3
roles:
  - PLATOON
  - AMBUSHER
ancestry:
  - Fey
  - Humanoid
  - Wode
  - Elf
ev: 10
stamina: 50
speed: 7 (teleport)
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - 0
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Splinter Dagger"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 11 damage
      <br />✸ 17+ 14 damage; M< 2 [[bleeding]] (save ends) 
      <br />**Effect:** The tree guerilla can teleport 3 after using this ability. <br />**3 Malice** The tree guerilla targets an additional creature or object. The tree guerilla deals an additional 3 damage if both targets are adjacent to each other. 
ta:
  - name: "Do Not Hesitate in the Wode"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** —
      <br />**Distance** Self and Squad
      <br />**Target** Self and Squad 
      <br />**Trigger** An ally ends their turn while the tree guerilla hasn’t acted this round. 
      <br />**Effect:** The targets take their turn immediately. Each target has an edge on their abilities until the end of their turn."
traits:
  - name: "Hunter's Glamor"
    desc: "The elf immediately hides at the end of their turn while in cover or concealment, even if they are observed."
# WODE ELF TREE GWEIADUR

name: "WODE ELF TREE GWEIADUR"
level: 3
roles:
  - PLATOON
  - ARTILLERY
ancestry:
  - Fey
  - Humanoid
  - Wode
  - Elf
ev: 10
stamina: 40
speed: 7
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - 0
  - +2
  - 0
  - +1
  - +0
actions:
  - name: "Snare Bow"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Strike, Weapon
      <br />**Distance** Ranged 15
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 11 damage
      <br />✸ 17+ 14 damage; A< 2 [[restrained]] (save ends) 
      <br />**Effect:** The tree gweiadur can shift 3 after using this ability. <br />**3 Malice** If this ability restrains the target, an enemy within 1 of the target is also [[restrained]] (save ends)."
maneuvers: 
  - name: "You Activated My Trap!"
    desc: "
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 3 cube within 10
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage; R< 0 marked (save ends)
      <br />★ 12–16 6 damage; R< 1 [[slowed]] and marked (save ends)
      <br />✸ 17+ 9 damage; R< 2 [[slowed]] and marked (save ends) 
      <br />**Effect:** Each ally has an edge on strikes and abilities against marked targets until the condition ends."
traits:
  - name: "Masking Glamor"
    desc: "The elf immediately hides at the end of their turn while in cover or concealment, even if they are observed."

# WODE ELF WARLEADER

name: "WODE ELF WARLEADER"
level: 3
roles:
  - LEADER
ancestry:
  - Fey
  - Humanoid
  - Wode
  - Elf
ev: 20
stamina: 120
speed: 7 (teleport)
size: 1M /
stability: 2
free_strike: 5
characteristics:
  - +2
  - +3
  - +2
  - +2
  - +2
actions:
  - name: "Wodeblade"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; M< 1 [[restrained]] (save ends)
      <br />★ 12–16 12 damage; M< 2 [[restrained]] (save ends)
      <br />✸ 17+ 15 damage; M< 3 [[restrained]] (save ends) 
      <br />**Effect:** The warleader strikes each target one at a time and can teleport 3 squares between each strike. <br />**2 Malice** A target [[restrained]] by this ability takes an additional 3 damage."
maneuvers:
  - name: "Fairness is a Human Concept"
    desc: "
      <br />**Cost** 5 Malice
      <br />**Keywords** Area
      <br />**Distance** 10 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Each target can make a free strike and then shifts 3. A target immediately hides at the end of the warleader’s turn while in cover or concealment."
ta:
  - name: "Wode Sickness"
    desc: "
      <br />**Keywords** — 
      <br />**Trigger** An ally ends their turn.
      <br />**Distance** Ranged 10
      <br />**Target** 1 enemy 
      <br />**Effect:** The target must take their turn now, if they have not already taken it. P< 2 the target is [[bleeding]] and has a bane on their strikes until the end of their turn. 
traits:
  - name: "End Effect"
    desc: "At the end of their turn, the warleader can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way.
  - name: "Masking Glamor"
    desc: "The elf immediately hides at the end of their turn while in cover or concealment, even if they are observed." 
va:
  - name: "You Will ALL Witness my Blade (Villain Action 1)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 5 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** The warleader uses Wodeblade against each target with an edge."
  - name: "Suppressing Volley (Villain Action 2)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 5 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** The warleader uses Wodeblade against a single creature or object. Each target then makes a free strike."
  - name: "Is it Now or is it Then? Where are We? (Villain Action 3)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** Self and 5 burst
      <br />**Target** Self and all allies in the burst 
      <br />**Effect:** Each target becomes invisible until the start of the next round. The warleader then uses Wodeblade."


# WODENELG

name: "WODENELG"
level: 1
roles:
  - PLATOON
  - MOUNT
ancestry:
  - Plant
  - Wode
  - Elf
ev: 6
stamina: 30
speed: 10
size: 2 /
stability: 1
free_strike: 3
characteristics:
  - +2
  - +1
  - −1
  - 0
  - −1
actions:
  - name: "Gore"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 7 damage
      <br />✸ 17+ 9 damage 
      <br />**Effect:** The wodenelg’s rider can make a free strike at any point during the charge. Sure Footed The wodenelg ignores all difficult terrain, including enemy squares, and doesn’t provoke opportunity attacks by moving."
maneuvers:
  - name: "Where I End the Woods Begin"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The wodenelg and their rider become invisible until the start of their next turn."
traits: 
  - name: "Mounted stability"
    desc: "The wodenelg’s rider has damage immunity 2."
  - name: "Shared Glamor"
    desc: "If the wodenelg’s rider has the Masking Glamor or Hunter’s Galamor trait, they also gain the trait’s benefits."
  - name: "Masking Glamor"
    desc: "The elf immediately hides at the end of their turn while in cover or concealment, even if they are observed."

# FOSSIL CRYPTIC

name: "FOSSIL CRYPTIC"
level: 2
roles:
  - SOLO
ancestry:
  - Elemental
ev: 40
stamina: 250
speed: 8 (burrow)
size: 1L /
stability: 3
free_strike: 5
characteristics:
  - +3
  - +2
  - +1
  - +1
  - 0
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The cryptic takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the cryptic can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the cryptic can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Churning Trunk"
    desc: "The cryptic emits a 1 aura of swirling debris that obscures their form. Any enemy who enters the aura for the first time in a round or starts their turn there takes 5 damage. Ranged abilities that target the cryptic have a bane.
  - name: "Seismic Step"
    desc: "The cryptic ignores difficult terrain. Additionally, they have [[Draw Steel Rules#LINE OF EFFECT|line of effect]] to concealed creatures touching the ground."
actions:
  - name: "Sand Slam"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; A< 1 [[prone]]
      <br />★ 12–16 12 damage; A< 2 [[prone]] and can’t stand (EoT)
      <br />✸ 17+ 15 damage; A< 3 [[prone]] and can’t stand (save ends) 
      <br />**Effect:** Each enemy within 1 square of the target takes 2 damage."
  - name: "Stone Bone Storm"
    desc:
      "
      <br />**Keywords** Area, Melee
      <br />**Distance** 6 × 1 line within 1
      <br />**Target** Each enemy in the line
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 4 damage; M< 1 push 2
      <br />★ 12–16 7 damage; M< 2 [[prone]]
      <br />✸ 17+ 10 damage; M< 3 [[prone]] 
      <br />**Effect:** The cryptic reforms their body and appears in an unoccupied space within the line."
  - name: "Shatterstone"
    desc:
      "
      <br />**Keywords** Area, Melee
      <br />**Distance** 4 burst
      <br />**Target** Each enemy in the burst 
      <br />**Effect:** The cryptic burrows up to half their speed, then creates the burst when they breach the surface.
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 damage; push 2
      <br />★ 12–16 9 damage; push 3; [[prone]]
      <br />✸ 17+ 12 damage; push 4; [[prone]]"
maneuvers:
  - name "Stoneshift"
      <br />**Keywords** Ranged
      <br />**Distance** Ranged 5
      <br />**Target** One creature or object on the ground 
      <br />**Effect:** Slide 3. <br />**2 Malice** The distance of the ability becomes Ranged 10 and the slide increases to slide 6."
ta:
  - name: "Dissipate"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The cryptic takes damage 
      <br />**Effect:** The cryptic halves the damage, ignores any additional effects associated with it, and shifts up to 3 squares."
va:
  - name: "First Warning Quake (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Melee
      <br />**Distance** 5 burst
      <br />**Target** Each enemy on the ground in the burst 
      <br />**Effect:** Each target makes a Might test.
      <br />✸ ≤11 The target is [[prone]] and can’t stand (EoT)
      <br />★ 12–16 [[prone]]
      <br />`dice: 2d10 +
      <br />✦ 17+ No effect 
      <br />**Effect:** The affected area becomes difficult terrain."
  - name: "Final Warning Fissure (Villain Action 2)"
    desc: "
      <br />**Keywords** Area, Melee
      <br />**Distance** 5 burst
      <br />**Target** Each enemy on the ground in the burst 
      <br />**Effect:** Each target makes a Might test.
      <br />✸ ≤11 9 damage; [[prone]]
      <br />★ 12–16 5 damage
      <br />`dice: 2d10 +
      <br />✦ 17+ The target moves to the nearest unoccupied space outside the area. 
      <br />**Effect:** The area drops 2 squares. Each enemy in the area falls, while allies of the fossil cryptic drop safely. The affected area then becomes difficult terrain."
  - name: "No Escape (Villain Action 3)"
    desc: "
      <br />**Keywords** Ranged 
      <br />**Effect:** The cryptic makes an initial power roll that calls down stone pillars from the ceiling.
      <br />**Distance** Ranged 10
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 damage; [[prone]]; M< 1 [[restrained]] (save ends)
      <br />★ 12–16 9 damage; [[prone]]; M< 2 [[restrained]] (save ends)
      <br />✸ 17+ 12 damage; [[prone]]; M< 3 [[restrained]] (save ends) <br />
      <br />**Effect:** The cryptic then makes a final power roll that raises stone pillars from the floor.
      <br />**Distance** Ranged 10
      <br />**Target** Two creatures or objects on the ground
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 2 damage; vertical slide 2
      <br />★ 12–16 3 damage; vertical slide 4
      <br />✸ 17+ 4 damage; vertical slide 8 or the target is [[restrained]] against the ceiling (save ends)"

# ABYSSAL HYENA

name: "ABYSSAL HYENA"
level: 2
roles:
  - MINION
  - BRUTE
ancestry:
  - Abyssal
  - Animal
  - Gnoll
ev: 4 for eight minions
stamina: 7
speed: 8
size: 1M /
stability: 1
with-captain:
speed: +2
free_strike: 3
characteristics:
  - +2
  - +1
  - −3
  - 0
  - −2
actions:
  - name: "Snapjaw"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 6 damage; [[grabbed]]"
traits:
  - name: "Death Snap"
    desc: "When the abyssal hyena is reduced to 0 stamina, they make a free strike before dying."

# GNOLL CHAINFLAIL

name: "GNOLL CHAINFLAIL"
level: 2
roles:
  - MINION
  - ARTILLERY
ancestry:
  - Abyssal
  - Gnoll
ev: 4 for eight minions
stamina: 4
speed: 5
size: 1M /
stability: 1
with-captain: Strike damage +1
free_strike: 3
characteristics:
  - +2
  - 0
  - +1
  - 0
  - −2
actions:
  - name: "Chain Shotput"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 8
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 4 damage; push 1
      <br />✸ 17+ 6 damage; push 3"
traits:
  - name: "Death Frenzy"
    desc: "Whenever an ally within 5 is reduced to 0 stamina, the gnoll moves up to their speed and makes a free strike."


# GNOLL MAGE MAULER

name: "GNOLL MAGE MAULER"
level: 2
roles:
  - MINION
  - HEXER
ancestry:
  - Abyssal
  - Gnoll
ev: 4 for eight minions
stamina: 4
speed: 5
size: 1M /
stability: 1
with-captain: Melee distance +2
free_strike: 2
characteristics:
  - +2
  - +1
  - −1
  - 0
  - 0
actions:
  - name: "Wizard Ripper"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Strike
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 acid damage
      <br />★ 12–16 3 cold damage
      <br />✸ 17+ 5 lightning damage; target can’t use magic abilities (EoT) 
      <br />**Effect:** The target has a bane on their next power roll."
traits:
  - name: "Death Frenzy"
    desc: "Whenever an ally within 5 is reduced to 0 stamina, the gnoll moves up to their speed and makes a free strike."

# GNOLL WILDLING

name: "GNOLL WILDLING"
level: 2
roles:
  - MINION
  - HARRIER
ancestry:
  - Abyssal
  - Gnoll
ev: 4 for eight minions
stamina: 5
speed: 7
size: 1M /
stability: 1
with-captain: Edge on strikes
free_strike: 2
characteristics:
  - +1
  - +2
  - 0
  - 0
  - −2
actions:
  - name: "Flail"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 3 damage
      <br />✸ 17+ 5 damage; wildling makes a free strike on a creature adjacent to the target"
traits:
  - name: "Death Frenzy"
    desc: "Whenever an ally within 5 is reduced to 0 stamina, the gnoll moves up to their speed and makes a free strike."

# GNOLL ABYSSAL ARCHER

name: "GNOLL ABYSSAL ARCHER"
level: 2
roles:
  - BAND
  - ARTILLERY
ancestry:
  - Abyssal
  - Gnoll
ev: 4
stamina: 15
speed: 5
size: 1M /
stability: 1
free_strike: 3
characteristics:
  - 0
  - +2
  - +1
  - 0
  - −1
actions:
  - name: "Dark Longbow"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 corruption damage
      <br />★ 12–16 6 corruption damage
      <br />✸ 17+ 8 corruption damage; M< 2 [[slowed]] (save ends) 
      <br />**Effect:** This ability has an edge against creatures not at full stamina."
maneuvers:
  - name: "Cackletongue"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** Self and 2 burst
      <br />**Target** Self and all allies 
      <br />**Effect:** Each target has an edge on their next strike before the end of their next turn. Targets who haven’t used a cackletongue maneuver on this turn use it immediately at no cost.
traits:
  - name: "Death Frenzy"
    desc: "Whenever an ally within 5 is reduced to 0 stamina, the gnoll moves up to their speed and makes a free strike."
  - name: "Bloodscent"
    desc: "The abyssal archer can target creatures not at full stamina with abilities, even if they don’t have [[Draw Steel Rules#LINE OF EFFECT|line of effect]]."


# GNOLL ABYSSAL SUMMONER

name: "GNOLL ABYSSAL SUMMONER"
level: 2
roles:
  - BAND
  - SUPPORT
ancestry:
  - Abyssal
  - Gnoll
ev: 4
stamina: 20
speed: 5
size: 1M /
stability: 1
free_strike: 2
characteristics:
  - +1
  - 0
  - 0
  - +2
  - +2
actions:
  - name: "Flame Wad"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 5
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 fire damage
      <br />★ 12–16 5 fire damage
      <br />✸ 17+ 7 fire damage; I< 2 burning (save ends) 
      <br />**Effect:** A burning target takes 1d6 fire damage at the start of each of their turns until the condition ends."
maneuvers:
  - name: "Call Abyssal Hyenas"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** —
      <br />**Distance** Ranged 5
      <br />**Target** Special 
      <br />**Effect:** 2 abyssal hyenas claw out of the ground into unoccupied squares.
  - name: "Cackletongue"
    desc: "
      <br />**Cost** 4 Malice
      <br />**Keywords** —
      <br />**Distance** 2 burst
      <br />**Target** All allies 
      <br />**Effect:** 1 abyssal hyena target turns into a gnoll maurader, keeping their stamina. Targets who haven’t used a cackletongue maneuver on this turn use it immediately at no cost."
traits:
  - name: "Death Frenzy"
    desc: "Whenever an ally within 5 is reduced to 0 stamina, the gnoll moves up to their speed and makes a free strike."

# GNOLL BONESPLITTER

name: "GNOLL BONESPLITTER"
level: 2
roles:
  - BAND
  - BRUTE
ancestry:
  - Abyssal
  - Gnoll
ev: 4
stamina: 25
speed: 5
size: 1L /
stability: 1
free_strike: 3
characteristics:
  - +2
  - +1
  - 0
  - 0
  - +1
actions:
  - name: "Three-Tail Flail"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; push 2
      <br />★ 12–16 6 damage; push 2
      <br />✸ 17+ 8 damage; [[grabbed]] M< 2 target has a bane on escaping the grab 
      <br />**Effect:** The bonesplitter can’t use three  -tail flail on another target while the current target is [[grabbed]]."
maneuvers:
  - name: "Cackletongue"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** —
      <br />**Distance** Self and 2 burst
      <br />**Target** Self and all allies 
      <br />**Effect:** Each target makes a free strike. Targets who haven’t used a cackletongue maneuver on this turn use it immediately at no cost."
traits:
  - name: "Death Frenzy"
    desc: "Whenever an ally within 5 is reduced to 0 stamina, the gnoll moves up to their speed and makes a free strike."

# CACKLER

name: "CACKLER"
level: 2
roles:
  - BAND
  - HEXER
ancestry:
  - Abyssal
  - Gnoll
ev: 4
stamina: 15
speed: 5
size: 1S /
stability: 1
free_strike: 2
characteristics:
  - 0
  - 0
  - +2
  - +2
  - +2
actions:
  - name: "Moment of Brutality"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 8
      <br />**Target** 1 creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 psychic damage; I< 0 target makes a free strike against a creature of the cackler’s choice
      <br />★ 12–16 5 psychic damage; I< 1 target makes a free strike against a creature of the cackler’s choice
      <br />✸ 17+ 7 psychic damage; I< 2 target uses a signature action against a creature of the cackler’s choice 
      <br />**Effect:** An ally targeted by this ability makes a free strike instead of taking damage."
maneuvers:
  - name: "Cackletongue"
    desc: "
      <br />**Cost** 4 Malice
      <br />**Keywords** Area, Magic, Resistance
      <br />**Distance** 2 burst
      <br />**Target** All creatures in the burst 
      <br />**Effect:** Each enemy target makes a Might test.
      <br />`dice: 2d10 + 2`
      <br />✸ ≤11 [[frightened]] (save ends)
      <br />★ 12–16 [[frightened]] (EoT)
      <br />✦ 17+ No effect 
      <br />**Effect:** Targets who haven’t used a cackletongue maneuver on this turn use it immediately at no cost."
traits:
  - name: "Death Frenzy"
    desc: "Whenever an ally within 5 is reduced to 0 stamina, the gnoll moves up to their speed and makes a free strike."

# GNOLL MARAUDER

name: "GNOLL MARAUDER"
level: 2
roles:
  - BAND
  - HARRIER
ancestry:
  - Abyssal
  - Gnoll
ev: 4
stamina: 20
speed: 7
size: 1M /
stability: 1
free_strike: 2
characteristics:
  - +1
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Fury Flail"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 5 damage
      <br />✸ 17+ 7 damage; [[prone]]; A< 2 [[bleeding]] (save ends) <br />**2+ Malice** The marauder targets an additional creature or object for every 2 malice spent. 
maneuvers:
  - name: "Cackletongue"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** —
      <br />**Distance** Self and 2 burst
      <br />**Target** Self and all allies 
      <br />**Effect:** Each target shifts up to their speed. Targets who haven’t used a cackletongue maneuver on this turn use it immediately at no cost."
traits:
  - name: "Death Frenzy"
    desc: "Whenever an ally within 5 is reduced to 0 stamina, the gnoll moves up to their speed and makes a free strike."

# TUSKER DEMON

name: "TUSKER DEMON"
level: 2
roles:
  - BAND
  - BRUTE
ancestry:
  - Abyssal
  - Demon
  - Gnoll
ev: 4
stamina: 34
speed: 7
size: 3 /
stability: 3
free_strike: 3
characteristics:
  - +2
  - −1
  - −3
  - 0
  - −1
actions:
  - name: "Gore"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; push 1
      <br />★ 12–16 6 damage; push 2
      <br />✸ 17+ 8 damage; push 3; [[prone]] 
      <br />**Effect:** This ability deals an additional 4 damage while charging."
ta:
  - name: "Vengeful Tusker"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 7
      <br />**Target** Triggering enemy 
      <br />**Trigger** An enemy within distance deals damage to the tusker. 
      <br />**Effect:** The tusker demon charges the target using Gore."
traits:
  - name: "Trample"
    desc: "The tusker demon can move through enemies and objects at normal speed. When the tusker enters a creature’s space for the first time on their turn, the creature takes 5 damage. The tusker demon can end their turn in a [[prone]] size 1 creature’s space, preventing the creature from getting up."
  - name: "Lethe"
    desc: "While [[winded]], the tusker demon has an edge on strikes, and strikes have an edge against them."


# GNOLL CARNAGE

name: "GNOLL CARNAGE"
level: 2
roles:
  - LEADER
ancestry:
  - Abyssal
  - Gnoll
ev: 16
stamina: 100
speed: 5
size: 1M /
stability: 1
free_strike: 5
characteristics:
  - +3
  - +3
  - 0
  - 0
  - +3
actions:
  - name: "Shrapnel Whip"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; A< 1 [[bleeding]] (save ends)
      <br />★ 12–16 11 damage; A< 2 [[bleeding]] (save ends)
      <br />✸ 17+ 14 damage; A< 3 [[bleeding]] and [[dazed]] (save ends) 
      <br />**Effect:** An ally targeted by this ability makes a free strike instead of taking damage."
maneuvers:
  - name: "Cackletongue"
    desc: "
      <br />**Cost** 4 Malice
      <br />**Keywords** —
      <br />**Distance** Self and 5 burst
      <br />**Target** Self and all allies 
      <br />**Effect:** Each target deals an additional 3 damage with their strikes until the start of the carnage’s next turn. Targets who haven’t used a cackletongue maneuver on this turn use it immediately at no cost."
traits:
  - name: "Death Rampage"
    desc: "Whenever an ally within 5 is reduced to 0 stamina, the carnage moves up to their speed and either chooses to target 2 creatures with free strikes or one creature with their shrapnel whip."
  - name: "Endless Hunger" 
    desc: "If the carnage is reduced to 0 stamina while there are still gnolls on the battle map, one gnoll on the map is transformed into the carnage, keeping the gnoll’s stamina."
va:
  - name: "Call Up from The Abyss (Villain Action 1)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** Special 
      <br />**Effect:** The carnage summons 5 gnoll wildlings and 5 abyssal hyenas into unoccupied spaces. "
  - name: "Edacity (Villain Action 2)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** Self and 10 burst
      <br />**Target** Self and all allies 
      <br />**Effect:** Each target moves up to their speed and makes a free strike. A creature that takes damage from this villain action is also knocked [[prone]]. "
  - name: "Deepest Wounds (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 burst
      <br />**Target** Each [[winded]] enemy in the burst 
      <br />**Effect:** The carnage’s eyes and all exposed blood within distance starts to glow bright red. Each target makes a Might test.
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 The target can’t regain stamina until the end of the encounter
      <br />★ 12–16 The target can’t regain stamina (save ends)
      <br />✸ 17+ No effect 
      <br />**Effect:** Until the end of the encounter, each gnoll has a double edge power rolls that target a [[winded]] enemy."

# GOBLIN RUNNER

name: "GOBLIN RUNNER"
level: 1
roles:
  - MINION
  - HARRIER
ancestry:
  - Goblin
  - Humanoid
ev: 3 for eight minions
stamina: 4
speed: 6 (climb)
size: 1S /
stability: 0
with-captain: Edge on strikes
free_strike: 1
characteristics:
  - −2
  - +2
  - +0
  - +0
  - −1
actions:
  - name: "Club Charge"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage
      <br />★ 12–16 2 damage
      <br />✸ 17+ 3 damage Crafty The runner doesn’t provoke opportunity attacks by moving."


# GOBLIN SNIPER

name: "GOBLIN SNIPER"
level: 1
roles:
  - MINION
  - ARTILLERY
ancestry:
  - Goblin
  - Humanoid
ev: 3 for eight minions
stamina: 3
speed: 5 (climb)
size: 1S /
stability: 0
with-captain: Ranged distance +5
free_strike: 2
characteristics:
  - −2
  - +2
  - +0
  - +0
  - −1
actions:
  - name: "Bow"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage 
      <br />**Effect:** If the sniper doesn’t use a move action this turn, the ability has an edge."
traits:
  - name: "Crafty"
    desc: "The goblin doesn’t provoke opportunity attacks by moving."


# GOBLIN SPINECLEAVER

name: "GOBLIN SPINECLEAVER"
level: 1
roles:
  - MINION
  - BRUTE
ancestry:
  - Goblin
  - Humanoid
ev: 3 for eight minions
stamina: 5
speed: 5 (climb)
size: 1S /
stability: 0
with-captain: Strike damage +1
free_strike: 2
characteristics:
  - +2
  - +0
  - +0
  - +0
  - −1
actions:
  - name: "Axe"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage; push 1
      <br />★ 12–16 4 damage; push 3
      <br />✸ 17+ 5 damage; push 4"
traits:
  - name: "Crafty"
    desc: "The goblin doesn’t provoke opportunity attacks by moving."

# SKITTERLING

name: "SKITTERLING"
level: 1
roles:
  - MINION
  - HEXER
ancestry:
  - Animal
  - Goblin
ev: 3 for eight minions
stamina: 3
speed: 5 (fly)
size: 1T /
stability: 0
with-captain:
speed: +3
free_strike: 1
characteristics:
  - −5
  - +2
  - −4
  - +0
  - −2
actions:
  - name: "Claws"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 poison damage
      <br />★ 12–16 2 poison damage
      <br />✸ 17+ 3 poison damage 
      <br />**Effect:** The target has a bane on their next strike."


# GOBLIN ASSASSIN

name: "GOBLIN ASSASSIN"
level: 1
roles:
  - BAND
  - AMBUSHER
ancestry:
  - Goblin
  - Humanoid
ev: 3
stamina: 15
speed: 6 (climb)
size: 1S /
stability: 0
free_strike: 2
characteristics:
  - −2
  - +2
  - +0
  - +0
  - −2
actions:
  - name: "Sword Stab"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 6 damage
      <br />✸ 17+ 7 damage 
      <br />**Effect:** This ability deals an additional 2 damage if the scoundrel has an edge on the power roll."
  - name: "Shadow Chains"
    desc:
      "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** Three creatures
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 corruption damage; A< 0 [[restrained]] (save ends)
      <br />★ 12–16 4 corruption damage; A< 1 [[restrained]] (save ends)
      <br />✸ 17+ 5 corruption damage; A< 2 [[restrained]] (save ends)"
traits:
  - name: "Crafty"
    desc: "The goblin doesn’t provoke opportunity attacks by moving."
  - name: "Hide While Observed"
    desc: "The assassin can take the Hide maneuver even while observed, though they still must have cover or concealment."


# GOBLIN CURSESPITTER

name: "GOBLIN CURSESPITTER"
level: 1
roles:
  - BAND
  - HEXER
ancestry:
  - Goblin
  - Humanoid
ev: 3
stamina: 10
speed: 5 (climb)
size: 1S /
stability: 0
free_strike: 1
characteristics:
  - −2
  - +1
  - +0
  - +2
  - +0
actions:
  - name: "Eye of Surlach"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 15
      <br />**Target** One creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 corruption damage; I< 0 [[weakened]] (save ends)
      <br />★ 12–16 4 corruption damage; I< 1 [[weakened]] (save ends)
      <br />✸ 17+ 5 corruption damage; I< 2 [[weakened]] (save ends)"
maneuvers:
  - name: "Dizzying Hex"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 I< 0 [[prone]]
      <br />★ 12–16 I< 1 [[prone]] can’t stand (EoT)
      <br />✸ 17+ [[prone]] I< 2 and can’t stand (save ends)"
traits:
  - name: "Crafty"
    desc: "The goblin doesn’t provoke opportunity attacks by moving."

# GOBLIN STINKER

name: "GOBLIN STINKER"
level: 1
roles:
  - BAND
  - CONTROLLER
ancestry:
  - Goblin
  - Humanoid
ev: 3
stamina: 10
speed: 5 (climb)
size: 1S /
stability: 0
free_strike: 1
characteristics:
  - −2
  - +1
  - +0
  - +0
  - +2
actions:
  - name: "Toxic Winds"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 3 cube within 15
      <br />**Target** Each enemy in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 poison damage; slide 1
      <br />★ 12–16 2 poison damage; slide 2
      <br />✸ 17+ 3 poison damage; slide 3 <br />**1+ Malice** Increase the slide for one target by 2 squares for each malice spent."
maneuvers:
  - name: "Swamp Gas"
    desc: "
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 3 cube within 10
      <br />**Target** Special 
      <br />**Effect:** The area is filled with a green haze until the start of the stinker’s next turn or until the stinker is reduced to stamina 0. The area is difficult terrain for non-goblin creatures, and each such creature who moves within the area takes 2 poison damage for each square moved. The haze can’t be dispersed by wind."
traits:
  - name: "Crafty"
    desc: "The goblin doesn’t provoke opportunity attacks by moving."

# GOBLIN UNDERBOSS

name: "GOBLIN UNDERBOSS"
level: 1
roles:
  - BAND
  - SUPPORT
ancestry:
  - Goblin
  - Humanoid
ev: 3
stamina: 15
speed: 5 (climb)
size: 1S /
stability: 0
free_strike: 1
characteristics:
  - −1
  - +2
  - +0
  - +0
  - +1
actions:
  - name: "Swordplay"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage 
      <br />**Effect:** One ally adjacent to the target can make a free strike against them."
maneuvers:
  - name: "Get Reckless!"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 5 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Until the start of the underboss’s next turn, each target has an edge on strikes, and strikes made against them have an edge. 2 Malice Strikes don’t have an edge against a target."
traits:
  - name: "Crafty"
    desc: "The goblin doesn’t provoke opportunity attacks by moving."

# GOBLIN WARRIOR

name: "GOBLIN WARRIOR"
level: 1
roles:
  - BAND
  - HARRIER
ancestry:
  - Goblin
  - Humanoid
ev: 3
stamina: 15
speed: 6 (climb)
size: 1S /
stability: 0
free_strike: 1
characteristics:
  - −2
  - +2
  - +0
  - +0
  - −1
actions:
  - name: "Spear Charge"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage"
  - name: "Bury the Point
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; M< 0 [[bleeding]] (save ends)
      <br />★ 12–16 6 damage; M< 1 [[bleeding]] (save ends)
      <br />✸ 17+ 7 damage; M< 2 [[bleeding]] (save ends)"
traits:
  - name: "Crafty"
    desc: "The goblin doesn’t provoke opportunity attacks by moving."

# GOBLIN MONARCH

name: "GOBLIN MONARCH"
level: 1
roles:
  - LEADER
ancestry:
  - Goblin
  - Humanoid
ev: 12
stamina: 80
speed: 6 (climb)
size: 1S /
stability: 1
free_strike: 4
characteristics:
  - +3
  - +2
  - −4
  - +0
  - −3
actions:
  - name: "Handaxe"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 10 damage
      <br />✸ 17+ 13 damage 
      <br />**Effect:** An ally within 10 of the monarch can make a free strike."
maneuvers:
  - name: "Get in Here!"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Ranged 20
      <br />**Target** Special 
      <br />**Effect:** Two goblin runners appear in unoccupied spaces."
ta:
  - name: "Meat Shield"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** One ally 
      <br />**Trigger** A creature targets the monarch with a strike. 
      <br />**Effect:** The ally becomes the target of the triggering strike instead. End 
      <br />**Effect:** At the end of their turn, the monarch can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
traits:
  - name: "Crafty"
    desc: "The goblin doesn’t provoke opportunity attacks by moving."
va:
  - name: "What Are You Waiting For? (Villain Action 1)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 10 burst
      <br />**Target** Each ally 
      <br />**Effect:** Each target can move up to their speed or make a free strike. "
  - name: "Focus Fire (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** One enemy 
      <br />**Effect:** Each ally within 10 squares of the enemy can move up to their speed toward the enemy. "
  - name: "Kill! (Villain Action 3)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 10 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Each target can make a free strike, dealing an additional 3 damage."


# WAR SPIDER

name: "WAR SPIDER"
level: 1
roles:
  - TROOP
  - MOUNT
ancestry:
  - Animal
  - Goblin
ev: 12
stamina: 60
speed: 7 (climb)
size: 3 /
stability: 2
free_strike: 4
characteristics:
  - +2
  - +1
  - −4
  - +0
  - −3
actions:
  - name: "Bite"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 poison damage
      <br />★ 12–16 11 poison damage
      <br />✸ 17+ 14 poison damage; M< 2 [[weakened]] (save ends) <br />**2 Malice** M< 3 [[weakened]] (save ends)."
  - name: "Leg Blade"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 9 damage
      <br />✸ 17+ 12 damage"
  - name: "Trample"
    desc:
      "<br />**Cost** 5 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The spider shifts up to their speed and makes a Leg Blade strike against each creature who comes within 1 of the spider during the move. The spider makes one power roll against all targets."
maneuvers:
  - name: "Web"
    desc: "
      <br />**Keywords** Area, Weapon
      <br />**Distance** 3 cube within 1
      <br />**Target** All creatures in the cube
      <br />`dice: 2d10 +
      <br />✦ ≤11 A< 0 [[restrained]] (save ends)
      <br />★ 12–16 A< 1 [[restrained]] (save ends)
      <br />✸ 17+ A< 2 [[restrained]] (save ends)
      <br />**Distance** The affected area is considered difficult terrain for enemies."
ta:
  - name: "Skitter"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The spider or an ally riding the spider is targeted by an ability. 
      <br />**Effect:** The spider shifts 2. Any damage dealt by the triggering ability is halved."
traits:
  - name: "Ride Launcher"
    desc: "An ally who leaps off the back of the spider can jump up to 6 squares without a test, and takes no damage if they fall during the jump. After the jump, the first melee strike an ally makes on the same turn gains an edge."
  - name: "Wide Back"
    desc: "Two of the spider’s size: 1 allies can occupy the same space while riding the spider."


# WARG

name: "WARG"
level: 1
roles:
  - BAND
  - MOUNT
ancestry:
  - Animal
  - Goblin
ev: 3
stamina: 15
speed: 5
size: 1L /
stability: 1
free_strike: 1
characteristics:
  - +1
  - +2
  - −1
  - +0
  - −1
actions:
  - name: "Bite"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage"
maneuvers:
  - name: "Sprint"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The warg moves up to their speed.
traits:
  - name: "Mounted Charger"
    desc: "If a warg used as a mount charges, their rider gains an edge on melee strikes until the end of their turn. "
  - name: "Shared Crafty"
    desc: "If the warg’s rider has the Crafty trait, the warg also has the Crafty trait."
  - name: "Crafty"
    desc: "The goblin doesn’t provoke opportunity attacks by moving."


# GRIFFON

name: "GRIFFON"
level: 2
roles:
  - TROOP
  - MOUNT
ancestry:
  - Beast
  - Griffon
ev: 16
stamina: 80
speed: 9 (fly)
size: 2 /
stability: 2
free_strike: 5
characteristics:
  - +2
  - +2
  - -1
  - +1
  - +2
actions:
  - name: "Claw Swipes"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; shift 1
      <br />★ 12–16 10 damage; shift 2
      <br />✸ 17+ 13 damage; shift 3 
      <br />**Effect:** If this ability is used while charging, the griffon grapples one of the targets."
maneuvers:
  - name: "Crack the Earth"
    desc: "
      <br />**Keywords** Area, Ranged
      <br />**Distance** 3 cube within 8 (while flying)
      <br />**Target** All enemies Special The griffon must be grabbing a creature or object to use this maneuver. 
      <br />**Effect:** The griffon flies up to half their speed towards the ground and then sends the creature or object they’ve grappled hurtling towards the affected area.
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 6 damage; A< 1 push 3
      <br />✸ 17+ 9 damage; A< 2 push 4 and [[prone]]"
  - name: "Wing Buffet"
    desc: "
      <br />**Keywords** Area, Melee
      <br />**Distance** 4 × 2 line within 1
      <br />**Target** All creatures and objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 Push 3; A< 0 forced movement is vertical
      <br />★ 12–16 Push 4; A< 1 forced movement is vertical
      <br />✸ 17+ Push 5; A< 2 forced movement is vertical"
ta:
  - name: "Zephyr Feint"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** — 
      <br />**Trigger** The griffon takes damage
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The griffon halves the damage, doesn’t suffer any effect associated with it, and shifts 2 squares."
traits:
  - name: "Beast of Prey"
    desc: "Creatures have a double bane on escaping the griffon’s grab."
  - name: "Steady"
    desc: "Creatures have a bane on power rolls that could knock the griffon [[prone]]."


# STRIPED CONDOR GRIFFON

name: "STRIPED CONDOR GRIFFON"
level: 2
roles:
  - TROOP
  - BRUTE
ancestry:
  - Beast
  - Griffon
ev: 16
stamina: 100
speed: 7 (fly)
size: 3 /
stability: 3
free_strike: 5
characteristics:
  - +2
  - +2
  - -1
  - +2
  - +1
actions:
  - name: "Violent Thrashing"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; push 1
      <br />★ 12–16 11 damage; one target is pushed 2; the other target is vertically pushed 2
      <br />✸ 17+ 14 damage; one target is pushed 2 and [[prone]]; the other target is vertically pushed 3"
  - name: "Bound Ahead"
    desc:
      "<br />**Cost** 5 Malice
      <br />**Keywords** —
      <br />**Distance** Self (while grounded)
      <br />**Target** Self 
      <br />**Effect:** The griffon shifts up to their speed in a straight line. Each enemy who comes within 1 of the griffon during the move can choose to either take 5 damage or be knocked [[prone]]. 
maneuvers:
  - name: "Power Wing Buffet"
    desc: "
      <br />**Keywords** Area, Melee
      <br />**Distance** 5 × 3 line within 1
      <br />**Target** All creatures and objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 Push 2; M< 0 forced movement is vertical
      <br />★ 12–16 Push 4; M< 1 forced movement is vertical
      <br />✸ 17+ Push 6; M< 2 forced movement is vertical"
ta:
  - name: "Circle and Strike"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Triggering creature 
      <br />**Trigger** The griffon flies above a creature on the ground within 5. 
      <br />**Effect:** The griffon falls down upon the target, taking no damage from falling. The target takes 3 damage for each square the griffon fell and is A< 2 [[prone]] or [[grabbed]]."
traits:
  - name: "Beast of Prey"
    desc: "Creatures have a double bane on escaping the griffon’s grab."
  - name: "Steady"
    desc: "Creatures have a bane on power rolls that could knock the griffon [[prone]]."
  - name: "Banded Predator"
    desc: "The griffon is hidden whenever they have cover or concealment."

# HAG OF THE GREEN AND ROT

name: "HAG OF THE GREEN AND ROT"
level: 3
roles:
  - SOLO
ancestry:
  - Fey
  - Hag
ev: 50
stamina: 300
speed: 5 (flying, hover)
size: 1L /
stability: 1
free_strike: 6
characteristics:
  - +2
  - +1
  - +1
  - +3
  - +3
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The hag takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the hag can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the hag can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Supernatural Resistance"
    desc: "Magic and Psionic abilities used against the hag have a bane."
actions:
  - name: "Corrosive Claws"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 corruption damage; A< 1 [[weakened]] (save ends)
      <br />★ 12–16 13 corruption damage; A< 2 [[weakened]] (save ends)
      <br />✸ 17+ 16 corruption damage; A< 3 [[weakened]] (save ends)"
  - name: "Soul Steal"
    desc:
      "
      <br />**Keywords** Area, Magic
      <br />**Distance** 4 cube within 1
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 corruption damage P< 1 4 corruption damage
      <br />★ 12–16 8 corruption damage; P< 2 5 corruption damage
      <br />✸ 17+ 10 corruption damage; P< 3 6 corruption damage 
      <br />**Effect:** This ability has an edge against creatures with a soul.
      <br />**3 Malice** The hag regains stamina equal to half the damage dealt."
maneuvers:
  - name: "Shapeshifter"
    desc: "
      <br />**Keywords** Magic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The hag alters their body to become any size 1 creature, such as a house cat. If the hag uses this ability while outside of an enemy’s [[Draw Steel Rules#LINE OF EFFECT|line of effect]], the hag is considered hidden. The hag can return to their original form as a free maneuver.
      <br />**5 Malice** The hag becomes a size 2 creature instead, such as a bear. While in this form, the distance of their melee abilities increases by 1 and deal an additional 4 damage."
ta:
  - name: "Turned Upside Down"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 1 burst
      <br />**Target** All enemies in the burst 
      <br />**Trigger** A creature hits the hag with a melee strike.
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 Slide 2; R< 1 slide is vertical
      <br />★ 12–16 Slide 3; R< 2 slide is vertical, [[restrained]] (EoT)
      <br />✸ 17+ Vertical slide 5; R< 3 [[restrained]] (EoT) 
      <br />**Effect:** A creature [[restrained]] by this ability that is force moved vertically is suspended in midair until the condition ends."
va:
  - name: "Snackies for Sweeties (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 burst
      <br />**Target** All creatures 
      <br />**Effect:** The hag A< 2 attaches an ornate explosive pastry to each target. Roll power at the end of the round, targeting each creature with a pastry attached to them.
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 poison damage
      <br />★ 12–16 10 poison damage
      <br />✸ 17+ 13 poison damage 
      <br />**Special** A creature wearing a pastry or adjacent to a creature wearing a pastry can attempt a hard Might test to remove the pastry as a maneuver. On success, the pastry is destroyed without exploding. On failure, the hag rolls power for all pastries immediately."
  - name: "Animal Alacrity (Villain Action 2)"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 1 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** The hag shifts up to their speed before using this action, uses Corrosive Claws against each target of this ability, pushes each target 2 squares, and then shifts up to their speed again."
  - name: "Open the Oven (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 5 cube within 1
      <br />**Target** All creatures in the cube
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 fire damage; A< 1 [[weakened]] (save ends)
      <br />★ 12–16 10 fire damage; A< 2 [[weakened]] (save ends)
      <br />✸ 17+ 13 fire damage; A< 3 [[weakened]] (save ends) 
      <br />**Effect:** The hag turns the affected area into a roiling oven. The hag deals an additional 5 damage on abilities that target creatures in the affected area."

# GRILP

name: "GRILP"
level: 4
roles:
  - MINION
  - AMBUSHER
ancestry:
  - Devil
  - Hobgoblin
  - Infernal
ev: 6 for eight minions
stamina: 8
immunities: fire 2
speed: 7 (fly)
size: 1T /
stability: 0
with-captain:
speed: +2
free_strike: 3
characteristics:
  - −1
  - +3
  - 0
  - +1
  - 0
actions:
  - name: "Flyby Bite"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 5 damage
      <br />✸ 17+ 7 damage; shift 2 
      <br />**Effect:** The grilp moves up to their speed and hides after attacking."
traits: 
  - name: "Bat Out Of Hell"
    desc: "Each enemy has -1 on their saving throws for each adjacent grilp."
  - name: "Shifting Camouflage"
    desc: "The grilp can hide even if they don’t have cover or concealment."


# HOBGOBLIN BRANDBEARER

name: "HOBGOBLIN BRANDBEARER"
level: 4
roles:
  - MINION
  - HEXER
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 6 for eight minions
stamina: 7
immunities: fire 2
speed: 5
size: 1M /
stability: 0
with-captain: Edge on strikes
free_strike: 2
characteristics:
  - 0
  - +1
  - +2
  - 0
  - +3
actions:
  - name: "Searing Grasp"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Strike
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 2 fire damage
      <br />★ 12–16 4 fire damage; M< 2 fire weakness 5 (save ends)
      <br />✸ 17+ 6 fire damage; M< 3 fire weakness 5 (save ends)"
  - name: "Open Furnace" 
    desc: "An enemy that takes fire damage receives 1 additional fire damage for each adjacent brandbearer."
  - name: "Infernal Ichor" 
    desc: "If the brandbearer’s stamina drops to 0, they spray burning blood. Each creature within 1 of the brandbearer takes 2 fire damage."


# HOBGOBLIN LANCER

name: "HOBGOBLIN LANCER"
level: 4
roles:
  - MINION
  - HARRIER
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 6 for eight minions
stamina: 8
immunities: fire 2
speed: 7
size: 1M /
stability: 0
with-captain: Strike damage +2
free_strike: 2
characteristics:
  - +1
  - +2
  - 0
  - +2
  - 0
actions:
  - name: "Grim Thrust"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2 or Ranged 5
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 2 corruption damage
      <br />★ 12–16 4 corruption damage; push 1
      <br />✸ 17+ 6 corruption damage; push 2 
      <br />**Effect:** The lancer deals an additional 2 damage if they strike the target from 1 or more squares above."
traits:
  - name: "Infernal Ichor"
    desc: "If the lancer’s stamina drops to 0, they spray burning blood. Each creature within 1 of the lancer takes 2 fire damage."


# HOBGOBLIN RECRUIT

name: "HOBGOBLIN RECRUIT"
level: 4
roles:
  - MINION
  - BRUTE
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 6 for eight minions
stamina: 9
immunities: fire 2
speed: 5
size: 1M /
stability: 0
with-captain: 4 temporary
stamina:
free_strike: 3
characteristics:
  - +3
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Sword Lunge"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 5 damage
      <br />✸ 17+ 7 damage; [[grabbed]] or [[prone]]"
traits:
  - name: "Tactical Positioning"
    desc: "A non-minion ally deals 1 additional damage for each adjacent recruit."
  - name: "Infernal Ichor"
    desc: "If the recruit’s stamina drops to 0, they spray burning blood. Each creature within 1 of the recruit takes 2 fire damage."


# HOBGOBLIN BURNING WITCH

name: "HOBGOBLIN BURNING WITCH"
level: 4
roles:
  - PLATOON
  - CONTROLLER
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 12
stamina: 50
immunities: fire 4
speed: 5 (teleport)
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - 0
  - +1
  - +2
  - +2
  - +3
actions:
  - name: "Soul Burn"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 fire or corruption damage; P< 1 [[weakened]] (save ends)
      <br />★ 12–16 12 fire or corruption damage; P< 2 [[weakened]] (save ends)
      <br />✸ 17+ 15 fire or corruption damage; P< 3 [[weakened]] (save ends) 
      <br />**Cost** 2 Malice Whenever an enemy starts their turn within 3 squares of a target [[weakened]] by this ability, they are P< 2 [[weakened]] (save ends)."
maneuvers:
  - name: "Burning Legion"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self or Ranged 10
      <br />**Target** 3 creatures 
      <br />**Effect:** Teleport 5. Each creature within 1 of a target where they appear takes 3 fire damage."
traits:
  - name: "Infernal Ichor"
    desc: "If the burning witch’s stamina drops to 0, they spray burning blood. Each creature within 1 of the burning witch takes 3 fire damage."


# HOBGOBLIN DEATH CAPTAIN

name: "HOBGOBLIN DEATH CAPTAIN"
level: 4
roles:
  - PLATOON
  - SUPPORT
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 12
stamina: 60
immunities: fire 4
speed: 5
size: 1M /
stability: 2
free_strike: 5
characteristics:
  - +2
  - 0
  - +1
  - 0
  - +2
actions:
  - name: "Blightblade"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage
      <br />★ 12–16 8 damage; 4 corruption damage
      <br />✸ 17+ 8 damage; 7 corruption damage 
      <br />**Effect:** The next strike made against the target has a double edge. 
      <br />**Cost** 3 Malice 1 ally adjacent to the target uses their signature action."
maneuvers:
  - name: "On My Mark!"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 5
      <br />**Target** 1 ally 
      <br />**Effect:** The target moves up to their speed and makes a free strike."
traits:
  - name: "Battle Ready"
    desc: "The death captain and each ally within 2 impose a bane on strikes made against them by hidden creatures."
  - name: "Infernal Ichor"
    desc: "If the death captain’s stamina drops to 0, they spray burning blood. Each creature within 1 of the death captain takes 3 fire damage."


# HOBGOBLIN GRANDGUARD

name: "HOBGOBLIN GRANDGUARD"
level: 6
roles:
  - PLATOON
  - DEFENDER
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 16
stamina: 111
immunities: fire 6
speed: 4
size: 2 /
stability: 4
free_strike: 6
characteristics:
  - +3
  - +2
  - +3
  - 0
  - +2
actions:
  - name: "Tower Shield Smash"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage
      <br />★ 12–16 14 damage
      <br />✸ 17+ 17+ damage; [[prone]]
      <br />**3 Malice** Each ally adjacent to a target that is knocked [[prone]] can make a free strike."
  - name: "Thunder Rush"
    desc:
      "
      <br />**Keywords** Area, Charge, Melee, Weapon
      <br />**Distance** 1 × 2 line within 1
      <br />**Target** All enemies and objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 11 damage
      <br />✸ 17+ 14 damage 
      <br />**Effect:** Push 10. The grandguard shifts into every 2 squares left behind by targets."
traits:
  - name: "Wide Guard"
    desc: "The grandguard imposes a bane on strikes against each ally within 2."
  - name: "Infernal Ichor"
    desc: "If the grandguard’s stamina drops to 0, they spray burning blood. Each creature within 1 of the grandguard takes 3 fire damage."


# HOBGOBLIN FIRERUNNER

name: "HOBGOBLIN FIRERUNNER"
level: 5
roles:
  - PLATOON
  - HARRIER
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 14
stamina: 70
immunities: fire 5
speed: 8
size: 1M /
stability: 0
free_strike: 6
characteristics:
  - +2
  - +3
  - +1
  - +1
  - 0
actions:
  - name: "Flaming Kick"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Magic, Strike, Melee
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 fire damage
      <br />★ 12–16 13 fire damage
      <br />✸ 17+ 16 fire damage; A< 3 [[dazed]] (EoT)"
maneuvers:
  - name: "Blazing Trail"
    desc: "
      <br />**Keywords** Magic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The firerunner moves up to their speed and creates a 8 wall of fire. Each segment must include one of the squares the firerunner touched. Creatures can enter and pass through the wall. Any enemy who enters the wall for the first time in a round or starts their turn there takes 5 fire damage."
traits:
  - name: "Hot to Go"
    desc: "The firerunner ignores difficult terrain. Whenever the firerunner takes fire damage, their speed and the wall they can create with Blazing Trail increases by 4 until the end of their next turn."
  - name: "Infernal Ichor"
    desc: "If the firerunner’s stamina drops to 0, they spray burning blood. Each creature within 1 of the firerunner takes 3 fire damage."


# HOBGOBLIN INCENDIARIST

name: "HOBGOBLIN INCENDIARIST"
level: 5
roles:
  - PLATOON
  - ARTILLERY
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 14
stamina: 60
immunities: fire 5
speed: 5
size: 1M /
stability: 0
free_strike: 6
characteristics:
  - +1
  - +3
  - 0
  - +2
  - +1
actions:
  - name: "Fire Crossbow"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 fire damage
      <br />★ 12–16 14 fire damage
      <br />✸ 17+ 17+ fire damage; A< 3 burning (save ends) 
      <br />**Effect:** A burning target takes 1d6 fire damage at the start of each of their turns until the condition ends."
  - name: "Fire Ball Volley"
    desc:
      "
      <br />**Keywords** Area, Ranged
      <br />**Distance** 4 Cube within 10
      <br />**Target** All enemies and objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 fire damage; A< 1 burning (save ends)
      <br />★ 12–16 9 fire damage; A< 2 burning (save ends)
      <br />✸ 17+ 11 fire damage; [[prone]]; A< 3 burning (save ends)"
traits:
  - name: "Raining Cinders"
    desc: "The ranged free strike of each ally within 3 of the incendiarist has a distance of 10 and it now deals fire damage."
  - name: "Infernal Ichor"
    desc: "If the incendiarist’s stamina drops to 0, they spray burning blood. Each creature within 1 of the incendiarist takes 3 fire damage."


# HOBGOBLIN REDGLARE

name: "HOBGOBLIN REDGLARE"
level: 6
roles:
  - PLATOON
  - HEXER
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 16
stamina: 70
immunities: fire 6
speed: 5 (teleport)
size: 1L /
stability: 4
free_strike: 6
characteristics:
  - 0
  - +2
  - +2
  - +3
  - +3
actions:
  - name: "Eye Flash"
    desc:
      "
      <br />`dice: 2d10+3 ◆
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 corruption damage; P< 1 [[slowed]] (save ends)
      <br />★ 12–16 14 corruption damage; P< 2 [[restrained]] (save ends)
      <br />✸ 17+ 17+ corruption damage; P< 3 [[restrained]] (save ends)"
  - name: "Glare of the Old Judgements"
    desc:
      "
      <br />`dice: 2d10+3 ◆ 5 Malice
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 corruption damage
      <br />★ 12–16 10 corruption damage or P< 2 Target is judged
      <br />✸ 17+ Target is judged 
      <br />**Effect:** A judged target takes 10 corruption damage for each turn they’ve taken during the encounter. The target then regains 5 stamina for each recovery they enabled a creature to spend during the encounter."
traits:
  - name: "Infernal Ichor"
    desc: "If the redglare’s stamina drops to 0, they spray burning blood. Each creature within 1 of the redglare takes 3 fire damage."


# HOBGOBLIN SMOKEBINDER

name: "HOBGOBLIN SMOKEBINDER"
level: 5
roles:
  - PLATOON
  - AMBUSHER
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 14
stamina: 70
immunities: fire 5
speed: 7 (fly, hover)
size: 1M /
stability: 0
free_strike: 6
characteristics:
  - +1
  - +3
  - +2
  - +1
  - 0
actions:
  - name: "Choking Bolt"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 5
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 fire damage
      <br />★ 12–16 14 fire damage
      <br />✸ 17+ 17+ fire damage; R< 3 [[slowed]] (save ends) 
      <br />**Effect:** If the smokebinder had an edge on the power roll, the target cannot communicate with anyone until the end of their next turn."
maneuvers:
  - name: "Smoke Bomb"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 3 Burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** Each target makes a Might test.
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 11 damage; target has a double bane on their next power roll
      <br />★ 12–16 9 damage; target has a bane on their next power roll
      <br />✦ 17+ 5 damage"
traits:
  - name: "Essence of Smoke"
    desc: "The smokebinder can move through other creatures and objects at normal speed. The smokebinder automatically hides at the end of their turn if they didn’t take any damage since their last turn."
  - name: "Infernal Ichor"
    desc: "If the smokebinder’s stamina drops to 0, they spray burning blood. Each creature within 1 of the smokebinder takes 3 fire damage."

# HOBGOBLIN SOLDIER

name: "HOBGOBLIN SOLDIER"
level: 4
roles:
  - PLATOON
  - BRUTE
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 12
stamina: 70
immunities: fire 4
speed: 5
size: 1M /
stability: 2
free_strike: 6
characteristics:
  - +3
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Fire Flail"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 fire damage
      <br />★ 12–16 10 fire damage
      <br />✸ 17+ 13 fire damage 
      <br />**Effect:** The soldier doesn’t provoke opportunity attacks from each target until the end of the trooper’s turn."
maneuvers:
  - name: "Fight Me, Coward!"
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** 1 creature 
      <br />**Effect:** The target is P< 2 [[taunted]] (EoT). While [[taunted]] by this ability, a creature takes 1d6 fire damage whenever they use an ability or attack that doesn’t target the soldier."
traits:
  - name: "Infernal Ichor"
    desc: "If the soldier’s stamina drops to 0, they spray burning blood. Each creature within 1 of the soldier takes 3 fire damage."


# HOBGOBLIN WAR MAGE

name: "HOBGOBLIN WAR MAGE"
level: 5
roles:
  - TROOP
  - CONTROLLER
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 28
stamina: 120
immunities: fire 5
speed: 5 (teleport, hover)
size: 1M /
stability: 0
free_strike: 6
characteristics:
  - 0
  - +2
  - +3
  - +2
  - +2
actions:
  - name: "Hellfire"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 3 cube within 10
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 fire damage; M< 1 [[weakened]] (save ends)
      <br />★ 12–16 9 fire damage; M< 2 [[weakened]] (save ends)
      <br />✸ 17+ 11 fire damage; M< 3 [[weakened]] (save ends) 
      <br />**Effect:** The war mage can teleport a creature within 10 up to 2 squares before using this ability."
  - name: "Enchantments of War"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** 2 allies 
      <br />**Effect:** Each target gains 10 temporary stamina and has a double edge on their next power roll. The war mage can spend any amount of their stamina to increase the temporary stamina each target gains by an equivalent amount."
maneuvers:
  - name: "Unhallowed Ground"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 cube within 10
      <br />**Target** Special 
      <br />**Effect:** The war mage consecrates the affected area and causes it to smolder. Until the end of the encounter, the affected area is considered difficult terrain and enemies have fire weakness 10 while occupying an affected square."
ta:
  - name: "Magic Siphon"
      <br />**Keywords** Magic 
      <br />**Trigger** A creature within distance uses a strike or ability with the magic keyword
      <br />**Distance** Ranged 10
      <br />**Target** Triggering creature 
      <br />**Effect:** Any damage dealt or stamina regained by the attack or ability is halved. The war mage regains stamina equal to the remainder."
traits:
  - name: "Infernal Ichor"
    desc: "If the war mage’s stamina drops to 0, they spray burning blood. Each creature within 1 of the war mage takes 3 fire damage."
  - name: "Despair, You Who Faces Death"
    desc: "Each enemy has -2 on saving throws while within 2 squares of the war mage."


# SLAUGHTER DEMON

name: "SLAUGHTER DEMON"
level: 4
roles:
  - TROOP
  - BRUTE
ancestry:
  - Abyssal
  - Demon
  - Hobgoblin
ev: 24
stamina: 140
immunities: fire 5
speed: 7 (burrow)
size: 3 /
stability: 3
free_strike: 6
characteristics:
  - +3
  - 0
  - −1
  - +1
  - 0
actions:
  - name: "Steely Skewer"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage
      <br />★ 12–16 14 damage; A< 2 [[bleeding]] (save ends)
      <br />✸ 17+ 17+ damage; A< 3 [[bleeding]] and [[restrained]] (save ends) 
      <br />**Effect:** A creature [[restrained]] by this attack moves along with the slaughter demon until the condition ends. The slaughter demon can have up to 6 creatures or objects [[restrained]] on their weapons."
  - name: "Tail Stinger"
    desc:
      "
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Melee 5
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 poison damage; M< 1 [[weakened]] (save ends)
      <br />★ 12–16 16 poison damage; M< 2 [[weakened]] (save ends)
      <br />✸ 17+ 20 poison damage; M< 3 [[weakened]] (save ends) 
      <br />**Effect:** A target [[weakened]] by this ability has damage weakness 3 until the condition ends."
maneuvers:
  - name: "Drag Below"
    desc: "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** 1 creature or object 
      <br />**Effect:** The slaughter demon makes a free strike against the target and burrows up to their speed. The target is pulled the same number of squares the slaughter demon burrows into, including vertically."
ta:
  - name: "Devour Soul"
    desc: "
      <br />**Keywords** Magic 
      <br />**Trigger** A creature with a soul dies.
      <br />**Distance** 5 burst
      <br />**Target** Triggering creature 
      <br />**Effect:** The target can’t be brought back to life. The slaughter demon gains an edge on all power rolls for the rest of the encounter."
traits:
  - name: "Soulsight"
    desc: "Each creature within 2 of the slaughter demon can’t be hidden from them."
  - name: "Lethe"
    desc: "While [[winded]], the slaughter demon has an edge on strikes, and strikes have an edge against them."


# HOBGOBLIN BLOODLORD

name: "HOBGOBLIN BLOODLORD"
level: 6
roles:
  - LEADER
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 32
stamina: 180
immunities: fire 6
speed: 6 (teleport)
size: 1M /
stability: 2
free_strike: 7
characteristics:
  - +4
  - +2
  - +2
  - +3
  - +3
actions:
  - name: "Soul Sword"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 corruption damage; P< 2 [[bleeding]] (save ends)
      <br />★ 12–16 16 corruption damage; P< 3 [[bleeding]] (save ends)
      <br />✸ 17+ 19 corruption damage; P< 4 [[bleeding]] (save ends)
      <br />**2 Malice** Each target is marked until they die or the end of the encounter. Allies have an edge on strikes against marked targets. The bloodlord can only have up to 3 targets marked this way, removing the oldest mark first."
maneuvers:
  - name: "Take Point!"
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** 1 ally 
      <br />**Effect:** The target moves up to their speed and uses a signature action. An Army From Blood (Triggered Action) ◆ 3 Malice
      <br />**Keywords** — 
      <br />**Trigger** The target takes damage
      <br />**Distance** Ranged 10
      <br />**Target** 1 non  -minion hobgoblin 
      <br />**Effect:** 3 hobgoblin recruits crawl out of the target’s blood and appear in unoccupied spaces adjacent to the target."
traits:
  - name: "Infernal Ichor"
    desc: "If the bloodlord’s stamina drops to 0, they spray burning blood. Each creature within 1 of the bloodlord takes 3 fire damage."
  - name: "End Effect"
    desc: "At the end of their turn, the bloodlord can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
va:
  - name: "Advance! (Villain Action 1)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** Self and 10 burst
      <br />**Target** Self and all allies 
      <br />**Effect:** Each target gains 10 temporary stamina, moves up to their speed, and makes a free strike."
  - name: "Skulls Abound (Villain Action 2)"
    desc: "
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 3 aura
      <br />**Target** Self 
      <br />**Effect:** The bloodlord surrounds themselves with a storm of flying skulls until the end of the encounter. An enemy that first enters the aura or starts their turn there takes 8 corruption damage and has a bane on their next power roll until the start of their next turn."
  - name: "I am Fire! I am Death! (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 5 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 5 fire damage; P< 2 2 fire damage; push 2, [[prone]]
      <br />★ 12–16 5 fire damage; P< 3 7 fire damage; push 3, [[prone]]
      <br />✸ 17+ 5 fire damage; P< 4 10 fire damage; push 5, [[prone]] 
      <br />**Effect:** The bloodlord is wreathed in black flames until the end of the encounter. When an adjacent enemy touches or uses a melee ability against the bloodlord, they take 5 corruption damage."

# HUMAN APPRENTICE MAGE

name: "HUMAN APPRENTICE MAGE"
level: 2
roles:
  - MINION
  - CONTROLLER
ancestry:
  - Human
  - Humanoid
ev: 4 for eight minions
stamina: 4
immunities: Corruption 2, Psychic 2
speed: 5
size: 1M /
stability: 0
with-captain: Ranged distance +5
free_strike: 2
characteristics:
  - +0
  - +1
  - +0
  - +0
  - +2
actions:
  - name: "Lightning Strike"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Strike, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 lightning damage
      <br />★ 12–16 3 lightning damage
      <br />✸ 17+ 5 lightning damage 
      <br />**Effect:** If the apprentice mage doesn’t use a maneuver or a move action this turn, the target is [[slowed]] (EoT)."
traits:
  - name: "Supernatural Insight"
    desc: "The apprentice mage ignores concealment if it’s granted by a supernatural effect, or the target is supernatural."


# HUMAN ARCHER

name: "HUMAN ARCHER"
level: 1
roles:
  - MINION
  - ARTILLERY
ancestry:
  - Human
  - Humanoid
ev: 3 for eight minions
stamina: 3
immunities: Corruption 1, Psychic 1
speed: 5
size: 1M /
stability: 0
with-captain: Ranged distance +5
free_strike: 2
characteristics:
  - +0
  - +2
  - +0
  - +0
  - +0
actions:
  - name: "Crossbow"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage"
traits:
  - name: "Supernatural Insight"
    desc: "The archer ignores concealment if it’s granted by a supernatural effect, or the target is supernatural."


# HUMAN DEATH ACOLYTE

name: "HUMAN DEATH ACOLYTE"
level: 1
roles:
  - MINION
  - HEXER
ancestry:
  - Human
  - Humanoid
ev: 3 for eight minions
stamina: 3
immunities: Corruption 1, Psychic 1
speed: 5
size: 1M /
stability: 0
with-captain: Ranged distance +5
free_strike: 1
characteristics:
  - +0
  - +1
  - +0
  - +0
  - +2
actions:
  - name: "Necrotic Bolt"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Strike, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 corruption damage
      <br />★ 12–16 2 corruption damage
      <br />✸ 17+ 3 corruption damage 
      <br />**Effect:** A creature within 5 squares of the death acolyte regains 1 stamina."
traits:
  - name: "Supernatural Insight"
    desc: "The death acolyte ignores concealment if it’s granted by a supernatural effect, or the target is supernatural."


# HUMAN GUARD

name: "HUMAN GUARD"
level: 1
roles:
  - MINION
  - BRUTE
ancestry:
  - Human
  - Humanoid
ev: 3 for eight minions
stamina: 5
immunities: Corruption 1, Psychic 1
speed: 5
size: 1M /
stability: 0
with-captain:
speed: +2
free_strike: 2
characteristics:
  - +2
  - +0
  - +0
  - +0
  - +0
actions:
  - name: "Halberd"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage 
      <br />**Effect:** If the guard is flanked, they can make a free strike against an additional target adjacent to them."
traits:
  - name: "Supernatural Insight"
    desc: "The guard ignores concealment if it’s granted by a supernatural effect, or the target is supernatural."


# HUMAN RAIDER

name: "HUMAN RAIDER"
level: 1
roles:
  - MINION
  - HARRIER
ancestry:
  - Human
  - Humanoid
ev: 3 for eight minions
stamina: 4
immunities: Corruption 1, Psychic 1
speed: 7
size: 1M /
stability: 0
with-captain: Edge on strikes
free_strike: 1
characteristics:
  - +0
  - +2
  - +0
  - +0
  - +0
actions:
  - name: "Handaxes"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage
      <br />★ 12–16 2 damage
      <br />✸ 17+ 3 damage 
      <br />**Effect:** If this ability is used while charging, the raider can make a ranged free strike before using the ability."
traits:
  - name: "Supernatural Insight"
    desc: "The raider ignores concealment if it’s granted by a supernatural effect, or the target is supernatural."


# HUMAN ROGUE

name: "HUMAN ROGUE"
level: 1
roles:
  - MINION
  - AMBUSHER
ancestry:
  - Human
  - Humanoid
ev: 3 for eight minions
stamina: 4
immunities: Corruption 1, Psychic 1
speed: 7
size: 1M /
stability: 0
with-captain: Edge on strikes
free_strike: 2
characteristics:
  - +0
  - +2
  - +0
  - +0
  - +1
actions:
  - name: "Concealed Dagger"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage 
      <br />**Effect:** This ability deals an additional 3 damage if the spy was disguised or hidden before using it."
traits:
  - name: "Supernatural Insight"
    desc: "The spy ignores concealment if it’s granted by a supernatural effect, or the target is supernatural."


# HUMAN BRAWLER

name: "HUMAN BRAWLER"
level: 1
roles:
  - PLATOON
  - BRUTE
ancestry:
  - Human
  - Humanoid
ev: 6
stamina: 40
immunities: Corruption 1, Psychic 1
speed: 5
size: 1M /
stability: 0
free_strike: 4
characteristics:
  - +2
  - +1
  - +0
  - +0
  - +0
actions:
  - name: "Haymaker"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 9 damage
      <br />✸ 17+ 12 damage; M< 2 [[grabbed]], target has a bane on escaping the grab 
      <br />**Effect:** brawler deals an additional 2 damage if the target is already [[grabbed]]."
maneuvers:
  - name: "Throw"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** One creature [[grabbed]] by the brawler 
      <br />**Effect:** Push 5."
traits:
  - name: "Shoot the Hostage"
    desc: "The brawler takes half damage from strikes if they have a creature or object [[grabbed]]. The [[grabbed]] creature or object takes the other half of the damage."
  - name: "Supernatural Insight"
    desc: "The brawler ignores concealment if it’s granted by a supernatural effect, or the target is supernatural."


# HUMAN DEATH CULTIST

name: "HUMAN DEATH CULTIST"
level: 2
roles:
  - PLATOON
  - SUPPORT
ancestry:
  - Human
  - Humanoid
ev: 8
stamina: 40
immunities: Corruption 2, Psychic 2
speed: 5
size: 1M /
stability: 0
free_strike: 4
characteristics:
  - +0
  - +1
  - +0
  - +0
  - +2
actions:
  - name: "Death Scythe"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 10
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 corruption damage
      <br />★ 12–16 9 corruption damage
      <br />✸ 17+ 12 corruption damage; I< 2 [[weakened]] (save ends)
      <br />**2 Malice** The death cultist regains stamina equal to half the damage dealt by this ability."
maneuvers:
  - name: "Rise, My Minions"
    desc: "
      <br />**Cost** 1 Malice per minion
      <br />**Keywords** Area
      <br />**Distance** 5 burst
      <br />**Target** One or more dead minions Special Each target must have died during this encounter 
      <br />**Effect:** Each target revives with their full stamina. They immediately die at the end of the encounter or if the death cultist is killed. A target can be revived multiple times by this ability."
traits:
  - name: "Supernatural Insight"
    desc: "The death cultist ignores concealment if it’s granted by a supernatural effect, or the target is supernatural."


# HUMAN KNAVE

name: "HUMAN KNAVE"
level: 2
roles:
  - PLATOON
  - DEFENDER
ancestry:
  - Human
  - Humanoid
ev: 8
stamina: 50
immunities: Corruption 2, Psychic 2
speed: 5
size: 1M/
stability: 0
free_strike: 4
characteristics:
  - +2
  - +0
  - +1
  - +0
  - +0
actions:
  - name: "Morningstar & Javelin"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 9 damage
      <br />✸ 17+ 12 damage; M< 2 the target has a double bane on their next power roll 
      <br />**Effect:** [[taunted]] (EoT)."
traits:
  - name: "I’m Your Enemy"
    desc: "The knave can make a free strike against an adjacent creature they have [[taunted]] whenever the creature deals damage to a creature other than the knave."
  - name: "Overwhelm"
    desc: "An enemy who starts their turn adjacent to the knave can’t shift."
  - name: "Supernatural Insight"
    desc: "The knave ignores concealment if it’s granted by a supernatural effect, or the target is supernatural."


# HUMAN SCOUNDREL

name: "HUMAN SCOUNDREL"
level: 1
roles:
  - PLATOON
  - AMBUSHER
ancestry:
  - Human
  - Humanoid
ev: 6
stamina: 30
immunities: Corruption 1, Psychic 1
speed: 5
size: 1M /
stability: 0
free_strike: 4
characteristics:
  - +0
  - +2
  - +0
  - +0
  - +1
actions:
  - name: "Rapier & Dagger"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 9 damage
      <br />✸ 17+ 12 damage 
      <br />**Effect:** This ability deals an additional 2 damage if the scoundrel has an edge on the power roll."
  - name: "Dagger Storm"
    desc:
      "<br />**Cost** 5 Malice 
      <br />The scoundrel uses Rapier & Dagger targeting three creatures or objects. They can shift 2 before or after each strike."
traits:
  - name: "Supernatural Insight"
    desc: "The scoundrel ignores concealment if it’s granted by a supernatural effect, or the target is supernatural."


# HUMAN STORM MAGE

name: "HUMAN STORM MAGE"
level: 3
roles:
  - PLATOON
  - CONTROLLER
ancestry:
  - Human
  - Humanoid
ev: 10
stamina: 40
immunities: Corruption 3, Psychic 3
speed: 5
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - +0
  - +0
  - +2
  - +0
  - +1
actions:
  - name: "Lightning Bolt"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 15
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 lightning damage
      <br />★ 12–16 10 lightning damage
      <br />✸ 17+ 13 lightning damage
      <br />**Cost** 5 Malice The ability takes the Area keyword and becomes a 10 × 1 line that targets each enemy and object in the area."
maneuvers:
  - name: "Gust of Wind"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 cube within 1
      <br />**Target** All enemies and objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 Slide 2; M< 0 [[slowed]] (save ends)
      <br />★ 12–16 Slide 4; M< 1 [[slowed]] (save ends)
      <br />✸ 17+ Slide 6; M< 2 [[slowed]] (save ends) 
      <br />**Effect:** The gust of wind disperses gas or vapor and extinguishes any flames, including persistent effects."
traits:
  - name: "Arcane Shield"
    desc: "The mage imposes a bane on incoming melee strikes and abilities. Whenever the mage takes damage from an adjacent enemy, the enemy takes 2 lightning damage and is R< 1 pushed 2."
  - name: "Supernatural Insight"
    desc: "The storm mage ignores concealment if it’s granted by a supernatural effect, or the target is supernatural."


# HUMAN TRICKSHOT

name: "HUMAN TRICKSHOT"
level: 1
roles:
  - PLATOON
  - ARTILLERY
ancestry:
  - Human
  - Humanoid
ev: 6
stamina: 20
immunities: Corruption 1, Psychic 1
speed: 5
size: 1M /
stability: 0
free_strike: 4
characteristics:
  - +0
  - +2
  - +0
  - +1
  - +0
actions:
  - name: "Trick Crossbow"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 15
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 9 damage
      <br />✸ 17+ 12 damage 
      <br />**Effect:** The trickshot ignores cover and concealment. 
      <br />**3 Malice** The trickshot targets an additional creature or object."
traits:
  - name: "Supernatural Insight"
    desc: "The trickshot ignores concealment if it’s granted by a supernatural effect, or the target is supernatural."


# HUMAN BLACKGUARD

name: "HUMAN BLACKGUARD"
level: 1
roles:
  - LEADER
ancestry:
  - Human
  - Humanoid
ev: 12
stamina: 80
immunities: Corruption 2, Psychic 2
speed: 5
size: 1M /
stability: 2
free_strike: 4
characteristics:
  - +3
  - +2
  - +2
  - +0
  - +2
actions:
  - name: "Zweihander Swing"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 1 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 damage; M< 1 [[slowed]] (save ends)
      <br />★ 12–16 6 damage; M< 2 [[slowed]] (save ends)
      <br />✸ 17+ 8 damage; M< 3 [[slowed]] (save ends) 
      <br />**Effect:** An ally within 10 of the blackguard can make a free strike. 
      <br />**1 Malice** The ally can use their signature action instead."
maneuvers:
  - name: "You!"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** One enemy 
      <br />**Effect:** The target is marked until the start of the blackguard’s next turn. The blackguard and each of their allies gain an edge on abilities used against targets marked by the blackguard."
traits:
  - name: "End Effect"
    desc: "At the end of their turn, the blackguard can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Supernatural Insight"
    desc: "The blackguard ignores concealment if it’s granted by a supernatural effect, or the target is supernatural."
ta:
  - name: "Parry!"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** Self or one ally 
      <br />**Trigger** A creature targets the blackguard or an ally adjacent to the blackguard with a strike. 
      <br />**Effect:** The damage is halved."
va:
  - name: "Advance! (Villain Action 1)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The blackguard shifts up to their speed. During or after this movement, they can use their Zweihander Swing twice."
  - name: "Back! (Villain Action 2)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** Slide 5."
  - name: "I Can Throw My Blade and So Should You! (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Magic, Ranged, Weapon
      <br />**Distance** 3 cube within 5
      <br />**Target** Each enemy in the cube 
      <br />**Effect:** The blackguard uses their Zweihander Swing against each enemy in the area. Each ally within 5 of the area can make a free strike against any enemy in the area."

# HUMAN BANDIT CHIEF

name: "HUMAN BANDIT CHIEF"
level: 3
roles:
  - LEADER
ancestry:
  - Human
  - Humanoid
ev: 20
stamina: 120
immunities: Corruption 4, Psychic 4
speed: 5
size: 1M /
stability: 2
free_strike: 5
characteristics:
  - +2
  - +3
  - +2
  - +3
  - +2
actions:
  - name: "Whip & Magic Longsword"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** Two enemies or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; pull 1
      <br />★ 12–16 12 damage; pull 2
      <br />✸ 17+ 15 damage; pull 3 
      <br />**Effect:** A target who is adjacent to the bandit chief after the ability resolves takes 5 corruption damage.
      <br />**2 Malice** The bandit chief targets an additional enemy or object."
maneuvers:
  - name: "Kneel, Peasant!"
    desc: "
      <br />**Keywords** Melee, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One enemy or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 Push 1; M< 1 [[prone]]
      <br />★ 12–16 Push 2; M< 2 [[prone]]
      <br />✸ 17+ Push 4; M< 3 [[prone]] 2 Malice This ability targets each enemy adjacent to the bandit chief."
ta:
  - name: "Bloodstones"
      <br />**Keywords** Magic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The bandit chief makes a power roll. 
      <br />**Effect:** The bandit chief takes 4 corruption damage and increases the result of the power roll by one tier. End 
      <br />**Effect:** At the end of their turn, the bandit chief can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
traits:
  - name: "Supernatural Insight"
    desc: "The bandit chief ignores concealment if it’s granted by a supernatural effect, or the target is supernatural."
va:
  - name: "Shoot! (Villain Action 1)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 10 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Each target makes a ranged free strike."
  - name: "Form Up! (Villain Action 2)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 10 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Each target shifts up to their speed. Until the end of the encounter, the bandit chief and all allies have damage immunity 2 while adjacent to a target."
  - name: "Lead From the Front (Villain Action 3)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Shift 10. During or after this movement, the bandit chief can use their Whip & Magic Longsword against up to four targets. Each ally adjacent to a target can make a free strike against them."


# GIANT HAWK

name: "GIANT HAWK"
level: 1
roles:
  - PLATOON
  - MOUNT
ancestry:
  - Animal
  - Human
ev: 6
stamina: 30
speed: 7 (flying)
size: 2/
stability: 0
free_strike: 3
characteristics:
  - +2
  - +2
  - −3
  - +1
  - −2
actions:
  - name: "Talons"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 7 damage
      <br />✸ 17+ 9 damage; [[grabbed]]"
maneuvers:
  - name: "Dive"
    desc: "The hawk moves up to their speed. Mounted Platform Any creature riding the hawk can make a free strike during or after the hawk’s movement."


# KOBOLD PRINCEPS

name: "KOBOLD PRINCEPS"
level: 1
roles:
  - MINION
  - SUPPORT
ancestry:
  - Humanoid
  - Kobold
ev: 3 for eight minions
stamina: 4
speed: 5
size: 1S /
stability: 0
with-captain: 2 temporary
stamina:
free_strike: 1
characteristics:
  - 0
  - +2
  - 0
  - 0
  - 0
actions:
  - name: "Hasta"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage
      <br />★ 12–16 2 damage
      <br />✸ 17+ 3 damage 
      <br />**Effect:** The princeps lunges with their spear. One ally within 3 can shift 2."
traits:
  - name: "Shield? Shield!"
    desc: "The princeps has cover, a stability of 1, and can act as cover for allies when adjacent to an ally who also has this trait."

# KOBOLD SAGITTARION

name: "KOBOLD SAGITTARION"
level: 1
roles:
  - MINION
  - ARTILLERY
ancestry:
  - Humanoid
  - Kobold
ev: 3 for eight minions
stamina: 3
speed: 5
size: 1S /
stability: 0
with-captain: Ranged distance +5
free_strike: 2
characteristics:
  - 0
  - +2
  - 0
  - 0
  - 0
actions:
  - name: "Composite Bow"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Attack, Ranged, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage 
      <br />**Effect:** The sagittarius has an edge on this ability while adjacent to an ally."
traits: 
  - name: "Shield? Shield!"
    desc: "The sagittarius has cover, a stability of 1, and can act as cover for allies when adjacent to an ally who also has this trait."

# KOBOLD TIRO

name: "KOBOLD TIRO"
level: 1
roles:
  - MINION
  - DEFENDER
ancestry:
  - Humanoid
  - Kobold
ev: 3 for eight minions
stamina: 5
speed: 5
size: 1S /
stability: 0
with-captain:
speed: +1
free_strike: 1
characteristics:
  - 0
  - +2
  - 0
  - 0
  - 0
actions:
  - name: "Pugio"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage
      <br />★ 12–16 2 damage; shift 1
      <br />✸ 17+ 3 damage; shift 2 
      <br />**Effect:** The trio slices the target with their dagger. The target can’t shift until the start of the tiro’s next turn."
traits:
  - name: "Shield? Shield!"
    desc: "The trio has cover, a stability of 1, and can act as cover for allies when adjacent to an ally who also has this trait."

# KOBOLD VELES

name: "KOBOLD VELES"
level: 1
roles:
  - MINION
  - HARRIER
ancestry:
  - Humanoid
  - Kobold
ev: 3 for eight minions
stamina: 4
speed: 6
size: 1S /
stability: 0
with-captain:
speed: +1
free_strike: 1
characteristics:
  - 0
  - +2
  - 0
  - 0
  - 0
actions:
  - name: "Pilum"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage
      <br />★ 12–16 2 damage
      <br />✸ 17+ 3 damage 
      <br />**Effect:** All kobolds ignore opportunity attacks from the target until the start of the veles’ next turn."
traits:
  - name: "Shield? Shield!"
    desc: "The veles has cover, a stability of 1, and can act as cover for allies when adjacent to an ally who also has this trait."

# KOBOLD ADEPTUS

name: "KOBOLD ADEPTUS"
level: 1
roles:
  - BAND
  - ARTILLERY
ancestry:
  - Humanoid
  - Kobold
ev: 3
stamina: 10
speed: 5
size: 1S /
stability: 0
free_strike: 2
characteristics:
  - 0
  - +1
  - +2
  - 0
  - 0
actions:
  - name: "Shocking Bolt"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 15
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 lighting damage
      <br />★ 12–16 6 lighting damage
      <br />✸ 17+ 7 lighting damage 
      <br />**Effect:** The adeptus has an edge on the ability if the target is adjacent to another enemy. All enemies adjacent to the target take 2 lighting damage." 
maneuvers:
  - name: "Arcane Telum"
    desc: "
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 15
      <br />**Target** 3 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 5 damage
      <br />✸ 17+ 6 damage 
      <br />**Effect:** This attack ignores all banes and damage reduction."
traits:
  - name: "Shield? Shield!"
    desc: "The adeptus has cover, a stability of 1, and can act as cover for allies when adjacent to an ally who also has this trait."

# KOBOLD ARTIFEX

name: "KOBOLD ARTIFEX"
level: 1
roles:
  - BAND
  - CONTROLLER
ancestry:
  - Humanoid
  - Kobold
ev: 3
stamina: 10
speed: 5
size: 1S /
stability: 0
free_strike: 1
characteristics:
  - 0
  - +2
  - +1
  - 0
  - 0
actions:
  - name: "Chain Hook"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 5
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage; pull 1
      <br />★ 12–16 4 damage; pull 2
      <br />✸ 17+ 5 damage; pull 3 
      <br />**Effect:** If the target’s forced movement triggers a trap, the trap has a double edge on its power roll."
maneuvers:
  - name: "Activate Trap"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** 1 trap or terrain object 
      <br />**Effect:** The trap or terrain object instantly triggers. 
      <br />**3 Malice** The artifex can place a new trap in the encounter and instantly trigger it."
traits:
  - name: "Shield? Shield!"
    desc: "The artifex has cover, a stability of 1, and can act as cover for allies when adjacent to an ally who also has this trait."

# KOBOLD LEGIONARY

name: "KOBOLD LEGIONARY"
level: 1
roles:
  - BAND
  - DEFENDER
ancestry:
  - Humanoid
  - Kobold
ev: 9
stamina: 20
speed: 5
size: 1S /
stability: 0
free_strike: 1
characteristics:
  - +2
  - +1
  - 0
  - 0
  - 0
actions:
  - name: "Gladius"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage 
      <br />**Effect:** [[taunted]] (EoT). 
      <br />**3 Malice** The legionary and their squad can shift 2 before this ability is used."
maneuvers:
  - name: "Shield Bash"
    desc: "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage; push 1; M< 0 [[prone]]
      <br />★ 12–16 3 damage; push 2; M< 1 [[prone]]
      <br />✸ 17+ 4 damage; push 3; M< 2 [[prone]]"
traits:
  - name: "Shield? Shield!"
    desc: "The legionary has cover, a stability of 1, and can act as cover for allies when adjacent to an ally who also has this trait."

# KOBOLD SIGNIFIER

name: "KOBOLD SIGNIFIER"
level: 1
roles:
  - BAND
  - SUPPORT
ancestry:
  - Humanoid
  - Kobold
ev: 3
stamina: 15
speed: 5
size: 1S /
stability: 0
free_strike: 1
characteristics:
  - 0
  - +1
  - 0
  - 0
  - +2
actions:
  - name: "Signum"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage 
      <br />**Effect:** An ally within 10 can shift their speed, so long as they end their movement adjacent to an ally. 
      <br />**2+ Malice** 1 additional ally can shift for every 2 malice spent."
maneuvers:
  - name: "Glory to the Legion"
    desc: "
      <br />**Cost** 5 Malice
      <br />**Keywords** Area
      <br />**Distance** 5 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Each target regains 5 stamina."
traits:
  - name: "Upholding High Standards"
    desc: "Each ally that starts their turn within 5 of the signifier has their speed increased by 2 and deals an additional 2 damage on their strikes until the end of their turn. If the signifier is killed, a minion can enter their square to retrieve the signum as a free action and replace their stat block with the signifier stat block."
  - name: "Shield? Shield!"
    desc: "The signifier has cover, a stability of 1, and can act as cover for allies when adjacent to an ally who also has this trait."

# KOBOLD VENATOR

name: "KOBOLD VENATOR"
level: 1
roles:
  - BAND
  - AMBUSHER
ancestry:
  - Humanoid
  - Kobold
ev: 3
stamina: 15
speed: 5
size: 1S /
stability: 0
free_strike: 2
characteristics:
  - 0
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Dolobra & Net"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 6 damage; M< 1 [[restrained]] (save ends)
      <br />✸ 17+ 7 damage; M< 2 [[restrained]] (save ends)"
  - name: "Then We Light the Net on Fire!"
    desc: "
      <br />**3 Malice** 
      <br />Each creature and object [[restrained]] by this ability takes 2 fire damage at the start of each of their turns until the condition ends. "
traits:
  - name: "Lost in the Crowd"
    desc: "If the venator is adjacent to an ally that is not hiding, they can use the hide maneuver, even if observed. "
  - name: "Not What I Seem"
    desc: "The venator begins the encounter disguised as a minion. The venator has a double edge on their first action of the encounter, when they reveal themselves. "
  - name: "Shield? Shield!"
    desc: "The venator has cover, a stability of 1, and can act as cover for allies when adjacent to an ally who also has this trait."

# SHIELDSCALE DRANGOLIN

name: "SHIELDSCALE DRANGOLIN"
level: 1
roles:
  - TROOP
  - BRUTE
ancestry:
  - Animal
  - Kobold
ev: 12
stamina: 80
speed: 7 (burrow)
size: 3 /
stability: 0
free_strike: 5
characteristics:
  - +2
  - +1
  - −3
  - 0
  - −2
actions:
  - name: "Fiery Claws"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 fire damage
      <br />★ 12–16 10 fire damage
      <br />✸ 17+ 13 fire damage"
  - name: "Drangolin Plume"
    desc:
      "
      <br />**Cost** 5 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The drangolin shifts their speed and uses Fiery Claws against each creature who comes within 1 during the move. The drangolin makes one power roll against all targets."
  - name: "Erupt"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** 2 burst (while burrowing)
      <br />**Target** All creatures
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage; push 1; A< 0 [[prone]]
      <br />★ 12–16 8 damage; push 3; A< 1 [[prone]]
      <br />✸ 17+ 11 damage; push 5; A< 2 [[prone]] 
      <br />**Effect:** This attack deals an additional 2 fire damage against targets directly above the dragonlin."
traits:
  - name: "Ash Shot"
    desc: "Each enemy adjacent to the drangolin has a bane on strikes and can’t be hidden."

# TRAINED GELATINOUS CUBE

name: "TRAINED GELATINOUS CUBE"
level: 1
roles:
  - TROOP
  - HEXER
ancestry:
  - Animal
  - Kobold
ev: 12
stamina: 40
immunities: Acid 3
speed: 5
size: 2 /
stability: 2
free_strike: 4
characteristics:
  - +2
  - −1
  - −3
  - 0
  - −2
actions:
  - name: "Engulf"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 acid damage; A< 0 [[dazed]] (save ends)
      <br />★ 12–16 10 acid damage; A< 1 [[dazed]] (save ends)
      <br />✸ 17+ 14 acid damage; A< 2 [[restrained]] (save ends) 
      <br />**Effect:** A size: 2 or smaller creature [[restrained]] by this ability is pulled into one of the cube’s squares and moves with the cube. The creature takes 4 acid damage at the start of each of their turn while [[restrained]]. When [[restrained]] ends, the creature moves to the nearest unoccupied square adjacent to the cube. <br />**2 Malice** The cube targets 1 additional creature or object."
ta:
  - name: "You Didn’t Pay Attention! (Free Triggered Action)"
    desc: "
      <br />**Keywords** — 
      <br />**Trigger** A creature moves or is force moved into the cube.
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The cube uses Engulf with a double edge."
traits:
  - name: "Translucent Cube"
    desc: "The cube completely occupies their space, blocking [[Draw Steel Rules#LINE OF EFFECT|line of effect]] on enemy abilities. The cube is hidden until they act."

# KOBOLD CENTURION

name: "KOBOLD CENTURION"
level: 1
roles:
  - LEADER
ancestry:
  - Humanoid
  - Kobold
ev: 12
stamina: 80
speed: 5
size: 1S /
stability: 2
free_strike: 2
characteristics:
  - +2
  - +3
  - +2
  - +0
  - +2
actions:
  - name: "Pilum"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 10
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 damage; M< 1 [[weakened]] (save ends)
      <br />★ 12–16 10 damage; M< 2 [[weakened]] (save ends)
      <br />✸ 17+ 13 damage; M< 3 [[weakened]] (save ends) 
      <br />**Effect:** Each ally adjacent to a target of this ability can make a free strike. <br />**3 Malice** Each target [[weakened]] by this ability is now [[restrained]] while they are [[weakened]]."
maneuvers:
  - name: "Concentrate All Fire on That Hero!"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** One enemy 
      <br />**Effect:** The target is marked until the start of the centurion’s next turn. The centurion and each of their allies have an edge on power rolls made against targets marked by the centurion. 
      <br />**3+ Malice** The centurion targets 1 additional enemy for every 3 malice spent."
ta:
  - name: "Testudo!"
    desc: "
      <br />**Keywords** Weapon 
      <br />**Trigger** A creature uses an ability against the centurion or an ally.
      <br />**Distance** 5 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Each target shifts 2 before the damage is resolved. All kobolds with Shield? Shield! has damage immunity 2 against the triggering ability "
  - name: "Firetail Pilum (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Weapon
      <br />**Distance** 10 × 1 line within 1
      <br />**Target** All enemies in the line 
      <br />**Effect:** The centurion uses Pilum against each target, dealing an additional 5 damage. Each [[weakened]] target takes 2 fire damage at the start of each of their turns until the condition ends."
  - name: "Boom Pilum! (Villain Action 2)"
    desc: "
      <br />**Keywords** Area, Weapon
      <br />**Distance** 5 cube within 10
      <br />**Target** All enemies in the cube 
      <br />**Effect:** The centurion uses Pilum against each target with a double edge. Each target is then pushed 3."
  - name: "Are You Not Entertained?! (Villain Action 3)"
    desc: "
      <br />**Keywords** Attack, Ranged, Weapon
      <br />**Distance** 10 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** Each target is P< 2 [[taunted]] (save ends). For the rest of the encounter the centurion has damage immunity 2. All allies within 10 of the centurion can make a free strike."
traits:
  - name: "End Effect"
    desc: "At the end of their turn, the centurion can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Shield? Shield!"
    desc: "The centurion has cover, a stability of 3, and can act as cover for allies when adjacent to an ally who also has this trait."

# LIGHTBENDER

name: "LIGHTBENDER"
level: 3
roles:
  - TROOP
  - AMBUSHER
ancestry:
  - Beast
  - Lightbender
ev: 20
stamina: 100
speed: 10
size: 2 /
stability: 1
free_strike: 6
characteristics:
  - +2
  - +1
  - −3
  - +1
  - −1
actions:
  - name: "Flash Swipe"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 9 damage
      <br />★ 12–16 14 damage
      <br />✸ 17+ 18 damage 
      <br />**Effect:** The lightbender deals an additional 4 damage if they have an edge."
  - name: "Piercing Tails"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 damage
      <br />★ 12–16 12 damage; M< 1 [[bleeding]] (save ends)
      <br />✸ 17+ 15 damage; M< 2 [[bleeding]] (save ends) 
      <br />**Effect:** A creature who is [[bleeding]] from this ability has a bane on tests to search for the lightbender until the condition ends."
maneuvers:
  - name: "Hypnotic Mane"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 I< 0 [[dazed]] (save ends)
      <br />★ 12–16 I< 1 [[dazed]] (save ends)
      <br />✸ 17+ I< 2 [[dazed]] (save ends) 
      <br />**Effect:** Targets [[dazed]] by this ability have a speed of 0 while [[dazed]]. If a [[dazed]] target takes damage or if someone else spends an action to shake the creature out of their stupor, the condition ends."
ta:
  - name: "Stalker’s Afterimage"
    desc: "
      <br />**Keywords** Magic 
      <br />**Trigger** The lightbender takes damage from a strike.
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The lightbender halves the damage, doesn’t suffer any effect associated with it, and teleports 5 squares. The lightbender immediately hides if they teleport into cover or concealment."
traits:
  - name: "Avoidance"
    desc: "The lightbender always treats a save ends effect as an EoT effect."

# LIGHTBENDER POUNCER

name: "LIGHTBENDER POUNCER"
level: 3
roles:
  - TROOP
  - HARRIER
ancestry:
  - Beast
  - Lightbender
ev: 20
stamina: 100
speed: 10
size: 2
stability: 1
free_strike: 5
characteristics:
  - +2
  - +2
  - −3
  - +1
  - −1
actions:
  - name: "Pounce"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 11 damage; A< 1 [[prone]]
      <br />✸ 17+ 14 damage; A< 2 [[prone]] 
      <br />**Effect:** The pouncer makes a free strike against each target they have knocked [[prone]]."
  - name: "Sparkling Tail Whip"
    desc:
      "
      <br />**Keywords** Area, Magic
      <br />**Distance** 2 burst
      <br />**Target** All enemies and objects in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 7 damage; A< 1 dazzled (save ends)
      <br />✸ 17+ 10 damage; A< 2 dazzled (save ends) 
      <br />**Effect:** A dazzled creature has a bane on strikes and can’t have [[Draw Steel Rules#LINE OF EFFECT|line of effect]] to targets who aren’t adjacent to them."
maneuvers:
  - name: "Illusory Feint"
    desc: "
      <br />**Cost** 5 Malice
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 cube within 10
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 R< 0 [[dazed]] (save ends)
      <br />★ 12–16 R< 1 [[dazed]] (save ends)
      <br />✸ 17+ R< 2 [[dazed]] (save ends) 
      <br />**Effect:** Targets [[dazed]] by this ability have a speed of 0 while [[dazed]]. If a [[dazed]] target takes damage or if someone else spends an action to shake the creature out of their stupor, the condition ends."
ta:
  - name: "Striking Afterimage"
    desc: "
      <br />**Keywords** Magic 
      <br />**Trigger** The pouncer takes damage from a strike.
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The pouncer halves the damage, doesn’t suffer any effect associated with it, and teleports 5 squares. The pouncer makes a free strike if they teleport into a space adjacent to an enemy."
traits:
  - name: "Avoidance"
    desc: "The pouncer always treats a save ends effect as an EoT effect."

# LIZARDFOLK GRUNT

name: "LIZARDFOLK GRUNT"
level: 1
roles:
  - MINION
  - HARRIER
ancestry:
  - Humanoid
  - Lizardfolk
ev: 3 for eight minions
stamina: 4
speed: 6 (swim)
size: 1M /
stability: 0
with-captain:
speed: +2
free_strike: 1
characteristics:
  - +1
  - +2
  - 0
  - 0
  - 0
actions:
  - name: "Snap and Toss"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage
      <br />★ 12–16 2 damage; slide 2
      <br />✸ 17+ 3 damage; slide 4"
traits:
  - name: "Reptilian Escape"
    desc: "While the grunt still has a tail, whenever the grunt is [[grabbed]], [[slowed]], [[weakened]], or knocked [[prone]], the grunt can lose their tail to immediately end the effect and shift 2."

# LIZARDFOLK SHELLGUARD

name: "LIZARDFOLK SHELLGUARD"
level: 1
roles:
  - MINION
  - DEFENDER
ancestry:
  - Humanoid
  - Lizardfolk
ev: 3 for eight minions
stamina: 6
speed: 5 (swim)
size: 1L /
stability: 1
with-captain: 2 temporary
stamina:
free_strike: 1
characteristics:
  - +2
  - +1
  - 0
  - 0
  - 0
actions:
  - name: "Shield Smash"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage
      <br />★ 12–16 2 damage
      <br />✸ 17+ 3 damage 
      <br />**Effect:** The target has a bane on their next strike."
traits:
  - name: "Reptilian Escape"
    desc: "While the shellguard still has a tail, whenever the shellguard is [[grabbed]], [[slowed]], [[weakened]], or knocked [[prone]], the shellguard can lose their tail to immediately end the effect and shift 2."

# LIZARDFOLK TONGUER

name: "LIZARDFOLK TONGUER"
level: 1
roles:
  - MINION
  - ARTILLERY
ancestry:
  - Humanoid
  - Lizardfolk
ev: 3 for eight minions
stamina: 3
speed: 5 (swim)
size: 1S /
stability: 0
with-captain: Strike damage +1
free_strike: 2
characteristics:
  - 0
  - +2
  - 0
  - +1
  - 0
actions:
  - name: "Tonguelash"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 8
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage; shift 1 towards target or pull 1
      <br />★ 12–16 4 damage; shift 2 towards target or pull 2
      <br />✸ 17+ 5 damage; shift 3 towards target or pull 3 
      <br />**Effect:** If the target ends up in a space adjacent to the tonguer, they are also [[grabbed]]."
traits:
  - name: "Reptilian Escape"
    desc: "While the tonguer still has a tail, whenever the tonguer is [[grabbed]], [[slowed]], [[weakened]], or knocked [[prone]], the tonguer can lose their tail to immediately end the effect and shift 2."

# LIZARDFOLK BLOODEYE

name: "LIZARDFOLK BLOODEYE"
level: 1
roles:
  - PLATOON
  - HEXER
ancestry:
  - Humanoid
  - Lizardfolk
ev: 6
stamina: 20
speed: 5 (swim)
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - +1
  - +1
  - 0
  - +2
  - 0
actions:
  - name: "Bola Knock"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 5
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; A< 0 [[restrained]] (save ends)
      <br />★ 12–16 7 damage; A< 1 [[restrained]] (save ends)
      <br />✸ 17+ 9 damage; A< 2 [[restrained]] (save ends)"
  - name: "Bloodshot"
    desc:
      "
      <br />**Keywords** Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 acid damage; M< 0 target can’t establish [[Draw Steel Rules#LINE OF EFFECT|line of effect]] beyond 4 squares (save ends)
      <br />★ 12–16 7 acid damage; M< 1 target can’t establish [[Draw Steel Rules#LINE OF EFFECT|line of effect]] beyond 3 squares (save ends)
      <br />✸ 17+ 9 acid damage; M< 2 target can’t establish [[Draw Steel Rules#LINE OF EFFECT|line of effect]] beyond 2 squares (save ends)"
traits:
  - name: "Reptilian Escape"
    desc: "While the bloodeye still has a tail, whenever the bloodeye is [[grabbed]], [[slowed]], [[weakened]], or knocked [[prone]], the bloodeye can lose their tail to immediately end the effect and shift 2."

# LIZARDFOLK SCALETOOTH

name: "LIZARDFOLK SCALETOOTH"
level: 1
roles:
  - PLATOON
  - BRUTE
ancestry:
  - Humanoid
  - Lizardfolk
ev: 6
stamina: 46
speed: 5 (swim)
size: 1M /
stability: 0
free_strike: 4
characteristics:
  - +2
  - +1
  - 0
  - 0
  - 0
actions:
  - name: "Razor Bite"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 9 damage
      <br />✸ 17+ 12 damage; A< 2 [[bleeding]] (save ends) 
      <br />**Effect:** The potency of this ability increases by 1 if the target is [[grabbed]] by the scaletooth."
  - name: "Tail Whip"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; slide 1
      <br />★ 12–16 8 damage; slide 2; M< 1 grappled if within 2 of the scaletooth
      <br />✸ 17+ 10 damage; slide 3; M< 2 grappled if within 2 of the scaletooth 
      <br />**Effect:** The scaletooth needs their tail to use this ability. The scaletooth can’t grapple more than one creature or object with this ability."
traits:
  - name: "Reptilian Escape"
    desc: "While the scaletooth still has a tail, whenever the scaletooth is [[grabbed]], [[slowed]], [[weakened]], or knocked [[prone]], the scaletooth can lose their tail to immediately end the effect and shift 2."

# LIZARDFOLK SKYTERROR

name: "LIZARDFOLK SKYTERROR"
level: 1
roles:
  - PLATOON
  - HARRIER
ancestry:
  - Humanoid
  - Lizardfolk
ev: 6
stamina: 30
speed: 7 (swim)
size: 1S /
stability: 0
free_strike: 3
characteristics:
  - +1
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Glaive Rush"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 7 damage
      <br />✸ 17+ 9 damage; [[prone]] 
      <br />**Effect:** The skyterror can shift 4 after using this ability if they are flying."
  - name: "Poison Blowdart"
    desc:
      "
      <br />**Keywords** Ranged, Weapon
      <br />**Distance** Ranged 5
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage; M< 0 [[weakened]] (save ends)
      <br />★ 12–16 5 damage; M< 1 [[weakened]] (save ends)
      <br />✸ 17+ 7 damage; M< 2 [[weakened]] (save ends) 
      <br />**Effect:** A creature that ends their turn adjacent to a creature or object [[weakened]] by this ability is [[weakened]] (EoT)."
traits:
  - name: "Glider"
    desc: "The skyterror adds the flying keyword to their movement until the end of their next turn whenever they move at least 2 squares along the ground or fall at least 2 squares."
  - name: "Reptilian Escape"
    desc: "While the skyterror still has a tail, whenever the skyterror is [[grabbed]], [[slowed]], [[weakened]], or knocked [[prone]], the skyterror can lose their tail to immediately end the effect and shift 2."

# LIZARDFOLK DEATHREX

name: "LIZARDFOLK DEATHREX"
level: 1
roles:
  - LEADER
ancestry:
  - Humanoid
  - Lizardfolk
ev: 12
stamina: 80
speed: 5 (climb, swim)
size: 2 /
stability: 2
free_strike: 4
characteristics:
  - +3
  - +2
  - 0
  - +1
  - +2
actions:
  - name: "Ripper Spear"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 damage; pull 1; A< 1 [[bleeding]] (save ends)
      <br />★ 12–16 10 damage; pull 1; A< 2 [[bleeding]] (save ends)
      <br />✸ 17+ 13 damage; pull 2; A< 3 [[bleeding]] (save ends) 
      <br />**1 Malice** One target that is adjacent to the deathrex is [[grabbed]] by the deathrex’s mouth."
  - name: "Death Roll"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 [[grabbed]] creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; M< 1 [[dazed]] (save ends)
      <br />★ 12–16 12 damage; M< 2 [[dazed]] (save ends)
      <br />✸ 17+ 15 damage; M< 3 [[dazed]] (save ends) 
      <br />**Effect:** The target is released from the grab and slides 5."
maneuvers:
  - name: "Trundle"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The deathrex moves up to their speed. The deathrex can make a free strike on each creature that makes an opportunity attack against them during this movement."
ta:
  - name: "Swat The Fly"
    desc: "
      <br />**Keywords** — 
      <br />**Trigger** The target moves or shifts away from the deathrex.
      <br />**Distance** Melee 1
      <br />**Target** 1 adjacent creature or object 
      <br />**Effect:** Slide 5."
  - name: "Snack Attack (Villain Action 1)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** Self and 10 burst
      <br />**Target** Self and all allies in the burst 
      <br />**Effect:** Each target moves up to their speed and makes a free strike. A target receives temporary stamina: equal to the amount of damage they dealt during this action."
  - name: "Shed Some Skin (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The deathrex shifts up to their speed, leaving behind a skin shed duplicate in the space that they started in. The duplicate has 10 stamina, has no villain actions, shares the rest of the deathrex’s characteristics, and takes their turn at the same time as the deathrex."
  - name: "Thresher Thrasher (Villain Action 3)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** Self and 10 burst
      <br />**Target** Self and all allies in the burst 
      <br />**Effect:** Each target moves up to their speed. Until the end of the encounter, when a creature enters or starts their turn adjacent to a target, the target can make a free strike against them."
traits:
  - name: "Rex Reptilian Escape"
    desc: " While the deathrex still has a tail, whenever the deathrex is inflicted with an EoT or save ends effect, the deathrex can lose their tail to immediately end the effect and shift 2."

# MANTICORE

name: "MANTICORE"
level: 4
roles:
  - SOLO
ancestry:
  - Beast
  - Manticore
ev: 60
stamina: 350
speed: 10 (fly)
size: 2 /
stability: 3
free_strike: 6
characteristics:
  - +4
  - +3
  - +0
  - +0
  - -1
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The manticore takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the manticore can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the manticore can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Agile Predator"
    desc: "When the manticore deals damage to a creature, they don’t provoke opportunity attacks from that creature during that turn."
actions:
  - name: "Carnivorous Bite"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 12 damage; A< 2 [[bleeding]] (save ends)
      <br />★ 12–16 17+ damage; A< 3 [[bleeding]] (save ends)
      <br />✸ 17+ 21 damage; A< 4 [[bleeding]] (save ends) 
      <br />**Effect:** This ability has an edge against [[frightened]] targets."
  - name: "Tail Spike"
    desc:
      "
      <br />**Keywords** Ranged, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 10 damage; M< 2 3 poison damage
      <br />★ 12–16 15 damage; M< 3 7 poison damage, [[weakened]] (save ends)
      <br />✸ 17+ 19 damage; M< 4 10 poison damage, [[weakened]] (save ends) 
      <br />**1 Malice** A target [[weakened]] from this ability takes 1d6 poison damage at the start of each of their turns until the condition ends."
maneuvers:
  - name: "Harrying Claws"
    desc: "
      <br />**Keywords** Melee
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 +
      <br />✦ ≤11 Slide 1; A< 2 3 damage
      <br />★ 12–16 Slide 2; A< 3 5 damage
      <br />✸ 17+ Slide 4; A< 4 7 damage"
ta:
  - name: "Reflexive Instinct"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature deals damage to the manticore. 
      <br />**Effect:** The manticore shifts up to 5 into the air, then uses their Tail Spike ability against the target."
va:
  - name: "Trumpeting Howl (Villain Action 1)
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 burst
      <br />**Target** All creatures
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 [[frightened]] (EoT) or I< 2 (save ends)
      <br />★ 12–16 [[frightened]] (EoT) or I< 3 (save ends)
      <br />✸ 17+ [[frightened]] (save ends); I< 4 [[dazed]] (save ends)"
  - name: "Cornered Predator (Villain Action 2)
    desc: "
      <br />**Keywords** Ranged, Weapon
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The manticore shifts up to their speed, then uses their Tail Spike ability against each enemy within 10 squares."
  - name: "Debilitating Poison (Villain Action 3)
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Special 
      <br />**Effect:** The manticore sours their own poison with enmity. Until the end of the encounter, the manticore has a double edge on power rolls targeting [[weakened]] creatures. A creature [[weakened]] by the manticore’s Tail Spike ability has their speed halved and takes an additional 1d3 poison damage at the start of each of their turns until the condition ends."


# MEDUSA

name: "MEDUSA"
level: 5
roles:
  - SOLO
ancestry:
  - Accursed
  - Humanoid
  - Medusa
ev: 70
stamina: 400
immunities: Poison 5, Acid 5
speed: 5
size: 1M /
stability: 0
free_strike: 7
characteristics:
  - +2
  - +4
  - +0
  - +0
  - +0
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The medusa takes 2 turns each round. They can use two actions on each of their turns and can take each turn after an enemy turn they choose. While [[dazed]], the medusa can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the medusa can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
actions:
  - name: "Snake Bite"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 damage; M< 2 [[slowed]] (save ends)
      <br />★ 12–16 16 damage; M< 3 [[slowed]] (save ends)
      <br />✸ 17+ 19 damage; M< 4 [[slowed]] (save ends)"
  - name: "Damning Gaze"
    desc:
      "
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 damage; push 3
      <br />★ 12–16 16 damage; push 5
      <br />✸ 17+ 19 damage; push 7 3 Malice The medusa targets two additional creatures or objects."
  - name: "Petrify"
    desc: "
      <br />**Cost** 5 Malice
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 burst
      <br />**Target** Each enemy in the burst 
      <br />**Effect:** The medusa turns dozens of eerie snake eyes on their foes. Each target must make a Might test. A target with cover has an edge on the test.
      <br />`dice: 2d10 + 4`
      <br />✸ ≤11 [[slowed]] (save ends) or M< 4 [[restrained]] (save ends)
      <br />★ 12–16 M< 3 [[restrained]] (save ends)
      <br />✦ 17+ M< 2 [[restrained]] (save ends) 
      <br />**Effect:** An already [[slowed]] target has -1 to resist the potency. A target [[restrained]] by this ability magically begins to turn to stone. A target that ends two consecutive turns [[restrained]] by this ability is petrified (see Petrification)."
maneuvers:
  - name: "Nimble Escape"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The medusa shifts 3 and hides, even if observed."
ta:
  - name: "Venomous Spit"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** One creature 
      <br />**Trigger** A creature deals damage to the medusa.
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 13 acid damage
      <br />★ 12–16 18 acid damage
      <br />✸ 17+ 22 acid damage"
traits:
  - name: "Cunning Edge"
    desc: "The medusa has an edge on power rolls made against any creature affected by their Petrify ability."
  - name: "Many Peering Eyes"
    desc: "The medusa can’t be flanked."
  - name: "Mass Petrify (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** [[Draw Steel Rules#LINE OF EFFECT|line of effect]]
      <br />**Target** All enemies 
      <br />**Effect:** The medusa uses their Petrify ability against each target without spending Malice. Each target not behind cover has a bane on the test."
  - name: "Serpent Wings (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The medusa manifests temporary wings and vertically shifts up to their speed. During or after this movement, they can use Snake Bite and Damning Gaze once each."
  - name: "Stone Puppets (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 10 burst
      <br />**Target** Special 
      <br />**Effect:** Each stone statue and creature affected by Petrify within distance moves up to their speed and uses a signature action with an edge targeting an enemy of medusa’s choice as a free triggered action. A stone statue without its own stats has a speed of 5 and uses the Medusa’s free strike instead."

# MINOTAUR

name: "MINOTAUR"
level: 3
roles:
  - TROOP
  - HARRIER
ancestry:
  - Accursed
  - Humanoid
  - Minotaur
ev: 20
stamina: 100
speed: 8
size: 2 /
stability: 2
free_strike: 5
characteristics:
  - +2
  - +2
  - 0
  - +1
  - −1
actions:
  - name: "Flail and Blade"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; push 1
      <br />★ 12–16 11 damage; push 2
      <br />✸ 17+ 14 damage; push 3 
      <br />**Effect:** Shift 3."
  - name: "Primal Bay"
    desc:
      "<br />**Cost** 3 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The minotaur has damage immunity 2 and deals an additional 5 damage with their strikes until the end of their next turn. On their next turn, they have access to an additional maneuver."
maneuvers:
  - name: "Goring Horns"
    desc: "
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; I< 0 [[dazed]] (save ends)
      <br />★ 12–16 8 damage; I< 1 [[dazed]] (save ends)
      <br />✸ 17+ 9 damage; I< 2 [[dazed]] (save ends) 
      <br />**Effect:** The potency of this ability increases by 1 if it’s used while charging."
ta:
  - name: "Retaliatory Gore"
    desc: "
      <br />**Keywords** — 
      <br />**Trigger** The minotaur takes damage from a creature within 8.
      <br />**Distance** Self
      <br />**Target** Triggering creature 
      <br />**Effect:** The minotaur charges the target using Flail and Blade or Goring Horns."
traits:
  - name: "Minotaur Sense"
    desc: "The minotaur cannot get a result lower than tier 2 when making Tests to navigate, search, or seek."

# MINOTAUR SUNDERER

name: "MINOTAUR SUNDERER"
level: 3
roles:
  - TROOP
  - BRUTE
ancestry:
  - Accursed
  - Humanoid
  - Minotaur
ev: 20
stamina: 120
speed: 6
size: 2 /
stability: 2
free_strike: 6
characteristics:
  - +2
  - +1
  - 0
  - +2
  - −1
actions:
  - name: "Spiked Maul"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 damage; pull 1
      <br />★ 12–16 12 damage; pull 2
      <br />✸ 17+ 15 damage; pull 3 
      <br />**Effect:** A target is [[grabbed]] if they are pulled adjacent to the sunderer."
  - name: "Fearsome Bay"
    desc:
      "
      <br />**Keywords** Area
      <br />**Distance** 3 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 I< 0 [[frightened]] (save ends)
      <br />★ 12–16 I< 1 [[frightened]] (save ends)
      <br />✸ 17+ I< 2 [[frightened]] (save ends) 
      <br />**Effect:** The minotaur has damage immunity 2 and deals an additional 5 damage with their strikes until the end of their next turn."
maneuvers:
  - name: "Disemboweling Horns"
    desc: "
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 [[grabbed]] creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; push 1; M< 0 [[bleeding]] (save ends)
      <br />★ 12–16 8 damage; push 3; M< 1 [[bleeding]] (save ends)
      <br />✸ 17+ 9 damage; push 5; M< 2 [[bleeding]] (save ends) 
      <br />**Effect:** The target takes 1d6 damage at the start of each of their turns while [[bleeding]] from this ability."
ta:
  - name: "Retaliatory Gore"
    desc: "
      <br />**Keywords** — 
      <br />**Trigger** The sunderer takes damage from a creature within 6.
      <br />**Distance** Self
      <br />**Target** Triggering creature 
      <br />**Effect:** The sunderer charges the target using Spiked Maul."
traits:
  - name: "Minotaur Sense"
    desc: "The sunderer cannot get a result lower than tier 2 when making Tests to navigate, search, or seek."

# MINOTAUR BULLY

name: "MINOTAUR BULLY"
level: 8
roles:
  - MINION
  - BRUTE
ancestry:
  - Accursed
  - Humanoid
  - Minotaur
ev: 10 for eight minions
stamina: 14
speed: 6
size: 2 /
stability: 2
with-captain: Strike damage +3
free_strike: 4
characteristics:
  - +4
  - +2
  - 0
  - +3
  - −1
actions:
  - name: "Javelin and Bellow"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2 or Ranged 5
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 7 damage
      <br />✸ 17+ 9 damage; I< 4 [[taunted]] (EoT) or [[frightened]] of all minotaurs (save ends)"
traits:
  - name: "Minotaur Sense"
    desc: "The bully cannot get a result lower than tier 2 when making Tests to navigate, search, or seek."

# MINOTAUR LACKEY

name: "MINOTAUR LACKEY"
level: 8
roles:
  - MINION
  - HARRIER
ancestry:
  - Accursed
  - Humanoid
  - Minotaur
ev: 10 for eight minions
stamina: 13
speed: 8
size: 2 /
stability: 2
with-captain:
speed: +2
free_strike: 3
characteristics:
  - +3
  - +4
  - 0
  - +1
  - −1
actions:
  - name: "Horn Vault"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 6 damage; slide 1
      <br />✸ 17+ 8 damage; slide 3 
      <br />**Effect:** A target that is force moved into an obstacle is M< 3 [[bleeding]] (save ends)."
traits:
  - name: "Minotaur Sense"
    desc: "The lackey cannot get a result lower than tier 2 when making Tests to navigate, search, or seek."

# MINOTAUR STAMPEDE

name: "MINOTAUR STAMPEDE"
level: 10
roles:
  - MINION
  - DEFENDER
ancestry:
  - Accursed
  - Humanoid
  - Minotaur
  - Swarm
ev: 12 for eight minions
stamina: 17+
speed: 8
size: 4 /
stability: 2
with-captain: Edge on strikes
free_strike: 4
characteristics:
  - +5
  - +5
  - 0
  - +2
  - −1
actions:
  - name: "Bull Rush"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 5`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 7 damage; [[prone]]
      <br />✸ 17+ 9 damage; [[prone]] and M< 5 can’t stand (save ends) 
      <br />**Effect:** Each creature that the stampede moves through as a part of charging with this ability is M< 4 knocked [[prone]]."
traits:
  - name: "Swarm"
    desc: "The stampede can move through squares as if they were size -2, and can occupy other creatures’ spaces. At the start of the stampede’s turn, they can make a free strike against each creature they share a square with."

# OGRE GOON

name: "OGRE GOON"
level: 2
roles:
  - TROOP
  - BRUTE
ancestry:
  - Giant
  - Ogre
ev: 16
stamina: 100
speed: 5
size: 2 /
stability: 4
free_strike: 5
characteristics:
  - +2
  - 0
  - −1
  - 0
  - −1
actions:
  - name: "Club Swing"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; push 2
      <br />★ 12–16 11 damage; push 4
      <br />✸ 17+ 14 damage; push 6; [[prone]] 
      <br />**Effect:** This attack deals an additional 4 damage to each creature and object that takes damage from any force movement it causes."
maneuvers:
  - name: "Grabby Hand"
    desc: "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 11 damage; [[grabbed]]
      <br />✸ 17+ 14 damage; [[grabbed]] 
      <br />**Effect:** The goon can only have one target [[grabbed]] at a time. 
      <br />**1 Malice** The target has a bane on escaping the grab while the goon crushes the target in their hand."
  - name: "People Bowling"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 6 × 1 Line within 1
      <br />**Target** All creatures and objects 
      <br />**Special** The goon must be grabbing a size -1 creature or object to use this maneuver. 
      <br />**Effect:** The goon hurls what’s in their hand down the line and rolls power. The hurled creature or object counts as a target and lands in the last square of the line (or nearest unoccupied square of the goon’s choice).
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 9 damage
      <br />✸ 17+ 12 damage; [[prone]]"
ta:
  - name: "Swat The Fly"
    desc: "
      <br />**Keywords** — 
      <br />**Trigger** The target moves or shifts away from the goon.
      <br />**Distance** Melee 1
      <br />**Target** 1 adjacent creature or object 
      <br />**Effect:** Slide 5."
traits:
  - name: "Defiant Anger"
    desc: "The goon has damage immunity 2 while they are [[winded]]."

# OGRE JUGGERNAUT

name: "OGRE JUGGERNAUT"
level: 2
roles:
  - TROOP
  - HARRIER
ancestry:
  - Giant
  - Ogre
ev: 16
stamina: 80
speed: 6
size: 2 /
stability: 2
free_strike: 5
characteristics:
  - +2
  - +1
  - −1
  - 0
  - −1
actions:
  - name: "Pitchfork Catapult"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 10 damage; A< 1 vertical push 3
      <br />✸ 17+ 13 damage; A< 2 vertical slide 5
      <br />**1 Malice** Each target is M< 1 [[bleeding]] (save ends)."
  - name: "Earth Breaking Jump"
    desc:
      "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 3 burst
      <br />**Target** All creatures in the burst 
      <br />**Effect:** The juggernaut jumps up to 6 squares before using this ability.
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 6 damage; push 2; M< 1 [[prone]]
      <br />✸ 17+ 9 damage; push 4; M< 2 [[prone]]"
maneuvers:
  - name: "Horrible Bellow"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 3 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 I< 0 [[frightened]] (save ends)
      <br />★ 12–16 I< 1 [[frightened]] (save ends)
      <br />✸ 17+ I< 2 [[frightened]] (save ends) 
      <br />**Effect:** All ogres have an edge on strikes against creatures [[frightened]] by this ability."
ta:
  - name: "Hrraaaaaagh! (Free Triggered Action)"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** — 
      <br />**Trigger** The juggernaut takes damage.
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The juggernaut moves up to their speed and makes a free strike."
traits:
  - name: "Destructive Path"
    desc: "The juggernaut automatically destroys unattended, mundane size 1 objects in their path during their movement. They can break through any mundane wall made of wood, stone, or a similarly sturdy material in this way, so long as the wall is no more than 1 square thick."
  - name: "Defiant Anger"
    desc: "The juggernaut has damage immunity 2 while they are [[winded]]."

# OGRE BLUE BLOOD

name: "OGRE BLUE BLOOD"
level: 7
roles:
  - MINION
  - BRUTE
ancestry:
  - Giant
  - Ogre
ev: 9 for eight minions
stamina: 13
speed: 5
size: 2 /
stability: 4
with-captain: Edge on strikes
free_strike: 4
characteristics:
  - +4
  - +1
  - −1
  - 0
  - +2
actions:
  - name: "Crush Underfoot"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 7 damage; M< 3 [[prone]]
      <br />✸ 17+ 8 damage; [[prone]] 
      <br />**Effect:** An already [[prone]] target takes an additional 4 damage."
traits:
  - name: "In My Stead"
    desc: "Whenever the blue blood would make a free strike, an ally within 5 can make a free strike instead."
  - name: "Defiant Anger"
    desc: "The blue blood has damage immunity 2 while they are [[winded]]."

# OGRE TANTRUM

name: "OGRE TANTRUM"
level: 7
roles:
  - MINION
  - ARTILLERY
ancestry:
  - Giant
  - Ogre
ev: 9 for eight minions
stamina: 10
speed: 5
size: 2 /
stability: 2
with-captain: Ranged distance +5
free_strike: 4
characteristics:
  - +4
  - +2
  - −1
  - 0
  - −1
actions:
  - name: "Throw Fit"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 8
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 4 damage
      <br />★ 12–167 damage; push 2
      <br />✸ 17+ 8 damage; push 4 
      <br />**Effect:** The tantrum unearths a rock or a hunk of terrain and tosses it. The tantrum can A< 3 grab an adjacent size -1 or smaller creature or object to use as the projectile for this ability."
traits:
  - name: "Excessive Anger" 
    desc: "The tantrum has damage immunity 3 and a speed of 8 while they are [[winded]]."


# OLOTHEC

name: "OLOTHEC"
level: 6
roles:
  - SOLO
ancestry:
  - Horror
  - Olothec
ev: 80
stamina: 450
immunities: psychic 6
speed: 7 (fly, swim)
size: 2 /
stability: 0
free_strike: 7
characteristics:
  - +4
  - -1
  - +4
  - +2
  - +3
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The olothec takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the olothec can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the olothec can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Gelatinosis"
    desc: "A creature permanently devolves into a slime servant if they spend 1 continuous minute [[weakened]] by Devolving Tentacles, they are reduced to 0 or lower stamina by the psychic damage from Devolving Tentacles, or they suffer all three transformations from Oozing Transformation."
actions:
  - name: "Devolving Tentacles"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 damage; M< 2 [[weakened]] or slimed (save ends)
      <br />★ 12–16 17+ damage; M< 3 [[weakened]] or slimed (save ends)
      <br />✸ 17+ 20 damage; M< 4 [[weakened]] and slimed (save ends) 
      <br />**Effect:** A slimed target takes 4 psychic damage whenever they roll power until the condition ends."
  - name: "Slime Spew"
    desc:
      "
      <br />**Keywords** Area, Weapon
      <br />**Distance** 7 x 2 line within 1
      <br />**Target** All creatures and objects
      <br />`dice: 2d10 + 4`
      <br />✦ 17+ 6 acid damage; A< 2 push (special)
      <br />★ 12–16 10 acid damage; A< 3 push (special)
      <br />✸ ≤11 13 acid damage; A< 4 push (special), [[prone]] 
      <br />**Effect:** A creature pushed by this ability is pushed to the squares within the line that are furthest from the olothec. 
      <br />**1 Malice** The affected area becomes difficult terrain. A creature that enters an affected square for the first time during a turn is A< 3 knocked [[prone]]."
  - name: "Oozing Transformation"
    desc:
      "
      <br />**Keywords** Psionic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** One creature
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 13 psychic damage; I< 2 transformed (save ends)
      <br />★ 12–16 20 psychic damage; I< 3 transformed (save ends)
      <br />✸ 17+ 23 psychic damage; I< 4 transformed (save ends) 
      <br />**Effect:** Each time a creature is transformed, the Director chooses one of the following transformations. When a creature ends the transformed effect, all transformations end. 
      <br />**Head** 
      <br />- The creature’s head becomes a ball of slime. They cannot communicate and they can’t establish [[Draw Steel Rules#LINE OF EFFECT|line of effect]] beyond 3 squares. 
      <br />**Legs**
      <br />- The creature’s legs become pillars of ooze. They are [[slowed]] while on land and add the swim keyword to their speed.
      <br />**Torso**
      <br />- The creature’s arms become gelatinous. They can’t benefit from edges or surges."
maneuvers:
  - name: "Jaunt"
    desc: "
      <br />**Keywords** Psionic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The olothec teleports to an unoccupied square within 10 or swaps places with a creature or object within 5."
ta:
  - name: "Liquify"
    desc: "
      <br />**Keywords** Psionic, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** One enemy 
      <br />**Trigger**
      <br />**Target** deals damage to the olothec 
      <br />**Effect:** The target takes 8 psychic damage and gains psychic weakness 3 until the end of the olothec’s next turn."
traits:
  - name: "Primordial Mind"
    desc: "The olothec is immune to the [[frightened]] and [[taunted]] conditions."
  - name: "Slime Sense"
    desc: "A slimed or transformed creature can’t be hidden or concealed from the olothec."
va:
  - name: "Horrifying Form (Villain Action 1)"
  desc: "
      <br />**Keywords** Psionic, Ranged, Strike
      <br />**Distance** Special
      <br />**Target** All enemies
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 10 psychic damage; P< 2 [[frightened]] (save ends)
      <br />★ 12–16 14 psychic damage; P< 3 [[frightened]] (save ends)
      <br />✸ 17+ 17+ psychic damage; P< 4 [[frightened]] (save ends) 
      <br />**Effect:** This ability targets each enemy the olothec has [[Draw Steel Rules#LINE OF EFFECT|line of effect]] to. A [[frightened]] enemy can’t save against any other effect until they are no longer [[frightened]]."
  - name: "Psychic Pulse (Villain Action 2)"
    desc: "
      <br />**Keywords** Area, Psionic
      <br />**Distance** 10 burst
      <br />**Target** All creatures 
      <br />**Effect:** Each target takes 12 psychic damage, slides 5, and is M< 3 [[weakened]] and slimed (save ends) (see devolving tentacles). The olothec has damage immunity 4 until the start of their next turn."
  - name: "Return to Perfection (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Ranged, Psionic
      <br />**Distance** 10 burst
      <br />**Target** All creatures
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 7 psychic damage; R< 2 devolved (save ends)
      <br />★ 12–16 13 psychic damage; R< 3 devolved (save ends)
      <br />✸ 17+ 16 psychic damage; R< 4 devolved (save ends) 
      <br />**Effect:** A devolved creature has a -1 modifier  to all their characteristic scores other than Might until the condition ends."

# MOHLER

name: "MOHLER"
level: 1
roles:
  - MINION
  - AMBUSHER
ancestry:
  - Animal
  - Orc
ev: 3 for eight minions
stamina: 4
speed: 7 (burrow)
size: 1S /
stability: 1
with-captain:
speed: +2
free_strike: 2
characteristics:
  - 0
  - +2
  - −4
  - +1
  - −3
actions:
  - name: "Earth Bump"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage 
      <br />**Effect:** The target is knocked [[prone]] if the mohler is striking from 1 or more squares below."
traits:
  - name: "Ground Grinder"
    desc: "The ground within 1 square of where the mohler moves while burrowing becomes difficult terrain."

# ORC BLITZER

name: "ORC BLITZER"
level: 1
roles:
  - MINION
  - HARRIER
ancestry:
  - Humanoid
  - Orc
ev: 3 for eight minions
stamina: 4
speed: 7
size: 1M /
stability: 0
with-captain:
speed: +2
free_strike: 1
characteristics:
  - +1
  - +2
  - 0
  - 0
  - 0
actions:
  - name: "Lugged Spear"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage
      <br />★ 12–16 2 damage
      <br />✸ 17+ 3 damage 
      <br />**Effect:** The target takes 3 damage if they start their next turn adjacent to 3 or more blitzers."
traits:
  - name: "Bloodfire Burn"
    desc: "If the blitzer’s stamina drops to 0, they can make a free strike before dying."

# ORC BLOODSPARK

name: "ORC BLOODSPARK"
level: 1
roles:
  - MINION
  - ARTILLERY
ancestry:
  - Humanoid
  - Orc
ev: 3 for eight minions
stamina: 3
speed: 6
size: 1M /
stability: 0
with-captain: Forced movement +2
free_strike: 2
characteristics:
  - 0
  - +1
  - 0
  - 0
  - +2
actions:
  - name: "Explosive Mote"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage; push 1 or shift 1 away from target
      <br />★ 12–16 4 damage; push 2 or shift 2 away from target
      <br />✸ 17+ 5 damage; push 4 or shift 4 away from target"
traits:
  - name: "Bloodfire Burn"
    desc: "If the bloodspark’s stamina drops to 0, they can make a free strike before dying."

# ORC GLORIFIER

name: "ORC GLORIFIER"
level: 1
roles:
  - MINION
  - CONTROLLER
ancestry:
  - Humanoid
  - Orc
ev: 3 for eight minions
stamina: 3
speed: 6
size: 1M /
stability: 0
with-captain: Ranged distance +5
free_strike: 1
characteristics:
  - 0
  - +1
  - 0
  - 0
  - +2
actions:
  - name: "Call to Victory"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Ranged, Strike
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 sonic damage
      <br />★ 12–16 2 sonic damage; P< 1 [[slowed]] (save ends)
      <br />✸ 17+ 3 sonic damage; P< 2 [[slowed]] (save ends) 
      <br />**Effect:** Each ally has an edge on melee strikes against the target until the glorifier and all other glorifiers in their squad are killed." 
traits:
  - name: "Bloodfire Burn"
    desc: "If the glorifier’s stamina drops to 0, they can make a free strike before dying."

# ORC RAZOR

name: "ORC RAZOR"
level: 1
roles:
  - MINION
  - BRUTE
ancestry:
  - Humanoid
  - Orc
ev: 3 for eight minions
stamina: 5
speed: 6
size: 1L /
stability: 0
with-captain: Strike damage +1
free_strike: 2
characteristics:
  - +2
  - +1
  - 0
  - 0
  - 0
actions:
  - name: "Boot and Blade"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage; push 3
      <br />✸ 17+ 5 damage; push 3 or [[prone]] 
      <br />**Effect:** The razor has an edge on strikes against targets already affected by a condition."
traits:
  - name: "Bloodfire Burn"
    desc: "If the razor’s stamina drops to 0, they can make a free strike before dying."

# ORC BLOODRUNNER

name: "ORC BLOODRUNNER"
level: 3
roles:
  - PLATOON
  - HARRIER
ancestry:
  - Humanoid
  - Orc
ev: 10
stamina: 50
speed: 8
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - +2
  - +2
  - 0
  - +1
  - +1
actions:
  - name: "Shield Bash"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage (enemy only); push X
      <br />★ 12–16 10 damage (enemy only); push X
      <br />✸ 17+ 13 damage (enemy only); push X or [[prone]] 
      <br />**Effect:** Push X is equal to the number of squares the bloodrunner moved on their turn before using this ability. 
      <br /><**2 Malice** An ally pushed by this ability can make a free strike on a creature."
traits:
  - name: "Unimpeded"
    desc: "This bloodrunner can share a [[prone]] creature’s square. The first time a bloodrunner enters a creature’s square on their turn, that creature takes 3 damage."
  - name: "Relentless"
    desc: "If the bloodrunner’s stamina drops to 0, they can make a free strike before dying. If the target is reduced to 0 stamina or killed by the strike, the  loodrunner lives and their stamina is reduced to 1 instead."

# ORC CHAINLOCK

name: "ORC CHAINLOCK"
level: 1
roles:
  - PLATOON
  - HEXER
ancestry:
  - Humanoid
  - Orc
ev: 6
stamina: 20
speed: 5
size: 1L /
stability: 2
free_strike: 3
characteristics:
  - +2
  - +2
  - +1
  - 0
  - 0
actions:
  - name: "Hook and Chain"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; pull 1; M< 0 hooked (save ends)
      <br />★ 12–16 7 damage; pull 2; M< 1 hooked (save ends)
      <br />✸ 17+ 9 damage; pull 3; M< 2 hooked (save ends) 
      <br />**Effect:** A hooked target can’t move more than 3 squares away from the chainlock’s original position until the condition ends."
  - name: "Heavy Crossbolt"
    desc:
      "
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 5
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; A< 0 [[slowed]] (save ends)
      <br />★ 12–16 7 damage; A< 1 [[slowed]] (save ends)
      <br />✸ 17+ 9 damage; [[prone]]; A< 2 [[slowed]] (save ends)"
traits:
  - name: "Chain Link"
    desc: "Whenever the chainlock is force moved by a creature’s melee ability, the creature is pulled the same distance towards the chainlock."
  - name: "Relentless"
    desc: "If the chainlock’s stamina drops to 0, they can make a free strike before dying. If the target is reduced to 0 stamina or killed by the strike, the chainlock lives and their stamina is reduced to 1 instead."

# ORC EYE OF GROLE

name: "ORC EYE OF GROLE"
level: 1
roles:
  - PLATOON
  - ARTILLERY
ancestry:
  - Humanoid
  - Orc
ev: 6
stamina: 20
immunities: affinity 5
speed: 6
size: 1M /
stability: 0
free_strike: 4
characteristics:
  - +1
  - +1
  - 0
  - 0
  - +2
traits:
  - name: "Affinity"
    desc: "The eye has an affinity for one of the following damage types: cold, fire, or lightning. This type determines the eye’s affinity immunity and the damage type of their attacks."
actions:
  - name: "Elemental Discharge"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 affinity damage; push 2 or shift 2 away from target
      <br />★ 12–16 9 affinity damage; slide 4 or shift 4 away from target
      <br />✸ 17+ 12 affinity damage; slide 6 or shift 6 away from target"
  - name: "Power Burst"
    desc:
      "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 × 2 line within 1
      <br />**Target** All enemies in the line
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 affinity damage; push 2
      <br />★ 12–16 5 affinity damage; push 3
      <br />✸ 17+ 8 affinity damage; push 4; [[prone]] 
      <br />**Effect:** An enemy has affinity weakness 3 in the affected area."
traits: 
  - name: "Relentless" 
    desc: "If the eye’s stamina drops to 0, they can make a free strike before dying. If the target is reduced to 0 stamina: or killed by the strike, the eye lives and their stamina: is reduced to 1 instead."

# ORC GARROTER

name: "ORC GARROTER"
level: 1
roles:
  - PLATOON
  - AMBUSHER
ancestry:
  - Humanoid
  - Orc
ev: 6
stamina: 30
speed: 5
size: 1L /
stability: 0
free_strike: 4
characteristics:
  - +1
  - +2
  - 0
  - +1
  - −1
actions:
  - name: "Dagger Feint"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage; shift 1
      <br />★ 12–16 9 damage; shift 2
      <br />✸ 17+ 12 damage; shift 3 
      <br />**Effect:** This ability deals an additional 4 damage when it’s made with an edge."
  - name: "Strangle"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature
      <br />✸ ≤11 6 damage
      <br />★ 12–16 9 damage; I< 1 [[dazed]] (save ends)
      <br />`dice: 2d10 + 2`
      <br />✦ 17+ 12 damage; [[grabbed]]; I< 2 [[dazed]] (save ends) 
      <br />**Effect:** The target can’t speak or use magic abilities while [[grabbed]]."
maneuvers:
  - name: "Chroma Cloak"
    desc: "
      <br />**1 Malice** The garroter turns invisible. <br />The effect ends when the garroter uses an ability, takes damage, or at the end of their turn."
traits:
  - name: "Relentless"
    desc: "If the garroter’s stamina drops to 0, they can make a free strike before dying. If the target is reduced to 0 stamina or killed by the strike, the  garroter lives and their stamina is reduced to 1 instead."

# ORC GODCALLER

name: "ORC GODCALLER"
level: 1
roles:
  - PLATOON
  - SUPPORT
ancestry:
  - Humanoid
  - Orc
ev: 6
stamina: 30
speed: 6
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - +1
  - 0
  - 0
  - +1
  - +2
actions:
  - name: "Power Chord"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Ranged, Strike
      <br />**Distance** Melee 1 or Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 sonic damage
      <br />★ 12–16 7 sonic damage
      <br />✸ 17+ 9 sonic damage; P< 2 [[weakened]] (save ends)"
  - name: "Cadenza"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** 1 ally 
      <br />**Effect:** The target moves up to their speed and uses an action. 
      <br />**3 Malice** The godcaller targets a second ally."
maneuvers:
  - name: "Rallying Ostinato"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** Magic
      <br />**Distance** Self and Ranged 10
      <br />**Target** Self and up to 3 allies 
      <br />**Effect:** Each target regains 15 stamina and ignores difficult terrain until the end of the encounter." 
traits:
  - name: "Relentless"
    desc: "If the godcaller’s stamina drops to 0, they can make a free strike before dying. If the target is reduced to 0 stamina or killed by the strike, the  godcaller lives and their stamina is reduced to 1 instead."

# ORC JUGGERNAUT

name: "ORC JUGGERNAUT"
level: 3
roles:
  - PLATOON
  - BRUTE
ancestry:
  - Humanoid
  - Orc
ev: 10
stamina: 60
speed: 6
size: 1L /
stability: 0
free_strike: 5
characteristics:
  - +2
  - +2
  - −1
  - −1
  - +2
actions:
  - name: "Haymaker Greataxe"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 11 damage; [[prone]]
      <br />✸ 17+ 14 damage; [[prone]]; M< 2 [[bleeding]] (save ends) 
      <br />**Effect:** This ability deals an additional 6 damage against already [[prone]] targets."
ta:
  - name: "Hrraaaaaagh! (Free Triggered Action)"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** — 
      <br />**Trigger** The juggernaut takes damage.
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The juggernaut moves up to their speed and makes a free strike."
traits:
  - name: "Blood in the Water"
    desc: "The juggernaut can move 3 additional squares if they end their movement closer to a [[prone]] creature."
  - name: "Relentless"
    desc: "If the juggernaut’s stamina drops to 0, they can take a free strike before dying. If the target is reduced to 0 stamina or killed by the strike, the juggernaut lives and their stamina is reduced to 1 instead."

# ORC RAMPART

name: "ORC RAMPART"
level: 2
roles:
  - PLATOON
  - DEFENDER
ancestry:
  - Humanoid
  - Orc
ev: 8
stamina: 59
speed: 6
size: 1L /
stability: 2
free_strike: 4
characteristics:
  - +2
  - +2
  - +2
  - +2
  - +2
actions:
  - name: "My Spear, My Foe"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 9 damage; [[taunted]] (EoT)
      <br />✸ 17+ 12 damage; [[taunted]] (EoT) 
      <br />**Effect:** This ability has a double edge if the target dealt damage to the rampart this round."
maneuvers:
  - name: "Castling"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** 1 ally 
      <br />**Effect:** The rampart moves or shifts up to their speed to a square adjacent to the target and then swaps places with the target."
ta:
  - name: "No."
    desc: "
      <br />**Keywords** — 
      <br />**Trigger** A creature targets an adjacent ally with an ability.
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The rampart becomes the new target."
traits:
  - name: "Relentless
    desc: "If the rampart’s stamina drops to 0, they can make a free strike before dying. If the target is reduced to 0 stamina or killed by the strike, the rampart lives and their stamina is reduced to 1 instead."

# ORC TERRANOVA

name: "ORC TERRANOVA"
level: 2
roles:
  - PLATOON
  - CONTROLLER
ancestry:
  - Humanoid
  - Orc
ev: 8
stamina: 30
speed: 6 (burrow)
size: 1M /
stability: 2
free_strike: 4
characteristics:
  - +1
  - +1
  - 0
  - +1
  - +2
actions:
  - name: "Earth Pillar"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** 3 creatures touching the ground
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage; A< 0 [[prone]] can’t stand (save ends)
      <br />★ 12–16 9 damage; A< 1 [[prone]] can’t stand (save ends)
      <br />✸ 17+ 12 damage; [[prone]] A< 2 and can’t stand (save ends) 
      <br />**Effect:** The ground beneath each target rises 1 square."
  - name: "Sinkhole"
    desc:
      "
      <br />**Keywords** Melee, Weapon
      <br />**Distance** 3 Burst
      <br />**Target** All enemies
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage; M< 0 [[restrained]] (save ends)
      <br />★ 12–16 7 damage; M< 1 [[restrained]] (save ends)
      <br />✸ 17+ 10 damage; M< 2 [[restrained]] (save ends) 
      <br />**Effect:** The affected area is considered difficult terrain."
traits:
  - name: "Seismic Step"
    desc: "The terranova ignores difficult terrain. The terranova doesn’t need [[Draw Steel Rules#LINE OF EFFECT|line of effect]] to target creatures touching the ground with abilities."
  - name: "Relentless"
    desc: "If the terranova’s stamina drops to 0, they can take a free strike before dying. If the target is reduced to 0 stamina or killed by the strike, the terranova lives and their stamina is reduced to 1 instead."

# ORC WARLEADER

name: "ORC WARLEADER"
level: 3
roles:
  - LEADER
ancestry:
  - Humanoid
  - Orc
ev: 20
stamina: 120
speed: 6
size: 1M /
stability: 2
free_strike: 5
characteristics:
  - +3
  - +2
  - +1
  - +2
  - +2
actions:
  - name: "Go."
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** 1 ally 
      <br />**Effect:** The target moves up to their speed and uses an action. 
      <br />**1 Malice** The warleader targets a second ally. 
      <br />**3 Malice** The warleader targets a squad instead of a second ally."
  - name: "Mace Lariat"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** All enemies
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 damage; push 1; M< 1 [[dazed]] (save ends)
      <br />★ 12–16 10 damage; push 3; M< 2 [[dazed]] (save ends)
      <br />✸ 17+ 13 damage; push 5; M< 3 [[dazed]] (save ends)"
maneuvers:
  - name: "Lockdown"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** 3 allies 
      <br />**Effect:** Each target moves up to their speed and uses the Grab maneuver with an edge. The warleader moves up to their speed."
ta:
  - name: "Courtesy Call"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature 
      <br />**Trigger** The target gets a tier 1 result on a power roll. 
      <br />**Effect:** The target has a double edge on next power roll."
va:
  - name: "Close In (Villain Action 1)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 10 Burst
      <br />**Target** All allies 
      <br />**Effect:** Each target moves up to their speed. Each enemy within 1 of a target makes a Might test.
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 [[frightened]] of the warleader (save ends)
      <br />★ 12–16 [[frightened]] of the warleader (EoT)
      <br />✦ 17+ no effect"
  - name: "Familial Reinforcements (Villain Action 2)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** Ranged 10
      <br />**Target** All allies 
      <br />**Effect:** The warleader shifts up to their speed and 5 orc blitzers appear in unoccupied spaces within distance."
  - name: "I’ll Do This Myself (Villain Action 3)"
    desc: "
      <br />**Keywords** Attack, Melee, Weapon
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The warleader shifts up to their speed and uses Mace Lariat. Then, the warleader shifts up to their speed and uses Mace Lariat. Finally, the warleader shifts up to their speed and uses Mace Lariat."
traits:
  - name: "End Effect"
    desc: "At the end of their turn, the warleader can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Relentless"
    desc: "If the warleader’s stamina drops to 0, they can take a free strike before dying. If the target is reduced to 0 stamina or killed by the strike, the dohma lives and their stamina is reduced to 1 instead."

# SCYZA

name: "SCYZA"
level: 3
roles:
  - TROOP
  - MOUNT
ancestry:
  - Animal
  - Orc
ev: 20
stamina: 100
speed: 6
size: 4 /
stability: 3
free_strike: 5
characteristics:
  - +2
  - −1
  - −4
  - 0
  - −1
actions:
  - name: "Clawed Kick"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 11 damage; [[prone]]
      <br />✸ 17+ 14 damage; [[prone]] 
      <br />**Effect:** The scyza roars and the target is I< 2 [[frightened]] (save ends)."
  - name: "Whiptail"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 damage
      <br />★ 12–16 13 damage
      <br />✸ 17+ 16 damage; A< 2 [[bleeding]] (save ends) 
      <br />**Effect:** This ability has an edge against a target on top of the scyza and knocks the target [[prone]] into an unoccupied adjacent square."
  - name: "Crestfall"
    desc:
      "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 3 cube within 2
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage; 1 sonic damage; R< 0 [[dazed]] (save ends)
      <br />★ 12–16 7 damage; 2 sonic damage; R< 1 [[dazed]] (save ends)
      <br />✸ 17+ 9 damage; 3 sonic damage; R< 2 [[dazed]] (save ends)"
maneuvers:
  - name: "Sandstorm"
    desc: "
      <br />**Keywords** —
      <br />**Distance** 3 burst
      <br />**Target** Special 
      <br />**Effect:** The scyza kicks up a sandstorm concealing themselves and each ally in the affected area until the end of the scyza’s next turn. Each enemy in the burst makes a Might test.
      <br />`dice: 2d10 + 2`
      <br />✸ ≤11 10 damage; [[prone]]; [[slowed]] (EoT)
      <br />★ 12–16 7 damage; [[slowed]] (EoT)
      <br />✦ 17+ 4 damage" 
ta:
  - name: "Brace and Bogart"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The scyza or an ally riding the scyza is targeted by an ability. 
      <br />**Effect:** Any damage dealt by the triggering ability is halved. If the creature or object who used the ability is within 3 of the scyza, the scyza makes a free strike against them."
traits:
  - name: "War Harness"
    desc: "Three of the scyza’s size 1 allies can occupy the same space while riding the scyza."
  - name: "Terrible Beast" 
    desc: "The scyza deals an additional 6 damage on strikes and abilities used against objects."


# RADENWIGHT MISCHIEVER

name: "RADENWIGHT MISCHIEVER"
level: 1
roles:
  - MINION
  - AMBUSHER
ancestry:
  - Humanoid
  - Radenwight
ev: 3 for eight minions
stamina: 4
speed: 7 (climb)
size: 1S /
stability: 0
with-captain: Strike damage +1
free_strike: 2
characteristics:
  - −1
  - +2
  - +0
  - +1
  - +0
actions:
  - name: "Dagger Dance"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** One creature per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage 
      <br />**Effect:** If the mischiever is hidden when they use this ability, they can target two creatures.
ta:
  - name: "Ready Rodent"
    desc: "
      <br />**Keywords** Melee, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature 
      <br />**Trigger** An ally deals damage to the target. 
      <br />**Effect:** The mischiever makes a free strike against the target."

# RADENWIGHT SCRAPPER

name: "RADENWIGHT SCRAPPER"
level: 1
roles:
  - MINION
  - DEFENDER
ancestry:
  - Humanoid
  - Radenwight
ev: 3 for eight minions
stamina: 5
speed: 6 (climb)
size: 1S /
stability: 1
with-captain: Melee distance +2
free_strike: 1
characteristics:
  - −1
  - +1
  - +0
  - +0
  - +2
actions:
  - name: "Buckler Bash"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage
      <br />★ 12–16 2 damage; [[taunted]] (EoT)
      <br />✸ 17+ 3 damage; [[taunted]] (EoT)"
ta:
  - name: "Ready Rodent"
    desc: "
      <br />**Keywords** Melee, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature 
      <br />**Trigger** An ally deals damage to the target. 
      <br />**Effect:** The scrapper makes a free strike against the target."

# RADENWIGHT SWIFTPAW

name: "RADENWIGHT SWIFTPAW"
level: 1
roles:
  - MINION
  - HARRIER
ancestry:
  - Humanoid
  - Radenwight
ev: 3 for eight minions
stamina: 4
speed: 7 (climb)
size: 1S /
stability: 0
with-captain: Edge on strikes
free_strike: 1
characteristics:
  - +0
  - +2
  - +1
  - +0
  - −1
actions:
  - name: "Rapier Flunge"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage; slide 1; shift 1
      <br />★ 12–16 2 damage; slide 2; shift 2
      <br />✸ 17+ 3 damage; slide 3; shift 3"
ta:
  - name: "Ready Rodent"
    desc: "
      <br />**Keywords** Melee, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature 
      <br />**Trigger** An ally deals damage to the target. 
      <br />**Effect:** The swiftpaw makes a free strike against the target."

# RADENWIGHT REDEYE

name: "RADENWIGHT REDEYE"
level: 1
roles:
  - MINION
  - ARTILLERY
ancestry:
  - Humanoid
  - Radenwight
ev: 3 for eight minions
stamina: 3
speed: 5 (climb)
size: 1S /
stability: 0
with-captain: Edge on strikes
free_strike: 2
characteristics:
  - +1
  - +2
  - −1
  - +0
  - +0
actions:
  - name: "Eyes-On-Me Shot"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage 
      <br />**Effect:** An ally of the redeye within 2 squares of the target can shift up to 2 squares."
ta:
  - name: "Ready Rodent"
    desc: "
      <br />**Keywords** Melee, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature 
      <br />**Trigger** An ally deals damage to the target. 
      <br />**Effect:** The redeye makes a free strike against the target."

# RADENWIGHT BRUXER

name: "RADENWIGHT BRUXER"
level: 1
roles:
  - PLATOON
  - BRUTE
ancestry:
  - Humanoid
  - Radenwight
ev: 6
stamina: 40
speed: 5 (climb)
size: 1L /
stability: 2
free_strike: 4
characteristics:
  - +2
  - +1
  - −1
  - +0
  - +0
actions:
  - name: "Lockjaw"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 9 damage
      <br />✸ 17+ 12 damage; [[grabbed]] 
      <br />**Effect:** While the target is [[grabbed]], they take 2 damage at the start of each of the bruxer’s turns."
  - name: "Flurry of Bites"
    desc:
      "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 1 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage; A< 0 [[bleeding]] (save ends)
      <br />★ 12–16 5 damage; A< 1 [[bleeding]] (save ends)
      <br />✸ 17+ 8 damage; A< 2 [[bleeding]] (save ends)"
ta:
  - name: "Ready Rodent"
    desc: "
      <br />**Keywords** Melee, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature 
      <br />**Trigger** An ally deals damage to the target. 
      <br />**Effect:** The bruxer makes a free strike against the target."
traits:
  - name: "Lockdown"
    desc: "An enemy can’t shift while adjacent to the bruxer."

# RADENWIGHT PIPER

name: "RADENWIGHT PIPER"
level: 1
roles:
  - PLATOON
  - SUPPORT
ancestry:
  - Humanoid
  - Radenwight
ev: 6
stamina: 30
speed: 5 (climb)
size: 1S /
stability: 0
free_strike: 3
characteristics:
  - +0
  - +0
  - +0
  - +2
  - +1
actions:
  - name: "Piercing Trill"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Ranged, Strike
      <br />**Distance** Melee 1 or Ranged 10
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 sonic damage; push 1
      <br />★ 12–16 7 sonic damage; push 3
      <br />✸ 17+ 9 sonic damage; push 4 
      <br />**Effect:** The piper or an ally within distance regains stamina equal to half the damage dealt."
maneuvers:
  - name: "Vivace Vivace!"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 burst
      <br />**Target** Each ally in the burst 
      <br />**Effect:** Each target who has used their Ready Rodent ability since their last turn regains the use of their triggered action.
      <br />**2 Malice** The area increases to 6 burst."
ta:
  - name: "Ready Rodent"
    desc: "
      <br />**Keywords** Melee, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature 
      <br />**Trigger** An ally deals damage to the target. 
      <br />**Effect:** The piper makes a free strike against the target."
traits:
  - name: "Musical Suggestion"
    desc: "At the end of the piper’s turn, they can choose an adjacent creature and slide them 2, ignoring stability."

# RADENWIGHT RATCROBAT

name: "RADENWIGHT RATCROBAT"
level: 1
roles:
  - PLATOON
  - HARRIER
ancestry:
  - Humanoid
  - Radenwight
ev: 6
stamina: 30
speed: 7 (climb)
size: 1S /
stability: 0
free_strike: 3
characteristics:
  - −1
  - +2
  - +0
  - +0
  - +1
actions:
  - name: "En Garde!"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 6 damage
      <br />✸ 17+ 8 damage 
      <br />**Effect:** The ratcrobat can shift up to 2 squares after striking the first target, then can shift 1 square after striking the second target."
maneuvers:
  - name: "Over Here, Thanks"
    desc: "
      <br />**Keywords** Melee
      <br />**Distance** Melee 1
      <br />**Target** One enemy 
      <br />**Effect:** Slide 3; the ratcrobat can then shift into any of the squares the target left."
ta:
  - name: "Ready Rodent"
    desc: "
      <br />**Keywords** Melee, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature 
      <br />**Trigger** An ally deals damage to the target. 
      <br />**Effect:** The ratcrobat makes a free strike against the target."
traits:
  - name: "Gymratstics"
    desc: "The ratcrobat has an edge on strikes against larger creatures."

# RADENWIGHT MAESTRO

name: "RADENWIGHT MAESTRO"
level: 1
roles:
  - LEADER
ancestry:
  - Humanoid
  - Radenwight
ev: 12
stamina: 80
speed: 5 (climb)
size: 1S /
stability: 1
free_strike: 4
characteristics:
  - −2
  - +2
  - +0
  - +0
  - +3
actions:
  - name: "Cacophony"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 sonic damage; slide 1; shift 1
      <br />★ 12–16 6 sonic damage; slide 3; shift 3
      <br />✸ 17+ 8 sonic damage; slide 5; shift 5 
      <br />**Effect:** Each ally within distance can use Ready Rodent as a free triggered action once before the end of the round."
maneuvers:
  - name: "Tempo Change"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** Two enemies
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 P< 1 [[slowed]] (save ends)
      <br />★ 12–16 P< 2 [[slowed]] (save ends)
      <br />✸ 17+ P< 3 [[slowed]] (save ends) 
      <br />**3 Malice** Each ally within 3 of a target has their speed increased by 2 until the end of their next turn."
ta:
  - name: "Ever Ready Rodent (Free Triggered Action)"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** Magic, Melee, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** One creature 
      <br />**Trigger** The target deals damage to an ally or takes damage from an ally. 
      <br />**Effect:** The maestro makes a free strike against the target.
traits:
  - name: "End Effect"
    desc: "At the end of their turn, the maestro can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Overture (Villain Action 1)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 10 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Each target shifts up to their speed or takes the Defend action."
  - name: "Solo Act (Villain Action 2)"
    desc: "
      <br />**Keywords** Ranged
      <br />**Distance** Ranged 15
      <br />**Target** One creature 
      <br />**Effect:** Until the end of their next turn, the target halves incoming damage, deals an additional 4 damage on strikes, and their speed is doubled."
  - name: "Rondo of Rat (Villain Action 3)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 10 burst
      <br />**Target** All dead allies in the burst 
      <br />**Effect:** Each target stands, makes a free strike, then collapses again. Allies of the targets can use Ready Rodent as a free triggered action once in conjunction with these free strikes."

# RIVAL CONDUIT

name: "RIVAL CONDUIT"
level: 2
roles:
  - TROOP
  - SUPPORT
ancestry:
  - Humanoid
  - Rival
ev: 16
stamina: 80
speed: 5
size: 1M /
stability: 1
free_strike: 5
characteristics:
  - +1
  - +0
  - +0
  - +2
  - +0
actions:
  - name: "Thunder of Heavens"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Ranged, Strike
      <br />**Distance** Melee 1 or Ranged 10
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 holy damage
      <br />★ 12–16 10 holy damage
      <br />✸ 17+ 13 holy damage 
      <br />**Effect:** The conduit or an ally within distance regains stamina equal to half the damage dealt."
maneuvers:
  - name: "Imbue with Might"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** Magic
      <br />**Distance** Ranged 10
      <br />**Target** Self and up to 5 allies 
      <br />**Effect:** Each target has an edge on their next strike."
traits:
  - name: "Stalwart Guardian"
    desc: "Strikes made against allies adjacent to the conduit have a bane."
  - name: "Rivalry"
    desc: "- The conduit selects one creature within [[Draw Steel Rules#LINE OF EFFECT|line of effect]] at the start of an encounter. Both the conduit and the creature can add a 1d3 to all power rolls made against each other."

# RIVAL ELEMENTALIST

name: "RIVAL ELEMENTALIST"
level: 2
roles:
  - TROOP
  - CONTROLLER
ancestry:
  - Humanoid
  - Rival
ev: 16
stamina: 60
speed: 5
size: 1M /
stability: 1
free_strike: 5
characteristics:
  - +0
  - +0
  - +2
  - +1
  - +0
actions:
  - name: "The Writhing Green"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Green, Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; slide 1
      <br />★ 12–16 10 damage; slide 2
      <br />✸ 17+ 13 damage; slide 3"
  - name: "The Earth Devours"
    desc:
      "
      <br />**Keywords** Area, Green, Magic
      <br />**Distance** 3 cube within 10
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 5 damage; [[restrained]] (EoT)
      <br />✸ 17+ 8 damage; [[restrained]] (save ends) 
      <br />**Effect:** The affected area is difficult terrain for enemies. An enemy has acid weakness 2 while occupying an affected square.
ta:
  - name: "Jaws of the Void"
    desc: "
      <br />**Keywords** Magic, Void
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The elementalist takes damage. 
      <br />**Effect:** The elementalist teleports 2 squares. Each creature adjacent to their original space takes 2 corruption damage."
traits:
  - name: "Rivalry"
    desc: "- The elementalist selects one creature within [[Draw Steel Rules#LINE OF EFFECT|line of effect]] at the start of an encounter. Both the elementalist and the creature can add a 1d3 to all power rolls made against each other."

# RIVAL FURY

name: "RIVAL FURY"
level: 2
roles:
  - TROOP
  - BRUTE
ancestry:
  - Humanoid
  - Rival
ev: 16
stamina: 100
speed: 5
size: 1M /
stability: 3
free_strike: 5
characteristics:
  - +2
  - +1
  - +0
  - +0
  - +0
actions:
  - name: "Brutal Impact"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; push 1
      <br />★ 12–16 11 damage; push 2
      <br />✸ 17+ 14 damage; push 3 
      <br />**2 Malice** Each target is M< 1 [[slowed]] (save ends)."
  - name: "Let’s Tussle"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature the fury’s size or smaller
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 damage; M< 0 [[grabbed]]
      <br />★ 12–16 13 damage; M< 1 [[grabbed]]
      <br />✸ 17+ 16 damage; M< 2 [[grabbed]] 
      <br />**Effect:** The fury has an edge on strikes against a [[grabbed]] creature."
traits:
  - name: "Overwhelm"
    desc: "- Once per turn, when the fury force moves a target or shifts into a square adjacent to a creature or object, they can make a free strike against them."
  - name: "Rivalry"
    desc: "- The fury selects one creature within [[Draw Steel Rules#LINE OF EFFECT|line of effect]] at the start of an encounter. Both the fury and the creature can add a 1d3 to all power rolls made against each other."

# RIVAL NULL

name: "RIVAL NULL"
level: 2
roles:
  - TROOP
  - HARRIER
ancestry:
  - Humanoid
  - Rival
ev: 16
stamina: 80
speed: 7
size: 1M /
stability: 3
free_strike: 5
characteristics:
  - +0
  - +2
  - +1
  - +0
  - +0
actions:
  - name: "Nimble Step"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; shift 2
      <br />★ 12–16 10 damage; shift 3
      <br />✸ 17+ 13 damage; shift 4"
maneuvers:
  - name: "Numb"
    desc: "
      <br />**Keywords** Melee, Psionic, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; R< 0 [[slowed]] (EoT)
      <br />★ 12–16 10 damage; R< 1 [[slowed]] (EoT)
      <br />✸ 17+ 13 damage; R< 2 [[slowed]] and [[dazed]] (EoT)"
traits:
  - name: "Inertial Shield"
    desc: "- The null halves the damage of the first strike they are targeted by each round. "
  - name: "Rivalry"
    desc: "- The null selects one creature within [[Draw Steel Rules#LINE OF EFFECT|line of effect]] at the start of an encounter. Both the null and the creature can add a 1d3 to all power rolls made against each other."

# RIVAL SHADOW

name: "RIVAL SHADOW"
level: 2
roles:
  - TROOP
  - AMBUSHER
ancestry:
  - Humanoid
  - Rival
ev: 16
stamina: 80
speed: 7
size: 1M /
stability: 1
free_strike: 5
characteristics:
  - +0
  - +2
  - +0
  - +0
  - +1
actions:
  - name: "Swift Serration"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 11 damage
      <br />✸ 17+ 14 damage; A< 2 [[bleeding]] (save ends) 
      <br />**1 Malice** The shadow teleports up to 5 squares and hides."
maneuvers:
  - name: "Coat the Blade"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The shadow coats their weapon with poison. They have an edge on their next strike, and the potency increases by 1."
traits:
  - name: "Exploit Opening"
    desc: "- The shadow deals an extra 5 damage to [[bleeding]] targets."
  - name: "Rivalry"
    desc: "- The shadow selects one creature within [[Draw Steel Rules#LINE OF EFFECT|line of effect]] at the start of an encounter. Both the shadow and the creature can add a 1d3 to all power rolls made against each other."

# RIVAL TACTICIAN

name: "RIVAL TACTICIAN"
level: 2
roles:
  - TROOP
  - ARTILLERY
ancestry:
  - Humanoid
  - Rival
ev: 16
stamina: 60
speed: 5
size: 1M /
stability: 2
free_strike: 5
characteristics:
  - +2
  - +0
  - +1
  - +0
  - +0
actions:
  - name: "Dual Targeting Shot"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 11 damage
      <br />✸ 17+ 14 damage 
      <br />**2 Malice** Two allies within distance can make a free strike against one of the targets."
  - name: "I’ll Cover You!"
    desc:
      "
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 5
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 damage; M< 0 [[weakened]] (save ends)
      <br />★ 12–16 13 damage; M< 1 [[weakened]] (save ends)
      <br />✸ 17+ 16 damage; M< 2 [[weakened]] (save ends) 
      <br />**Effect:** An ally adjacent to the target regains 5 stamina."
ta:
  - name: "Overwatch"
      <br />**Keywords** Ranged
      <br />**Distance** Ranged 10
      <br />**Target** 1 enemy 
      <br />**Trigger** The target moves. 
      <br />**Effect:** At any point during the movement, the tactician makes a free strike against the target."
traits:
  - name: "Rivalry"
    desc: "- The tactician selects one creature within [[Draw Steel Rules#LINE OF EFFECT|line of effect]] at the start of an encounter. Both the tactician and the creature can add a 1d3 to all power rolls made against each other."

# RIVAL TALENT

name: "RIVAL TALENT"
level: 2
roles:
  - TROOP
  - HEXER
ancestry:
  - Humanoid
  - Rival
ev: 16
stamina: 60
speed: 5
size: 1M /
stability: 2
free_strike: 5
characteristics:
  - +0
  - +0
  - +2
  - +0
  - +1
actions:
  - name: "Reverberating Blast"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Psionic, Ranged, Strike, Telekinesis
      <br />**Distance** Ranged 10
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 psychic damage; M< 0 [[prone]]
      <br />★ 12–16 10 psychic damage; push 2; M< 1 [[prone]]
      <br />✸ 17+ 13 psychic damage; push 3; M< 2 [[prone]]"
maneuvers:
  - name: "Muddle the Mind"
      <br />**Keywords** Psionic, Ranged, Telepathy
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 R< 0 [[slowed]] (save ends)
      <br />★ 12–16 R< 1 [[dazed]] (save ends)
      <br />✸ 17+ R< 2 [[slowed]] and [[dazed]] (save ends)"
ta:
  - name: "Precognitive Shift"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** A creature deals damage to the talent. 
      <br />**Effect:** The talent halves the damage and shifts 2."
traits:
  - name: "Rivalry"
    desc: "- The talent selects one creature within [[Draw Steel Rules#LINE OF EFFECT|line of effect]] at the start of an encounter. Both the talent and the creature can add a 1d3 to all power rolls made against each other."

# RIVAL CONDUIT

name: "RIVAL CONDUIT"
level: 5
roles:
  - TROOP
  - SUPPORT
ancestry:
  - Humanoid
  - Rival
ev: 28
stamina: 140
speed: 5
size: 1M /
stability: 1
free_strike: 6
characteristics:
  - +2
  - +0
  - +0
  - +3
  - +1
actions:
  - name: "Raging Tempest"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Ranged, Strike
      <br />**Distance** Melee 1 or Ranged 10
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 holy damage; vertical slide 1
      <br />★ 12–16 14 holy damage; vertical slide 2
      <br />✸ 17+ 17+ holy damage; vertical slide 3 
      <br />**Effect:** The conduit or an ally within distance regains stamina equal to half the damage dealt."
maneuvers:
  - name: "Imbue with Power"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** Magic
      <br />**Distance** Ranged 10
      <br />**Target** Self and up to 5 allies 
      <br />**Effect:** Each target has a double edge on their next strike."
traits:
  - name: "Stalwart Guardian"
    desc: "Strikes made against allies adjacent to the conduit have a bane. "
  - name: "Rivalry"
    desc: "- The conduit selects one creature within [[Draw Steel Rules#LINE OF EFFECT|line of effect]] at the start of an encounter. Both the conduit and the creature can add a 1d3 to all power rolls made against each other."

# RIVAL ELEMENTALIST

name: "RIVAL ELEMENTALIST"
level: 5
roles:
  - TROOP
  - CONTROLLER
ancestry:
  - Humanoid
  - Rival
ev: 28
stamina: 120
speed: 5
size: 1M /
stability: 1
free_strike: 6
characteristics:
  - +0
  - +1
  - +3
  - +2
  - +0
actions:
  - name: "The Thriving Wilds"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Green, Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** Two creatures or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage; slide 1; M< 1 3 acid damage
      <br />★ 12–16 14 damage; slide 2; M< 2 5 acid damage
      <br />✸ 17+ 17+ damage; slide 3; M< 3 7 acid damage"
  - name: "The Depths Hunger"
    desc:
      "
      <br />**Keywords** Area, Green, Magic
      <br />**Distance** 4 cube within 10
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 9 damage; [[restrained]] (EoT)
      <br />✸ 17+ 11 damage; [[restrained]] (save ends) 
      <br />**Effect:** The affected area is difficult terrain for enemies. An enemy has acid weakness 3 while occupying an affected square."
ta:
  - name: "Fissures of Darkness"
    desc: "
      <br />**Keywords** Magic, Void
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The elementalist takes damage. 
      <br />**Effect:** The elementalist teleports 3 squares. Each creature adjacent to their original space takes 3 corruption damage."
traits:
  - name: "Rivalry"
    desc: "- The elementalist selects one creature within [[Draw Steel Rules#LINE OF EFFECT|line of effect]] at the start of an encounter. Both the elementalist and the creature can add a 1d3 to all power rolls made against each other."

# RIVAL FURY

name: "RIVAL FURY"
level: 5
roles:
  - TROOP
  - BRUTE
ancestry:
  - Humanoid
  - Rival
ev: 28
stamina: 160
speed: 5
size: 1M /
stability: 3
free_strike: 7
characteristics:
  - +3
  - +2
  - +0
  - +0
  - +1
actions:
  - name: "Thunderous Slam"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 damage; push 2
      <br />★ 12–16 15 damage; push 3
      <br />✸ 17+ 18 damage; push 4 2 Malice Each target is M< 2 [[slowed]] (save ends)."
  - name: "Roughed Up"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature the fury’s size or smaller
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 11 damage; M< 1 [[grabbed]]
      <br />★ 12–16 16 damage; M< 2 [[grabbed]]
      <br />✸ 17+ 21 damage; M< 3 [[grabbed]] 
      <br />**Effect:** The fury and each ally have an edge on strikes against a creature [[grabbed]] by this ability."
traits:
  - name: "Overpower"
    desc: "- Once per turn, when the fury force moves a target or shifts into a square adjacent to a creature or object, they can use a signature action against them."
  - name: "Rivalry"
    desc: "- The fury selects one creature within [[Draw Steel Rules#LINE OF EFFECT|line of effect]] at the start of an encounter. Both the fury and the creature can add a 1d3 to all power rolls made against each other."

# RIVAL NULL

name: "RIVAL NULL"
level: 5
roles:
  - TROOP
  - HARRIER
ancestry:
  - Humanoid
  - Rival
ev: 28
stamina: 140
speed: 7
size: 1M /
stability: 3
free_strike: 6
characteristics:
  - +0
  - +3
  - +2
  - +1
  - +0
actions:
  - name: "Agile Stride"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage; shift 3; A< 1 6 damage
      <br />★ 12–16 14 damage; shift 4; A< 2 11 damage
      <br />✸ 17+ 17+ damage; shift 5; A< 3 11 damage"
maneuvers:
  - name: "Deaden"
      <br />**Keywords** Melee, Psionic, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage; R< 1 [[dazed]] (EoT)
      <br />★ 12–16 14 damage; R< 2 [[dazed]] (save ends)
      <br />✸ 17+ 17+ damage; R< 3 [[dazed]] and [[restrained]] (save ends)"
traits:
  - name: "Inertial Shield"
    desc: "- The null halves the damage of the first strike they are targeted by each round."
  - name: "Rivalry"
    desc: "- The null selects one creature within [[Draw Steel Rules#LINE OF EFFECT|line of effect]] at the start of an encounter. Both the null and the creature can add a 1d3 to all power rolls made against each other."

# RIVAL SHADOW

name: "RIVAL SHADOW"
level: 5
roles:
  - TROOP
  - AMBUSHER
ancestry:
  - Humanoid
  - Rival
ev: 28
stamina: 140
speed: 7
size: 1M /
stability: 1
free_strike: 7
characteristics:
  - +0
  - +3
  - +1
  - +0
  - +2
actions:
  - name: "Ambuscade"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 damage
      <br />★ 12–16 15 damage; A< 2 [[bleeding]] (save ends)
      <br />✸ 17+ 18 damage; A< 3 [[bleeding]] (save ends) 
      <br />**1 Malice** The shadow teleports up to 6 squares and hides."
maneuvers:
  - name: "Coat the Blade"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The shadow coats their weapon with poison. They have an edge on their next strike, and the potency increases by 1."
traits:
  - name: "Exploit Opening"
    desc: "- The shadow deals an extra 7 damage to [[bleeding]] targets."
  - name: "Rivalry"
    desc: "- The shadow selects one creature within [[Draw Steel Rules#LINE OF EFFECT|line of effect]] at the start of an encounter. Both the shadow and the creature can add a 1d3 to all power rolls made against each other."

# RIVAL TACTICIAN

name: "RIVAL TACTICIAN"
level: 5
roles:
  - TROOP
  - ARTILLERY
ancestry:
  - Humanoid
  - Rival
ev: 28
stamina: 120
speed: 5
size: 1M /
stability: 2
free_strike: 7
characteristics:
  - +3
  - +0
  - +2
  - +0
  - +1
actions:
  - name: "Mark Targets"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 damage
      <br />★ 12–16 15 damage
      <br />✸ 17+ 18 damage 3 Malice Two allies within distance can use a signature action against one of the targets."
  - name: "Preserve and Protect"
    desc:
      "
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 5
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 11 damage; M< 1 [[weakened]] (save ends)
      <br />★ 12–16 16 damage; M< 2 [[weakened]] (save ends)
      <br />✸ 17+ 21 damage; M< 3 [[weakened]] (save ends) 
      <br />**Effect:** An ally adjacent to the target regains 7 stamina."
ta:
  - name: "Take the Opening"
    desc: "
      <br />**Keywords** Ranged
      <br />**Distance** Ranged 10
      <br />**Target** 1 enemy 
      <br />**Trigger** The target moves. 
      <br />**Effect:** At any point during the movement, the tactician and one ally within distance make a free strike against the target."
traits:
  - name: "Rivalry The tactician selects one creature within [[Draw Steel Rules#LINE OF EFFECT|line of effect]] at the start of an encounter. Both the tactician and the creature can add a 1d3 to all power rolls made against each other."

# RIVAL TALENT

name: "RIVAL TALENT"
level: 5
roles:
  - TROOP
  - HEXER
ancestry:
  - Humanoid
  - Rival
ev: 28
stamina: 120
speed: 5
size: 1M /
stability: 2
free_strike: 6
characteristics:
  - +0
  - +0
  - +3
  - +0
  - +1
actions:
  - name: "Overwhelming Rend"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Psionic, Ranged, Strike, Telekinesis
      <br />**Distance** Ranged 10
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 psychic damage; push 2; M< 1 [[prone]]
      <br />★ 12–16 14 psychic damage; push 3; M< 2 [[prone]]
      <br />✸ 17+ 17+ psychic damage; push 4; M< 3 [[prone]]"
maneuvers:
  - name: "Disarrange Thoughts"
    desc: "
      <br />**Keywords** Psionic, Ranged, Telepathy
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 psychic damage; R< 1 [[dazed]] (save ends)
      <br />★ 12–16 6 psychic damage; R< 2 [[dazed]] (save ends)
      <br />✸ 17+ 6 psychic damage; R< 3 [[dazed]] and [[slowed]] (save ends)"
ta:
  - name: "Precognitive Shift"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** A creature deals damage to the talent. 
      <br />**Effect:** The talent halves the damage and shifts 2."
traits:
  - name: "Rivalry"
    desc: "- The talent selects one creature within [[Draw Steel Rules#LINE OF EFFECT|line of effect]] at the start of an encounter. Both the talent and the creature can add a 1d3 to all power rolls made against each other."

# SHAMBLING MOUND

name: "SHAMBLING MOUND"
level: 5
roles:
  - SOLO
ancestry:
  - Plant
  - Shambling Mound
ev: 70
stamina: 400
speed: 3
size: 3 /
stability: 5
free_strike: 7
characteristics:
  - +4
  - −1
  - +0
  - +1
  - +0
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The shambling mound takes 2 turns each round. They can use two actions on each of their turns and can take each turn after an enemy turn they choose. While [[dazed]], the shambling mound can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the shambling mound can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Engulfing Sack"
    desc: "The shambling mound has a vegetative sack on their body where they carry engulfed creatures. The sack has 30 stamina, damage immunity 5, and fire weakness 10. Destroying the sack frees creatures trapped by the shambling mound’s Engulf action. The shambling mound regrows the sack at the beginning of their next turn."
actions:
  - name: "Vine Lash"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 6
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 damage; A< 3 [[grabbed]]
      <br />★ 12–16 16 damage; A< 4 [[grabbed]]
      <br />✸ 17+ 19 damage; [[grabbed]] 
      <br />**2 Malice** The shambling mound can slide one or both targets up to 6 squares. 
      <br />**3 Malice** Each target takes 7 poison damage."
  - name: "Seismic Slam"
    desc:
      "
      <br />**Keywords** Area, Weapon
      <br />**Distance** 6 burst
      <br />**Target** Each enemy in the burst
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 4 damage; M< 2 [[dazed]] (save ends)
      <br />★ 12–16 6 damage; M< 3 [[dazed]] (save ends)
      <br />✸ 17+ 7 damage; M< 4 [[dazed]] (save ends)"
  - name: "Engulf"
    desc:
      "<br />**Cost** 2 Malice
      <br />**Keywords** Area, Melee
      <br />**Distance** Melee 6
      <br />**Target** 1 creature or object 
      <br />**Effect:** The shambling mound reaches out with writhing vines and A< 3 engulfs an enemy size 1L or smaller into their sack. The potency increases by 1 if the target is [[grabbed]] by the shambling mound. An engulfed creature is [[restrained]], takes 3 poison damage at the start of each turn of combat, and can’t take damage from abilities used from outside the sack. When the shambling mound moves, the engulfed creature moves with them. If the mound dies or their engulfing sack is destroyed, each engulfed creature is freed and shunted to an unoccupied square within 2 squares. 2+ Malice The shambling mound can engulf 1 additional enemy for every 2 malice spent."
maneuvers:
  - name: "Leech"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Each creature trapped by Engulf 
      <br />**Effect:** 5 poison damage. The shambling mound gains 5 temporary stamina for each creature affected by this maneuver." 
ta:
  - name: "Tether Down"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 6
      <br />**Target** One creature 
      <br />**Trigger** A creature within distance moves.
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 7 damage; M< 2 [[restrained]] (EoT)
      <br />★ 12–16 12 damage; M< 3 [[restrained]] (EoT)
      <br />✸ 17+ 15 damage; M< 4 [[restrained]] (EoT)"
traits:
  - name: "False Appearance"
    desc: "While the shambling mound remains motionless, they are indistinguishable from ordinary vegetation."
  - name: "Frothing Flora"
    desc: "The area within 6 squares of the shambling mound is considered difficult terrain."
  - name: "Ravenous Overgrowth (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 10 x 2 line within 1
      <br />**Target** All creatures in the line
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 7 damage, pull 3
      <br />★ 12–16 12 damage; pull 4; targets gain poison weakness 3 until the encounter ends
      <br />✸ 17+ 15 damage; pull 6; targets gain poison weakness 5 until the encounter ends"
  - name: "Composting (Villain Action 2)"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** Melee 6
      <br />**Target** All enemies 
      <br />**Effect:** The shambling mound attempts to devour each enemy within distance with its Engulf action without spending malice."
  - name: "Exposed Crux (Villain Action 3)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The shambling mound rips themself apart to lay waste, exposing the crux of magic holding them together. The distance of the shambling mound’s melee abilities increases to 10, they have a double edge on power rolls, and strikes have an edge against them."

# TIME RAIDER ARCHON

name: "TIME RAIDER ARCHON"
level: 3
roles:
  - MINION
  - HARRIER
ancestry:
  - Humanoid
  - Time
  - Raider
ev: 5 for eight minions
stamina: 7
immunities: Psychic 3
speed: 7
size: 1M /
stability: 0
with-captain: Strike damage +1
free_strike: 2
characteristics:
  - +2
  - +2
  - +2
  - +1
  - −1
actions:
  - name: "Brutal Flail"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Psionic, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage; an ally can make a free strike against the target"
traits:
  - name: "Foresight"
    desc: "The archon doesn’t have a bane on strikes against concealed creatures."

# TIME RAIDER MYRIAD

name: "TIME RAIDER MYRIAD"
level: 3
roles:
  - MINION
  - BRUTE
ancestry:
  - Humanoid
  - Time
  - Raider
ev: 5 for eight minions
stamina: 8
immunities: Psychic 3
speed: 5
size: 1M /
stability: 0
with-captain: Strike damage +1
free_strike: 3
characteristics:
  - +2
  - +1
  - +2
  - +1
  - +1
actions:
  - name: "Fifth Fist"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Psionic, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage; slide 1
      <br />★ 12–16 5 damage; slide 2
      <br />✸ 17+ 6 damage; slide 3; [[prone]]"
traits:
  - name: "Foresight"
    desc: "The myriad doesn’t have a bane on strikes against concealed creatures."

# TIME RAIDER ARMIGER

name: "TIME RAIDER ARMIGER"
level: 3
roles:
  - PLATOON
  - DEFENDER
ancestry:
  - Humanoid
  - Time
  - Raider
ev: 10
stamina: 60
immunities: Psychic 3
speed: 5
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - +0
  - +2
  - +2
  - +2
  - +0
actions:
  - name: "Serrated Saber"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Psionic, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 10 damage
      <br />✸ 17+ 13 damage; R< 2 [[weakened]] (save ends) 
      <br />**2 Malice** A creature is [[bleeding]] while [[weakened]] from this ability."
ta:
  - name: "Shared Sickness"
    desc: "
      <br />**Keywords** Psionic, Ranged
      <br />**Distance** Ranged 20
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature deals damage to any ally of the armiger to whom the armiger has [[Draw Steel Rules#LINE OF EFFECT|line of effect]].
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 psychic damage; R< 0 5 poison damage
      <br />★ 12–16 6 psychic damage; R< 1 5 poison damage
      <br />✸ 17+ 9 psychic damage; R< 2 5 poison damage"
traits:
  - name: "Foresight"
    desc: "The armiger doesn’t have a bane on strikes against concealed creatures."
  - name: "Kuran’zoi Heraldry"
    desc: "While any time raider starts their turn with [[Draw Steel Rules#LINE OF EFFECT|line of effect]] to the armiger, that time raider can end one condition affecting them."

# TIME RAIDER CANNONFALL

name: "TIME RAIDER CANNONFALL"
level: 3
roles:
  - PLATOON
  - ARTILLERY
ancestry:
  - Humanoid
  - Time
  - Raider
ev: 10
stamina: 40
immunities: Psychic 3
speed: 5
size: 1L /
stability: 3
free_strike: 5
characteristics:
  - +0
  - +2
  - +2
  - +2
  - +0
actions:
  - name: "Sunderbuss"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Psionic, Ranged, Weapon
      <br />**Distance** 3 cube within 10
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 sonic damage
      <br />★ 12–16 7 sonic damage
      <br />✸ 17+ 10 sonic damage; [[prone]]; M< 2 [[slowed]] (save ends) 
      <br />**Effect:** A layer of ground or floor beneath the area that is 1 square deep is destroyed."
ta:
  - name: "Buss Buffer (Free Triggered Action)"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Area, Psionic
      <br />**Distance** Self and 5 burst
      <br />**Target** Self and all allies in the burst 
      <br />**Trigger** A creature damages the cannonfall with a ranged or area ability. 
      <br />**Effect:** The damage is reduced by half for the cannonfall and each target also affected by the triggering ability."
traits:
  - name: "Foresight"
    desc: "The cannonfall doesn’t have a bane on strikes against concealed creatures."

# TIME RAIDER HELIX

name: "TIME RAIDER HELIX"
level: 3
roles:
  - PLATOON
  - CONTROLLER
ancestry:
  - Humanoid
  - Time
  - Raider
ev: 10
stamina: 40
immunities: Psychic 3
speed: 5 (fly)
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - +0
  - +2
  - +2
  - +2
  - +2
actions:
  - name: "Blaster Volley"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Psionic, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** Three creatures
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 corruption damage; push 2
      <br />★ 12–16 8 corruption damage; push 4
      <br />✸ 17+ 11 corruption damage; push 6; [[prone]]"
maneuvers:
  - name: "Kinetic Lane"
    desc: "
      <br />**Keywords** Area, Psionic, Ranged
      <br />**Distance** 4 × 2 line within 10
      <br />**Target** Special 
      <br />**Effect:** The area becomes a psionically charged treadmill that pushes creatures and objects at high speed in one direction of the helix’s choice. Any creature that moves into the area or starts their turn there immediately slides 3 squares toward the square at the end of the area in the chosen direction. Each enemy in the area when it first appears takes 3 damage before they are moved. 
      <br />**3 Malice** The helix creates a second kinetic lane."
traits:
  - name: "Foresight"
    desc: "The helix doesn’t have a bane on strikes against concealed creatures."

# TIME RAIDER HIJACK

name: "TIME RAIDER HIJACK"
level: 3
roles:
  - PLATOON
  - AMBUSHER
ancestry:
  - Humanoid
  - Time
  - Raider
ev: 0
stamina: 50
immunities: Psychic 3
speed: 6
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - +0
  - +2
  - +2
  - +2
  - +1
actions:
  - name: "Golden Sickles"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Psionic, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 11 damage
      <br />✸ 17+ 14 damage; A< 2 [[bleeding]] (save ends) 
      <br />**Effect:** The hijack is hidden from creatures [[bleeding]] from this ability until the condition ends."
maneuvers:
  - name: "Psi-Sickle"
      <br />**Keywords** Psionic, Ranged, Weapon
      <br />**Distance** Ranged 5
      <br />**Target** One creature or object 
      <br />**Effect:** The hijack psychically latches their sickle onto the target and closes the distance between them. If the target is larger than the hijack, the hijack moves adjacent to the target. Otherwise, the target is pulled 4 squares toward the hijack."
traits:
  - name: "Foresight"
    desc: "The hijack doesn’t have a bane on strikes against concealed creatures."

# TIME RAIDER MIND PUNK

name: "TIME RAIDER MIND PUNK"
level: 3
roles:
  - PLATOON
  - HEXER
ancestry:
  - Humanoid
  - Time
  - Raider
ev: 10
stamina: 40
immunities: Psychic 3
speed: 5
size: 2 /
stability: 2
free_strike: 5
characteristics:
  - +2
  - +0
  - +2
  - +2
  - +1
actions:
  - name: "Repelling Psihander"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Psionic, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures adjacent to each other
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 8 damage; M< 1 [[dazed]] (save ends)
      <br />✸ 17+ 11 damage; M< 2 [[dazed]] (save ends) 
      <br />**Effect:** A target who ends their next turn adjacent to the other target falls [[prone]]."
  - name: "Mindpunk"
    desc:
      "
      <br />**Keywords** Area, Psionic
      <br />**Distance** 3 Burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 psychic damage; R< 0 [[prone]]
      <br />★ 12–16 6 psychic damage; push 1; R< 1 [[prone]] can’t stand (save ends)
      <br />✸ 17+ 9 psychic damage; push 2; R< 2 [[prone]] can’t stand (save ends)"
traits:
  - name: "Foresight"
    desc: "The mind punk doesn’t have a bane on strikes against concealed creatures."

# TIME RAIDER NEMESIS

name: "TIME RAIDER NEMESIS"
level: 3
roles:
  - PLATOON
  - HARRIER
ancestry:
  - Humanoid
  - Time
  - Raider
ev: 10
stamina: 50
immunities: Psychic 3
speed: 7
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - +1
  - +2
  - +2
  - +1
  - +0
actions:
  - name: "Golden Scythe"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Psionic, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; pull 1
      <br />★ 12–16 10 damage; pull 2
      <br />✸ 17+ 13 damage; pull 3; A< 2 [[restrained]] (save ends) 
      <br />**Effect:** This ability can affect creatures on parallel planes of existence and pull them onto the nemesis’s plane."
  - name: "Kinetic Crush"
    desc:
      "
      <br />**Keywords** Psionic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** One creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 psychic damage; M< 0 [[slowed]] (save ends)
      <br />★ 12–16 10 psychic damage; M< 1 [[slowed]] (save ends)
      <br />✸ 17+ 13 psychic damage; M< 2 [[slowed]] (save ends) 
      <br />**Effect:** A creature [[slowed]] by this ability takes 2 damage whenever they move into or are force moved into a square until the condition ends. 
traits:
  - name: "Foresight"
    desc: "The nemesis doesn’t have a bane on strikes against concealed creatures."

# TIME RAIDER VERTEX

name: "TIME RAIDER VERTEX"
level: 3
roles:
  - PLATOON
  - SUPPORT
ancestry:
  - Humanoid
  - Time
  - Raider
ev: 10
stamina: 50
immunities: Psychic 3
speed: 5 (fly, hover)
size: 2 /
stability: 3
free_strike: 5
characteristics:
  - +1
  - +1
  - +2
  - +1
  - +0
actions:
  - name: "Psionic Slam"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Psionic, Strike
      <br />**Distance** Reach 2
      <br />**Target** One creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; 2 psychic damage
      <br />★ 12–16 7 damage; 3 psychic damage
      <br />✸ 17+ 9 damage; 4 psychic damage 
      <br />**Effect:** Power rolls made against the target have an edge until the start of the vertex’s next turn.
  - name: "Split Space"
    desc:
      "<br />**Cost** 5 Malice
      <br />**Keywords** Area, Psionic, Ranged
      <br />**Distance** 2 cube within 10
      <br />**Target** Special 
      <br />**Effect:** A portal fills the area, leading to a location the vertex has experienced (in person or otherwise) on any plane of existence. Each creature who touches the portal is instantly teleported to the nearest unoccupied square at the chosen location. The portal lasts until the vertex dies, uses this ability again, dismisses the portal (no action required), or is transported by the portal."
maneuvers:
  - name: "Invigorated March"
    desc: "
      <br />**Keywords** Area, Psionic
      <br />**Distance** 4 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Each target shifts up to half their speed."
traits:
  - name: "Foresight"
    desc: "The vertex doesn’t have a bane on strikes against concealed creatures."

# TIME RAIDER TYRANNIS

name: "TIME RAIDER TYRANNIS"
level: 3
roles:
  - LEADER
ancestry:
  - Humanoid
  - Time
  - Raider
ev: 20
stamina: 120
immunities: Psychic 5
speed: 10 (teleport, hover)
size: 2 /
stability: 2
free_strike: 5
characteristics:
  - +0
  - +3
  - +3
  - +1
  - +0
actions:
  - name: "Gatling Blaster"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Psionic, Strike, Weapon
      <br />**Distance** Melee 2 or Ranged 10
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 corruption damage
      <br />★ 12–16 12 corruption damage
      <br />✸ 17+ 15 corruption damage 
      <br />**Effect:** Each target’s speed is reduced by 2 until the start of the tyrannis’ next turn.
maneuvers:
  - name: "Air Raid!"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** Psionic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** Three time raiders 
      <br />**Effect:** Each target is psionically lifted into the air, flies up to their speed, and makes a free strike. If a target doesn’t land in an unoccupied space, they fall."
ta:
  - name: "Precog Reflexes"
    desc: "
      <br />**Keywords** Psionic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One creature 
      <br />**Trigger** The target strikes the tyrannis. 
      <br />**Effect:** The strike has a bane. After the strike resolves, the tyrannis makes a free strike against the target. 
      <br />**2 Malice** The strike has a double bane instead."
traits:
  - name: "End Effect"
    desc: "At the end of their turn, the tyrannis can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Foresight"
    desc: "The tyrannis doesn’t have a bane on strikes against concealed creatures."
va:
  - name: "We Will Win! (Villain Action 1)"
    desc: "
      <br />**Keywords** Psionic, Ranged
      <br />**Distance** Self and Ranged 10
      <br />**Target** Self and three allies 
      <br />**Effect:** Each target gains 15 temporary stamina and has their speed doubled until the end of their turn."
  - name: "Stick To The Plan! (Villain Action 2)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** Self and 10 burst
      <br />**Target** Self and all allies in the burst 
      <br />**Effect:** Each target can end one effect or condition affecting them or can move up to their speed."
  - name: "Armageddon (Villain Action 3)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 5 burst
      <br />**Target** Special 
      <br />**Effect:** The tyrannis fires a sensor mine into each unoccupied square in the burst and a gravity well (see [[Gravity Well]]) into one of their own squares. Whenever an enemy moves into a square with a sensor mine in it, the mine explodes, dealing 3 damage to the enemy."

# TROLL LIMBJUMBLE

name: "TROLL LIMBJUMBLE"
level: 5
roles:
  - MINION
  - HEXER
ancestry:
  - Troll
ev: 7 for eight minions
stamina: 8
speed: 5
size: 1S /
stability: 0
with-captain: Edge on strikes
free_strike: 3
characteristics:
  - +3
  - +1
  - -2
  - -1
  - -1
actions:
  - name: "Arm and a Leg"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 damage; A< 2 [[prone]]
      <br />★ 12–16 5 damage; A< 3 [[prone]]
      <br />✸ 17+ 6 damage; [[prone]] 
      <br />**Effect:** If the target is already [[prone]], they are [[grabbed]] instead."
traits:
  - name: "Hyper Regeneration"
    desc: "The limbjumble regains 2 stamina at the start of each of their turns. The limbjumble instantly dies if they take acid or fire damage."

# TROLL WHELP

name: "TROLL WHELP"
level: 5
roles:
  - MINION
  - BRUTE
ancestry:
  - Giant
  - Troll
ev: 7 for eight minions
stamina: 10
speed: 6
size: 1L /
stability: 3
with-captain: Strike damage +2
free_strike: 3
characteristics:
  - +3
  - +1
  - -1
  - +0
  - +0
actions:
  - name: "Jaws and Claws"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 6 damage; slide 1
      <br />✸ 17+ 7 damage; slide 2; M< 2 [[bleeding]] (save ends)" 
traits:
  - name: "Lingering Hunger"
    desc: "Whenever two or more whelps are simultaneously reduced to 0 stamina with non-acid or fire damage, half of the killed whelps become troll limbjumbles with 4 stamina."

# TROLL BUTCHER

name: "TROLL BUTCHER"
level: 5
roles:
  - TROOP
  - HEXER
ancestry:
  - Giant
  - Troll
ev: 28
stamina: 120
weaknesses: Acid 5, Fire 5
speed: 8
size: 2 /
stability: 2
free_strike: 6
characteristics:
  - +3
  - +1
  - +1
  - +0
  - +0
actions:
  - name: "Savoring Bite"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage; M< 1 [[bleeding]] (save ends)
      <br />★ 12–16 14 damage; M< 2 [[bleeding]] (save ends)
      <br />✸ 17+ 17+ damage; M< 3 [[bleeding]] (save ends) 
      <br />**1 Malice** The gourmand regains stamina equal to the damage dealt.
  - name: "Rotten Scraps"
    desc: "
      <br />**Keywords** Area, Ranged
      <br />**Distance** 3 cube within 10
      <br />**Target** Each enemy in the cube
      <br />`dice: 2d10 +
      <br />✦ ≤11 5 poison damage; M< 1 [[weakened]] (save ends)
      <br />★ 12–16 9 poison damage; M< 2 [[weakened]] (save ends)
      <br />✸ 17+ 11 poison damage; M< 3 [[weakened]] (save ends) 
      <br />**Effect:** Each troll in the cube regains 3 stamina."
maneuvers:
  - name: "Gourmet Flesh"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The gourmand enhances their next Savoring Bite ability, changing the damage type and inflicted condition to one of the following combinations: corruption and [[dazed]], acid and [[restrained]], or lightning and [[frightened]]."
ta:
  - name: "Acquired Taste"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature with deals damage to the gourmand with an Edge or a Surge. 
      <br />**Effect:** The gourmand makes a free strike against the target. The gourmand has an edge on power rolls and deals an additional 3 damage on their strikes until the end of their next turn."
traits:
  - name: "Bloody Feast"
    desc: "Each ally within 5 of the gourmand has an edge on power rolls that target an enemy suffering from a condition. "
  - name: "Relentless Hunger"
    desc: "The gourmand only dies when they are reduced to 0 stamina by acid or fire damage, end their turn with 0 stamina, or take acid or fire damage while at 0 stamina."

# TROLL GLUTTON

name: "TROLL GLUTTON"
level: 5
roles:
  - TROOP
  - BRUTE
ancestry:
  - Giant
  - Troll
ev: 28
stamina: 160
weaknesses: Acid 5, Fire 5
speed: 6
size: 2 /
stability: 4
free_strike: 7
characteristics:
  - +3
  - +1
  - -1
  - +0
  - +1
actions:
  - name: "Voracious Mastication"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 damage
      <br />★ 12–16 15 damage; M< 2 [[slowed]] (save ends)
      <br />✸ 17+ 18 damage; M< 3 [[slowed]] (save ends) 
      <br />**1 Malice** The glutton regains stamina equal to the damage dealt."
  - name: "Crash Through"
    desc:
      "<br />**Cost** 3 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The glutton shifts up to their speed in a straight line, ignoring difficult terrain. A creature can choose to fall [[prone]] or take 10 damage the first time the glutton passes through their space during the movement. If the glutton moves into a creature or object larger than them and the glutton doesn’t knock the creature [[prone]] or destroy the object, the glutton’s movement stops early and they become [[dazed]] until the end of their next turn."
maneuvers:
  - name: "Food Frenzy"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The glutton has a double edge on strikes and strikes have an edge against them, until the start of their next turn."
ta:
  - name: "Spiteful Retort (Free Triggered Action)"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** Self 
      <br />**Trigger** The glutton is reduced to 0 stamina but doesn’t die. 
      <br />**Effect:** The glutton uses their Voracious Mastication ability against an adjacent creature."
traits:
  - name: "Insatiable Appetite"
    desc: "- Once per turn, the glutton can take the Charge action as a free maneuver if they target a [[winded]] creature."
  - name: "Relentless Hunger"
    desc: "The glutton only dies when they are reduced to 0 stamina by acid or fire damage, end their turn with 0 stamina, or take acid or fire damage while at 0 stamina."


# CRAWLING CLAW

name: "CRAWLING CLAW"
level: 1
roles:
  - MINION
  - HARRIER
ancestry:
  - Undead
ev: 3 for eight minions
stamina: 4
immunities: corruption 1, poison 1
speed: 6 (climb)
size: 1T /
stability: 0
with-captain:
speed: +2
free_strike: 1
characteristics:
  - 0
  - +2
  - −5
  - −1
  - −1
actions:
  - name: "Fingernails"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage
      <br />★ 12–16 2 damage
      <br />✸ 17+ 3 damage 
      <br />**Effect:** The crawling claw shifts a number of squares equal to the damage dealt."
traits:
  - name: "Disorganized"
    desc: "The crawling claw can’t grant the flanking benefit to allies."

# DECREPIT SKELETON

name: "DECREPIT SKELETON"
level: 1
roles:
  - MINION
  - ARTILLERY
ancestry:
  - Undead
ev: 3 for eight minions
stamina: 3
immunities: corruption 1, poison 1
speed: 5
size: 1M /
stability: 0
with-captain: Edge on strikes
free_strike: 2
characteristics:
  - 0
  - +2
  - −2
  - 0
  - −2
actions:
  - name: "Bone Bow"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage 
      <br />**Effect:** The decrepit skeleton chooses one other target within distance to take 1 damage."
traits:
  - name: "Bonetrops"
    desc: "When the decrepit skeleton is reduced to stamina 0, their square becomes difficult terrain. The first time any enemy enters this space, they take 1 damage."

# ROTTING ZOMBIE

name: "ROTTING ZOMBIE"
level: 1
roles:
  - MINION
  - BRUTE
ancestry:
  - Undead
ev: 3 for eight minions
stamina: 5
immunities: corruption 1, poison 1
speed: 4
size: 1M /
stability: 0
with-captain: Strike damage +1
free_strike: 2
characteristics:
  - +2
  - −2
  - −5
  - −2
  - −3
actions:
  - name: "Rotting Fist"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage; M< 2 [[prone]] if size 1, [[slowed]] (save ends) otherwise"
traits:
  - name: "Death Grasp"
    desc: "- When the rotting zombie is reduced to stamina 0, their square becomes difficult terrain. The first time any enemy enters this space, they are M< 2 [[slowed]] (save ends)."

# SHADE

name: "SHADE"
level: 1
roles:
  - MINION
  - AMBUSHER
ancestry:
  - Undead
ev: 3 for eight minions
stamina: 4
immunities: corruption 1, poison 1
speed: 5 (fly, hover)
size: 1M/
stability: 1
with-captain:
speed: +2
free_strike: 2
characteristics:
  - −5
  - +1
  - 0
  - 0
  - +2
actions:
  - name: "Life Drain"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 corruption damage
      <br />★ 12–16 4 corruption damage
      <br />✸ 17+ 5 corruption damage; the target moves up to their speed away from all shades"
traits:
  - name: "Corruptive Phasing"
    desc: "The shade can move through other creatures and objects at normal speed. The first time in a round that the shade passes through a creature, that creature takes 2 corruption damage. The shade doesn’t take damage from being force moved into objects."

# GHOUL

name: "GHOUL"
level: 1
roles:
  - BAND
  - HARRIER
ancestry:
  - Undead
ev: 3
stamina: 15
immunities: corruption 1, poison 1
speed: 7
size: 1M/
stability: 0
free_strike: 1
characteristics:
  - 0
  - +2
  - −2
  - 0
  - −1
actions:
  - name: "Razor Claws"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage; M< 2 [[bleeding]] (save ends)"
maneuvers:
  - name: "Leap"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The ghoul jumps 3 squares. If they land on a size 1 enemy, that enemy is knocked [[prone]] and the ghoul makes a free strike against them."
traits:
  - name: "Hunger"
    desc: "If the ghoul charges, their speed increases by 2 until the end of their turn."
  - name: "Arise"
    desc: "The first time the ghoul is reduced to stamina 0 by damage that isn’t fire damage or holy damage and their body isn’t destroyed, they regain half their stamina and fall [[prone]]."

# SKELETON

name: "SKELETON"
level: 1
roles:
  - BAND
  - ARTILLERY
ancestry:
  - Undead
ev: 3
stamina: 10
immunities: corruption 1, poison 1
speed: 5
size: 1M/
stability: 0
free_strike: 2
characteristics:
  - 0
  - +1
  - +1
  - 0
  - −1
actions:
  - name: "Bone Shards"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 10
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 6 damage
      <br />✸ 17+ 7 damage 
      <br />**Effect:** Until the start of the skeleton’s next turn, the target takes 2 damage the first time they move on their turn."
maneuvers:
  - name: "Bone Spur"
    desc: "
      <br />**Keywords** Area, Weapon
      <br />**Distance** 1 burst
      <br />**Target** Each enemy in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage; M< 0 [[bleeding]] (save ends)
      <br />★ 12–16 2 damage; M< 1 [[bleeding]] (save ends)
      <br />✸ 17+ 3 damage; M< 2 [[bleeding]] (save ends) 
      <br />**Effect:** Each target has a bane on their next strike."
traits:
  - name: "Arise"
    desc: "The first time the skeleton is reduced to stamina 0 by damage that isn’t fire damage or holy damage and their body isn’t destroyed, they regain half their stamina and fall [[prone]]."

# SPECTER

name: "SPECTER"
level: 1
roles:
  - BAND
  - HEXER
ancestry:
  - Undead
ev: 3
stamina: 10
immunities: corruption 1, poison 1
speed: 5 (fly, hover)
size: 1M/
stability: 1
free_strike: 1
characteristics:
  - −5
  - +1
  - 0
  - 0
  - +2
actions:
  - name: "Decaying Touch"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Strike
      <br />**Distance** Melee 1
      <br />**Target** One creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 corruption damage; P< 0 [[weakened]] (save ends)
      <br />★ 12–16 4 corruption damage; P< 1 [[weakened]] (save ends)
      <br />✸ 17+ 5 corruption damage; P< 2 [[weakened]] (save ends) 
      <br />**2 Malice** The potency of this ability increases by 1. A living creature killed by this ability becomes a specter who appears in the target’s space under the Director’s control."
maneuvers:
  - name: "Hidden Movement"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The specter turns invisible, moves up to their speed, and becomes visible again."
traits:
  - name: "Corruptive Phasing"
    desc: "The specter can move through other creatures and objects at normal speed. The first time in a round that the specter passes through a creature, that creature takes 2 corruption damage. The specter doesn’t take damage from being force moved into objects."

# UMBRAL STALKER

name: "UMBRAL STALKER"
level: 1
roles:
  - BAND
  - AMBUSHER
ancestry:
  - Undead
ev: 3
stamina: 15
immunities: corruption 1, poison 1
speed: 7 (climb)
size: 1M/
stability: 1
free_strike: 2
characteristics:
  - 0
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Chilling Grasp"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Strike
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 cold damage
      <br />★ 12–16 6 cold damage
      <br />✸ 17+ 7 cold damage 
      <br />**Effect:** The umbral stalker shifts 2 before or after using this ability."
  - name: "Freezing Dark"
    desc:
      "
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 cube within 1
      <br />**Target** Each enemy in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 cold damage
      <br />★ 12–16 3 cold damage
      <br />✸ 17+ 4 cold damage 
      <br />**Effect:** Until the end of the umbral stalker’s next turn, the area is concealed and blocks [[Draw Steel Rules#LINE OF EFFECT|line of effect]] for all enemies."
maneuvers:
  - name: "Shadow Jump (Free Maneuver)"
    desc: "
      <br />**Cost** 1 Malice
      <br />The umbral stalker teleports to an unoccupied space in concealment within 10 squares."
traits:
  - name: "Corruptive Phasing"
    desc: "The umbral stalker can move through other creatures and objects at normal speed. The first time in a round that the umbral stalker passes through a creature, that creature takes 2 corruption damage. The umbral stalker doesn’t take damage from being force moved into objects."

# WIGHT

name: "WIGHT"
level: 1
roles:
  - BAND
  - HEXER
ancestry:
  - Undead
ev: 3
stamina: 10
immunities: corruption 1, poison 1
speed: 5
size: 1M/
stability: 0
free_strike: 1
characteristics:
  - +2
  - +1
  - 0
  - 0
  - +1
actions:
  - name: "Lifestealer Longsword"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 corruption damage
      <br />★ 12–16 4 corruption damage; M< 1 [[slowed]] (save ends)
      <br />✸ 17+ 5 corruption damage; M< 2 [[slowed]] and [[weakened]] (save ends) 
      <br />**Effect:** The target appears to rapidly age each time they take damage from this ability. The target regains their former appearance when the wight is destroyed."
maneuvers:
  - name: "Raise"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 3
      <br />**Target** One dead ally 
      <br />**Effect:** The target revives with half their stamina. The wight can’t use this maneuver again until they attack a creature with their lifestealer longsword."
traits:
  - name: "Arise"
    desc: "The first time the wight is reduced to stamina 0 by damage that isn’t fire damage or holy damage and their body isn’t destroyed, they regain half their stamina and fall [[prone]]."

# ZOMBIE

name: "ZOMBIE"
level: 1
roles:
  - BAND
  - BRUTE
ancestry:
  - Undead
ev: 3
stamina: 20
immunities: corruption 1, poison 1
speed: 5
size: 1M /
stability: 1
free_strike: 2
characteristics:
  - +2
  - +1
  - −5
  - −2
  - +1
actions:
  - name: "Clobber and Clutch"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 6 damage
      <br />✸ 17+ 7 damage; [[grabbed]] 
      <br />**Effect:** A target who starts their turn [[grabbed]] by the zombie takes 2 corruption damage. If a creature takes 5 or more corruption damage this way, they become insatiably hungry for flesh. The target must complete the Find a Cure project to end this effect."
maneuvers:
  - name: "Breakfall"
    desc: "
      <br />**Keywords** Area, Melee
      <br />**Distance** 2 burst
      <br />**Target** Each enemy in the burst 
      <br />**Effect:** The zombie falls [[prone]], expelling a wave of rot and dust.
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 corruption damage
      <br />★ 12–16 3 corruption damage; M< 1 [[weakened]] (save ends)
      <br />✸ 17+ 4 corruption damage; M< 2 [[dazed]] (save ends)"
traits:
  - name: "Endless Knight"
    desc: "The first time the zombie is reduced to stamina 0 by damage that isn’t fire damage or holy damage and their body isn’t destroyed, they regain their full stamina and fall [[prone]]."

# GHOST

name: "GHOST"
level: 1
roles:
  - LEADER
ancestry:
  - Undead
ev: 12
stamina: 80
immunities: corruption 3, poison 3
speed: 6 (fly, hover)
size: 1M/
stability: 1
free_strike: 4
characteristics:
  - −2
  - +2
  - 0
  - 0
  - +3
actions:
  - name: "Heat Death"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 5
      <br />**Target** Two creatures
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 cold damage; P< 1 [[slowed]] (save ends)
      <br />★ 12–16 10 cold damage; P< 2 [[slowed]] (save ends)
      <br />✸ 17+ 13 cold damage; P< 3 [[slowed]] (save ends) 
      <br />**Effect:** The next strike made against the target has an edge."
maneuvers:
  - name: "Haunt"
    desc: "
      <br />**Keywords** Ranged
      <br />**Distance** Ranged 8
      <br />**Target** Self or one incorporeal ally 
      <br />**Effect:** The target shifts up to their speed. 
      <br />**2 Malice** The ghost chooses one additional target."
ta:
  - name: "Shriek"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Magic
      <br />**Distance** Melee 1
      <br />**Target** The triggering creature 
      <br />**Trigger** A creature within distance targets the ghost with a strike. 
      <br />**Effect:** The ghost halves the incoming damage and the target takes 2 sonic damage."
traits:
  - name: "Phantom Flow"
    desc: "Each incorporeal undead creature within 10 squares of the ghost ignores difficult terrain."
  - name: "Paranormal Activity (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 burst
      <br />**Target** Each size: 1S or larger object in the burst 
      <br />**Effect:** Each target floats 1 square into the air and is pulled 5 squares toward the nearest enemy within 3 squares of them."
  - name: "Spirited Away (Villain Action 2)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 burst
      <br />**Target** Each enemy in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 P< 1 levitated (EoT) (see effect)
      <br />★ 12–16 P< 2 levitated (EoT)
      <br />✸ 17+ P< 3 levitated for the rest of the encounter 
      <br />**Effect:** A levitated target floats 1 square off the ground when they are first affected, then rises 1 square at the end of each of their turns. If a levitated target can’t already fly, they can fly but are [[slowed]] and [[weakened]] while flying in this way."
  - name: "Awful Wail (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 burst
      <br />**Target** Each enemy in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 sonic damage
      <br />★ 12–16 5 sonic damage
      <br />✸ 17+ 8 sonic damage 
      <br />**Effect:** P< 2 the target is reduced to 1 stamina if they have 2 or more stamina after taking damage."
traits:
  - name: "Corruptive Phasing"
    desc: "The ghost can move through other creatures and objects at normal speed. The first time in a round that the ghost passes through a creature, that creature takes 2 corruption damage. The ghost doesn’t take damage from being force moved into objects."


# FLESHFLAYED SHAMBLER

name: "FLESHFLAYED SHAMBLER"
level: 4
roles:
  - MINION
  - BRUTE
ancestry:
  - Undead
ev: 6 for eight minions
stamina: 9
immunities: corruption 4, poison 4
speed: 5
size: 1M /
stability: 0
with-captain: Strike damage +2
free_strike: 3
characteristics:
  - +3
  - -1
  - +0
  - +0
  - +0
actions:
  - name: "Bone Carvers"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 5 damage
      <br />✸ 17+ 7 damage 
      <br />**Effect:** The target is [[bleeding]] (save ends) if the shambler has an edge on this ability."
traits:
  - name: "Fleshfused Spines"
    desc: "Whenever an enemy makes physical contact with the shambler or uses a melee ability against the shambler, they take 2 damage."

# GHOUL CRAVER

name: "GHOUL CRAVER"
level: 4
roles:
  - MINION
  - HARRIER
ancestry:
  - Undead
ev: 6 for eight minions
stamina: 8
immunities: corruption 4, poison 4
speed: 7 (climb)
size: 1M /
stability: 0
with-captain: Strike damage +2
free_strike: 2
characteristics:
  - +3
  - +2
  - 0
  - 0
  - 0
actions:
  - name: "Taste"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 6 damage 
      <br />**Effect:** The ghoul craver has a double edge on this ability when targeting [[bleeding]] creatures."
traits:
  - name: "Ever So Hungry"
    desc: "While 3 or more ghoul cravers are adjacent to an enemy, that enemy can’t shift."
  - name: "Hunger"
    desc: "The ghoul craver’s speed increases by 2 while charging, until the end of their turn."

# HOLLOWBONE LAUNCHER

name: "HOLLOWBONE LAUNCHER"
level: 4
roles:
  - MINION
  - ARTILLERY
ancestry:
  - Undead
ev: 6 for eight minions
stamina: 7
immunities: corruption 4, poison 4
speed: 5
size: 1M /
stability: 0
with-captain: Ranged distance +5
free_strike: 3
characteristics:
  - -2
  - +3
  - +0
  - +0
  - +0
actions:
  - name: "Hollowbone Slug"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 5 damage
      <br />✸ 17+ 7 damage; M< 3 [[bleeding]] (save ends) 
      <br />**Effect:** Each creature adjacent to the target takes 2 damage from exploding bone shards."
traits:
  - name: "Brittle Revenge"
    desc: "The hollowbone launcher explodes when they are reduced to 0 stamina, dealing 2 damage to each adjacent creature."

# FLESH MOURNLING

name: "FLESH MOURNLING"
level: 4
roles:
  - BAND
  - DEFENDER
ancestry:
  - Undead
ev: 6
stamina: 35
immunities: corruption 4, poison 4
speed: 6
size: 2 /
stability: 2
free_strike: 2
characteristics:
  - +3
  - +1
  - 0
  - +2
  - -1
actions:
  - name: "Multiarm Strike"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object
      <br />✸ ≤11 5 damage
      <br />★ 12–16 7 damage
      <br />`dice: 2d10 + 3`
      <br />✦ 17+ 9 damage 
      <br />**Effect:** The target can’t shift away from the mournling until the end of their turn. 
      <br />**1 Malice** The mournling targets an additional creature.
  - name: "Horrid Wail"
    desc:
      "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 burst
      <br />**Target** all enemies in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 2 psychic damage
      <br />★ 12–16 3 psychic damage; I< 2 [[frightened]] (save ends)
      <br />✸ 17+ 4 psychic damage; I< 3 [[frightened]] (save ends) 
      <br />**Effect:** If a target is still [[frightened]] by this ability at the end of the encounter, they cannot take a respite activity during their next respite"
traits:
  - name: "Immutable Form"
    desc: "The mournling’s shape can’t change via any external effects." 
  - name: "Arise"
    desc: "The first time in an encounter that the mournling is reduced to 0 stamina with non-fire/non-holy damage and their body isn’t destroyed, they regain half their stamina and fall [[prone]]."

# GIANT ZOMBIE

name: "GIANT ZOMBIE"
level: 4
roles:
  - TROOP
  - BRUTE
ancestry:
  - Undead
ev: 24
stamina: 140
immunities: corruption 4, poison 4
speed: 6
size: 3 /
stability: 2
free_strike: 6
characteristics:
  - +3
  - -1
  - -2
  - +1
  - +2
actions:
  - name: "Rotten Smash"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage
      <br />★ 12–16 14 damage; A< 2 [[grabbed]]
      <br />✸ 17+ 17+ damage; A< 3 [[grabbed]]"
ta:
  - name: "Knocking Heads"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Two creatures or objects 
      <br />**Trigger** The giant zombie grabs both targets or starts their turn with each target [[grabbed]]. 
      <br />**Effect:** The giant zombie smashes the targets together, using their Rotten Smash against both targets with a double edge."
traits:
  - name: "Negative Nerves"
    desc: "When the giant zombie is targeted by an ability, they halve the damage from any tier-1 results."
  - name: "Arise"
    desc: "The first time the giant zombie is reduced to 0 stamina with non  -fire/non  -holy damage and their body isn’t destroyed, they regain half their stamina and fall [[prone]]."

# MUMMY

name: "MUMMY"
level: 4
roles:
  - BAND
  - BRUTE
ancestry:
  - Mummy
  - Undead
ev: 6
stamina: 50
immunities: corruption 4, poison 4 /
weaknesses: fire 5
speed: 5
size: 1M /
stability: 2
free_strike: 3
characteristics:
  - +3
  - -1
  - +1
  - +3
  - +0
actions:
  - name: "Accursed Bindings"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 corruption damage; pull 1
      <br />★ 12–16 8 corruption damage; pull 2
      <br />✸ 17+ 10 corruption damage; pull 2; M< 3 [[restrained]] (save ends) 
      <br />**Effect:** The potency of the mummy’s next ability used against the target increases by 1."
  - name: "Eldritch Curse"
    desc:
      "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One creature
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 corruption damage; I< 1 cursed (save ends)
      <br />★ 12–16 5 corruption damage; I< 2 cursed (save ends)
      <br />✸ 17+ 7 corruption damage; I< 3 cursed (save ends) 
      <br />**Effect:** A cursed target is [[bleeding]] and [[weakened]], and allies have an edge on strikes made against them."
ta:
  - name: "Blast of Mummy Dust"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Area
      <br />**Distance** 1 burst
      <br />**Target** 1 [[restrained]] target 
      <br />**Trigger** The mummy comes within distance of the target or starts their turn within distance of the target. 
      <br />**Effect:** 8 poison damage."

# VAMPIRE SPAWN

name: "VAMPIRE SPAWN"
level: 4
roles:
  - BAND
  - HARRIER
ancestry:
  - Undead
  - Vampire
ev: 6
stamina: 30
immunities: corruption 4, poison 4
speed: 5 (climb)
size: 1M /
stability: 0
free_strike: 2
characteristics:
  - +2
  - +3
  - -1
  - +1
  - +2
actions:
  - name: "Exsanguinating Bite"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 7 corruption damage; M< 2 [[bleeding]] (save ends)
      <br />✸ 17+ 9 corruption damage; M< 3 [[bleeding]] (save ends) 
      <br />**Effect:** The vampire spawn regains stamina equal to the corruption damage they deal.
      <br />**1 Malice** The target takes an additional 3 corruption damage."
maneuvers:
  - name: "Vampiric Celerity"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The vampire spawn shifts 1 and then moves up to their speed. The next ability the vampire uses before the start of their next turn has an edge."
traits:
  - name: "Unslakable Bloodthirst"
    desc: "The vampire spawn has a speed of 10 while a creature is [[bleeding]] within 10. The vampire spawn must strike a [[bleeding]] creature on their turn if they are able to."

# WRAITH

name: "WRAITH"
level: 4
roles:
  - BAND
  - HEXER
ancestry:
  - Undead
ev: 6
stamina: 25
immunities: corruption 4, poison 4
speed: 8 (fly, hover)
size: 1M /
stability: 0
free_strike: 2
characteristics:
  - -2
  - +2
  - +1
  - +1
  - +3
actions:
  - name: "Chilling Gravetouch"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 cold damage; P< 1 [[slowed]] (save ends)
      <br />★ 12–16 7 cold damage; P< 2 [[slowed]] (save ends)
      <br />✸ 17+ 9 cold damage; P< 3 [[slowed]] (save ends) 
      <br />**Effect:** Living creatures killed by this ability return as a ghoul craver the next round, under the Director’s control.
maneuvers:
  - name: "Hidden Movement"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The specter turns invisible, moves up to their speed, and becomes visible again."
ta:
  - name: "Stolen Vitality (Free Triggered Action)"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** 1 enemy 
      <br />**Trigger** The target regains stamina. 
      <br />**Effect:** The target only regains half the stamina they would normally. The wraith regains the remaining stamina."
traits:
  - name: "Agonizing Phasing"
    desc: "The wraith can move through other creatures and objects at normal speed. The first time in a round that the shade passes through a creature, that creature takes 5 corruption damage and has a bane on their next attack. The wraith doesn’t take damage from being force moved into objects."

# MUMMY LORD

name: "MUMMY LORD"
level: 4
roles:
  - LEADER
ancestry:
  - Mummy
  - Undead
ev: 24
stamina: 155
immunities: corruption 6, poison 6 /
weaknesses: fire 5
speed: 6
size: 1M /
stability: 4
free_strike: 6
characteristics:
  - +4
  - +0
  - +2
  - +4
  - +2
actions:
  - name: "Accursed Slam"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 10 corruption damage; I< 2 [[bleeding]] (save ends)
      <br />★ 12–16 14 corruption damage; I< 3 [[bleeding]] (save ends)
      <br />✸ 17+ 17+ corruption damage; I< 4 [[bleeding]] (save ends) 
      <br />**Effect:** The potency of abilities used against a target [[bleeding]] from this ability increase by 1."
  - name: "Binding Curse"
    desc:
      "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 20
      <br />**Target** One creature
      <br />`dice: 2d10 + 4`
      <br />✸ ≤11 7 corruption damage; I< 2 [[frightened]] (save ends)
      <br />★ 12–16 12 corruption damage; I< 3 [[frightened]] (save ends)
      <br />✦ 17+ 16 corruption damage; I< 4 [[frightened]] (save ends) 
      <br />**Effect:** A target [[frightened]] by this ability takes 4 psychic damage whenever they use a move action until the condition ends. 
      <br />**2+ Malice** The mummy lord targets an additional creature for every 2 malice spent."
ta:
  - name: "Summon my Guard!"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** Special 
      <br />**Trigger** The Mummy Lord becomes [[winded]] for the first time. 
      <br />**Effect:** Two mummies and 4 ghoul carvers appear within distance."
traits:
  - name: "Cursed Transference"
    desc: "At the end of their turn, the mummy lord can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way. <br />**5 Malice** The effect is transferred to a creature within 10."
  - name: "Plague of Flies (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 burst
      <br />**Target** All enemies
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 5 poison damage
      <br />★ 12–16 8 poison damage
      <br />✸ 17+ 10 poison damage 
      <br />**Effect:** Each target has a bane on their next strike."
  - name: "Land’s Guardian (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The mummy lord’s speed increases by 2 and adds the burrow keyword to their movement. The mummy lord burrows up to their speed. Each enemy within 2 squares of the mummy lord’s movement must make a Might test.
      <br />✸ ≤11 [[prone]], can’t stand (EoT)
      <br />★ 12–16 [[prone]]
      <br />`dice: 2d10 +
      <br />✦ 17+ no effect"
  - name: "Unbound Horrors (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 burst
      <br />**Target** All enemies
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 5 corruption damage; I< 2 [[frightened]] (save ends)
      <br />★ 12–16 8 corruption damage; I< 3 [[frightened]] (save ends)
      <br />✸ 17+ 10 corruption damage; I< 4 [[frightened]] and [[restrained]] (save ends)"

# VOICELESS TALKER GRAYWARPER

name: "VOICELESS TALKER GRAYWARPER"
level: 6
roles:
  - MINION
  - CONTROLLER
ancestry:
  - Horror
  - Voiceless Talker
ev: 8 for eight minions
stamina: 9
speed: 5
size: 1M /
stability: 0
with-captain: 2 temporary stamina
free_strike: 3
characteristics:
  - -1
  - +0
  - +3
  - +1
  - +1
actions:
  - name: "Phase Chant"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Psionic, Ranged, Strike
      <br />**Distance** Ranged 8
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 psychic damage
      <br />★ 12–16 5 psychic damage; slide 2
      <br />✸ 17+ 7 psychic damage; slide 4 Psionic Conductor When a non-minion Voiceless Talker within 5 of the graywarper uses an ability with the Psionic keyword, they can do so as if they were in the graywarper’s space."

# MINDKILLER WHELP

name: "MINDKILLER WHELP"
level: 6
roles:
  - MINION
  - HEXER
ancestry:
  - Horror
  - Voiceless Talker
ev: 8 for eight minions
stamina: 9
immunities: psychic 6
speed: 4 (fly, hover)
size: 1S /
stability: 0
with-captain: Strike damage +2
free_strike: 3
characteristics:
  - -1
  - +3
  - +1
  - +1
  - +0
actions:
  - name: "Eager Claws"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 5 damage; target has a bane on their next strike
      <br />✸ 17+ 7 damage; target has a bane on their next strike"
ta:
  - name: "Feast"
    desc: "
      <br />**Keywords** Psionic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The whelp kills a creature. 
      <br />**Effect:** The whelp transforms into a mindkiller. They have stamina equal to their squad’s stamina pool before transforming."
traits:
  - name: "Psionic Conductor"
    desc: "When a non-minion Voiceless Talker within 5 of the whelp uses an ability with the Psionic keyword, they can do so as if they were in the whelp’s space."

# HULKING BRAIN

name: "HULKING BRAIN"
level: 6
roles:
  - TROOP
  - BRUTE
ancestry:
  - Horror
  - Voiceless Talker
ev: 32
stamina: 180
speed: 5
size: 1L /
stability: 4
free_strike: 7
characteristics:
  - +3
  - +1
  - -2
  - -2
  - +0
actions:
  - name: "Four-Way Grasp"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 4 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 10 damage; A< 2 [[grabbed]]
      <br />✸ 17+ 11 damage; A< 3 [[grabbed]] 
      <br />**2 Malice** The potency of this ability increases by 1."
  - name: "Cerebral Suplex"
    desc:
      "
      <br />**Keywords** Melee
      <br />**Distance** Melee 1
      <br />**Target** All [[grabbed]] enemies
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 damage; M< 1 3 damage
      <br />★ 12–16 10 damage; M< 2 3 damage
      <br />✸ 17+ 13 damage; M< 3 6 damage 
      <br />**Effect:** Each target is no longer [[grabbed]]."
maneuvers:
  - name: "Lumber"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Shift 4. This movement ignores difficult terrain."
ta:
  - name: "Brawny Buffer (Free Triggered Action)"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Ranged 5
      <br />**Target** Self 
      <br />**Trigger** An ally voiceless talker takes damage from an enemy 
      <br />**Effect:** The hulking brain shifts to a square adjacent to the ally and takes the damage instead.
      <br />**2 Malice** The enemy that dealt damage is knocked [[prone]]."
traits:
  - name: "Biceps to Spare"
    desc: "The hulking brain can carry up to 4 size 1 [[grabbed]] creatures at no penalty to their movement."
  - name: "Psionic Conductor"
    desc: "When a non-minion Voiceless Talker within 5 of the hulking brain uses an ability with the Psionic keyword, they can do so as if they were in the hulking brain’s space."

# MINDKILLER

name: "MINDKILLER"
level: 6
roles:
  - TROOP
  - HEXER
ancestry:
  - Horror
  - Voiceless Talker
ev: 32
stamina: 140
immunities: psychic 6
speed: 6 (fly, hover)
size: 1M /
stability: 2
free_strike: 7
characteristics:
  - -1
  - +3
  - +2
  - +2
  - +0
actions:
  - name: "Killer Claws"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 11 damage
      <br />★ 12–16 17+ damage; A< 2 [[grabbed]]
      <br />✸ 17+ 21 damage; A< 3 [[grabbed]]"
  - name: "Concealing Strike"
    desc:
      "
      <br />**Keywords** Psionic, Ranged, Strike
      <br />**Distance** Ranged 5
      <br />**Target** 2 creatures
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 10 damage; R< 1 the mindkiller is invisible to the target (save ends)
      <br />★ 12–16 15 damage; R< 2 the mindkiller is invisible to the target (save ends)
      <br />✸ 17+ 18 damage; R< 3 the mindkiller is invisible to the target (save ends)"
maneuvers:
  - name: "Mindwipe"
    desc: "
      <br />**Keywords** Attack, Psionic
      <br />**Distance** Melee 1
      <br />**Target** 1 [[grabbed]] creature 
      <br />**Effect:** R< 2 The mindkiller drains one point from the target’s Reason, Intuition, or Presence score (Director’s choice) and adds it to their own score until the end of the encounter."
ta:
  - name: "Meat Shield"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** 1 [[grabbed]] creature 
      <br />**Trigger** The mindkiller takes damage 
      <br />**Effect:** The mindkiller halves the incoming damage. The target takes the other half of the damage. 
      <br />**3 Malice** The target takes the full damage in place of the mindkiller."
traits:
  - name: "Psionic Conductor"
    desc: "When a non-minion Voiceless Talker within 5 of the mindkiller uses an ability with the Psionic keyword, they can do so as if they were in the mindkiller’s space."
  - name: "Nimble"
    desc: "The mindkiller can move through other creatures and objects at normal speed."

# VOICELESS TALKER ARTILLERIST

name: "VOICELESS TALKER ARTILLERIST"
level: 6
roles:
  - ARTILLERY
  - TROOP
ancestry:
  - Horror
  - Voiceless Talker
ev: 32
stamina: 140
immunities: psychic 6
speed: 5 (teleport, hover)
size: 1M /
stability: 2
free_strike: 7
characteristics:
  - +0
  - +3
  - +1
  - +2
  - +1
actions:
  - name: "Psionic Rifle Burst"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Psionic, Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 11 damage
      <br />★ 12–16 19 damage; spread 1
      <br />✸ 17+ 22 damage; spread 2 
      <br />**Effect:** The blast hits nearby targets, dealing 3 damage to each enemy within a number of squares of the target equal to the result’s spread value. 
      <br />**2 Malice** The attack deals an additional 3 damage to each enemy within the spread distance"
  - name: "Mind Jolt"
    desc:
      "
      <br />**Keywords** Area, Psionic
      <br />**Distance** 1 × 10 line within 10
      <br />**Target** All enemies
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 lightning damage
      <br />★ 12–16 10 lightning damage; I< 2 [[slowed]] (save ends)
      <br />✸ 17+ 13 lightning damage; I< 3 [[slowed]] (save ends)"
maneuvers:
  - name: "In Our Sights"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature 
      <br />**Effect:** The next power roll with the psionic keyword made against the target will automatically be a 17+ until the start of the artillerist’s next turn."
ta:
  - name: "Tactical Reposition
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The artillerist takes damage. 
      <br />**Effect:** The artillerist teleports 5 and doesn’t suffer any additional effects associated with the damage."
traits:
  - name: "Psionic Conductor"
    desc: "When a non-minion Voiceless Talker within 5 of the artillerist uses an ability with the Psionic keyword, they can do so as if they were in the artillerist’s space."
  - name: "Locked On"
    desc: "The artillerist ignores invisibility, cover, and concealment. A creature can’t hide from the artillerist while the artillerist has [[Draw Steel Rules#LINE OF EFFECT|line of effect]] to them."

# VOICELESS TALKER INVADER

name: "VOICELESS TALKER INVADER"
level: 6
roles:
  - TROOP
  - CONTROLLER
ancestry:
  - Horror
  - Voiceless Talker
ev: 32
stamina: 140
immunities: psychic 6
speed: 5 (teleport, hover)
size: 1M /
stability: 2
free_strike: 7
characteristics:
  - -1
  - +1
  - +3
  - +2
  - +2
actions:
  - name: "Tentacle"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 damage
      <br />★ 12–16 15 damage; M< 2 [[grabbed]]
      <br />✸ 17+ 18 damage; M< 3 [[grabbed]]"
  - name: "Psionic Boom"
    desc:
      "
      <br />**Keywords** Area, Psionic
      <br />**Distance** 3 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 psychic damage; R< 1 push 2
      <br />★ 12–16 10 psychic damage; R< 2 push 3
      <br />✸ 17+ 12 psychic damage; R< 3 push 4 and [[prone]] 
      <br />**2 Malice** The area of the burst increases to 5."
maneuvers:
  - name: "Tentacle Toss"
    desc: "
      <br />**Keywords** Melee, Psionic
      <br />**Distance** Melee 1
      <br />**Target** 1 [[grabbed]] creature
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 damage; vertical slide 2
      <br />★ 12–16 10 damage; vertical slide 3
      <br />✸ 17+ 12 damage; vertical slide 5"
ta:
  - name: "Brain Drain"
    desc: "
      <br />**Keywords** Psionic
      <br />**Distance** Melee 1
      <br />**Target** 1 creature [[grabbed]] by the invader 
      <br />**Trigger** The target resists an ability’s effect. 
      <br />**Effect:** The potency of the effect increases by 2."
traits:
  - name: "Psionic Amplifier"
    desc: "When a non-minion Voiceless Talker within 5 of the invader uses an ability with the Psionic keyword, they can do so with a double edge and as if they were in the invader’s space."

# VOICELESS TALKER EVOLUTIONIST

name: "VOICELESS TALKER EVOLUTIONIST"
level: 6
roles:
  - LEADER
ancestry:
  - Horror
  - Voiceless Talker
ev: 32
stamina: 180
immunities: psychic 8
speed: 5 (teleport, hover)
size: 1M /
stability: 3
free_strike: 7
characteristics:
  - +0
  - +3
  - +4
  - +1
  - +2
actions:
  - name: "Psionic Intrusion"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Psionic, Ranged, Strike
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 psychic damage; R< 2 [[slowed]] (save ends)
      <br />★ 12–16 16 psychic damage; R< 3 [[slowed]] (save ends)
      <br />✸ 17+ 19 psychic damage; R< 4 [[slowed]] (save ends)"
maneuvers:
  - name: "Carpe Quadratum"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The evolutionist teleports, swapping places with one creature within 5."
ta:
  - name: "Adaptability"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The evolutionist takes typed damage. 
      <br />**Effect:** The evolutionist gains immunity 5 to the triggering type of damage until the start of their next turn. 
traits:
  - name: "End Effect"
    desc: "At the end of their turn, the evolutionist can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Witness Evolutionary Superiority"
    desc: "The evolutionist has the first listed trait of every minion in their squad."
va:
  - name: "Show Me Who You Are (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Psionic
      <br />**Distance** 5 burst
      <br />**Target** All enemies 
      <br />**Effect:** Each target makes a Might test.
      <br />`dice: 2d10 + 4`
      <br />✸ ≤11 Target uses a Signature action against the nearest enemy within distance.
      <br />★ 12–16 Target makes a free strike against the nearest enemy within distance.
      <br />✦ 17+ [[frightened]] (save ends)."
  - name: "Release the Thralls (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 5
      <br />**Target** Special 
      <br />**Effect:** The evolutionist teleports 3 minions of level 4 or lower into unoccupied squares within distance. All three minions can be from any monster type but must share the same name."
  - name: "Brainstorm (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Psionic
      <br />**Distance** 3 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 7 lightning damage
      <br />★ 12–16 12 lightning damage
      <br />✸ 17+ 15 lightning damage 
      <br />**Effect:** The evolutionist is surrounded by a psionic electrical storm until the end of the encounter. The area within 5 of them is considered difficult terrain for enemies. An enemy who enters an affected square for the first time on their turn or starts their turn in it takes 8 lightning damage."

# LORD SYUUL

name: "LORD SYUUL"
level: 6
roles:
  - SOLO
ancestry:
  - Horror
  - Voiceless Talker
ev: 80
stamina: 450
immunities: psychic 10
speed: 7 (teleport, hover)
size: 1M /
stability: 3
free_strike: 7
characteristics:
  - +1
  - +3
  - +4
  - +4
  - +3
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** Lord Syuul takes up to two turns each round. He can’t take turns consecutively. He can use two actions on each of his turns. While [[dazed]], he can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of his turn, Lord Syuul can take 10 damage to end one save ends effect affecting him. This damage can’t be reduced in any way."
  - name: "Mind Over Manners"
    desc: "When Lord Syuul uses an ability with the Psionic keyword, he can do so as if he were in the space of any creature within [[Draw Steel Rules#LINE OF EFFECT|line of effect]] he has observed using an ability with the Psionic keyword."
actions:
  - name: "Tentacle Grab"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 damage; A< 2 [[grabbed]]
      <br />★ 12–16 17+ damage; A< 3 [[grabbed]]
      <br />✸ 17+ 20 damage; A< 4 [[grabbed]] 
      <br />**2 **Malice** The distance of this ability increases to Melee 10. Each target [[grabbed]] by Lord Syuul is immediately pulled 10."
  - name: "Dampening Grenade"
    desc:
      "
      <br />**Keywords** Area, Psionic, Ranged
      <br />**Distance** 2 cube within 5
      <br />**Target** All enemies 
      <br />**Effect:** All psionic or magical abilities within the affected area have a double bane. All tests against psionic or magical effects within this area have a double edge.
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 6 damage; effect ends after 2 turns.
      <br />★ 12–16 10 damage; effect ends after 1 round.
      <br />✸ 17+ 13 damage; effect ends with the encounter."
  - name: "Mind Blown"
    desc:
      "
      <br />**Keywords** Melee, Psionic, Strike
      <br />**Distance** Melee 1
      <br />**Target** One [[grabbed]] enemy
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 12 damage
      <br />★ 12–16 20 damage
      <br />✸ 17+ 24 damage 
      <br />**Effect:** If this action reduces the target to 0 stamina and they have a brain, their brain explodes, instantly killing them."
maneuvers:
  - name: "You Come With Me"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Lord Syuul teleports 5 along with each creature and object he has [[grabbed]]. He can release them as part of this maneuver."
ta:
  - name: "Adaptability"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** Lord Syuul takes typed damage. 
      <br />**Effect:** Lord Syuul gains immunity 5 to the triggering type of damage until the start of his next turn."
va:
  - name: "See Only Me (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Psionic
      <br />**Distance** 10 burst
      <br />**Target** All enemies 
      <br />**Effect:** Each target makes a Might test.
      <br />`dice: 2d10 +
      <br />✸ ≤11 16 psychic damage; can’t establish [[Draw Steel Rules#LINE OF EFFECT|line of effect]] to creatures besides Lord Syuul, and strikes targeting Lord Syuul have a bane (save ends)
      <br />★ 12–16 13 psychic damage; can’t establish [[Draw Steel Rules#LINE OF EFFECT|line of effect]] to creatures besides Lord Syuul (save ends)
      <br />✦ 17+ 7 psychic damage"
  - name: "Phantom Pain (Villain Action 2)"
    desc: "
      <br />**Keywords** Psionic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Lord Syuul teleports up to 10 and projects an illusory double within 10. The double can’t move or act, but Lord Syuul can use psionic abilities as if he were in its space. When a creature touches or damages the double with a melee strike, they take 10 psionic damage. The double disappears when Lord Syuul takes damage."
  - name: "Mindshatter (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Psionic
      <br />**Distance** 5 Burst
      <br />**Target** All creatures
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 7 psychic damage
      <br />★ 12–16 13 psychic damage
      <br />✸ 17+ 16 psychic damage 
      <br />**Effect:** Each target gains damage weakness 3 until the end of the encounter."

# WAR DOG COMMANDO

name: "WAR DOG COMMANDO"
level: 1
roles:
  - MINION
  - AMBUSHER
ancestry:
  - Humanoid
  - War
  - Dog
ev: 3 for eight minions
stamina: 4
speed: 5
size: 1M /
stability: 0
with-captain: Strike damage +1
free_strike: 2
characteristics:
  - +0
  - +2
  - +0
  - +0
  - +0
actions:
  - name: "Daggers"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** One creature per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage 
      <br />**Effect:** The commando can use the Hide maneuver, even if observed."
traits:
  - name: "Loyalty Collar"
    desc: "When the commando dies, they explode, dealing 1d6 damage to each adjacent enemy."

# WAR DOG CONSCRIPT

name: "WAR DOG CONSCRIPT"
level: 1
roles:
  - MINION
  - HARRIER
ancestry:
  - Humanoid
  - War
  - Dog
ev: 3 for eight minions
stamina: 4
speed: 7
size: 1M /
stability: 0
with-captain: Strike damage +1
free_strike: 1
characteristics:
  - +2
  - +0
  - +0
  - +0
  - +0
actions:
  - name: "Blade"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** One creature per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage
      <br />★ 12–16 2 damage
      <br />✸ 17+ 3 damage 
      <br />**Effect:** This ability has an edge if it’s used while charging."
traits:
  - name: "Loyalty Collar"
    desc: "When the conscript dies, they explode, dealing 1d6 damage to each adjacent enemy."


# WAR DOG SHARPSHOOTER

name: "WAR DOG SHARPSHOOTER"
level: 1
roles:
  - MINION
  - ARTILLERY
ancestry:
  - Humanoid
  - War
  - Dog
ev: 3 for eight minions
stamina: 3
speed: 7
size: 1M /
stability: 0
with-captain: Ranged distance +5
free_strike: 2
characteristics:
  - +0
  - +2
  - +0
  - +0
  - +0
actions:
  - name: "Bolt Launcher"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 5
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage 
      <br />**Effect:** This ability ignores cover and concealment."
traits:
  - name: "Loyalty Collar"
    desc: "When the sharpshooter dies, they explode, dealing 1d6 damage to each adjacent enemy."


# WAR DOG TETHERITE

name: "WAR DOG TETHERITE"
level: 1
roles:
  - MINION
  - BRUTE
ancestry:
  - Humanoid
  - War
  - Dog
ev: 3 for eight minions
stamina: 5
speed: 5
size: 1M /
stability: 1
with-captain: Edge on strikes
free_strike: 2
characteristics:
  - +2
  - +0
  - +0
  - +0
  - +0
actions:
  - name: "Banded Dagger"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage"
traits:
  - name: "Tethered"
    desc: "A captain attached to a tetherite squad has their stability increased by the number of tetherites within 2 squares of them."
  - name: "Loyalty Collar"
    desc: "When the tetherite dies, they explode, dealing 1d6 damage to each adjacent enemy."


# WAR DOG AMALGAMITE

name: "WAR DOG AMALGAMITE"
level: 2
roles:
  - BAND
  - BRUTE
ancestry:
  - Humanoid
  - War
  - Dog
ev: 4
stamina: 25
speed: 5
size: 2 /
stability: 2
free_strike: 3
characteristics:
  - +2
  - +0
  - +0
  - +0
  - +0
actions:
  - name: "Several Arms"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 5 damage; A< 1 [[grabbed]]
      <br />✸ 17+ 6 damage; A< 2 [[grabbed]] 
      <br />**Effect:** The amalgamite can have up to four targets [[grabbed]]. 
      <br />**3 Malice** The amalgamite deals an additional 3 damage to each creature they have [[grabbed]] and regains stamina equal to the damage dealt."
maneuvers:
  - name: "Posthumous Promotion"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One war dog with a loyalty collar 
      <br />**Effect:** The target’s loyalty collar detonates, killing them instantly."
traits:
  - name: "Loyalty Collar"
    desc: "When the amalgamite dies, they explode, dealing 1d6 damage to each adjacent enemy."


# WAR DOG CRUCIBITE

name: "WAR DOG CRUCIBITE"
level: 1
roles:
  - BAND
  - ARTILLERY
ancestry:
  - Humanoid
  - War
  - Dog
ev: 3
stamina: 10
immunities: Fire 2
speed: 5
size: 1M /
stability: 0
free_strike: 2
characteristics:
  - +0
  - +2
  - +0
  - +0
  - +0
actions:
  - name: "Flamebelcher"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Weapon
      <br />**Distance** 5 × 1 line within 1
      <br />**Target** All creatures and objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 fire damage
      <br />★ 12–16 4 fire damage
      <br />✸ 17+ 5 fire damage 
      <br />**Effect:** The area is covered in sticky fire until the start of the crucibite’s next turn. Whenever a creature enters the area for the first time in a round or starts their turn there, they take 2 fire damage. 
      <br />**3 Malice** The area increases to a 10 × 1 line, and if any ally of the crucibite is in the area when it is created, the crucibite deals an additional 2 damage to each target.
maneuvers:
  - name: "Posthumous Promotion"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One war dog with a loyalty collar 
      <br />**Effect:** The target’s loyalty collar detonates, killing them instantly."
traits:
  - name: "Loyalty Collar"
    desc: "When the crucibite dies, they explode, dealing 1d6 damage to each adjacent enemy."


# WAR DOG EVISCERITE

name: "WAR DOG EVISCERITE"
level: 1
roles:
  - BAND
  - HARRIER
ancestry:
  - Humanoid
  - War
  - Dog
ev: 3
stamina: 15
speed: 7
size: 1M /
stability: 0
free_strike: 1
characteristics:
  - +1
  - +2
  - +0
  - +0
  - +0
actions:
  - name: "Chainsaw Whip"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 4 damage; pull 1
      <br />✸ 17+ 5 damage; pull 2 
      <br />**Effect:** The eviscerite can grab a target pulled adjacent to them by this ability."
maneuvers:
  - name: "Posthumous Promotion"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One war dog with a loyalty collar 
      <br />**Effect:** The target’s loyalty collar detonates, killing them instantly."
traits:
  - name: "Loyalty Collar"
    desc: "When the eviscerite dies, they explode, dealing 1d6 damage to each adjacent enemy."


# WAR DOG NEURONITE

name: "WAR DOG NEURONITE"
level: 1
roles:
  - BAND
  - DEFENDER
ancestry:
  - Humanoid
  - War
  - Dog
ev: 3
stamina: 20
immunities: Psychic 2
speed: 5 (fly)
size: 1M /
stability: 0
free_strike: 1
characteristics:
  - +0
  - +1
  - +0
  - +0
  - +2
actions:
  - name: "Synlirii Grafts"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Psionic
      <br />**Distance** 1 burst
      <br />**Target** Each enemy in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 psychic damage; vertical slide 1
      <br />★ 12–16 2 psychic damage; vertical slide 2
      <br />✸ 17+ 3 psychic damage; vertical slide 3"
maneuvers:
  - name: "Posthumous Promotion"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One war dog with a loyalty collar 
      <br />**Effect:** The target’s loyalty collar detonates, killing them instantly."
  - name: "The Voice"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Area, Psionic
      <br />**Distance** 5 burst
      <br />**Target** Each enemy in the burst 
      <br />**Effect:** The neuronite chooses an ally within 10 squares, then chooses whether each target is [[taunted]] by the ally or the ally has damage immunity 3 whenever they’re attacked by a target until the start of the neuronite’s next turn."
traits:
  - name: "Loyalty Collar"
    desc: "When the neuronite dies, they explode, dealing 1d6 damage to each adjacent enemy."


# WAR DOG PESTILITE

name: "WAR DOG PESTILITE"
level: 3
roles:
  - BAND
  - CONTROLLER
ancestry:
  - Humanoid
  - War
  - Dog
ev: 5
stamina: 20
immunities: Poison 3
speed: 5
size: 1M /
stability: 0
free_strike: 2
characteristics:
  - +0
  - +1
  - +0
  - +0
  - +2
actions:
  - name: "Plaguecaster"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 3 cube within 10
      <br />**Target** Each creature in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 poison damage; I< 0 [[frightened]] (save ends)
      <br />★ 12–16 4 poison damage; I< 1 [[frightened]] (save ends)
      <br />✸ 17+ 5 poison damage; I< 2 [[frightened]] (save ends) 
      <br />**Effect:** The area is covered in a cloud of pestilence that lasts until the start of the pestilite’s next turn. Any creature who enters the area for the first time in a round or starts their turn there takes 2 poison damage."
maneuvers:
  - name: "Posthumous Promotion"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One war dog with a loyalty collar 
      <br />**Effect:** The target’s loyalty collar detonates, killing them instantly."
traits:
  - name: "Loyalty Collar"
    desc: "When the pestilite dies, they explode, dealing 1d6 damage to each adjacent enemy."


# WAR DOG PORTALITE

name: "WAR DOG PORTALITE"
level: 1
roles:
  - BAND
  - AMBUSHER
ancestry:
  - Humanoid
  - War
  - Dog
ev: 3
stamina: 15
speed: 5 (teleport)
size: 1M/
stability: 0
free_strike: 2
characteristics:
  - +0
  - +2
  - +0
  - +0
  - +0
actions:
  - name: "Corrupted Ash Daggers"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage; slide 1
      <br />★ 12–16 6 damage; slide 2
      <br />✸ 17+ 7 damage; slide 3 
      <br />**Effect:** The portalite has an edge on this ability if an ally is adjacent to the target. 
      <br />**1 Malice** The portalite teleports the target 3 squares before sliding them."
maneuvers:
  - name: "Posthumous Promotion"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One war dog with a loyalty collar 
      <br />**Effect:** The target’s loyalty collar detonates, killing them instantly."
  - name: "Corrupted Ash Teleport
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Magic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The portalite teleports up to 5 squares and has an edge on strikes until the end of their turn."
traits:
  - name: "Loyalty Collar"
    desc: "When the portalite dies, they explode, dealing 1d6 damage to each adjacent enemy."


# WAR DOG SUBCOMMANDER

name: "WAR DOG SUBCOMMANDER"
level: 2
roles:
  - BAND
  - SUPPORT
ancestry:
  - Humanoid
  - War
  - Dog
ev: 4
stamina: 20
speed: 5
size: 1M /
stability: 0
free_strike: 2
characteristics:
  - +2
  - +0
  - +0
  - +0
  - +1
actions:
  - name: "Command Saber"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 5 damage
      <br />✸ 17+ 7 damage 
      <br />**Effect:** An ally within 5 squares of the subcommander can make a free strike against the target."
maneuvers:
  - name: "Posthumous Promotion"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One war dog with a loyalty collar 
      <br />**Effect:** The target’s loyalty collar detonates, killing them instantly."
traits:
  - name: "The Iron Saint Does Not Recognize Retreat"
    desc: "Each ally within 5 squares of the subcommander adds 3 to their stability."
  - name: "Loyalty Collar"
    desc: "When the subcommander dies, they explode, dealing 1d6 damage to each adjacent enemy."


# WAR DOG GROUND COMMANDER

name: "WAR DOG GROUND COMMANDER"
level: 3
roles:
  - LEADER
ancestry:
  - Humanoid
  - War
  - Dog
ev: 20
stamina: 120
speed: 5
size: 1M /
stability: 2
free_strike: 5
characteristics:
  - +3
  - +2
  - +3
  - +2
  - +2
actions:
  - name: "Conditioning Spear"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; pull 1
      <br />★ 12–16 12 damage; pull 2
      <br />✸ 17+ 15 damage; pull 3 
      <br />**Effect:** One ally within 10 squares of the commander can make a free strike. 
      <br />**1 Malice** A target who is adjacent to the ground commander after this ability is resolved is I< 2 [[grabbed]] (save ends). This grab can’t be escaped using the Escape Grab maneuver. The ground commander can grab up to two creatures at a time."
maneuvers:
  - name: "Highest Posthumous Promotion"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 10 burst
      <br />**Target** Each war dog with a loyalty collar 
      <br />**Effect:** The ground commander selects any number of targets’ loyalty collars and detonates them, killing the target instantly."
ta:
  - name: "Final Orders"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One ally 
      <br />**Trigger** The target has a condition imposed on them, is force moved, or is killed. 
      <br />**Effect:** The target can move up to their speed and make a free strike before the triggering effect happens."
traits:
  - name: "End Effect"
    desc: "At the end of their turn, the ground commander can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Loyalty Collar"
    desc: "When the ground commander dies, they explode, dealing 2d6 damage to each adjacent enemy."
va:
  - name: "Combined Arms (Villain Action 1)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 10 burst
      <br />**Target** Each ally 
      <br />**Effect:** Each target can make a ranged free strike, then immediately use the Charge action."
  - name: "Make an Example of Them (Villain Action 2)"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One enemy 
      <br />**Effect:** Each ally within 5 squares of the target can move up to their speed and make a free strike against the target. The target is then I< 2 [[frightened]] of the ground commander (save ends)."
  - name: "Claim Them for the Body Banks (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 10 burst
      <br />**Target** Each ally 
      <br />**Effect:** Each target can shift 2 and use the Grab maneuver. For the rest of the encounter, each enemy has a bane on escaping grabs."


# WAR DOG SPARKSLINGER

name: "WAR DOG SPARKSLINGER"
level: 4
roles:
  - MINION
  - ARTILLERY
ancestry:
  - Humanoid
  - War
  - Dog
ev: 6 for eight minions
stamina: 7
immunities: lightning 4
speed: 5
size: 1M /
stability: 0
with-captain: Spread +1
free_strike: 3
characteristics:
  - +0
  - +0
  - +3
  - +0
  - +2
actions:
  - name: "Galvanic Arc"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Strike, Ranged
      <br />**Distance** Ranged 7
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 lightning damage
      <br />★ 12–16 5 lightning damage; spread 1
      <br />✸ 17+ 7 lightning damage; spread 2 
      <br />**Effect:** The lightning arcs to nearby targets, dealing 2 damage to each enemy within a number of squares of the target equal to the result’s spread value."
traits:
  - name: "Loyalty Collar"
    desc: "When the sparkslinger dies, they explode, dealing 1d6 damage to each adjacent enemy."

# WAR DOG SWEEPER

name: "WAR DOG SWEEPER"
level: 4
roles:
  - MINION
  - HARRIER
ancestry:
  - Humanoid
  - War
  - Dog
ev: 6 for eight minions
stamina: 8
speed: 6
size: 1M /
stability: 0
with-captain: Edge on strikes
free_strike: 2
characteristics:
  - +0
  - +3
  - +0
  - +2
  - +0
actions:
  - name: "Shrikegun Shot"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 3
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage; push 1
      <br />✸ 17+ 6 damage; push 3
      <br />**Effect:** This ability deals an additional 3 damage if the target is within 2 squares of the sweeper."
traits:
  - name: "Shrapnel-Laced Loyalty Collar"
    desc: "When the sweeper dies, they explode, dealing 1d6 damage to each enemy within 2 squares of them."

# WAR DOG WAR FROG

name: "WAR DOG WAR FROG"
level: 4
roles:
  - MINION
  - AMBUSHER
ancestry:
  - Humanoid
  - War
  - Dog
ev: 6 for eight minions
stamina: 8
immunities: Poison 4
speed: 5 (swim, climb)
size: 1S /
stability: 0
with-captain:
speed: +2
free_strike: 3
characteristics:
  - -1
  - +3
  - +0
  - +2
  - +0
actions:
  - name: "Poisoned Dagger"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Attack, Melee, Ranged, Weapon
      <br />**Distance** Melee 1 or Ranged 4
      <br />**Target** One creature per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 poison damage
      <br />★ 12–16 5 poison damage
      <br />✸ 17+ 7 poison damage 
      <br />**Effect:** The war frog jumps 3 squares before or after making their attack. If the war frog lands in cover or concealment, they can take the Hide maneuver as part of this ability."
traits:
  - name: "Loyalty Collar"
    desc: "When the war frog dies, they explode, dealing 1d6 damage to each adjacent enemy."

# WAR DOG ARACHNITE

name: "WAR DOG ARACHNITE"
level: 6
roles:
  - BAND
  - ARTILLERY
ancestry:
  - Humanoid
  - War
  - Dog
ev: 8
stamina: 35
immunities: psychic 6
speed: 5 (climb)
size: 1L /
stability: 0
free_strike: 4
characteristics:
  - +0
  - +3
  - +2
  - +2
  - +1
actions:
  - name: "Longarm Shrikegun"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 15
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 special damage
      <br />★ 12–16 9 special damage
      <br />✸ 17+ 11 special damage; A< 3 [[bleeding]] (save ends) 
      <br />**Effect:** This ability ignores cover and concealment. The arachnite chooses one of the following damage types when making the attack: acid, cold, fire, lightning, poison, psychic, or sonic. 
      <br />**2 Malice** The arachnite can use this ability as if they were occupying the space of an ally within distance."
maneuvers:
  - name: "Web Vial"
    desc: "
      <br />**Keywords** Area, Ranged
      <br />**Distance** 2 Cube within 10
      <br />**Target** Special 
      <br />**Effect:** The affected area becomes difficult terrain."
traits:
  - name: "Eight-Eyed Sight"
    desc: "The arachnite automatically finds all hidden creatures within 10 at the start of their turn."
  - name: "Loyalty Collar"
    desc: "When the arachnite dies, they explode, dealing 2d6 damage to each adjacent enemy."


# WAR DOG DOOMTHIEF

name: "WAR DOG DOOMTHIEF"
level: 5
roles:
  - BAND
  - DEFENDER
ancestry:
  - Humanoid
  - War
  - Dog
ev: 7
stamina: 40
speed: 5
size: 1L /
stability: 2
free_strike: 3
characteristics:
  - +3
  - -1
  - +0
  - +3
  - +1
actions:
  - name: "Ripper Shrikegun"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Weapon
      <br />**Distance** 10 x 3 line within 1
      <br />**Target** all enemies
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 3 damage; push 1
      <br />★ 12  -16 5 damage; push 3
      <br />✦ 17+ 6 damage; push 5; A< 3 [[slowed]] (save ends) 
      <br />**Effect:** The doomthief cannot move on the same turn they use this ability."
traits:
  - name: "Doom Magnet"
    desc: "The doomthief emits a 3 aura of warped fate, blocking [[Draw Steel Rules#LINE OF EFFECT|line of effect]] for enemy abilities that don’t include the doomthief as a target."
  - name: "Loyalty Collar"
    desc: "When the doomthief dies, they explode, dealing 2d6 damage to each adjacent enemy."
maneuvers:
  - name: "Expanding Doom"
    desc: "
      <br />**Cost** 4 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The doomthief gains damage immunity 4 and their doom magnet aura increases by 3 until the start of their next turn."


# WAR DOG EQUIVITE

name: "WAR DOG EQUIVITE"
level: 4
roles:
  - BAND
  - BRUTE
ancestry:
  - War
  - Dog
ev: 6
stamina: 53
speed: 8
size: 2 /
stability: 2
free_strike: 3
characteristics:
  - +3
  - +3
  - -1
  - -2
  - +0
actions:
  - name: "Fuse-Iron Lance"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 8 damage
      <br />✸ 17+ 10 damage; I< 3 [[frightened]] (save ends) 
      <br />**Effect:** The equivite has an edge on this ability while charging. 
      <br />**2 Malice** The ability deals an additional 3 fire damage to the target and each enemy adjacent to the target."
maneuvers:
  - name: "Blazing Charge"
    desc: "
      <br />**Keywords** Melee, Weapon
      <br />**Distance** Special
      <br />**Target** Special 
      <br />**Effect:** The equivite moves up to their speed and can move through enemies and objects at normal speed. They make one power roll total against each enemy and object they pass through.
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 2 damage; push 1
      <br />★ 12–16 4 damage; push 2
      <br />✸ 17+ 5 damage; push 3; M< 3 [[prone]]"
traits:
  - name: "Loyalty Collar"
    desc: "When the equivite dies, they explode, dealing 2d6 damage to each adjacent enemy."

# WAR DOG HYPOKRITE

name: "WAR DOG HYPOKRITE"
level: 4
roles:
  - BAND
  - AMBUSHER
ancestry:
  - Humanoid
  - War
  - Dog
ev: 6
stamina: 30
speed: 8
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - +1
  - +3
  - +0
  - +0
  - +2
actions:
  - name: "Needle-Knife"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 8 damage; A< 2 [[bleeding]] (save ends)
      <br />✸ 17+ 10 damage; A< 3 [[bleeding]] and [[weakened]] (save ends) 
      <br />**Effect:** This ability deals an additional 6 damage if the hypocrite is hidden or disguised."
ta:
  - name: "Feign Death"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** Ranged 20
      <br />**Target** Self 
      <br />**Trigger** The hypokrite takes damage. 
      <br />**Effect:** The hypokrite activates their Loyalty Collar ability and teleports to an unoccupied square adjacent to an ally within distance alive.
traits:
  - name: "Face in the Crowd"
    desc: "The hypokrite is invisible while adjacent to an unhidden ally. When using the Hide maneuver, the hypocrite can choose to disguise themself as another creature within [[Draw Steel Rules#LINE OF EFFECT|line of effect]]."
  - name: "Loyalty Collar"
    desc: "When the hypokrite dies, they explode, dealing 2d6 damage to each adjacent enemy."

# WAR DOG MISCHIEVITE

name: "WAR DOG MISCHIEVITE"
level: 5
roles:
  - BAND
  - HARRIER
ancestry:
  - Humanoid
  - War
  - Dog
ev: 7
stamina: 35
speed: 6
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - +1
  - +3
  - +0
  - +2
  - +0
actions:
  - name: "Fuse-Iron Knives"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** 2 creatures
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 7 damage
      <br />✸ 17+ 8 damage; R< 3 dazzled (save ends) 
      <br />**Effect:** A dazzled creature has a bane on strikes and can’t have [[Draw Steel Rules#LINE OF EFFECT|line of effect]] to targets who aren’t adjacent to them."
maneuvers:
  - name: "Misdirection"
    desc: "
      <br />**Keywords**   -  -
      <br />**Distance** Ranged 3
      <br />**Target** 1 ally or dazzled creature 
      <br />**Effect:** The mischievite swaps positions with the target. An ally targeted by this ability can make a free strike either before or after being swapped. 
      <br />**2 Malice** The mischievite may use this ability as a triggered action when targeted by a strike or ability. The swapped target becomes the new target of the triggering strike or ability."
traits:
  - name: "Crafty"
    desc: "The mischievite’s movement does not trigger opportunity attacks."
  - name: "Loyalty Collar"
    desc: "When the mischievite dies, they explode, dealing 2d6 damage to each adjacent enemy."

# WAR DOG THANATITE

name: "WAR DOG THANATITE"
level: 6
roles:
  - BAND
  - CONTROLLER
ancestry:
  - Humanoid
  - War
  - Dog
ev: 8
stamina: 35
speed: 5
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - +1
  - +1
  - +2
  - +3
  - +1
actions:
  - name: "Snaking Entrails"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** 1 ally 
      <br />**Effect:** The target dies. The thanatite makes one power roll against each enemy within 2 of the target:
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 corruption damage; A< 1 [[slowed]] (save ends)
      <br />★ 12–16 5 corruption damage; A< 2 [[slowed]] (save ends)
      <br />✸ 17+ 7 corruption damage; A< 3 [[restrained]] (save ends) 
      <br />**3 Malice** If an affected enemy is adjacent to a corpse, they are [[frightened]] of the thanatite (save ends)."
maneuvers:
  - name: "Wall of Flesh"
    desc: "
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 10 wall within 10
      <br />**Target** One corpse 
      <br />**Effect:** The target is molded into a wall of blood and bone. The wall must share at least one square with the target. Each enemy within the affected area vertical slides 2 and is knocked [[prone]]. Each square of wall has 3 stamina."
traits:
  - name: "Loyalty Collar"
    desc: "When the thanatite dies, they explode, dealing 2d6 damage to each adjacent enemy."

# WAR DOG TORMENTITE

name: "WAR DOG TORMENTITE"
level: 5
roles:
  - BAND
  - HEXER
ancestry:
  - Humanoid
  - War
  - Dog
ev: 7
stamina: 30
speed: 5
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - +0
  - +0
  - +2
  - +3
  - +0
actions:
  - name: "Mark of Agony"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 corruption damage
      <br />★ 12–16 8 corruption damage; marked (save ends)
      <br />✸ 17+ 9 corruption damage; marked (save ends) 
      <br />**Effect:** Strikes against marked targets have an edge. Whenever the tormentite takes damage, each marked target takes 3 damage."
  - name: "Vortex of Pain"
    desc:
      "
      <br />**Keywords** Area, Magic
      <br />**Distance** 4 cube within 10
      <br />**Target** All enemies
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 2 corruption damage
      <br />★ 12–16 4 corruption damage
      <br />✸ 17+ 5 corruption damage; an ally within the affected area can end one save ends effect affecting them and give it to a target. 
      <br />**Effect:** The tormentite regains 2 stamina per target of this ability."
traits:
  - name: "Persistent Pain" 
    desc: "The tormentite takes 1 damage at the start of each of their turns."
  - name: "Loyalty Collar"
    desc: "When the tormentite dies, they explode, dealing 2d6 damage to each adjacent enemy."

# WAR DOG WAR DOC

name: "WAR DOG WAR DOC"
level: 5
roles:
  - BAND
  - SUPPORT
ancestry:
  - Humanoid
  - War
  - Dog
ev: 7
stamina: 35
speed: 5
size: 1L /
stability: 1
free_strike: 3
characteristics:
  - +0
  - +1
  - +3
  - +2
  - +0
actions:
  - name: "Syringe Crossbow"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** One creature
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 poison damage
      <br />★ 12–16 8 poison damage
      <br />✸ 17+ 9 poison damage; M< 3 [[weakened]] (save ends) 
      <br />**Effect:** An ally targeted by this ability gains 5 temporary stamina and makes a free strike instead of taking damage."
ta:
  - name: "Sanguine Stimulants"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Ranged 15
      <br />**Target** One war dog ally 
      <br />**Trigger** The target dies 
      <br />**Effect:** Each ally adjacent to the target deals an additional 6 damage on their next strike."
maneuvers:
  - name: "Posthumous Promotion"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One war dog with a loyalty collar 
      <br />**Effect:** The target’s loyalty collar detonates, killing them instantly."
traits:
  - name: "Body Bank Branch Manager"
    desc: "The Reconstitute Malice effect costs 1 malice fewer. Each ally may treat the war doc as a source of corpses for the purposes of using Reconstitute."

# WAR DOG TETRARCH

name: "WAR DOG TETRARCH"
level: 6
roles:
  - LEADER
ancestry:
  - Humanoid
  - War
  - Dog
ev: 32
stamina: 180
speed: 7
size: 1M /
stability: 2
free_strike: 7
characteristics:
  - +4
  - +3
  - +2
  - +3
  - +4
actions:
  - name: "Houndblade"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 3
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 damage
      <br />★ 12–16 16 damage; [[taunted]] (EoT)
      <br />✸ 17+ 19 damage; [[taunted]] (EoT) 
      <br />**Effect:** A creature [[taunted]] by this ability has a bane on strikes. 
      <br />**3 Malice** Each target loses 1d3 Recoveries."
maneuvers:
  - name: "Get them, you dolts!"
    desc: "
      <br />**Cost** 1 Malice per target
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** Up to three creatures 
      <br />**Effect:** The target shifts up to their speed and makes a free strike. The target deals an additional 4 damage if they strike a [[taunted]] enemy."
ta:
  - name: "Sneering Disregard"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Triggering creature 
      <br />**Trigger** A non  -[[taunted]] creature targets the tetrarch with a power roll. 
      <br />**Effect:** The tetrarch imposes a double bane on the power roll. If the target gets a tier-1 result, the tetrarch ignores any additional effects of the ability, and the target is [[frightened]] of the tetrarch (save ends)."
traits:
  - name: "End Effect"
    desc: "At the end of their turn, the tetrarch can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Chosen of the Iron Saint"
    desc: "The Director gains 1 malice whenever an ally within 10 of the tetrarch gets a tier-3 result on an attack."
va:
  - name: "Enter the Fray (Villain Action 1)"
      <br />**Keywords** Area
      <br />**Distance** 2 burst
      <br />**Target** All enemies 
      <br />**Effect:** The tetrarch leaps 7 squares before using this action.
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 push 2; I< 2 [[frightened]] (save ends)
      <br />★ 12–16 push 4; I< 3 [[frightened]] (save ends)
      <br />✸ 17+ push 5; I< 4 [[frightened]] (save ends)"
  - name: "Lay Waste (Villain Action 2)"
      <br />**Keywords** Area, Weapon
      <br />**Distance** Five 2 cubes within 20
      <br />**Target** All creatures and objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 7 fire damage; A< 2 [[slowed]] (EoT)
      <br />★ 12–16 13 fire damage; A< 3 [[slowed]] (save ends)
      <br />✸ 17+ 16 fire damage; A< 4 [[slowed]] (save ends) 
      <br />**Effect:** The cubes are set ablaze. Until the end of the encounter, the affected area is considered difficult terrain, and a creature takes 2 fire damage for each affected square they enter."
  - name: "“You Would Dare?!” (Villain Action 3)"
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Until the end of the encounter, the tetrarch rallies themself, gains damage immunity 2, and their signature action now targets three creatures or objects."

# WEREWOLF

name: "WEREWOLF"
level: 1
roles:
  - SOLO
ancestry:
  - Accursed
  - Humanoid
  - Werebeast
ev: 30
stamina: 200
speed: 8
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - +3
  - +2
  - −1
  - +1
  - +1
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The werewolf takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the werewolf can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the werewolf can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Shapeshifter" The werewolf enters combat in their hybrid humanoid form. Their shape can’t change via any effects beyond their own ability."
  - name: "Ferocity"
    desc: "The werewolf’s abilities are capable of inflicting ferocity points on non-stormwight enemies. If a creature has 10 or more ferocity at the start of their turn, they spend all their ferocity and either make a free strike at the nearest creature or shift up to their speed towards the nearest creature and take a free strike. Non-stormwight creatures that take damage in this way gain 1 ferocity. All accumulated ferocity disappears after completing a respite."
  - name: "Vukenstep"
    desc: "The werewolf ignores difficult terrain."
actions:
  - name: "Accursed Bite"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage; 2 ferocity
      <br />★ 12–16 13 damage; 4 ferocity
      <br />✸ 17+ 16 damage; 5 ferocity 
      <br />**2 Malice** The target has P< 0 lycanthropy. The potency of this attack increases by 1 each time the werewolf forces the same target to resist it. 
      <br />**Effect:** A creature afflicted with lycanthropy accumulates 2 ferocity at the end of each of their turns whenever they’re in combat. Their ferocity does not disappear after completing a respite; they must complete the Find a Cure project to end this condition."
  - name: "Claws"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage
      <br />★ 12–16 11 damage; 1 ferocity; M< 2 push 3
      <br />✸ 17+ 14 damage; 3 ferocity; M< 3 vertical slide 3"
  - name: "Berserker Slash"
    desc:
      "<br />**Cost** 5 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The werewolf shifts up to their speed and uses Claws against each creature who comes within 1 of the werewolf during the move. The werewolf makes one power roll against all targets."
maneuvers:
  - name: "Wall Leap"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The werewolf jumps 4 squares. If they end this movement at a wall, the werewolf jumps off the wall 4 squares and makes a melee free strike."
ta:
  - name: "Facepalm and Head Slam"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** — 
      <br />**Trigger** The target targets the werewolf with a melee ability after charging or moving 3 or more squares in a straight line towards them.
      <br />**Distance** Melee 1
      <br />**Target** 1 creature 
      <br />**Effect:** The target is knocked [[prone]] and takes 5 damage before executing the ability."
va:
  - name: "Howl (Villain Action 1)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 5 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** Each target makes a Might test.
      <br />✸ ≤11
      <br />**Target** moves up to their speed away from the werewolf; [[frightened]] (save ends)
      <br />★ 12–16 [[frightened]] (EoT)
      <br />`dice: 2d10 +
      <br />✦ 17+ no effect 
      <br />**Effect:** Enemies that have 1 or more ferocity gain 4 ferocity and howl along with the werewolf."
  - name: "Full Wolf (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The werewolf changes into a massive wolf, pushing adjacent creatures out of their way and moving into a square that can accommodate their new size:. Until they die or the end of the encounter, their speed is 10, their size is 3, and their stability is 2. Each of the werewolf’s strikes deal an additional 3 damage and inflict an additional 1 ferocity. The potency of the werewolf’s Accursed Bite increases by 1."
  - name: "Rampage (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 2 burst
      <br />**Target** All creatures in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; 2 ferocity
      <br />★ 12–16 11 damage; 4 ferocity
      <br />✸ 17+ 14 damage; 8 ferocity; [[prone]] 
      <br />**Effect:** The werewolf shifts up to twice their speed either before or after using this ability."

# WYVERN LURKER

name: "WYVERN LURKER"
level: 4
roles:
  - TROOP
  - AMBUSHER
ancestry:
  - Beast
  - Wyvern
ev: 24
stamina: 120
immunities: Acid 5
speed: 9 (fly)
size: 2 /
stability: 2
free_strike: 6
characteristics:
  - +2
  - +3
  - -1
  - +1
  - 0
actions: 
  - name: "Agonizing Stinger"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage
      <br />★ 12–16 14 damage; M< 2 [[bleeding]] (save ends)
      <br />✸ 17+ 17+ damage; M< 3 [[bleeding]] (save ends) 
      <br />**1 Malice** The lurker deals an additional 6 acid damage to one target if they were hidden from them."
  - name: "Acidic Anguish"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 10 acid damage; M< 1 [[weakened]] (save ends)
      <br />★ 12–16 16 acid damage; M< 2 [[weakened]] (save ends)
      <br />✦ 17+ 20 acid damage; M< 3 [[weakened]] (save ends) 
      <br />**Effect:** A target [[weakened]] from this ability takes 1d4 acid damage at the start of each of their turns until the condition ends."
maneuvers:
  - name: "Swooping Torment"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The lurker flies up to their speed and hides. Each enemy that comes within 1 square of the lurker during this movement can choose to take 3 sonic damage or fall [[prone]]."
ta:
  - name: "Retaliatory Dive"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 5
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature deals damage to the lurker with a ranged ability. 
      <br />**Effect:** The lurker flies into a square adjacent to the target and makes a free strike against them."
traits:
  - name: "Ruthless Rage"
    desc: "The lurker deals an additional 3 damage on strikes while within 10 squares of another wyvern."
  - name: "Tenacious Hunter"
    desc: "Any creature suffering a condition inflicted by a wyvern can’t be hidden from the lurker."

# WYVERN PREDATOR

name: "WYVERN PREDATOR"
level: 4
roles:
  - TROOP
  - BRUTE
ancestry:
  - Beast
  - Wyvern
ev: 24
stamina: 140
immunities: Acid 5
speed: 7 (fly)
size: 3 /
stability: 3
free_strike: 6
characteristics:
  - +3
  - +2
  - -1
  - +1
  - 0
actions:
  - name: "Sedating Stinger"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage
      <br />★ 12–16 14 damage; M< 2 [[slowed]] (save ends)
      <br />✸ 17+ 17+ damage; M< 3 [[slowed]] (save ends) 
      <br />**Effect:** The target is [[restrained]] (save ends) if they are already [[slowed]]."
  - name: "Tail Sweep"
    desc:
      "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 3 × 6 line within 1
      <br />**Target** All enemies and objects in the line
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 damage; A< 1 3 acid damage
      <br />★ 12–16 11 damage; A< 2 3 acid damage
      <br />✸ 17+ 14 damage A< 3 3 acid damage 5 Malice The predator uses this ability a second time. They can target a new line or the same one."
maneuvers:
  - name: "Grasping Jaws"
    desc: "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object
      <br />✸ ≤11 9 damage; A< 1 [[grabbed]]
      <br />★ 12–16 14 damage; A< 2 [[grabbed]]
      <br />`dice: 2d10 + 3`
      <br />✦ 17+ 17+ damage; A< 3 [[grabbed]] (bane to escape)"
ta:
  - name: "Deterring Sting"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature deals damage to the predator with a melee ability. 
      <br />**Effect:** The predator uses their Sedating Stinger ability against the target and then shifts 3."
traits:
  - name: "Stubborn Rage"
    desc: "The predator is immune to being [[dazed]] or [[frightened]] while [[winded]] or while within 10 squares of another wyvern.
  - name: "Tenacious Hunter"
    desc: "Any creature suffering a condition inflicted by a wyvern can’t be hidden from the predator."

# XORANNOX THE TYRACT

name: "XORANNOX THE TYRACT"
level: 6
roles:
  - SOLO
ancestry:
  - Horror
  - Overmind
ev: 80
stamina: 450
speed: 5 (fly, hover)
size: 3 /
stability: 3
free_strike: 7
characteristics:
  - +4
  - +2
  - +4
  - +3
  - +3
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** Xorannox takes up to two turns each round. He can’t take turns consecutively. He can use two actions on each of his turns. While [[dazed]], Xorannox can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of his turn, Xorannox can take 10 damage to end one save ends effect affecting him. This damage can’t be reduced in any way."
  - name: "Eyes of the Tyract"
    desc: "Six unique eyestalks float around Xorannox and act on his turn at his command. On each of Xorannox’s turns, he directs one eyestalk to move and use a signature action. When an eyestalk is destroyed, Xorannox can’t use that eyestalk’s ability."
  - name: "Above It All"
    desc: "Xorannox can’t be flanked, [[frightened]], or knocked [[prone]]."
  -  name: "Natural Enemies"
    desc: "If Xorannox perceives another overmind or voiceless talker on the battlefield, he targets that threat at least once every turn."
actions:
  - name: "Toothful Thrashing"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 12 damage; slide 2; M< 2 [[bleeding]] (EoT)
      <br />★ 12–16 20 damage; slide 3; M< 3 [[bleeding]] (EoT)
      <br />✸ 17+ 23 damage; vertical slide 3; M< 4 [[bleeding]] (EoT)"
  - name: "Grav Spike"
    desc:
      "
      <br />**Keywords** Area, Psionic, Ranged
      <br />**Distance** 2 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 Vertical push 3
      <br />★ 12–16 Vertical push 5
      <br />✸ 17+ Vertical push 7 
      <br />**Effect:** Xorannox shifts up to his speed before or after using this ability."
maneuvers:
  - name: "Optical Collusion"
    desc: "
      <br />**Keywords** Area, Melee
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Xorannox commands all eyestalks to move up to their speed."
  - name: "Shutout"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** 5 x 2 line within 1
      <br />**Target** Special 
      <br />**Effect:** Xorannox ends all ongoing supernatural effects and suppresses supernatural effects from equipment in the affected area. New supernatural effects cannot activate in the affected area until the end of Xorannox’s next turn."
ta:
  - name: "Cower!"
    desc: "
      <br />**Keywords** Psionic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** Special 
      <br />**Trigger** A creature deals damage to Xorannox. 
      <br />**Effect:** The triggering creature is I< 3 [[frightened]] (save ends)."
va: 
  - name: "Disruption Beam (Villain Action 1)"
    desc: "
      <br />**Keywords** Psionic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** Three creatures
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 psychic damage; R< 2 [[dazed]] (save ends)
      <br />★ 12–16 17+ psychic damage; R< 3 [[dazed]] (save ends)
      <br />✸ 17+ 20 psychic damage; R< 4 [[dazed]] (save ends)"
  - name: "All Eyes, All Rise (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Xorannox reforms all destroyed eyestalks and raises them at full stamina."
  - name: "Panoptibeam (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 2 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** Xorannox directs each remaining eyestalk to use a signature action, targeting each creature in the area."

# COMPULSION EYE

name: "COMPULSION EYE"
level: 6
roles:
  - CONTROLLER
ancestry:
  - Eyestalk
  - Overmind
stamina: 30
speed: 5 (fly, hover)
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - -1
  - +1
  - +4
  - +1
  - -1
actions:
  - name: "Compulsion Beam"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Psionic, Ranged
      <br />**Distance** Ranged 6
      <br />**Target** 1 creature
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 I< 2 charmed
      <br />★ 12–16 I< 3 charmed
      <br />✸ 17+ I< 4 charmed 
      <br />**Effect:** A charmed creature moves up to their speed and makes a free strike against an enemy of Xorannox’s choice as a free triggered action, and then is no longer charmed."
traits:
  - name: "Psionic Barrier"
    desc: "The compulsion eye has damage immunity 15. When the compulsion eye uses an action, this immunity disappears until the end of the round."

# DEMOLITION EYE

name: "DEMOLITION EYE"
level: 6
roles:
  - ARTILLERY
ancestry:
  - Eyestalk
  - Overmind
stamina: 30
speed: 5 (fly, hover)
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - -1
  - +1
  - +4
  - +1
  - -1
actions:
  - name: "Explosion"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Psionic, Ranged
      <br />**Distance** 4 cube within 10
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 6 fire damage
      <br />★ 12–16 10 fire damage; A< 3 [[prone]]
      <br />✸ 17+ 13 fire damage; A< 4 [[prone]]"
traits:
  - name: "Psionic Barrier"
    desc: "The demolition eye has damage immunity 15. When the demolition eye uses an action, this immunity disappears until the end of the round."

# MOVER EYE

name: "MOVER EYE"
level: 6
roles:
  - CONTROLLER
ancestry:
  - Eyestalk
  - Overmind
stamina: 30
speed: 5 (fly, hover)
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - -1
  - +1
  - +4
  - +1
  - -1
actions:
  - name: "Telekinetic Beam"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Psionic, Ranged, Strike
      <br />**Distance** Ranged 6
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 damage; slide 4
      <br />★ 12–16 17 damage; slide 5
      <br />✸ 17+ 20 damage; slide 6"
traits:
  - name: "Psionic Barrier"
    desc: "The mover eye has damage immunity 15. When the mover eye uses an action, this immunity disappears until the end of the round."

# NECROTIC EYE

name: "NECROTIC EYE"
level: 6
roles:
  - HEXER
ancestry:
  - Eyestalk
  - Overmind
stamina: 30
speed: 5 (fly, hover)
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - -1
  - +1
  - +4
  - +1
  - -1
actions:
  - name: "Necro Beam"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Psionic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 corruption damage
      <br />★ 12–16 17 corruption damage; M< 3 [[bleeding]] (save ends)
      <br />✸ 17+ 20 corruption damage; M< 4 [[bleeding]] (save ends) 
      <br />**Effect:** If this effect or the resulting stamina loss from the [[bleeding]] condition reduces a creature’s stamina to 0, the target dies."
traits:
  - name: "Psionic Barrier"
    desc: "The necrotic has damage immunity 15. When the necrotic eye uses an action, this immunity disappears until the end of the round."

# TOXIC EYE

name: "TOXIC EYE"
level: 6
roles:
  - HEXER
ancestry:
  - Eyestalk
  - Overmind
stamina: 30
speed: 5 (fly, hover)
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - -1
  - +1
  - +4
  - +1
  - -1
actions:
  - name: "Toxic Vapors"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Psionic, Ranged
      <br />**Distance** 4 cube within 10
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 6 poison damage
      <br />★ 12–16 10 poison damage; M< 3 [[weakened]] (save ends)
      <br />✸ 17+ 13 poison damage; M< 4 [[weakened]] (save ends)"
traits:
  - name: "Psionic Barrier"
    desc: "The toxic eye has damage immunity 15. When the toxic eye uses an action, this immunity disappears until the end of the round."

# ZAPPER EYE

name: "ZAPPER EYE"
level: 6
roles:
  - ARTILLERY
ancestry:
  - Eyestalk
  - Overmind
stamina: 30
speed: 5 (fly, hover)
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - -1
  - +1
  - +4
  - +1
  - -1
actions:
  - name: "Lightning Beam"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Psionic, Ranged
      <br />**Distance** 10 × 1 line within 1
      <br />**Target** All enemies in the line
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 6 lightning damage
      <br />★ 12–16 10 lightning damage
      <br />✸ 17+ 13 lightning damage 
      <br />**Effect:** Each target loses all Surges."
traits:
  - name: "Psionic Barrier"
    desc: "The zapper eye has damage immunity 15. When the zapper eye uses an action, this immunity disappears until the end of the round."
