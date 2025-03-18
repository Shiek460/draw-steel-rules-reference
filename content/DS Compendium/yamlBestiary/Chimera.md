![[DS Compendium/Malice/Chimera Malice|Chimera Malice]]
#Monster
```statblock
columns: 2
name: "Chimera"
ancestry:
- "Monster"
roles:
- "SOLO"
level: 3
ev: 50
stamina: 300
immunities:
- "Fire 6"
weaknesses: []
speed: "10 Fly"
size: "2"
stability: 1
free_strike: 6
characteristics: 
- 3
- 2
- -2
- 1
- 0
traits:
- name: "Solo Monster"
  desc: "- The chimera takes 2 turns each round. They can use two actions on each of their turns and can take each turn after an enemy turn they choose. While [[Dazed|dazed]], the chimera can take one action and one maneuver per turn."
- name: "Volant"
  desc: "- When the chimera makes a creature [[Winded|winded]] or reduces them to 0 Stamina or less, the chimera can move their speed towards one enemy within line of effect."
actions:
- name: "Bite"
  desc: 
    "<br />
    __Type__: Action    **Cost**: Signature<br />
    **Keywords**: Attack , Melee , Weapon<br />
    **Distance**: Melee 2<br />
    **Target**: 2 creatures or objects<br />
    **Effects**: <br />
    `dice: 2d10 + 3`<br />
      **✦**: 9 damage<br />
      **★**: 13 damage<br />
      **✸**: 16 damage<br />
      **Effect**: This attack deals an additional 3 damage if the chimera has an edge on the attack."
- name: "Roar"
  desc: 
    "<br />
    __Type__: Action    **Cost**: 5 Malice<br />
    **Keywords**: Area, Magic<br />
    **Distance**: 5 burst<br />
    **Target**: All enemies in the burst<br />
    **Effects**: <br />
    `dice: 2d10 + 3`<br />
      **✦**: 4 psychic damage<br />
      **★**: 8 psychic damage; I2 [[Frightened|frightened]] (save ends)<br />
      **✸**: 10 psychic damage; I3 [[Frightened|frightened]] (save ends)"

- name: "Dragon's Eruption"
  desc: 
    "<br />
    __Type__: Action    **Cost**: 7 Malice<br />
    **Keywords**: Area, Magic<br />
    **Distance**: 3 cube within 10<br />
    **Target**: All enemies in the cube<br />
    **Effects**: <br />
    `dice: 2d10 + 3`<br />
      **✦**: 3 fire damage; A1 3 fire damage<br />
      **★**: 5 fire damage; A2 5 fire damage<br />
      **✸**: 7 fire damage; A3 7 fire damage"
maneuvers:
- name: "Lion's Toss"
  desc: 
    "<br />
    __Type__: Maneuver<br />
    **Keywords**: Attack, Melee, Weapon<br />
    **Distance**: Melee 2<br />
    **Target**: 1 creature or object<br />
    **Effects**: <br />
    `dice: 2d10 + 3`<br />
      **✦**: vertical push 2<br />
      **★**: vertical push 3<br />
      **✸**: vertical push 5"
ta:
- name: "Ram's Defiance"
  desc: 
    "<br />
    __Type__: Triggered Action<br />
    **Keywords**: Attack, Melee, Weapon<br />
    **Distance**: Ranged 5<br />
    **Target**: 1 creature<br />
    **Trigger**: The target attacks the chimera and gets a tier-1 result.<br />
    **Effects**: <br />
    `dice: 2d10 + 3`<br />
      **✦**: 3 damage; M2 [[Slowed|slowed]] (save ends)<br />
      **★**: 5 damage; [[Prone|prone]]; M3 [[Slowed|slowed]] (save ends)<br />
      **✸**: 7 damage; [[Prone|prone]]; M4 [[Slowed|slowed]] (save ends)<br />
    **Effect**: The chimera shifts 5. If they end this movement adjacent to the target, roll power."
va:
- name: "Overture of Destruction"
  desc: 
    "<br />
    __Type__: Villain Action 1<br />
    **Keywords**: Area, Melee, Weapon<br />
    **Distance**: 1 burst<br />
    **Target**: All enemies in the burst<br />
    **Effect**: The chimera uses **Bite** and **Lion's Toss** against each target."

- name: "Fire Solo"
  desc: 
    "<br />
    __Type__: Villain Action 2<br />
    **Keywords**: Area, Melee, Weapon<br />
    **Distance**: Self<br />
    **Target**: Self<br />
    **Effect**: The chimera uses **Dragon's Eruption** and **Roar** without spending malice."

- name: "Chorus of Destruction"
  desc: 
    "<br />
    __Type__: Villain Action 3<br />
    **Keywords**: --<br />
    **Distance**: Self<br />
    **Target**: Self<br />
    **Effect**: The chimera uses **Roar**. The chimera then shifts their speed and can make a [[Free Strike|free strike]] against each enemy who comes within 1 of them during the move. When the chimera ends this movement, they use **Dragon's Eruption**."
```
