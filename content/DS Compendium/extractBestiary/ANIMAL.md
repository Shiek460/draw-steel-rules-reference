# ANIMAL
```statblock
name: "ANIMAL"
level: 1
roles:
  - TROOP
  - HARRIER
ancestry:
  - Animal
ev: 12
stamina: 60
speed: 6
size: 1M /
stability: 0
free_strike: 4
characteristics:
  - +0
  - +2
  - -2
  - +1
  - -2
actions:
  - name: "Natural Weapon"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 9 damage
      <br />✸ 17+ 12 damage 
      <br />**Effect:** The animal can shift 2 between striking the first and second target."
maneuvers:
  - name: "Rush"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The animal moves up to their speed."
traits:
  - name: "Nature Calls"
    desc: 
      "- The animal ignores 1 bane on their abilities while in an encounter outside or in a natural environment."

```
