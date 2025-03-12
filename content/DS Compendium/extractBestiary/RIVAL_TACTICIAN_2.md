```statblock
name: "RIVAL TACTICIAN 2"
level: 2
roles:
  - TROOP
  - ARTILLERY
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
  - +2
  - +0
  - +1
  - +0
  - +0
actions:
  - name: "Dual Targeting Shot"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 11 damage
      <br />✸ 17+ 14 damage
      <br />**2 Malice** Two allies within distance can make a free strike against one of the targets."
  - name: "I’ll Cover You!"
    desc:
      "
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 5
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 damage; M< 0 [[weakened]] (save ends)
      <br />★ 12–16 13 damage; M< 1 [[weakened]] (save ends)
      <br />✸ 17+ 16 damage; M< 2 [[weakened]] (save ends)
      <br />**Effect:** An ally adjacent to the target regains 5 stamina."
ta:
  - name: "Overwatch"
    desc: "
      <br />**Keywords** Ranged
      <br />**Distance** Ranged 10
      <br />**Target** 1 enemy
      <br />**Trigger** The target moves.
      <br />**Effect:** At any point during the movement, the tactician makes a free strike against the target."
traits:
  - name: "Rivalry"
    desc: "- The tactician selects one creature within [[Line of Effect]] at the start of an encounter. Both the tactician and the creature can add a 1d3 to all power rolls made against each other."
```