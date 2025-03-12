# GHOUL
```statblock
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

```
