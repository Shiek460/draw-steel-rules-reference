# GRIFFON
```statblock
name: "GRIFFON"
level: 2
roles:
  - TROOP
  - MOUNT
ancestry:
  - Beast
  - Griffon
ev: 16
stamina: 80
speed: 9 (fly)
size: 2 /
stability: 2
free_strike: 5
characteristics:
  - +2
  - +2
  - -1
  - +1
  - +2
actions:
  - name: "Claw Swipes"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; shift 1
      <br />★ 12–16 10 damage; shift 2
      <br />✸ 17+ 13 damage; shift 3 
      <br />**Effect:** If this ability is used while charging, the griffon grapples one of the targets."
maneuvers:
  - name: "Crack the Earth"
    desc: "
      <br />**Keywords** Area, Ranged
      <br />**Distance** 3 cube within 8 (while flying)
      <br />**Target** All enemies Special The griffon must be grabbing a creature or object to use this maneuver. 
      <br />**Effect:** The griffon flies up to half their speed towards the ground and then sends the creature or object they’ve grappled hurtling towards the affected area.
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 6 damage; A< 1 push 3
      <br />✸ 17+ 9 damage; A< 2 push 4 and [[prone]]"
  - name: "Wing Buffet"
    desc: "
      <br />**Keywords** Area, Melee
      <br />**Distance** 4 × 2 line within 1
      <br />**Target** All creatures and objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 Push 3; A< 0 forced movement is vertical
      <br />★ 12–16 Push 4; A< 1 forced movement is vertical
      <br />✸ 17+ Push 5; A< 2 forced movement is vertical"
ta:
  - name: "Zephyr Feint"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** — 
      <br />**Trigger** The griffon takes damage
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The griffon halves the damage, doesn’t suffer any effect associated with it, and shifts 2 squares."
traits:
  - name: "Beast of Prey"
    desc: "Creatures have a double bane on escaping the griffon’s grab."
  - name: "Steady"
    desc: "Creatures have a bane on power rolls that could knock the griffon [[prone]]."


```
