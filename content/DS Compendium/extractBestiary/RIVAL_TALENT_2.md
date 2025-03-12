```statblock
name: "RIVAL TALENT 2"
level: 2
roles:
  - TROOP
  - HEXER
ancestry:
  - Humanoid
  - Rival
ev: 16
stamina: 60
speed: 5
size: 1M /
stability: 2
free_strike: 5
characteristics:
  - +0
  - +0
  - +2
  - +0
  - +1
actions:
  - name: "Reverberating Blast"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Psionic, Ranged, Strike, Telekinesis
      <br />**Distance** Ranged 10
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 psychic damage; M< 0 [[prone]]
      <br />★ 12–16 10 psychic damage; push 2; M< 1 [[prone]]
      <br />✸ 17+ 13 psychic damage; push 3; M< 2 [[prone]]"
maneuvers:
  - name: "Muddle the Mind"
    desc: "
      <br />**Keywords** Psionic, Ranged, Telepathy
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 R< 0 [[slowed]] (save ends)
      <br />★ 12–16 R< 1 [[dazed]] (save ends)
      <br />✸ 17+ R< 2 [[slowed]] and [[dazed]] (save ends)"
ta:
  - name: "Precognitive Shift"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self
      <br />**Trigger** A creature deals damage to the talent.
      <br />**Effect:** The talent halves the damage and shifts 2."
traits:
  - name: "Rivalry"
    desc: "- The talent selects one creature within [[Line of Effect]] at the start of an encounter. Both the talent and the creature can add a 1d3 to all power rolls made against each other."
```