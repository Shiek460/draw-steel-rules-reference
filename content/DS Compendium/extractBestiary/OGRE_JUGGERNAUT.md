# OGRE JUGGERNAUT
```statblock
name: "OGRE JUGGERNAUT"
level: 2
roles:
  - TROOP
  - HARRIER
ancestry:
  - Giant
  - Ogre
ev: 16
stamina: 80
speed: 6
size: 2 /
stability: 2
free_strike: 5
characteristics:
  - +2
  - +1
  - −1
  - 0
  - −1
actions:
  - name: "Pitchfork Catapult"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 10 damage; A< 1 vertical push 3
      <br />✸ 17+ 13 damage; A< 2 vertical slide 5
      <br />**1 Malice** Each target is M< 1 [[bleeding]] (save ends)."
  - name: "Earth Breaking Jump"
    desc:
      "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 3 burst
      <br />**Target** All creatures in the burst 
      <br />**Effect:** The juggernaut jumps up to 6 squares before using this ability.
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 6 damage; push 2; M< 1 [[prone]]
      <br />✸ 17+ 9 damage; push 4; M< 2 [[prone]]"
maneuvers:
  - name: "Horrible Bellow"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 3 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 I< 0 [[frightened]] (save ends)
      <br />★ 12–16 I< 1 [[frightened]] (save ends)
      <br />✸ 17+ I< 2 [[frightened]] (save ends) 
      <br />**Effect:** All ogres have an edge on strikes against creatures [[frightened]] by this ability."
ta:
  - name: "Hrraaaaaagh! (Free Triggered Action)"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** — 
      <br />**Trigger** The juggernaut takes damage.
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The juggernaut moves up to their speed and makes a free strike."
traits:
  - name: "Destructive Path"
    desc: "The juggernaut automatically destroys unattended, mundane size 1 objects in their path during their movement. They can break through any mundane wall made of wood, stone, or a similarly sturdy material in this way, so long as the wall is no more than 1 square thick."
  - name: "Defiant Anger"
    desc: "The juggernaut has damage immunity 2 while they are [[winded]]."

```
