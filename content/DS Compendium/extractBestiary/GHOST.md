# GHOST
```statblock
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


```
