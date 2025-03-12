# AEOLYXRIA THE UNCANNY
```statblock
name: "AEOLYXRIA THE UNCANNY"
level: 6
roles:
  - TROOP
  - CONTROLLER
ancestry:
  - Draconian
  - Dragon
  - Humanoid
ev: 32
stamina: 140
immunities: poison 6
speed: 5 (flying)
size: 1M /
stability: 2
free_strike: 7
characteristics:
  - -1
  - +2
  - +4
  - +3
  - +1
actions:
  - name: "Spittlesplash"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** 2 enemies
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 poison damage; M< 1 [[slowed]] (save ends)
      <br />★ 12–16 15 poison damage; M< 2 [[slowed]] (save ends)
      <br />✸ 17+ 18 poison damage; M< 3 [[slowed]] (save ends)"
  - name: "Experimental Treasure"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 The target regains 10 stamina
      <br />★ 12–16 12 corruption damage; A< 2 [[weakened]] (save ends)
      <br />✸ 17+ 12 lightning damage; A< 2 [[bleeding]] (save ends) 
      <br />**Effect:** The first time in an encounter that Lydixavus rolls a result with this ability, she can choose that result instead of rolling whenever she uses this ability for the rest of the encounter. 
      <br />**2+ Malice** Aeolyxria targets an additional creature or object for every 2 malice spent."
maneuvers:
  - name: "Elevate!"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** 1 cube within 5
      <br />**Target** Special 
      <br />**Effect:** The ground is elevated by 5 squares, creating a pillar of dirt. Each creature in the affected area is lifted along with it. 
      <br />**1+ Malice** Aeolyxria creates an additional pillar for each malice spent."
ta:
  - name: "Blood For Blood"
    desc: "
      <br />**Keywords** Ranged, Weapon
      <br />**Distance** Ranged 5
      <br />**Target** One creature 
      <br />**Trigger** The target inflicts the [[bleeding]] condition on an ally.
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 poison damage; A< 2 [[bleeding]] (save ends)
      <br />★ 12–16 12 poison damage; A< 3 [[bleeding]] (save ends)
      <br />✸ 17+ 15 poison damage; [[bleeding]] (save ends)"
traits:
  - name: "That’s Our Opening!"
    desc: "The Director gains 1 malice whenever Aeolyxria inflicts a condition on an enemy."


```
