# WODE ELF GREENSKEEPER
```statblock
name: "WODE ELF GREENSKEEPER"
level: 1
roles:
  - PLATOON
  - DEFENDER
ancestry:
  - Fey
  - Humanoid
  - Wode
  - Elf
ev: 6
stamina: 40
speed: 7
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - 0
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Growing Longsword"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 7 damage
      <br />✸ 17+ 9 damage 
      <br />**Effect:** [[taunted]] (EoT). The greenskeeper can shift 3 after making the attack. 
      <br />**2 Malice** The distance increases to Melee 5."
maneuvers:
  - name: "Overgrowth"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** Area, Ranged
      <br />**Distance** 3 cube within 10
      <br />**Target** Special 
      <br />**Effect:** The affected area is overgrown with heavy brush and bramble. It provides cover and concealment for the greenskeeper and all allies, and is considered difficult terrain for enemies. An enemy that starts their turn in an affected square takes 3 damage."
traits:
  - name: "Masking Glamor"
    desc: "The elf immediately hides at the end of their turn while in cover or concealment, even if they are observed."

```
