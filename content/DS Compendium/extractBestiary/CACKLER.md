# CACKLER
```statblock
name: "CACKLER"
level: 2
roles:
  - BAND
  - HEXER
ancestry:
  - Abyssal
  - Gnoll
ev: 4
stamina: 15
speed: 5
size: 1S /
stability: 1
free_strike: 2
characteristics:
  - 0
  - 0
  - +2
  - +2
  - +2
actions:
  - name: "Moment of Brutality"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 8
      <br />**Target** 1 creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 psychic damage; I< 0 target makes a free strike against a creature of the cackler’s choice
      <br />★ 12–16 5 psychic damage; I< 1 target makes a free strike against a creature of the cackler’s choice
      <br />✸ 17+ 7 psychic damage; I< 2 target uses a signature action against a creature of the cackler’s choice 
      <br />**Effect:** An ally targeted by this ability makes a free strike instead of taking damage."
maneuvers:
  - name: "Cackletongue"
    desc: "
      <br />**Cost** 4 Malice
      <br />**Keywords** Area, Magic, Resistance
      <br />**Distance** 2 burst
      <br />**Target** All creatures in the burst 
      <br />**Effect:** Each enemy target makes a Might test.
      <br />`dice: 2d10 + 2`
      <br />✸ ≤11 [[frightened]] (save ends)
      <br />★ 12–16 [[frightened]] (EoT)
      <br />✦ 17+ No effect 
      <br />**Effect:** Targets who haven’t used a cackletongue maneuver on this turn use it immediately at no cost."
traits:
  - name: "Death Frenzy"
    desc: "Whenever an ally within 5 is reduced to 0 stamina, the gnoll moves up to their speed and makes a free strike."

```
