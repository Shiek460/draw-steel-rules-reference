# GNOLL MAGE MAULER
```statblock
name: "GNOLL MAGE MAULER"
level: 2
roles:
  - MINION
  - HEXER
ancestry:
  - Abyssal
  - Gnoll
ev: 4 for four minions
stamina: 4
speed: 5
size: 1M /
stability: 1
with-captain: Melee distance +2
free_strike: 2
characteristics:
  - +2
  - +1
  - −1
  - 0
  - 0
actions:
  - name: "Wizard Ripper"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Strike
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 acid damage
      <br />★ 12–16 3 cold damage
      <br />✸ 17+ 5 lightning damage; target can’t use magic abilities (EoT) 
      <br />**Effect:** The target has a bane on their next power roll."
traits:
  - name: "Death Frenzy"
    desc: "Whenever an ally within 5 is reduced to 0 stamina, the gnoll moves up to their speed and makes a free strike."

```
