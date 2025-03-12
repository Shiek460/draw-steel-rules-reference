# GHOUL CRAVER
```statblock
name: "GHOUL CRAVER"
level: 4
roles:
  - MINION
  - HARRIER
ancestry:
  - Undead
ev: 6 for four minions
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

```
