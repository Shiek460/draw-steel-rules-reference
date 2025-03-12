# BRUSH STALKER
```statblock
name: "BRUSH STALKER"
level: 4
roles:
  - PLATOON
  - MOUNT
ancestry:
  - Animal
  - Fey
ev: 12
stamina: 60
speed: 8
size: 2 /
stability: 3
free_strike: 5
characteristics:
  - +3
  - +2
  - -1
  - +0
  - +1
actions:
  - name: "Gore"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 10 damage
      <br />✸ 17+ 13 damage"
  - name: "Reclamation"
    desc:
      "
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 2 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 4 corruption damage; M< 1 [[weakened]] (save ends)
      <br />★ 12–16 7 corruption damage; M< 2 [[weakened]] (save ends)
      <br />✸ 17+ 10 corruption damage; M< 3 [[weakened]] (save ends)"
traits:
  - name: "Suneater"
    desc: "The brush stalker sheds darkness like other creatures would shed light. Each square within 2 of the brush stalker is devoid of light and provides concealment."
  - name: "Wyrd Dyr"
    desc: "Each non brush stalker creature with the Animal keyword is [[frightened]] while they have [[Line of Effect]] to the brush stalker."

```
