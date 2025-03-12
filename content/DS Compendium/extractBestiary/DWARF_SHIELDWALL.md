# DWARF SHIELDWALL
```statblock
name: "DWARF SHIELDWALL"
level: 3
roles:
  - PLATOON
  - DEFENDER
ancestry:
  - Dwarf
  - Humanoid
ev: 21
stamina: 72
speed: 5
size: 1M /
stability: 4
free_strike: 5
characteristics:
  - +2
  - 0
  - +0
  - +0
  - +1
actions:
  - name: "Wide Axe"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; slide 1
      <br />★ 12–16 10 damage; slide 1
      <br />✸ 17+ 13 damage; slide 1 
      <br />**Effect:** The shieldwall can shift 1 to remain adjacent to the target. A target [[restrained]] by a dwarf can be slid by this ability. 3 Malice The shieldwall targets an additional creature or object."
ta:
  - name: "Intercepting Shield"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** A creature strikes an adjacent ally. 
      <br />**Effect:** The shieldwall becomes the strike’s target and halves the damage."
traits:
  - name: "Call to the Wall"
    desc: "The shieldwall inflicts [[taunted]] (EoT) on a creature whenever they deal damage to the shieldwall or take damage from the shieldwall."


```
