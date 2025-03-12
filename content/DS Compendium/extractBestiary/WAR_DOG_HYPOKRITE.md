# WAR DOG HYPOKRITE
```statblock
name: "WAR DOG HYPOKRITE"
level: 4
roles:
  - BAND
  - AMBUSHER
ancestry:
  - Humanoid
  - War
  - Dog
ev: 6
stamina: 30
speed: 8
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - +1
  - +3
  - +0
  - +0
  - +2
actions:
  - name: "Needle-Knife"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 8 damage; A< 2 [[bleeding]] (save ends)
      <br />✸ 17+ 10 damage; A< 3 [[bleeding]] and [[weakened]] (save ends) 
      <br />**Effect:** This ability deals an additional 6 damage if the hypocrite is hidden or disguised."
ta:
  - name: "Feign Death"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** Ranged 20
      <br />**Target** Self 
      <br />**Trigger** The hypokrite takes damage. 
      <br />**Effect:** The hypokrite activates their Loyalty Collar ability and teleports to an unoccupied square adjacent to an ally within distance alive."
traits:
  - name: "Face in the Crowd"
    desc: "The hypokrite is invisible while adjacent to an unhidden ally. When using the Hide maneuver, the hypocrite can choose to disguise themself as another creature within [[Draw Steel Rules#LINE OF EFFECT|line of effect]]."
  - name: "Loyalty Collar"
    desc: "When the hypokrite dies, they explode, dealing 2d6 damage to each adjacent enemy."

```
