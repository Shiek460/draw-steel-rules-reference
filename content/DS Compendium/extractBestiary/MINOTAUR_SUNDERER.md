# MINOTAUR SUNDERER
```statblock
name: "MINOTAUR SUNDERER"
level: 3
roles:
  - TROOP
  - BRUTE
ancestry:
  - Accursed
  - Humanoid
  - Minotaur
ev: 20
stamina: 120
speed: 6
size: 2 /
stability: 2
free_strike: 6
characteristics:
  - +2
  - +1
  - 0
  - +2
  - −1
actions:
  - name: "Spiked Maul"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 damage; pull 1
      <br />★ 12–16 12 damage; pull 2
      <br />✸ 17+ 15 damage; pull 3 
      <br />**Effect:** A target is [[grabbed]] if they are pulled adjacent to the sunderer."
  - name: "Fearsome Bay"
    desc:
      "
      <br />**Keywords** Area
      <br />**Distance** 3 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 I< 0 [[frightened]] (save ends)
      <br />★ 12–16 I< 1 [[frightened]] (save ends)
      <br />✸ 17+ I< 2 [[frightened]] (save ends) 
      <br />**Effect:** The minotaur has damage immunity 2 and deals an additional 5 damage with their strikes until the end of their next turn."
maneuvers:
  - name: "Disemboweling Horns"
    desc: "
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 [[grabbed]] creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; push 1; M< 0 [[bleeding]] (save ends)
      <br />★ 12–16 8 damage; push 3; M< 1 [[bleeding]] (save ends)
      <br />✸ 17+ 9 damage; push 5; M< 2 [[bleeding]] (save ends) 
      <br />**Effect:** The target takes 1d6 damage at the start of each of their turns while [[bleeding]] from this ability."
ta:
  - name: "Retaliatory Gore"
    desc: "
      <br />**Keywords** — 
      <br />**Trigger** The sunderer takes damage from a creature within 6.
      <br />**Distance** Self
      <br />**Target** Triggering creature 
      <br />**Effect:** The sunderer charges the target using Spiked Maul."
traits:
  - name: "Minotaur Sense"
    desc: "The sunderer cannot get a result lower than tier 2 when making Tests to navigate, search, or seek."

```
