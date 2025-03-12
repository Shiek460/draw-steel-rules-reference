# DWARF GUNNER
```statblock
name: "DWARF GUNNER"
level: 1
roles:
  - PLATOON
  - ARTILLERY
ancestry:
  - Dwarf
  - Humanoid
ev: 12
stamina: 26
speed: 5
size: 1M /
stability: 1
free_strike: 4
characteristics:
  - 0
  - +2
  - 0
  - +1
  - 0
actions:
  - name: "Portable Ballista"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage; push 1
      <br />★ 12–16 9 damage; push 3
      <br />✸ 17+ 12 damage; push 5 
      <br />**Effect:** If the target is adjacent to a wall or object after the power roll is resolved, they are [[restrained]] (EoT). A target [[restrained]] by a dwarf can be pushed by this ability. 
      <br />**5 Malice** If the target is pushed into another creature, both the target and the creature are [[restrained]] (EoT)."
maneuvers:
  - name: "Ensnaring Chains (Maneuver)"
    desc: "
      <br />**Cost** 5 Malice
      <br />**Keywords** Ranged, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** 1 [[restrained]], [[slowed]], or [[prone]] target 
      <br />**Effect:** The gunner makes a free strike against the target. The target loses any [[restrained]], [[slowed]] or [[prone]] conditions and gains [[restrained]] (save ends)."
traits:
  - name: "Split Shot"
    desc: "Whenever the gunner deals damage to a creature or object, a creature or object within 1 of the recipient takes 3 damage."


```
