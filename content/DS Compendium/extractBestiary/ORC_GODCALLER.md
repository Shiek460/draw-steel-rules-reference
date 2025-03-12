# ORC GODCALLER
```statblock
name: "ORC GODCALLER"
level: 1
roles:
  - PLATOON
  - SUPPORT
ancestry:
  - Humanoid
  - Orc
ev: 6
stamina: 30
speed: 6
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - +1
  - 0
  - 0
  - +1
  - +2
actions:
  - name: "Power Chord"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Ranged, Strike
      <br />**Distance** Melee 1 or Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 sonic damage
      <br />★ 12–16 7 sonic damage
      <br />✸ 17+ 9 sonic damage; P< 2 [[weakened]] (save ends)"
  - name: "Cadenza"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** 1 ally 
      <br />**Effect:** The target moves up to their speed and uses an action. 
      <br />**3 Malice** The godcaller targets a second ally."
maneuvers:
  - name: "Rallying Ostinato"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** Magic
      <br />**Distance** Self and Ranged 10
      <br />**Target** Self and up to 3 allies 
      <br />**Effect:** Each target regains 15 stamina and ignores difficult terrain until the end of the encounter." 
traits:
  - name: "Relentless"
    desc: "If the godcaller’s stamina drops to 0, they can make a free strike before dying. If the target is reduced to 0 stamina or killed by the strike, the  godcaller lives and their stamina is reduced to 1 instead."

```
