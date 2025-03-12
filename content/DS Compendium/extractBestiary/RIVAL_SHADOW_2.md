```statblock
name: "RIVAL SHADOW 2"
level: 2
roles:
  - TROOP
  - AMBUSHER
ancestry:
  - Humanoid
  - Rival
ev: 16
stamina: 80
speed: 7
size: 1M /
stability: 1
free_strike: 5
characteristics:
  - +0
  - +2
  - +0
  - +0
  - +1
actions:
  - name: "Swift Serration"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 11 damage
      <br />✸ 17+ 14 damage; A< 2 [[bleeding]] (save ends)
      <br />**1 Malice** The shadow teleports up to 5 squares and hides."
maneuvers:
  - name: "Coat the Blade"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self
      <br />**Effect:** The shadow coats their weapon with poison. They have an edge on their next strike, and the potency increases by 1."
traits:
  - name: "Exploit Opening"
    desc: "- The shadow deals an extra 5 damage to [[bleeding]] targets."
  - name: "Rivalry"
    desc: "- The shadow selects one creature within [[Line of Effect]] at the start of an encounter. Both the shadow and the creature can add a 1d3 to all power rolls made against each other."
```