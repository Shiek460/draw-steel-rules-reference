# ORC TERRANOVA
```statblock
name: "ORC TERRANOVA"
level: 2
roles:
  - PLATOON
  - CONTROLLER
ancestry:
  - Humanoid
  - Orc
ev: 8
stamina: 30
speed: 6 (burrow)
size: 1M /
stability: 2
free_strike: 4
characteristics:
  - +1
  - +1
  - 0
  - +1
  - +2
actions:
  - name: "Earth Pillar"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** 3 creatures touching the ground
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage; A< 0 [[prone]] can’t stand (save ends)
      <br />★ 12–16 9 damage; A< 1 [[prone]] can’t stand (save ends)
      <br />✸ 17+ 12 damage; [[prone]] A< 2 and can’t stand (save ends) 
      <br />**Effect:** The ground beneath each target rises 1 square."
  - name: "Sinkhole"
    desc:
      "
      <br />**Keywords** Melee, Weapon
      <br />**Distance** 3 Burst
      <br />**Target** All enemies
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage; M< 0 [[restrained]] (save ends)
      <br />★ 12–16 7 damage; M< 1 [[restrained]] (save ends)
      <br />✸ 17+ 10 damage; M< 2 [[restrained]] (save ends) 
      <br />**Effect:** The affected area is considered difficult terrain."
traits:
  - name: "Seismic Step"
    desc: "The terranova ignores difficult terrain. The terranova doesn’t need [[Line of Effect]] to target creatures touching the ground with abilities."
  - name: "Relentless"
    desc: "If the terranova’s stamina drops to 0, they can take a free strike before dying. If the target is reduced to 0 stamina or killed by the strike, the terranova lives and their stamina is reduced to 1 instead."

```
