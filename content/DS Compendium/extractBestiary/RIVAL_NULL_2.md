```statblock
name: "RIVAL NULL 2"
level: 2
roles:
  - TROOP
  - HARRIER
ancestry:
  - Humanoid
  - Rival
ev: 16
stamina: 80
speed: 7
size: 1M /
stability: 3
free_strike: 5
characteristics:
  - +0
  - +2
  - +1
  - +0
  - +0
actions:
  - name: "Nimble Step"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; shift 2
      <br />★ 12–16 10 damage; shift 3
      <br />✸ 17+ 13 damage; shift 4"
maneuvers:
  - name: "Numb"
    desc: "
      <br />**Keywords** Melee, Psionic, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; R< 0 [[slowed]] (EoT)
      <br />★ 12–16 10 damage; R< 1 [[slowed]] (EoT)
      <br />✸ 17+ 13 damage; R< 2 [[slowed]] and [[dazed]] (EoT)"
traits:
  - name: "Inertial Shield"
    desc: "- The null halves the damage of the first strike they are targeted by each round. "
  - name: "Rivalry"
    desc: "- The null selects one creature within [[Line of Effect]] at the start of an encounter. Both the null and the creature can add a 1d3 to all power rolls made against each other."
```