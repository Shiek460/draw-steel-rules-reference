# HOBGOBLIN SMOKEBINDER
```statblock
name: "HOBGOBLIN SMOKEBINDER"
level: 5
roles:
  - PLATOON
  - AMBUSHER
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 14
stamina: 70
immunities: fire 5
speed: 7 (fly, hover)
size: 1M /
stability: 0
free_strike: 6
characteristics:
  - +1
  - +3
  - +2
  - +1
  - 0
actions:
  - name: "Choking Bolt"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 5
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 fire damage
      <br />★ 12–16 14 fire damage
      <br />✸ 17+ 17+ fire damage; R< 3 [[slowed]] (save ends) 
      <br />**Effect:** If the smokebinder had an edge on the power roll, the target cannot communicate with anyone until the end of their next turn."
maneuvers:
  - name: "Smoke Bomb"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 3 Burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** Each target makes a Might test.
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 11 damage; target has a double bane on their next power roll
      <br />★ 12–16 9 damage; target has a bane on their next power roll
      <br />✦ 17+ 5 damage"
traits:
  - name: "Essence of Smoke"
    desc: "The smokebinder can move through other creatures and objects at normal speed. The smokebinder automatically hides at the end of their turn if they didn’t take any damage since their last turn."
  - name: "Infernal Ichor"
    desc: "If the smokebinder’s stamina drops to 0, they spray burning blood. Each creature within 1 of the smokebinder takes 3 fire damage."

```
