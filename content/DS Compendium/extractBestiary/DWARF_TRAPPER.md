# DWARF TRAPPER
```statblock
name: "DWARF TRAPPER"
level: 1
roles:
  - PLATOON
  - HARRIER
ancestry:
  - Dwarf
  - Humanoid
ev: 6
stamina: 36
speed: 7
size: 1M /
stability: 2
free_strike: 3
characteristics:
  - 0
  - +2
  - 0
  - +1
  - 0
actions:
  - name: "Concussive Bolts"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; push 2
      <br />★ 12–16 7 damage; push 4
      <br />✸ 17+ 9 damage; push 6 
      <br />**Effect:** A target [[restrained]] by a dwarf can be pushed by this ability."
maneuvers:
  - name: "Steam Powered Snare"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** Area, Ranged
      <br />**Distance** 3 cube within 5
      <br />**Target** All enemies in the cube 
      <br />**Effect:** Each target makes a Might test.
      <br />`dice: 2d10 +
      <br />✸ ≤11 7 damage; [[restrained]] (EoT)
      <br />★ 12–16 5 damage; [[slowed]] (EoT)
      <br />✦ 17+ No effect 
      <br />**Effect:** The snare remains until the end of the encounter. An enemy that moves into an affected square for the first time on their turn must make the test."


```
