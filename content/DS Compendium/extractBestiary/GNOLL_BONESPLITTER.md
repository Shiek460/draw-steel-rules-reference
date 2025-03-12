# GNOLL BONESPLITTER
```statblock
name: "GNOLL BONESPLITTER"
level: 2
roles:
  - BAND
  - BRUTE
ancestry:
  - Abyssal
  - Gnoll
ev: 4
stamina: 25
speed: 5
size: 1L /
stability: 1
free_strike: 3
characteristics:
  - +2
  - +1
  - 0
  - 0
  - +1
actions:
  - name: "Three-Tail Flail"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; push 2
      <br />★ 12–16 6 damage; push 2
      <br />✸ 17+ 8 damage; [[grabbed]] M< 2 target has a bane on escaping the grab 
      <br />**Effect:** The bonesplitter can’t use three  -tail flail on another target while the current target is [[grabbed]]."
maneuvers:
  - name: "Cackletongue"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** —
      <br />**Distance** Self and 2 burst
      <br />**Target** Self and all allies 
      <br />**Effect:** Each target makes a free strike. Targets who haven’t used a cackletongue maneuver on this turn use it immediately at no cost."
traits:
  - name: "Death Frenzy"
    desc: "Whenever an ally within 5 is reduced to 0 stamina, the gnoll moves up to their speed and makes a free strike."

```
