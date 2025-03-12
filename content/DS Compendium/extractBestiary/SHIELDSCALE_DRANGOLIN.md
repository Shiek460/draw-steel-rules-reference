# SHIELDSCALE DRANGOLIN
```statblock
name: "SHIELDSCALE DRANGOLIN"
level: 1
roles:
  - TROOP
  - BRUTE
ancestry:
  - Animal
  - Kobold
ev: 12
stamina: 80
speed: 7 (burrow)
size: 3 /
stability: 0
free_strike: 5
characteristics:
  - +2
  - +1
  - −3
  - 0
  - −2
actions:
  - name: "Fiery Claws"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 fire damage
      <br />★ 12–16 10 fire damage
      <br />✸ 17+ 13 fire damage"
  - name: "Drangolin Plume"
    desc:
      "
      <br />**Cost** 5 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The drangolin shifts their speed and uses Fiery Claws against each creature who comes within 1 during the move. The drangolin makes one power roll against all targets."
  - name: "Erupt"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** 2 burst (while burrowing)
      <br />**Target** All creatures
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage; push 1; A< 0 [[prone]]
      <br />★ 12–16 8 damage; push 3; A< 1 [[prone]]
      <br />✸ 17+ 11 damage; push 5; A< 2 [[prone]] 
      <br />**Effect:** This attack deals an additional 2 fire damage against targets directly above the dragonlin."
traits:
  - name: "Ash Shot"
    desc: "Each enemy adjacent to the drangolin has a bane on strikes and can’t be hidden."

```
