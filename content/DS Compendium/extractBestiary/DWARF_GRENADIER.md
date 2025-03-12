# DWARF GRENADIER
```statblock
name: "DWARF GRENADIER"
level: 2
roles:
  - PLATOON
  - HEXER
ancestry:
  - Dwarf
  - Humanoid
ev: 8
stamina: 39
speed: 5
size: 1M /
stability: 3
free_strike: 4
characteristics:
  - +1
  - 0
  - 0
  - +2
  - 0
actions:
  - name: "Concussive Grenade"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Ranged, Weapon
      <br />**Distance** 3 cube within 5
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage; push 1
      <br />★ 12–16 6 damage; push 3; M< 1 [[slowed]] (save ends)
      <br />✸ 17+ 8 damage; push 5; M< 2 [[slowed]] (save ends) 
      <br />**Effect:** A target [[restrained]] by a dwarf can be pushed by this ability."
  - name: "Sleep Grenade"
    desc:
      "
      <br />**Keywords** Area, Ranged
      <br />**Distance** 3 cube within 5
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 poison damage; I< 0 [[dazed]] (save ends)
      <br />★ 12–16 6 poison damage; I< 1 [[dazed]] (save ends)
      <br />✸ 17+ 8 poison damage; I< 2 [[dazed]] (save ends) 
      <br />**Effect:** A creature [[dazed]] by this ability has -1 to all characteristics while resisting potent effects until the condition ends."
traits:
  - name: "Indirect Fire"
    desc: "The grenadier ignores cover and concealment and doesn’t need to establish [[Line of Effect]] for their abilities."


```
