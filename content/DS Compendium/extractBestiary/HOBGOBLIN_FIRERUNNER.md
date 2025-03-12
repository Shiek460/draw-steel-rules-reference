# HOBGOBLIN FIRERUNNER
```statblock
name: "HOBGOBLIN FIRERUNNER"
level: 5
roles:
  - PLATOON
  - HARRIER
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 14
stamina: 70
immunities: fire 5
speed: 8
size: 1M /
stability: 0
free_strike: 6
characteristics:
  - +2
  - +3
  - +1
  - +1
  - 0
actions:
  - name: "Flaming Kick"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Magic, Strike, Melee
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 fire damage
      <br />★ 12–16 13 fire damage
      <br />✸ 17+ 16 fire damage; A< 3 [[dazed]] (EoT)"
maneuvers:
  - name: "Blazing Trail"
    desc: "
      <br />**Keywords** Magic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The firerunner moves up to their speed and creates a 8 wall of fire. Each segment must include one of the squares the firerunner touched. Creatures can enter and pass through the wall. Any enemy who enters the wall for the first time in a round or starts their turn there takes 5 fire damage."
traits:
  - name: "Hot to Go"
    desc: "The firerunner ignores difficult terrain. Whenever the firerunner takes fire damage, their speed and the wall they can create with Blazing Trail increases by 4 until the end of their next turn."
  - name: "Infernal Ichor"
    desc: "If the firerunner’s stamina drops to 0, they spray burning blood. Each creature within 1 of the firerunner takes 3 fire damage."


```
