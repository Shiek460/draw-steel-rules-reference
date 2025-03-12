# ORC RAMPART
```statblock
name: "ORC RAMPART"
level: 2
roles:
  - PLATOON
  - DEFENDER
ancestry:
  - Humanoid
  - Orc
ev: 8
stamina: 59
speed: 6
size: 1L /
stability: 2
free_strike: 4
characteristics:
  - +2
  - +2
  - +2
  - +2
  - +2
actions:
  - name: "My Spear, My Foe"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 9 damage; [[taunted]] (EoT)
      <br />✸ 17+ 12 damage; [[taunted]] (EoT) 
      <br />**Effect:** This ability has a double edge if the target dealt damage to the rampart this round."
maneuvers:
  - name: "Castling"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** 1 ally 
      <br />**Effect:** The rampart moves or shifts up to their speed to a square adjacent to the target and then swaps places with the target."
ta:
  - name: "No."
    desc: "
      <br />**Keywords** — 
      <br />**Trigger** A creature targets an adjacent ally with an ability.
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The rampart becomes the new target."
traits:
  - name: "Relentless"
    desc: "If the rampart’s stamina drops to 0, they can make a free strike before dying. If the target is reduced to 0 stamina or killed by the strike, the rampart lives and their stamina is reduced to 1 instead."

```
