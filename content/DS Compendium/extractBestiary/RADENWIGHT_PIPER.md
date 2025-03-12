# RADENWIGHT PIPER
```statblock
name: "RADENWIGHT PIPER"
level: 1
roles:
  - PLATOON
  - SUPPORT
ancestry:
  - Humanoid
  - Radenwight
ev: 6
stamina: 30
speed: 5 (climb)
size: 1S /
stability: 0
free_strike: 3
characteristics:
  - +0
  - +0
  - +0
  - +2
  - +1
actions:
  - name: "Piercing Trill"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Ranged, Strike
      <br />**Distance** Melee 1 or Ranged 10
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 sonic damage; push 1
      <br />★ 12–16 7 sonic damage; push 3
      <br />✸ 17+ 9 sonic damage; push 4 
      <br />**Effect:** The piper or an ally within distance regains stamina equal to half the damage dealt."
maneuvers:
  - name: "Vivace Vivace!"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 burst
      <br />**Target** Each ally in the burst 
      <br />**Effect:** Each target who has used their Ready Rodent ability since their last turn regains the use of their triggered action.
      <br />**2 Malice** The area increases to 6 burst."
ta:
  - name: "Ready Rodent"
    desc: "
      <br />**Keywords** Melee, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature 
      <br />**Trigger** An ally deals damage to the target. 
      <br />**Effect:** The piper makes a free strike against the target."
traits:
  - name: "Musical Suggestion"
    desc: "At the end of the piper’s turn, they can choose an adjacent creature and slide them 2, ignoring stability."

```
