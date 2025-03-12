```statblock
name: "RIVAL CONDUIT 2"
level: 2
roles:
  - TROOP
  - SUPPORT
ancestry:
  - Humanoid
  - Rival
ev: 16
stamina: 80
speed: 5
size: 1M /
stability: 1
free_strike: 5
characteristics:
  - +1
  - +0
  - +0
  - +2
  - +0
actions:
  - name: "Thunder of Heavens"
    desc: 
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Ranged, Strike
      <br />**Distance** Melee 1 or Ranged 10
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 holy damage
      <br />★ 12–16 10 holy damage
      <br />✸ 17+ 13 holy damage
      <br />**Effect:** The conduit or an ally within distance regains stamina equal to half the damage dealt."
maneuvers:
  - name: "Imbue with Might"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** Magic
      <br />**Distance** Ranged 10
      <br />**Target** Self and up to 5 allies
      <br />**Effect:** Each target has an edge on their next strike."
traits:
  - name: "Stalwart Guardian"
    desc: "- Strikes made against allies adjacent to the conduit have a bane."
  - name: "Rivalry"
    desc: "- The conduit selects one creature within [[Line of Effect]] at the start of an encounter. Both the conduit and the creature can add a 1d3 to all power rolls made against each other."
```