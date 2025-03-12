# WYVERN LURKER
```statblock
name: "WYVERN LURKER"
level: 4
roles:
  - TROOP
  - AMBUSHER
ancestry:
  - Beast
  - Wyvern
ev: 24
stamina: 120
immunities: Acid 5
speed: 9 (fly)
size: 2 /
stability: 2
free_strike: 6
characteristics:
  - +2
  - +3
  - -1
  - +1
  - 0
actions: 
  - name: "Agonizing Stinger"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage
      <br />★ 12–16 14 damage; M< 2 [[bleeding]] (save ends)
      <br />✸ 17+ 17+ damage; M< 3 [[bleeding]] (save ends) 
      <br />**1 Malice** The lurker deals an additional 6 acid damage to one target if they were hidden from them."
  - name: "Acidic Anguish"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 10 acid damage; M< 1 [[weakened]] (save ends)
      <br />★ 12–16 16 acid damage; M< 2 [[weakened]] (save ends)
      <br />✦ 17+ 20 acid damage; M< 3 [[weakened]] (save ends) 
      <br />**Effect:** A target [[weakened]] from this ability takes 1d4 acid damage at the start of each of their turns until the condition ends."
maneuvers:
  - name: "Swooping Torment"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The lurker flies up to their speed and hides. Each enemy that comes within 1 square of the lurker during this movement can choose to take 3 sonic damage or fall [[prone]]."
ta:
  - name: "Retaliatory Dive"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 5
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature deals damage to the lurker with a ranged ability. 
      <br />**Effect:** The lurker flies into a square adjacent to the target and makes a free strike against them."
traits:
  - name: "Ruthless Rage"
    desc: "The lurker deals an additional 3 damage on strikes while within 10 squares of another wyvern."
  - name: "Tenacious Hunter"
    desc: "Any creature suffering a condition inflicted by a wyvern can’t be hidden from the lurker."

```
