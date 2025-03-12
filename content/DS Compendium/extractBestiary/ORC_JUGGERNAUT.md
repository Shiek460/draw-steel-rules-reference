# ORC JUGGERNAUT
```statblock
name: "ORC JUGGERNAUT"
level: 3
roles:
  - PLATOON
  - BRUTE
ancestry:
  - Humanoid
  - Orc
ev: 10
stamina: 60
speed: 6
size: 1L /
stability: 0
free_strike: 5
characteristics:
  - +2
  - +2
  - −1
  - −1
  - +2
actions:
  - name: "Haymaker Greataxe"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 11 damage; [[prone]]
      <br />✸ 17+ 14 damage; [[prone]]; M< 2 [[bleeding]] (save ends) 
      <br />**Effect:** This ability deals an additional 6 damage against already [[prone]] targets."
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
  - name: "Blood in the Water"
    desc: "The juggernaut can move 3 additional squares if they end their movement closer to a [[prone]] creature."
  - name: "Relentless"
    desc: "If the juggernaut’s stamina drops to 0, they can take a free strike before dying. If the target is reduced to 0 stamina or killed by the strike, the juggernaut lives and their stamina is reduced to 1 instead."

```
