# BUGBEAR ROUGHNECK
```statblock
name: "BUGBEAR ROUGHNECK"
level: 2
roles:
  - TROOP
  - BRUTE
ancestry:
- Bugbear
- Goblin 
- Humanoid 
- Fey
ev: 16
stamina: 109
speed: 6
size: 1L /
stability: 0
free_strike: 5
characteristics:
  - +2
  - +2
  - 0
  - 0
  - 0
actions:
  - name: "Haymaker"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 11 damage; one target is [[grabbed]]; one target is pushed 2
      <br />✸ 17+ 14 damage; one target is [[grabbed]]; one target is vertically pushed 3 
      <br />**5 Malice** The distance becomes 1 Burst, the Strike keyword is replaced with Area, and the roughneck targets all enemies instead."
  - name: "Leaping Fury"
    desc:
      "
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; M< 1 [[prone]]
      <br />★ 12–16 13 damage; M< 2 [[prone]]
      <br />✸ 17+ 16 damage; M< 3 [[prone]] 
      <br />**Effect:** The roughneck leaps 5 to an unoccupied space adjacent to the target before making the attack."
maneuvers:
  - name: "Drag Through Hell"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object [[grabbed]] by the roughneck 
      <br />**Effect:** The roughneck moves up to their speed, dragging the target across the ground. The target takes 2 damage for each square they were dragged through before being released [[prone]]. Each square the target was dragged through becomes difficult terrain for enemies."
  - name: "Throw"
    desc: "
      <br />**Keywords** Attack, Melee
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object [[grabbed]] by the roughneck 
      <br />**Effect:** Vertical push 5. An ally target doesn’t take damage from being force moved."
ta:
  - name: "Catcher (Free Triggered Action)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** 1 size 1 creature or object 
      <br />**Trigger** The target is force moved into a square adjacent to the roughneck. 
      <br />**Effect:** The target is [[grabbed]] by the roughneck."
  - name: "Flying Sawblade"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The roughneck is vertically moved by another creature. 
      <br />**Effect:** The roughneck uses their Haymaker ability against a creature or object at the end of the movement."


```
