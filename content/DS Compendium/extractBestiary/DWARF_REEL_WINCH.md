# DWARF REEL WINCH
```statblock
name: "DWARF REEL WINCH"
level: 1
roles:
  - PLATOON
  - SUPPORT
ancestry:
  - Dwarf
  - Humanoid
ev: 13
stamina: 36
speed: 5
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
  - name: "Snaring Crossbow"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 7 damage
      <br />✸ 17+ 9 damage; M< 2 [[restrained]] (save ends) 
      <br />**Effect:** Pull 5. A target [[restrained]] by a dwarf, including by this ability, can be pulled this way."
maneuvers:
  - name: "Reel Them In"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** Ranged, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** 3 creatures 
      <br />**Effect:** Pull 8. A [[slowed]] or [[restrained]] target is pulled an additional 2. A target [[restrained]] by a dwarf can be pulled this way."
traits:
  - name: "We Have a Quota!"
    desc: "If the engineer applies the [[slowed]] condition to a target who is already [[slowed]] or [[grabbed]], the target becomes [[restrained]] (save ends) and the [[slowed]] or [[grabbed]] condition ends."


```
