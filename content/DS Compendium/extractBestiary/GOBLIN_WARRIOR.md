# GOBLIN WARRIOR
```statblock
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
  - name: "Bury the Point"
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

```
