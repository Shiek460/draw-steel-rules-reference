# CERAMIC HORSE
```statblock
name: "CERAMIC HORSE"
level: 1
roles:
  - PLATOON
  - MOUNT
ancestry:
  - Elemental
  - High
  - Elf
ev: 6
stamina: 30
speed: 10
size: 2 /
stability: 2
free_strike: 3
characteristics:
  - +2
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Elemental Charge"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 7 fire damage
      <br />✸ 17+ 9 lightning damage; M< 2 [[prone]]"
  - name: "Stomp"
    desc:
      "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 1 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 5 damage
      <br />✸ 17+ 7 damage 
      <br />**Effect:** This attack deals an additional 2 damage to [[prone]] targets."
maneuvers: 
  - name: "Buck"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** The horse’s rider 
      <br />**Effect:** Vertical slide 3; The rider can use a ranged ability at any point during the movement and then fall without taking damage."
traits:
  - name: "Shared Otherworldly Grace"
    desc: "If the ceramic horse’s rider has the Otherworldly Grace trait, it also gains the Otherworldly Grace trait."
  - name: "Otherworldly Grace"
    desc: "At the start of their turn, the dawn mage can turn the duration of one save ends effect they suffer from into EoT."

```
