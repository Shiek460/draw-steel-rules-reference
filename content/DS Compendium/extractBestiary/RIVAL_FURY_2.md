```statblock
name: "RIVAL FURY 2"
level: 2
roles:
  - TROOP
  - BRUTE
ancestry:
  - Humanoid
  - Rival
ev: 16
stamina: 100
speed: 5
size: 1M /
stability: 3
free_strike: 5
characteristics:
  - +2
  - +1  - +0
  - +0
  - +0
actions:
  - name: "Brutal Impact"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; push 1
      <br />★ 12–16 11 damage; push 2
      <br />✸ 17+ 14 damage; push 3
      <br />**2 Malice** Each target is M< 1 [[slowed]] (save ends)."
  - name: "Let’s Tussle"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature the fury’s size or smaller
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 damage; M< 0 [[grabbed]]
      <br />★ 12–16 13 damage; M< 1 [[grabbed]]
      <br />✸ 17+ 16 damage; M< 2 [[grabbed]]
      <br />**Effect:** The fury has an edge on strikes against a [[grabbed]] creature."
traits:
  - name: "Overwhelm"
    desc: "- Once per turn, when the fury force moves a target or shifts into a square adjacent to a creature or object, they can make a free strike against them."
  - name: "Rivalry"
    desc: "- The fury selects one creature within [[Line of Effect]] at the start of an encounter. Both the fury and the creature can add a 1d3 to all power rolls made against each other."
```