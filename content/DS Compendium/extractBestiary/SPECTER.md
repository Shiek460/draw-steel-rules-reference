# SPECTER
```statblock
name: "SPECTER"
level: 1
roles:
  - BAND
  - HEXER
ancestry:
  - Undead
ev: 3
stamina: 10
immunities: corruption 1, poison 1
speed: 5 (fly, hover)
size: 1M/
stability: 1
free_strike: 1
characteristics:
  - −5
  - +1
  - 0
  - 0
  - +2
actions:
  - name: "Decaying Touch"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Strike
      <br />**Distance** Melee 1
      <br />**Target** One creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 corruption damage; P< 0 [[weakened]] (save ends)
      <br />★ 12–16 4 corruption damage; P< 1 [[weakened]] (save ends)
      <br />✸ 17+ 5 corruption damage; P< 2 [[weakened]] (save ends) 
      <br />**2 Malice** The potency of this ability increases by 1. A living creature killed by this ability becomes a specter who appears in the target’s space under the Director’s control."
maneuvers:
  - name: "Hidden Movement"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The specter turns invisible, moves up to their speed, and becomes visible again."
traits:
  - name: "Corruptive Phasing"
    desc: "The specter can move through other creatures and objects at normal speed. The first time in a round that the specter passes through a creature, that creature takes 2 corruption damage. The specter doesn’t take damage from being force moved into objects."

```
