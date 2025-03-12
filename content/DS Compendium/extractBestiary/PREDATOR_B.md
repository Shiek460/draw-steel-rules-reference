# PREDATOR B
```statblock
name: "PREDATOR B"
level: 2
roles:
  - TROOP
  - BRUTE
ancestry:
  - Animal
ev: 16
stamina: 100
speed: 5
size: 3 /
stability: 2
free_strike: 5
characteristics:
  - +2
  - +1
  - -1
  - +1
  - +0
actions:
  - name: "Natural Weapon"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 11 damage; push 1; M < 1 [[prone]]
      <br />✸ 17+ 14 damage; push 2; M < 2 [[prone]] "
  - name: "Wild Swing"
    desc:
      "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 1 burst
      <br />**Target** All enemies and objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 6 damage
      <br />✸ 17+ 8 damage; A < 2 [[bleeding]] (save ends) 
      <br />**Effect:** The predator uses their weapons in a wanton flurry."
ta:
  - name: "Swat"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** Triggering creature or object 
      <br />**Trigger** The predator takes damage from a creature or object within distance. 
      <br />**Effect:** Push 5. Trample The predator can move through enemies and objects at normal speed. When the predator enters a creature’s space for the first time on their turn, the creature takes 3 damage."
traits:
  - name: "Nature Calls"
    desc: "The predator ignores 1 bane on their abilities while in an encounter outside or in a natural environment."

```
