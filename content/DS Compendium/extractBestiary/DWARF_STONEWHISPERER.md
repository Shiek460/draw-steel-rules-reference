# DWARF STONEWHISPERER
```statblock
name: "DWARF STONEWHISPERER"
level: 3
roles:
  - PLATOON
  - CONTROLLER
ancestry:
  - Dwarf
  - Humanoid
ev: 10
stamina: 52
speed: 5
size: 1M /
stability: 2
free_strike: 5
characteristics:
  - +1
  - 0
  - +2
  - +2
  - 0
actions:
  - name: "Tile Slide"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic
      <br />**Distance** 2 cube within 1
      <br />**Target** All creatures and objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; slide 1; M< 0 [[slowed]] (save ends)
      <br />★ 12–16 8 damage; slide 3; M< 1 [[slowed]] (save ends)
      <br />✸ 17+ 11 damage; slide 5; M< 2 [[restrained]] (save ends) 
      <br />**Effect:** A target [[restrained]] by a dwarf can be slid by this ability."
maneuvers:
  - name: "Stone Wave"
    desc: "
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 3 cube within 10
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage; push 2; R< 1 [[slowed]] (save ends)
      <br />★ 12–16 6 damage; push 3; R< 2 [[slowed]] (save ends)
      <br />✸ 17+ 9 damage; push 3; R< 3 [[slowed]] (save ends) 
      <br />**Effect:** A target [[restrained]] by a dwarf can be pushed by this ability. The affected area is considered difficult terrain for enemies."
traits:
  - name: "Stonewalker"
    desc: "The stonewhisperer can phase through 2 squares of stone as part of any movement they take. If they end their movement inside stone, they are shunted out into the square where they entered it."


```
