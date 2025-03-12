# FOSSIL CRYPTIC
```statblock
name: "FOSSIL CRYPTIC"
level: 2
roles:
  - SOLO
ancestry:
  - Elemental
ev: 40
stamina: 250
speed: 8 (burrow)
size: 1L /
stability: 3
free_strike: 5
characteristics:
  - +3
  - +2
  - +1
  - +1
  - 0
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The cryptic takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the cryptic can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the cryptic can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Churning Trunk"
    desc: "The cryptic emits a 1 aura of swirling debris that obscures their form. Any enemy who enters the aura for the first time in a round or starts their turn there takes 5 damage. Ranged abilities that target the cryptic have a bane."
  - name: "Seismic Step"
    desc: "The cryptic ignores difficult terrain. Additionally, they have [[Line of Effect]] to concealed creatures touching the ground."
actions:
  - name: "Sand Slam"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; A< 1 [[prone]]
      <br />★ 12–16 12 damage; A< 2 [[prone]] and can’t stand (EoT)
      <br />✸ 17+ 15 damage; A< 3 [[prone]] and can’t stand (save ends) 
      <br />**Effect:** Each enemy within 1 square of the target takes 2 damage."
  - name: "Stone Bone Storm"
    desc:
      "
      <br />**Keywords** Area, Melee
      <br />**Distance** 6 × 1 line within 1
      <br />**Target** Each enemy in the line
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 4 damage; M< 1 push 2
      <br />★ 12–16 7 damage; M< 2 [[prone]]
      <br />✸ 17+ 10 damage; M< 3 [[prone]] 
      <br />**Effect:** The cryptic reforms their body and appears in an unoccupied space within the line."
  - name: "Shatterstone"
    desc:
      "
      <br />**Keywords** Area, Melee
      <br />**Distance** 4 burst
      <br />**Target** Each enemy in the burst 
      <br />**Effect:** The cryptic burrows up to half their speed, then creates the burst when they breach the surface.
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 damage; push 2
      <br />★ 12–16 9 damage; push 3; [[prone]]
      <br />✸ 17+ 12 damage; push 4; [[prone]]"
maneuvers:
  - name "Stoneshift"
      <br />**Keywords** Ranged
      <br />**Distance** Ranged 5
      <br />**Target** One creature or object on the ground 
      <br />**Effect:** Slide 3. <br />**2 Malice** The distance of the ability becomes Ranged 10 and the slide increases to slide 6."
ta:
  - name: "Dissipate"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The cryptic takes damage 
      <br />**Effect:** The cryptic halves the damage, ignores any additional effects associated with it, and shifts up to 3 squares."
va:
  - name: "First Warning Quake (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Melee
      <br />**Distance** 5 burst
      <br />**Target** Each enemy on the ground in the burst 
      <br />**Effect:** Each target makes a Might test.
      <br />✸ ≤11 The target is [[prone]] and can’t stand (EoT)
      <br />★ 12–16 [[prone]]
      <br />`dice: 2d10 +
      <br />✦ 17+ No effect 
      <br />**Effect:** The affected area becomes difficult terrain."
  - name: "Final Warning Fissure (Villain Action 2)"
    desc: "
      <br />**Keywords** Area, Melee
      <br />**Distance** 5 burst
      <br />**Target** Each enemy on the ground in the burst 
      <br />**Effect:** Each target makes a Might test.
      <br />✸ ≤11 9 damage; [[prone]]
      <br />★ 12–16 5 damage
      <br />`dice: 2d10 +
      <br />✦ 17+ The target moves to the nearest unoccupied space outside the area. 
      <br />**Effect:** The area drops 2 squares. Each enemy in the area falls, while allies of the fossil cryptic drop safely. The affected area then becomes difficult terrain."
  - name: "No Escape (Villain Action 3)"
    desc: "
      <br />**Keywords** Ranged 
      <br />**Effect:** The cryptic makes an initial power roll that calls down stone pillars from the ceiling.
      <br />**Distance** Ranged 10
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 damage; [[prone]]; M< 1 [[restrained]] (save ends)
      <br />★ 12–16 9 damage; [[prone]]; M< 2 [[restrained]] (save ends)
      <br />✸ 17+ 12 damage; [[prone]]; M< 3 [[restrained]] (save ends) <br />
      <br />**Effect:** The cryptic then makes a final power roll that raises stone pillars from the floor.
      <br />**Distance** Ranged 10
      <br />**Target** Two creatures or objects on the ground
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 2 damage; vertical slide 2
      <br />★ 12–16 3 damage; vertical slide 4
      <br />✸ 17+ 4 damage; vertical slide 8 or the target is [[restrained]] against the ceiling (save ends)"

```
