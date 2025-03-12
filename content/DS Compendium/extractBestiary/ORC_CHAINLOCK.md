# ORC CHAINLOCK
```statblock
name: "ORC CHAINLOCK"
level: 1
roles:
  - PLATOON
  - HEXER
ancestry:
  - Humanoid
  - Orc
ev: 6
stamina: 20
speed: 5
size: 1L /
stability: 2
free_strike: 3
characteristics:
  - +2
  - +2
  - +1
  - 0
  - 0
actions:
  - name: "Hook and Chain"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; pull 1; M< 0 hooked (save ends)
      <br />★ 12–16 7 damage; pull 2; M< 1 hooked (save ends)
      <br />✸ 17+ 9 damage; pull 3; M< 2 hooked (save ends) 
      <br />**Effect:** A hooked target can’t move more than 3 squares away from the chainlock’s original position until the condition ends."
  - name: "Heavy Crossbolt"
    desc:
      "
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 5
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; A< 0 [[slowed]] (save ends)
      <br />★ 12–16 7 damage; A< 1 [[slowed]] (save ends)
      <br />✸ 17+ 9 damage; [[prone]]; A< 2 [[slowed]] (save ends)"
traits:
  - name: "Chain Link"
    desc: "Whenever the chainlock is force moved by a creature’s melee ability, the creature is pulled the same distance towards the chainlock."
  - name: "Relentless"
    desc: "If the chainlock’s stamina drops to 0, they can make a free strike before dying. If the target is reduced to 0 stamina or killed by the strike, the chainlock lives and their stamina is reduced to 1 instead."

```
