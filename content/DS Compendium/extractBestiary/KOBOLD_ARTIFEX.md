# KOBOLD ARTIFEX
```statblock
name: "KOBOLD ARTIFEX"
level: 1
roles:
  - BAND
  - CONTROLLER
ancestry:
  - Humanoid
  - Kobold
ev: 3
stamina: 10
speed: 5
size: 1S /
stability: 0
free_strike: 1
characteristics:
  - 0
  - +2
  - +1
  - 0
  - 0
actions:
  - name: "Chain Hook"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 5
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage; pull 1
      <br />★ 12–16 4 damage; pull 2
      <br />✸ 17+ 5 damage; pull 3 
      <br />**Effect:** If the target’s forced movement triggers a trap, the trap has a double edge on its power roll."
maneuvers:
  - name: "Activate Trap"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** 1 trap or terrain object 
      <br />**Effect:** The trap or terrain object instantly triggers. 
      <br />**3 Malice** The artifex can place a new trap in the encounter and instantly trigger it."
traits:
  - name: "Shield? Shield!"
    desc: "The artifex has cover, a stability of 1, and can act as cover for allies when adjacent to an ally who also has this trait."

```
