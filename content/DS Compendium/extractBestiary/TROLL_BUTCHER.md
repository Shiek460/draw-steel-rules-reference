# TROLL BUTCHER
```statblock
name: "TROLL BUTCHER"
level: 5
roles:
  - TROOP
  - HEXER
ancestry:
  - Giant
  - Troll
ev: 28
stamina: 120
weaknesses: Acid 5, Fire 5
speed: 8
size: 2 /
stability: 2
free_strike: 6
characteristics:
  - +3
  - +1
  - +1
  - +0
  - +0
actions:
  - name: "Savoring Bite"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage; M< 1 [[bleeding]] (save ends)
      <br />★ 12–16 14 damage; M< 2 [[bleeding]] (save ends)
      <br />✸ 17+ 17+ damage; M< 3 [[bleeding]] (save ends) 
      <br />**1 Malice** The gourmand regains stamina equal to the damage dealt."
  - name: "Rotten Scraps"
    desc: "
      <br />**Keywords** Area, Ranged
      <br />**Distance** 3 cube within 10
      <br />**Target** Each enemy in the cube
      <br />`dice: 2d10 +
      <br />✦ ≤11 5 poison damage; M< 1 [[weakened]] (save ends)
      <br />★ 12–16 9 poison damage; M< 2 [[weakened]] (save ends)
      <br />✸ 17+ 11 poison damage; M< 3 [[weakened]] (save ends) 
      <br />**Effect:** Each troll in the cube regains 3 stamina."
maneuvers:
  - name: "Gourmet Flesh"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The gourmand enhances their next Savoring Bite ability, changing the damage type and inflicted condition to one of the following combinations: corruption and [[dazed]], acid and [[restrained]], or lightning and [[frightened]]."
ta:
  - name: "Acquired Taste"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature with deals damage to the gourmand with an Edge or a Surge. 
      <br />**Effect:** The gourmand makes a free strike against the target. The gourmand has an edge on power rolls and deals an additional 3 damage on their strikes until the end of their next turn."
traits:
  - name: "Bloody Feast"
    desc: "Each ally within 5 of the gourmand has an edge on power rolls that target an enemy suffering from a condition. "
  - name: "Relentless Hunger"
    desc: "The gourmand only dies when they are reduced to 0 stamina by acid or fire damage, end their turn with 0 stamina, or take acid or fire damage while at 0 stamina."

```
