# BUGBEAR CHANNELER
```statblock
name: "BUGBEAR CHANNELER"
level: 2
roles:
  - TROOP
  - CONTROLLER
ancestry:
- Bugbear 
- Goblin 
- Humanoid 
- Fey
ev: 16
stamina: 60
speed: 5
size: 1L /
stability: 0
free_strike: 5
characteristics:
  - +1
  - +1
  - +2
  - +2
  - +2
actions:
  - name: "Shadow Drag"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Strike, Ranged
      <br />**Distance** Ranged 8
      <br />**Target** 2 creatures or objects on the ground
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; pull 2
      <br />★ 12–16 10 damage; pull 3
      <br />✸ 17+ 13 damage; pull 4 
      <br />**Effect:** Each square that a target is pulled through becomes difficult terrain for enemies."
  - name: "Blistering Element"
    desc:
      "
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage; M<  0 [[bleeding]] (save ends)
      <br />★ 12–16 3 damage; M<  1 [[bleeding]] (save ends)
      <br />✸ 17+ 4 damage; M<  2 [[bleeding]] (save ends) 
      <br />**Effect:** The channeler chooses one of the following damage types for the damage: acid, cold, corruption, fire, or poison."
  - name: "Twist Shape"
    desc:
      "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** 1 creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 corruption damage; P<  0 [[slowed]] (save ends)
      <br />★ 12–16 8 corruption damage; P<  1 shapechanged (save ends)
      <br />✸ 17+ 11 corruption damage; P<  2 shapechanged (save ends) 
      <br />**Effect:** A shapechanged creature has their limbs violently stretched and their skin becomes paper thin. They are [[slowed]] and have fire weakness 10 while they have this effect."
maneuvers:
  - name: "Throw"
    desc: "
      <br />**Keywords** Attack, Melee
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object [[grabbed]] by the channeler 
      <br />**Effect:** Vertical push 3. An ally target doesn’t take damage from being force moved."
ta:
  - name: "Catcher (Free Triggered Action)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** 1 size 1 creature or object 
      <br />**Trigger** The target is force moved into a square adjacent to the channeler. 
      <br />**Effect:** The target is [[grabbed]] by the channeler."
  - name: "Shadow Veil (Triggered Action)"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** 1 ally 
      <br />**Trigger** The target takes damage. 
      <br />**Effect:** The channeler collapses the target into their shadow and halves the damage. The target can’t be targeted by strikes until they reform from the shadows at the start of their next turn."


```
