# GNOLL ABYSSAL ARCHER
```statblock
name: "GNOLL ABYSSAL ARCHER"
level: 2
roles:
  - BAND
  - ARTILLERY
ancestry:
  - Abyssal
  - Gnoll
ev: 4
stamina: 15
speed: 5
size: 1M /
stability: 1
free_strike: 3
characteristics:
  - 0
  - +2
  - +1
  - 0
  - −1
actions:
  - name: "Dark Longbow"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 corruption damage
      <br />★ 12–16 6 corruption damage
      <br />✸ 17+ 8 corruption damage; M< 2 [[slowed]] (save ends) 
      <br />**Effect:** This ability has an edge against creatures not at full stamina."
maneuvers:
  - name: "Cackletongue"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** Self and 2 burst
      <br />**Target** Self and all allies 
      <br />**Effect:** Each target has an edge on their next strike before the end of their next turn. Targets who haven’t used a cackletongue maneuver on this turn use it immediately at no cost."
traits:
  - name: "Death Frenzy"
    desc: "Whenever an ally within 5 is reduced to 0 stamina, the gnoll moves up to their speed and makes a free strike."
  - name: "Bloodscent"
    desc: "The abyssal archer can target creatures not at full stamina with abilities, even if they don’t have [[Line of Effect]]."


```
