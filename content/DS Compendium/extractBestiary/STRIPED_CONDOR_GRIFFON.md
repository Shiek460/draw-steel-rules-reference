# STRIPED CONDOR GRIFFON
```statblock
name: "STRIPED CONDOR GRIFFON"
level: 2
roles:
  - TROOP
  - BRUTE
ancestry:
  - Beast
  - Griffon
ev: 16
stamina: 100
speed: 7 (fly)
size: 3 /
stability: 3
free_strike: 5
characteristics:
  - +2
  - +2
  - -1
  - +2
  - +1
actions:
  - name: "Violent Thrashing"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; push 1
      <br />★ 12–16 11 damage; one target is pushed 2; the other target is vertically pushed 2
      <br />✸ 17+ 14 damage; one target is pushed 2 and [[prone]]; the other target is vertically pushed 3"
  - name: "Bound Ahead"
    desc:
      "<br />**Cost** 5 Malice
      <br />**Keywords** —
      <br />**Distance** Self (while grounded)
      <br />**Target** Self 
      <br />**Effect:** The griffon shifts up to their speed in a straight line. Each enemy who comes within 1 of the griffon during the move can choose to either take 5 damage or be knocked [[prone]]. "
maneuvers:
  - name: "Power Wing Buffet"
    desc: "
      <br />**Keywords** Area, Melee
      <br />**Distance** 5 × 3 line within 1
      <br />**Target** All creatures and objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 Push 2; M< 0 forced movement is vertical
      <br />★ 12–16 Push 4; M< 1 forced movement is vertical
      <br />✸ 17+ Push 6; M< 2 forced movement is vertical"
ta:
  - name: "Circle and Strike"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Triggering creature 
      <br />**Trigger** The griffon flies above a creature on the ground within 5. 
      <br />**Effect:** The griffon falls down upon the target, taking no damage from falling. The target takes 3 damage for each square the griffon fell and is A< 2 [[prone]] or [[grabbed]]."
traits:
  - name: "Beast of Prey"
    desc: "Creatures have a double bane on escaping the griffon’s grab."
  - name: "Steady"
    desc: "Creatures have a bane on power rolls that could knock the griffon [[prone]]."
  - name: "Banded Predator"
    desc: "The griffon is hidden whenever they have cover or concealment."

```
