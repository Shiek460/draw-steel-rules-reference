# WAR DOG TETRARCH
```statblock
name: "WAR DOG TETRARCH"
level: 6
roles:
  - LEADER
ancestry:
  - Humanoid
  - War
  - Dog
ev: 32
stamina: 180
speed: 7
size: 1M /
stability: 2
free_strike: 7
characteristics:
  - +4
  - +3
  - +2
  - +3
  - +4
actions:
  - name: "Houndblade"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 3
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 damage
      <br />★ 12–16 16 damage; [[taunted]] (EoT)
      <br />✸ 17+ 19 damage; [[taunted]] (EoT) 
      <br />**Effect:** A creature [[taunted]] by this ability has a bane on strikes. 
      <br />**3 Malice** Each target loses 1d3 Recoveries."
maneuvers:
  - name: "Get them, you dolts!"
    desc: "
      <br />**Cost** 1 Malice per target
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** Up to three creatures 
      <br />**Effect:** The target shifts up to their speed and makes a free strike. The target deals an additional 4 damage if they strike a [[taunted]] enemy."
ta:
  - name: "Sneering Disregard"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Triggering creature 
      <br />**Trigger** A non  -[[taunted]] creature targets the tetrarch with a power roll. 
      <br />**Effect:** The tetrarch imposes a double bane on the power roll. If the target gets a tier-1 result, the tetrarch ignores any additional effects of the ability, and the target is [[frightened]] of the tetrarch (save ends)."
traits:
  - name: "End Effect"
    desc: "At the end of their turn, the tetrarch can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Chosen of the Iron Saint"
    desc: "The Director gains 1 malice whenever an ally within 10 of the tetrarch gets a tier-3 result on an attack."
va:
  - name: "Enter the Fray (Villain Action 1)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 2 burst
      <br />**Target** All enemies 
      <br />**Effect:** The tetrarch leaps 7 squares before using this action.
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 push 2; I< 2 [[frightened]] (save ends)
      <br />★ 12–16 push 4; I< 3 [[frightened]] (save ends)
      <br />✸ 17+ push 5; I< 4 [[frightened]] (save ends)"
  - name: "Lay Waste (Villain Action 2)"
    desc: "
      <br />**Keywords** Area, Weapon
      <br />**Distance** Five 2 cubes within 20
      <br />**Target** All creatures and objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 7 fire damage; A< 2 [[slowed]] (EoT)
      <br />★ 12–16 13 fire damage; A< 3 [[slowed]] (save ends)
      <br />✸ 17+ 16 fire damage; A< 4 [[slowed]] (save ends) 
      <br />**Effect:** The cubes are set ablaze. Until the end of the encounter, the affected area is considered difficult terrain, and a creature takes 2 fire damage for each affected square they enter."
  - name: "You Would Dare?! (Villain Action 3)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Until the end of the encounter, the tetrarch rallies themself, gains damage immunity 2, and their signature action now targets three creatures or objects."

```
