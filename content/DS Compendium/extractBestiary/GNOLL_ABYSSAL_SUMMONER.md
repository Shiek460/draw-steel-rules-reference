# GNOLL ABYSSAL SUMMONER
```statblock
name: "GNOLL ABYSSAL SUMMONER"
level: 2
roles:
  - BAND
  - SUPPORT
ancestry:
  - Abyssal
  - Gnoll
ev: 4
stamina: 20
speed: 5
size: 1M /
stability: 1
free_strike: 2
characteristics:
  - +1
  - 0
  - 0
  - +2
  - +2
actions:
  - name: "Flame Wad"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 5
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 fire damage
      <br />★ 12–16 5 fire damage
      <br />✸ 17+ 7 fire damage; I< 2 burning (save ends) 
      <br />**Effect:** A burning target takes 1d6 fire damage at the start of each of their turns until the condition ends."
maneuvers:
  - name: "Call Abyssal Hyenas"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** —
      <br />**Distance** Ranged 5
      <br />**Target** Special 
      <br />**Effect:** 2 abyssal hyenas claw out of the ground into unoccupied squares."
  - name: "Cackletongue"
    desc: "
      <br />**Cost** 4 Malice
      <br />**Keywords** —
      <br />**Distance** 2 burst
      <br />**Target** All allies 
      <br />**Effect:** 1 abyssal hyena target turns into a gnoll maurader, keeping their stamina. Targets who haven’t used a cackletongue maneuver on this turn use it immediately at no cost."
traits:
  - name: "Death Frenzy"
    desc: "Whenever an ally within 5 is reduced to 0 stamina, the gnoll moves up to their speed and makes a free strike."

```
