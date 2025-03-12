
# HOLLOWBONE LAUNCHER
```statblock
name: "HOLLOWBONE LAUNCHER"
level: 4
roles:
  - MINION
  - ARTILLERY
ancestry:
  - Undead
ev: 6 for four minions
stamina: 7
immunities: corruption 4, poison 4
speed: 5
size: 1M /
stability: 0
with-captain: Ranged distance +5
free_strike: 3
characteristics:
  - -2
  - +3
  - +0
  - +0
  - +0
actions:
  - name: "Hollowbone Slug"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 5 damage
      <br />✸ 17+ 7 damage; M< 3 [[bleeding]] (save ends) 
      <br />**Effect:** Each creature adjacent to the target takes 2 damage from exploding bone shards."
traits:
  - name: "Brittle Revenge"
    desc: "The hollowbone launcher explodes when they are reduced to 0 stamina, dealing 2 damage to each adjacent creature."

```
