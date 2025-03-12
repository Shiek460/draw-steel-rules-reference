# SERVITOR WAR WALKER
```statblock
name: "SERVITOR WAR WALKER"
level: 1
roles:
  - TROOP
  - MOUNT
ancestry:
  - Construct
  - Dwarf
ev: 12
stamina: 60
speed: 8 (climb)
size: 3 /
stability: 2
free_strike: 3
characteristics:
  - +2
  - +0
  - −2
  - 0
  - −2
actions:
  - name: "Grasping Claws"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 9 damage
      <br />✸ 17+ 12 damage; M< 2 [[restrained]] (save ends) 
      <br />**Effect:** [[restrained]] targets and targets [[restrained]] by this ability are pulled 3. A target [[restrained]] by a dwarf can be pulled by this ability."
maneuvers:
  - name: "Stunning Blast"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 3 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 2`
      <br />✸ ≤11 3 lightning damage; A< 0 [[slowed]] (save ends)
      <br />★ 12–16 6 lightning damage; A< 1 [[slowed]] (save ends)
      <br />✦ 17+ 8 lightning damage; A< 2 [[slowed]] (save ends)"
traits:
  - name: "Cupola" 
    desc: "Three of the war walker’s 1 allies can occupy the same space while riding the war walker. Riders have cover against attacks that target them."
  - name: "Mobile Prison Harness"
    desc: "[[slowed|Slowed]] or [[restrained]] creatures adjacent to the war walker become [[restrained]] (save ends) and have a bane on all power rolls. Adjacent [[restrained]] creatures are automatically moved with the war walker, ignoring stability."

```
