# SWARM
```statblock
name: "SWARM"
level: 1
roles:
  - TROOP
  - HEXER
ancestry:
  - Animal
  - Swarm
ev: 16
stamina: 40
speed: 5
size: 2 /
stability: 1
free_strike: 4
characteristics:
  - -2
  - +1
  - -3
  - +2
  - -3
actions:
  - name: "Flurry"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 9 damage; pull 1
      <br />✸ 17+ 12 damage; pull 2 
      <br />**Effect:** The target can be pulled into the swarm without inflicting damage."
maneuvers:
  - name: "Impede"
    desc: "
      <br />**Keywords** —
      <br />**Distance** 1 aura
      <br />**Target** Special 
      <br />**Effect:** The swarm forces themselves in the way of their foes. The affected area is considered difficult terrain for enemies until the start of the swarm’s next turn."
traits:
  - name: "Swarm"
    desc: "The swarm can move through squares as if they were size -1M, and can occupy other creatures’ spaces. At the start of the swarm’s turn, they can make a free strike against each creature they share a square with."
  - name: "Nature Calls"
    desc: "The swarm ignores 1 bane on their abilities while in an encounter outside or in a natural environment."

```
