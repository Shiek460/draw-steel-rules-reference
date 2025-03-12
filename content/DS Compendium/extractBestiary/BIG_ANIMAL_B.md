# BIG ANIMAL B
```statblock
name: "BIG ANIMAL B"
level: 2
roles:
  - TROOP
  - MOUNT
ancestry:
  - Animal
ev: 16
stamina: 80
speed: 6
size: 3 /
stability: 3
free_strike: 5
characteristics:
  - +2
  - +1
  - -1
  - +1
  - +0
actions:
  - name: "Natural Weapon"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 10 damage; push 1
      <br />✸ 17+ 13 damage; push 2 Trundle (Maneuver)
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The beast moves up to their speed. The beast can make a free strike on each creature that makes an opportunity attack against them during this movement."
ta:
  - name: "Animal Rally"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** An ally within [[Line of Effect]] is knocked [[prone]]. 
      <br />**Effect:** The beast moves up to their speed. If they end their turn adjacent to the triggering ally, they can pick the ally up and allow them to climb on top of the beast."
traits:
  - name: "Beast of Burden"
    desc: "Two of the beast’s  1 allies can occupy the same space while riding the beast."
  - name: "Nature Calls"
    desc: "The beast ignores 1 bane on their abilities while in an encounter outside or in a natural environment."

```
