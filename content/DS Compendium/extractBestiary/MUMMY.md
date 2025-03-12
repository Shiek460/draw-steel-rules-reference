# MUMMY
```statblock
name: "MUMMY"
level: 4
roles:
  - BAND
  - BRUTE
ancestry:
  - Mummy
  - Undead
ev: 6
stamina: 50
immunities: corruption 4, poison 4 /
weaknesses: fire 5
speed: 5
size: 1M /
stability: 2
free_strike: 3
characteristics:
  - +3
  - -1
  - +1
  - +3
  - +0
actions:
  - name: "Accursed Bindings"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 corruption damage; pull 1
      <br />★ 12–16 8 corruption damage; pull 2
      <br />✸ 17+ 10 corruption damage; pull 2; M< 3 [[restrained]] (save ends) 
      <br />**Effect:** The potency of the mummy’s next ability used against the target increases by 1."
  - name: "Eldritch Curse"
    desc:
      "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One creature
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 corruption damage; I< 1 cursed (save ends)
      <br />★ 12–16 5 corruption damage; I< 2 cursed (save ends)
      <br />✸ 17+ 7 corruption damage; I< 3 cursed (save ends) 
      <br />**Effect:** A cursed target is [[bleeding]] and [[weakened]], and allies have an edge on strikes made against them."
ta:
  - name: "Blast of Mummy Dust"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Area
      <br />**Distance** 1 burst
      <br />**Target** 1 [[restrained]] target 
      <br />**Trigger** The mummy comes within distance of the target or starts their turn within distance of the target. 
      <br />**Effect:** 8 poison damage."

```
