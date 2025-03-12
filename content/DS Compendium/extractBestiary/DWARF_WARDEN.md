# DWARF WARDEN
```statblock
name: "DWARF WARDEN"
level: 2
roles:
  - PLATOON
  - BRUTE
ancestry:
  - Dwarf
  - Humanoid
ev: 8
stamina: 59
speed: 5
size: 1M /
stability: 3
free_strike: 5
characteristics:
  - +2
  - 0
  - 0
  - +1
  - 0
actions:
  - name: "Concussive Maul"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; push 1
      <br />★ 12–16 10 damage; push 3
      <br />✸ 17+ 13 damage; push 5; M< 2 [[restrained]] (save ends) 
      <br />**Effect:** A target [[restrained]] by a dwarf can be pushed by this ability."
maneuvers:
  - name: "Concussive Shockwave"
    desc: "
      <br />**Keywords** Area, Melee
      <br />**Distance** 3 cube within 1
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; push 2; A< 0 [[slowed]] (save ends)
      <br />★ 12–16 8 damage; push 4; A< 1 [[slowed]] (save ends)
      <br />✸ 17+ 11 damage; push 6; A< 2 [[dazed]] (save ends) 
      <br />**Effect:** A target [[restrained]] by a dwarf can be pushed by this ability. Escort the Prisoners Whenever the warden moves, they can carry an adjacent [[restrained]] enemy as if they were [[grabbed]]."


```
