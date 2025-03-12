# WAR DOG THANATITE
```statblock
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

```
