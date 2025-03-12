# ESSENCE OF TIDES
```statblock
name: "ESSENCE OF TIDES"
level: 3
roles:
  - TROOP
  - CONTROLLER
ancestry:
  - Elemental
ev: 20
stamina: 80
immunities: cold 5
speed: 7 (swim)
size: 1M /
stability: 1
free_strike: 5
characteristics:
  - +2
  - 0
  - +1
  - −1
  - +2
actions:
  - name: "Water Wing"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Strike
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; slide 1
      <br />★ 12–16 11 damage; slide 2
      <br />✸ 17+ 14 damage; slide 3 
      <br />**Effect:** P< 2 the target’s stability is reduced to 0 and they move 2 additional squares whenever they are force moved (save ends)"
maneuvers:
  - name: "Convocation of Waves"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** Self or 1 elemental 
      <br />**Effect:** The target receives cold immunity 5 until the start of the essence’s next turn if they don’t already have it. 
      <br >**3 Malice** The target emits a 1 aura pool of water until the end of the encounter. The area beneath the aura becomes a river that trails behind the target as they move and is considered difficult terrain. An enemy that ends their turn standing in the river is M< 2 [[slowed]] (save ends)."
ta:
  - name: "Sea Salted Wounds"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Malice 1
      <br />**Target** 1 creature 
      <br />**Trigger** An ally deals damage to the target. 
      <br />**Effect:** The essence makes a free strike against the target."
traits:
  - name: "Water Glide"
    desc: "When the essence starts their turn on a space containing water, they can add the flying keyword to their movement until the end of their turn. While flying, the essence doesn’t provoke opportunity attacks."
  - name: "Fickle and Free"
    desc: "The essence can’t be [[restrained]], [[slowed]], or knocked [[prone]], and they ignore difficult terrain."


```
