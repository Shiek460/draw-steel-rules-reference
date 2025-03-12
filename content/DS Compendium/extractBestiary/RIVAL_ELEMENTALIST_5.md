# RIVAL ELEMENTALIST
```statblock
name: "RIVAL ELEMENTALIST 5"
level: 5
roles:
  - TROOP
  - CONTROLLER
ancestry:
  - Humanoid
  - Rival
ev: 28
stamina: 120
speed: 5
size: 1M /
stability: 1
free_strike: 6
characteristics:
  - +0
  - +1
  - +3
  - +2
  - +0
actions:
  - name: "The Thriving Wilds"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Green, Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** Two creatures or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage; slide 1; M< 1 3 acid damage
      <br />★ 12–16 14 damage; slide 2; M< 2 5 acid damage
      <br />✸ 17+ 17+ damage; slide 3; M< 3 7 acid damage"
  - name: "The Depths Hunger"
    desc:
      "
      <br />**Keywords** Area, Green, Magic
      <br />**Distance** 4 cube within 10
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 9 damage; [[restrained]] (EoT)
      <br />✸ 17+ 11 damage; [[restrained]] (save ends) 
      <br />**Effect:** The affected area is difficult terrain for enemies. An enemy has acid weakness 3 while occupying an affected square."
ta:
  - name: "Fissures of Darkness"
    desc: "
      <br />**Keywords** Magic, Void
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The elementalist takes damage. 
      <br />**Effect:** The elementalist teleports 3 squares. Each creature adjacent to their original space takes 3 corruption damage."
traits:
  - name: "Rivalry"
    desc: "- The elementalist selects one creature within [[Line of Effect]] at the start of an encounter. Both the elementalist and the creature can add a 1d3 to all power rolls made against each other."

```
