# WIGHT
```statblock
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

```
