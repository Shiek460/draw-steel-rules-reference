# ANKHEG
```statblock
name: "ANKHEG"
level: 1
roles:
  - SOLO
ancestry:
  - Ankheg
  - Beast
ev: 30
stamina: 200
speed: 5 (burrow)
size: 2 /
stability: 2
free_strike: 5
characteristics:
  - +3
  - +1
  - −3
  - +1
  - −4
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The ankheg takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the ankheg can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the ankheg can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Soft Underbelly"
    desc: "A [[prone]] creature gains an edge on melee strikes against the ankheg instead of taking a bane."
actions:
  - name: "Bite"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage
      <br />★ 12–16 13 damage; [[grabbed]]
      <br />✸ 17+ 16 damage; [[grabbed]] 
      <br />**Effect:** A size 1 target [[grabbed]] this way takes 3 acid damage at the start of each of their turns."
  - name: "Claws"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; A < 1 [[grabbed]]
      <br />★ 12–16 11 damage; A < 2 [[grabbed]]
      <br />✸ 17+ 14 damage; A < 3 [[grabbed]] 2 Malice The ankheg can vertical slide each target up to 5 squares."
  - name: "Spitfire"
    desc:
      "
      <br />**Keywords** Area, Ranged, Weapon
      <br />**Distance** 1 cube within 5
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 acid damage
      <br />★ 12–16 8 acid damage
      <br />✸ 17+ 11 acid damage 
      <br />**Effect:** The affected area is covered in burning acid. An enemy who enters an affected square for the first time on their turn or starts their turn there takes 2 acid damage."
  - name: "Earth Eruption"
    desc:
      "
      <br />**Keywords** Area, Melee
      <br />**Distance** 4 burst
      <br />**Target** Each enemy in the burst 
      <br />**Effect:** The ankheg burrows up to their speed, then creates the burst when they breach the surface.
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 6 damage
      <br />✸ 17+ 7 damage; push 2 Dust Cloud (Maneuver)
      <br />**Keywords** Area
      <br />**Distance** 1 burst
      <br />**Target** Special 
      <br />**Effect:** The ankheg kicks up dust into the affected area that blocks [[Line of Effect]] for enemies. The ankheg then shifts or burrows up to their speed."
ta:
  - name: "Skitter"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** A creature damages the ankheg 
      <br />**Effect:** The ankheg shifts up to 3 squares."
traits:
  - name: "Earthwalk"
    desc: "Difficult terrain composed of earth or loose rock doesn’t cost the ankheg extra movement."
  - name: "Tunneler"
    desc: "When the ankheg burrows, they create a size 2 tunnel. The tunnel remains stable for one day, then collapses."
va:
  - name: "Acid Spew (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Weapon
      <br />**Distance** 10 x 1 line within 1
      <br />**Target** Each creature in the line
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 acid damage
      <br />★ 12–16 8 acid damage
      <br />✸ 17+ 11 acid damage 
      <br />**Effect:** The ground within the affected area is covered in a puddle of acid. A creature who enters an affected square for the first time on their turn or starts their turn there takes 2 acid damage."
  - name: "Sinkhole (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The ankheg shifts up to their speed by burrowing. If the ankheg ends this move underground and within 2 squares of a creature on the surface, the ankheg uses Bite against the creature."
  - name: "Acid and Claws (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 2 burst
      <br />**Target** Each creature in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 acid damage; M < 1 [[bleeding]] (save ends)
      <br />★ 12–16 8 acid damage; M < 2 [[bleeding]] (save ends)
      <br />✸ 17+ 11 acid damage; M < 3 [[bleeding]] (save ends)"

```
