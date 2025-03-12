# RADENWIGHT BRUXER
```statblock
name: "RADENWIGHT BRUXER"
level: 1
roles:
  - PLATOON
  - BRUTE
ancestry:
  - Humanoid
  - Radenwight
ev: 6
stamina: 40
speed: 5 (climb)
size: 1L /
stability: 2
free_strike: 4
characteristics:
  - +2
  - +1
  - −1
  - +0
  - +0
actions:
  - name: "Lockjaw"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 9 damage
      <br />✸ 17+ 12 damage; [[grabbed]] 
      <br />**Effect:** While the target is [[grabbed]], they take 2 damage at the start of each of the bruxer’s turns."
  - name: "Flurry of Bites"
    desc:
      "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 1 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage; A< 0 [[bleeding]] (save ends)
      <br />★ 12–16 5 damage; A< 1 [[bleeding]] (save ends)
      <br />✸ 17+ 8 damage; A< 2 [[bleeding]] (save ends)"
ta:
  - name: "Ready Rodent"
    desc: "
      <br />**Keywords** Melee, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature 
      <br />**Trigger** An ally deals damage to the target. 
      <br />**Effect:** The bruxer makes a free strike against the target."
traits:
  - name: "Lockdown"
    desc: "An enemy can’t shift while adjacent to the bruxer."

```
