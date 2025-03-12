# FORCE OF EARTH
```statblock
name: "FORCE OF EARTH"
level: 3
roles:
  - TROOP
  - BRUTE
ancestry:
  - Elemental
ev: 20
stamina: 132
speed: 5 (burrow)
size: 2 /
stability: 2
free_strike: 6
characteristics:
  - +2
  - −1
  - 0
  - +1
  - +2
actions:
  - name: "Slam Into Dirt"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 damage
      <br />★ 12–16 12 damage; M< 1 [[restrained]] (save ends)
      <br />✸ 17+ 15 damage; M< 2 [[restrained]] (save ends) 
      <br />**Effect:** The area beneath the target becomes difficult terrain."
maneuvers:
  - name: "Convocation of Quartz"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** Self or 1 elemental 
      <br />**Effect:** The target imposes a bane on melee strikes made against them until the start of the force’s next turn if they don’t already have it. 3 Malice The target grows a carapace of stone, increasing their stability by 3 and granting them 15 temporary stamina until the end of the encounter."
ta:
  - name: "Break Armor"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The force takes damage 
      <br />**Effect:** The force halves the damage, gains damage weakness 3, and increases their speed by 3. The damage weakness increases by 3 each time the force uses this ability in an encounter. Primordial Strength The force deals an additional 6 damage with strikes targeting objects. "
traits:
  - name: "Fickle and Free"
    desc: "The force can’t be [[restrained]], [[slowed]], or knocked [[prone]], and they ignore difficult terrain."

```
