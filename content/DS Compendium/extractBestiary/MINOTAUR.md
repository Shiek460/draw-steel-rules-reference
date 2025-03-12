# MINOTAUR
```statblock
name: "MINOTAUR"
level: 3
roles:
  - TROOP
  - HARRIER
ancestry:
  - Accursed
  - Humanoid
  - Minotaur
ev: 20
stamina: 100
speed: 8
size: 2 /
stability: 2
free_strike: 5
characteristics:
  - +2
  - +2
  - 0
  - +1
  - −1
actions:
  - name: "Flail and Blade"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; push 1
      <br />★ 12–16 11 damage; push 2
      <br />✸ 17+ 14 damage; push 3 
      <br />**Effect:** Shift 3."
  - name: "Primal Bay"
    desc:
      "<br />**Cost** 3 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The minotaur has damage immunity 2 and deals an additional 5 damage with their strikes until the end of their next turn. On their next turn, they have access to an additional maneuver."
maneuvers:
  - name: "Goring Horns"
    desc: "
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; I< 0 [[dazed]] (save ends)
      <br />★ 12–16 8 damage; I< 1 [[dazed]] (save ends)
      <br />✸ 17+ 9 damage; I< 2 [[dazed]] (save ends) 
      <br />**Effect:** The potency of this ability increases by 1 if it’s used while charging."
ta:
  - name: "Retaliatory Gore"
    desc: "
      <br />**Keywords** — 
      <br />**Trigger** The minotaur takes damage from a creature within 8.
      <br />**Distance** Self
      <br />**Target** Triggering creature 
      <br />**Effect:** The minotaur charges the target using Flail and Blade or Goring Horns."
traits:
  - name: "Minotaur Sense"
    desc: "The minotaur cannot get a result lower than tier 2 when making Tests to navigate, search, or seek."

```
