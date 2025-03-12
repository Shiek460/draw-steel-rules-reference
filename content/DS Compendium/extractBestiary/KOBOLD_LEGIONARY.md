# KOBOLD LEGIONARY
```statblock
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

```
