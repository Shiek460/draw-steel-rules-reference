# MINOTAUR STAMPEDE
```statblock
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
ev: 12 for four minions
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

```
