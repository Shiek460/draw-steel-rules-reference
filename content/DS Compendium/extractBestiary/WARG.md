# WARG
```statblock
name: "WARG"
level: 1
roles:
  - BAND
  - MOUNT
ancestry:
  - Animal
  - Goblin
ev: 3
stamina: 15
speed: 5
size: 1L /
stability: 1
free_strike: 1
characteristics:
  - +1
  - +2
  - −1
  - +0
  - −1
actions:
  - name: "Bite"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage"
maneuvers:
  - name: "Sprint"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The warg moves up to their speed."
traits:
  - name: "Mounted Charger"
    desc: "If a warg used as a mount charges, their rider gains an edge on melee strikes until the end of their turn. "
  - name: "Shared Crafty"
    desc: "If the warg’s rider has the Crafty trait, the warg also has the Crafty trait."
  - name: "Crafty"
    desc: "The goblin doesn’t provoke opportunity attacks by moving."


```
