# ROTTING ZOMBIE
```statblock
name: "ROTTING ZOMBIE"
level: 1
roles:
  - MINION
  - BRUTE
ancestry:
  - Undead
ev: 3 for four minions
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

```
