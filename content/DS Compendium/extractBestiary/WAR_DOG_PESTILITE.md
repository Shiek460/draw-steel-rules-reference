# WAR DOG PESTILITE
```statblock
name: "WAR DOG PESTILITE"
level: 3
roles:
  - BAND
  - CONTROLLER
ancestry:
  - Humanoid
  - War
  - Dog
ev: 5
stamina: 20
immunities: Poison 3
speed: 5
size: 1M /
stability: 0
free_strike: 2
characteristics:
  - +0
  - +1
  - +0
  - +0
  - +2
actions:
  - name: "Plaguecaster"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 3 cube within 10
      <br />**Target** Each creature in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 poison damage; I< 0 [[frightened]] (save ends)
      <br />★ 12–16 4 poison damage; I< 1 [[frightened]] (save ends)
      <br />✸ 17+ 5 poison damage; I< 2 [[frightened]] (save ends) 
      <br />**Effect:** The area is covered in a cloud of pestilence that lasts until the start of the pestilite’s next turn. Any creature who enters the area for the first time in a round or starts their turn there takes 2 poison damage."
maneuvers:
  - name: "Posthumous Promotion"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One war dog with a loyalty collar 
      <br />**Effect:** The target’s loyalty collar detonates, killing them instantly."
traits:
  - name: "Loyalty Collar"
    desc: "When the pestilite dies, they explode, dealing 1d6 damage to each adjacent enemy."


```
