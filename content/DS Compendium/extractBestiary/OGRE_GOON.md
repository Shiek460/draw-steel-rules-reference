# OGRE GOON
```statblock
name: "OGRE GOON"
level: 2
roles:
  - TROOP
  - BRUTE
ancestry:
  - Giant
  - Ogre
ev: 16
stamina: 100
speed: 5
size: 2 /
stability: 4
free_strike: 5
characteristics:
  - +2
  - 0
  - −1
  - 0
  - −1
actions:
  - name: "Club Swing"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; push 2
      <br />★ 12–16 11 damage; push 4
      <br />✸ 17+ 14 damage; push 6; [[prone]] 
      <br />**Effect:** This attack deals an additional 4 damage to each creature and object that takes damage from any force movement it causes."
maneuvers:
  - name: "Grabby Hand"
    desc: "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 11 damage; [[grabbed]]
      <br />✸ 17+ 14 damage; [[grabbed]] 
      <br />**Effect:** The goon can only have one target [[grabbed]] at a time. 
      <br />**1 Malice** The target has a bane on escaping the grab while the goon crushes the target in their hand."
  - name: "People Bowling"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 6 × 1 Line within 1
      <br />**Target** All creatures and objects 
      <br />**Special** The goon must be grabbing a size -1 creature or object to use this maneuver. 
      <br />**Effect:** The goon hurls what’s in their hand down the line and rolls power. The hurled creature or object counts as a target and lands in the last square of the line (or nearest unoccupied square of the goon’s choice).
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 9 damage
      <br />✸ 17+ 12 damage; [[prone]]"
ta:
  - name: "Swat The Fly"
    desc: "
      <br />**Keywords** — 
      <br />**Trigger** The target moves or shifts away from the goon.
      <br />**Distance** Melee 1
      <br />**Target** 1 adjacent creature or object 
      <br />**Effect:** Slide 5."
traits:
  - name: "Defiant Anger"
    desc: "The goon has damage immunity 2 while they are [[winded]]."

```
