# ORC BLOODRUNNER
```statblock
name: "ORC BLOODRUNNER"
level: 3
roles:
  - PLATOON
  - HARRIER
ancestry:
  - Humanoid
  - Orc
ev: 10
stamina: 50
speed: 8
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - +2
  - +2
  - 0
  - +1
  - +1
actions:
  - name: "Shield Bash"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage (enemy only); push X
      <br />★ 12–16 10 damage (enemy only); push X
      <br />✸ 17+ 13 damage (enemy only); push X or [[prone]] 
      <br />**Effect:** Push X is equal to the number of squares the bloodrunner moved on their turn before using this ability. 
      <br /><**2 Malice** An ally pushed by this ability can make a free strike on a creature."
traits:
  - name: "Unimpeded"
    desc: "This bloodrunner can share a [[prone]] creature’s square. The first time a bloodrunner enters a creature’s square on their turn, that creature takes 3 damage."
  - name: "Relentless"
    desc: "If the bloodrunner’s stamina drops to 0, they can make a free strike before dying. If the target is reduced to 0 stamina or killed by the strike, the  loodrunner lives and their stamina is reduced to 1 instead."

```
