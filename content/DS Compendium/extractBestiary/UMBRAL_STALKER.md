 S# UMBRAL STALKER
```statblock
name: "UMBRAL STALKER"
level: 1
roles:
  - BAND
  - AMBUSHER
ancestry:
  - Undead
ev: 3
stamina: 15
immunities: corruption 1, poison 1
speed: 7 (climb)
size: 1M/
stability: 1
free_strike: 2
characteristics:
  - 0
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Chilling Grasp"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Strike
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 cold damage
      <br />★ 12–16 6 cold damage
      <br />✸ 17+ 7 cold damage 
      <br />**Effect:** The umbral stalker shifts 2 before or after using this ability."
  - name: "Freezing Dark"
    desc:
      "
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 cube within 1
      <br />**Target** Each enemy in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 cold damage
      <br />★ 12–16 3 cold damage
      <br />✸ 17+ 4 cold damage 
      <br />**Effect:** Until the end of the umbral stalker’s next turn, the area is concealed and blocks [[Line of Effect]] for all enemies."
maneuvers:
  - name: "Shadow Jump (Free Maneuver)"
    desc: "
      <br />**Cost** 1 Malice
      <br />The umbral stalker teleports to an unoccupied space in concealment within 10 squares."
traits:
  - name: "Corruptive Phasing"
    desc: "The umbral stalker can move through other creatures and objects at normal speed. The first time in a round that the umbral stalker passes through a creature, that creature takes 2 corruption damage. The umbral stalker doesn’t take damage from being force moved into objects."

```
