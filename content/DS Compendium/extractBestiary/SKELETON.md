# SKELETON
```statblock
name: "SKELETON"
level: 1
roles:
  - BAND
  - ARTILLERY
ancestry:
  - Undead
ev: 3
stamina: 10
immunities: corruption 1, poison 1
speed: 5
size: 1M/
stability: 0
free_strike: 2
characteristics:
  - 0
  - +1
  - +1
  - 0
  - −1
actions:
  - name: "Bone Shards"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 10
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 6 damage
      <br />✸ 17+ 7 damage 
      <br />**Effect:** Until the start of the skeleton’s next turn, the target takes 2 damage the first time they move on their turn."
maneuvers:
  - name: "Bone Spur"
    desc: "
      <br />**Keywords** Area, Weapon
      <br />**Distance** 1 burst
      <br />**Target** Each enemy in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage; M< 0 [[bleeding]] (save ends)
      <br />★ 12–16 2 damage; M< 1 [[bleeding]] (save ends)
      <br />✸ 17+ 3 damage; M< 2 [[bleeding]] (save ends) 
      <br />**Effect:** Each target has a bane on their next strike."
traits:
  - name: "Arise"
    desc: "The first time the skeleton is reduced to stamina 0 by damage that isn’t fire damage or holy damage and their body isn’t destroyed, they regain half their stamina and fall [[prone]]."

```
