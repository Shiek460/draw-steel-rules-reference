# BIG ANIMAL A
```statblock
name: "BIG ANIMAL A"
level: 1
roles:
  - TROOP
  - MOUNT
ancestry:
  - Animal
ev: 12
stamina: 60
speed: 6
size: 2 /
stability: 1
free_strike: 4
characteristics:
  - +1
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
      <br />★ 12–16 9 damage; A< 1 3 damage
      <br />✸ 17+ 12 damage; A< 2 3 damage Toss (Maneuver)
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object 
      <br />**Effect:** Vertical slide 3. If the target is an ally, they can make a free strike and then fall without taking damage."
ta:
  - name: "Juke"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The animal is targeted by an area ability. 
      <br />**Effect:** The animal shifts 2 before the ability activates."
traits:
  - name: "Nature Calls"
    desc: "The beast ignores 1 bane on their abilities while in an encounter outside or in a natural environment."


```
