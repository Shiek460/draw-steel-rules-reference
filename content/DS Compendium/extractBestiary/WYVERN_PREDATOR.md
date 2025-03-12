# WYVERN PREDATOR
```statblock
name: "WYVERN PREDATOR"
level: 4
roles:
  - TROOP
  - BRUTE
ancestry:
  - Beast
  - Wyvern
ev: 24
stamina: 140
immunities: Acid 5
speed: 7 (fly)
size: 3 /
stability: 3
free_strike: 6
characteristics:
  - +3
  - +2
  - -1
  - +1
  - 0
actions:
  - name: "Sedating Stinger"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage
      <br />★ 12–16 14 damage; M< 2 [[slowed]] (save ends)
      <br />✸ 17+ 17+ damage; M< 3 [[slowed]] (save ends) 
      <br />**Effect:** The target is [[restrained]] (save ends) if they are already [[slowed]]."
  - name: "Tail Sweep"
    desc:
      "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 3 × 6 line within 1
      <br />**Target** All enemies and objects in the line
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 damage; A< 1 3 acid damage
      <br />★ 12–16 11 damage; A< 2 3 acid damage
      <br />✸ 17+ 14 damage A< 3 3 acid damage 5 Malice The predator uses this ability a second time. They can target a new line or the same one."
maneuvers:
  - name: "Grasping Jaws"
    desc: "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object
      <br />✸ ≤11 9 damage; A< 1 [[grabbed]]
      <br />★ 12–16 14 damage; A< 2 [[grabbed]]
      <br />`dice: 2d10 + 3`
      <br />✦ 17+ 17+ damage; A< 3 [[grabbed]] (bane to escape)"
ta:
  - name: "Deterring Sting"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature deals damage to the predator with a melee ability. 
      <br />**Effect:** The predator uses their Sedating Stinger ability against the target and then shifts 3."
traits:
  - name: "Stubborn Rage"
    desc: "The predator is immune to being [[dazed]] or [[frightened]] while [[winded]] or while within 10 squares of another wyvern."
  - name: "Tenacious Hunter"
    desc: "Any creature suffering a condition inflicted by a wyvern can’t be hidden from the predator."

```
