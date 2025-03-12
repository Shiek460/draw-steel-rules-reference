# ORC GARROTER
```statblock
name: "ORC GARROTER"
level: 1
roles:
  - PLATOON
  - AMBUSHER
ancestry:
  - Humanoid
  - Orc
ev: 6
stamina: 30
speed: 5
size: 1L /
stability: 0
free_strike: 4
characteristics:
  - +1
  - +2
  - 0
  - +1
  - −1
actions:
  - name: "Dagger Feint"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage; shift 1
      <br />★ 12–16 9 damage; shift 2
      <br />✸ 17+ 12 damage; shift 3 
      <br />**Effect:** This ability deals an additional 4 damage when it’s made with an edge."
  - name: "Strangle"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature
      <br />✸ ≤11 6 damage
      <br />★ 12–16 9 damage; I< 1 [[dazed]] (save ends)
      <br />`dice: 2d10 + 2`
      <br />✦ 17+ 12 damage; [[grabbed]]; I< 2 [[dazed]] (save ends) 
      <br />**Effect:** The target can’t speak or use magic abilities while [[grabbed]]."
maneuvers:
  - name: "Chroma Cloak"
    desc: "
      <br />**1 Malice** The garroter turns invisible. <br />The effect ends when the garroter uses an ability, takes damage, or at the end of their turn."
traits:
  - name: "Relentless"
    desc: "If the garroter’s stamina drops to 0, they can make a free strike before dying. If the target is reduced to 0 stamina or killed by the strike, the  garroter lives and their stamina is reduced to 1 instead."

```
