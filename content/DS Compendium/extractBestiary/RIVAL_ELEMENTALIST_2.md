```statblock
name: "RIVAL ELEMENTALIST 2"
level: 2
roles:
  - TROOP
  - CONTROLLER
ancestry:
  - Humanoid
  - Rival
ev: 16
stamina: 60
speed: 5
size: 1M /
stability: 1
free_strike: 5
characteristics:
  - +0
  - +0
  - +2
  - +1
  - +0
actions:
  - name: "The Writhing Green"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Green, Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; slide 1
      <br />★ 12–16 10 damage; slide 2
      <br />✸ 17+ 13 damage; slide 3"
  - name: "The Earth Devours"
    desc:
      "
      <br />**Keywords** Area, Green, Magic
      <br />**Distance** 3 cube within 10
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 5 damage; [[restrained]] (EoT)
      <br />✸ 17+ 8 damage; [[restrained]] (save ends)
      <br />**Effect:** The affected area is difficult terrain for enemies. An enemy has acid weakness 2 while ccupying an affected square."
ta:
  - name: "Jaws of the Void"
    desc: "
      <br />**Keywords** Magic, Void
      <br />**Distance** Self
      <br />**Target** Self
      <br />**Trigger** The elementalist takes damage.
      <br />**Effect:** The elementalist teleports 2 squares. Each creature adjacent to their original space takes 2 corruption damage."
traits:
  - name: "Rivalry"
    desc: "- The elementalist selects one creature within [[Line of Effect]] at the start of an encounter. Both the elementalist and the creature can add a 1d3 to all power rolls made against each other."
```