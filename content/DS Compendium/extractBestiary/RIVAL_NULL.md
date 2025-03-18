# RIVAL NULL
```statblock
name: "RIVAL NULL"
level: 5
roles:
  - TROOP
  - HARRIER
ancestry:
  - Humanoid
  - Rival
ev: 28
stamina: 140
speed: 7
size: 1M /
stability: 3
free_strike: 6
characteristics:
  - +0
  - +3
  - +2
  - +1
  - +0
actions:
  - name: "Agile Stride"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage; shift 3; A< 1 6 damage
      <br />★ 12–16 14 damage; shift 4; A< 2 11 damage
      <br />✸ 17+ 17+ damage; shift 5; A< 3 11 damage"
maneuvers:
  - name: "Deaden"
    desc: "
      <br />**Keywords** Melee, Psionic, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage; R< 1 [[dazed]] (EoT)
      <br />★ 12–16 14 damage; R< 2 [[dazed]] (save ends)
      <br />✸ 17+ 17+ damage; R< 3 [[dazed]] and [[restrained]] (save ends)"
traits:
  - name: "Inertial Shield"
    desc: "The null halves the damage of the first strike they are targeted by each round."
  - name: "Rivalry"
    desc: "The null selects one creature within [[Line of Effect]] at the start of an encounter. Both the null and the creature can add a 1d3 to all power rolls made against each other."

```
