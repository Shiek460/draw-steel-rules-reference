# GNOLL MARAUDER
```statblock
name: "GNOLL MARAUDER"
level: 2
roles:
  - BAND
  - HARRIER
ancestry:
  - Abyssal
  - Gnoll
ev: 4
stamina: 20
speed: 7
size: 1M /
stability: 1
free_strike: 2
characteristics:
  - +1
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Fury Flail"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 5 damage
      <br />✸ 17+ 7 damage; [[prone]]; A< 2 [[bleeding]] (save ends) <br />**2+ Malice** The marauder targets an additional creature or object for every 2 malice spent." 
maneuvers:
  - name: "Cackletongue"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** —
      <br />**Distance** Self and 2 burst
      <br />**Target** Self and all allies 
      <br />**Effect:** Each target shifts up to their speed. Targets who haven’t used a cackletongue maneuver on this turn use it immediately at no cost."
traits:
  - name: "Death Frenzy"
    desc: "Whenever an ally within 5 is reduced to 0 stamina, the gnoll moves up to their speed and makes a free strike."

```
