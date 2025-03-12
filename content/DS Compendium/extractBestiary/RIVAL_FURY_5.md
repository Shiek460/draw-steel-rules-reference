# RIVAL FURY
```statblock
name: "RIVAL FURY 5"
level: 5
roles:
  - TROOP
  - BRUTE
ancestry:
  - Humanoid
  - Rival
ev: 28
stamina: 160
speed: 5
size: 1M /
stability: 3
free_strike: 7
characteristics:
  - +3
  - +2
  - +0
  - +0
  - +1
actions:
  - name: "Thunderous Slam"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 damage; push 2
      <br />★ 12–16 15 damage; push 3
      <br />✸ 17+ 18 damage; push 4 2 Malice Each target is M< 2 [[slowed]] (save ends)."
  - name: "Roughed Up"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature the fury’s size or smaller
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 11 damage; M< 1 [[grabbed]]
      <br />★ 12–16 16 damage; M< 2 [[grabbed]]
      <br />✸ 17+ 21 damage; M< 3 [[grabbed]] 
      <br />**Effect:** The fury and each ally have an edge on strikes against a creature [[grabbed]] by this ability."
traits:
  - name: "Overpower"
    desc: "- Once per turn, when the fury force moves a target or shifts into a square adjacent to a creature or object, they can use a signature action against them."
  - name: "Rivalry"
    desc: "- The fury selects one creature within [[Line of Effect]] at the start of an encounter. Both the fury and the creature can add a 1d3 to all power rolls made against each other."

```
