# SHADE
```statblock
name: "SHADE"
level: 1
roles:
  - MINION
  - AMBUSHER
ancestry:
  - Undead
ev: 3 for four minions
stamina: 4
immunities: corruption 1, poison 1
speed: 5 (fly, hover)
size: 1M/
stability: 1
with-captain:
speed: +2
free_strike: 2
characteristics:
  - −5
  - +1
  - 0
  - 0
  - +2
actions:
  - name: "Life Drain"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 corruption damage
      <br />★ 12–16 4 corruption damage
      <br />✸ 17+ 5 corruption damage; the target moves up to their speed away from all shades"
traits:
  - name: "Corruptive Phasing"
    desc: "The shade can move through other creatures and objects at normal speed. The first time in a round that the shade passes through a creature, that creature takes 2 corruption damage. The shade doesn’t take damage from being force moved into objects."

```
