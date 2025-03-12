# RIVAL TACTICIAN
```statblock
name: "RIVAL TACTICIAN 5"
level: 5
roles:
  - TROOP
  - ARTILLERY
ancestry:
  - Humanoid
  - Rival
ev: 28
stamina: 120
speed: 5
size: 1M /
stability: 2
free_strike: 7
characteristics:
  - +3
  - +0
  - +2
  - +0
  - +1
actions:
  - name: "Mark Targets"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 damage
      <br />★ 12–16 15 damage
      <br />✸ 17+ 18 damage 3 Malice Two allies within distance can use a signature action against one of the targets."
  - name: "Preserve and Protect"
    desc:
      "
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 5
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 11 damage; M< 1 [[weakened]] (save ends)
      <br />★ 12–16 16 damage; M< 2 [[weakened]] (save ends)
      <br />✸ 17+ 21 damage; M< 3 [[weakened]] (save ends) 
      <br />**Effect:** An ally adjacent to the target regains 7 stamina."
ta:
  - name: "Take the Opening"
    desc: "
      <br />**Keywords** Ranged
      <br />**Distance** Ranged 10
      <br />**Target** 1 enemy 
      <br />**Trigger** The target moves. 
      <br />**Effect:** At any point during the movement, the tactician and one ally within distance make a free strike against the target."
traits:
  - name: "Rivalry"
    desc: "- The tactician selects one creature within [[Line of Effect]] at the start of an encounter. Both the tactician and the creature can add a 1d3 to all power rolls made against each other."

```
