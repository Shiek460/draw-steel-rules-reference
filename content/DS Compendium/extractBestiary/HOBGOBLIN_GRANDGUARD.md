# HOBGOBLIN GRANDGUARD
```statblock
name: "HOBGOBLIN GRANDGUARD"
level: 6
roles:
  - PLATOON
  - DEFENDER
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 16
stamina: 111
immunities: fire 6
speed: 4
size: 2 /
stability: 4
free_strike: 6
characteristics:
  - +3
  - +2
  - +3
  - 0
  - +2
actions:
  - name: "Tower Shield Smash"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage
      <br />★ 12–16 14 damage
      <br />✸ 17+ 17+ damage; [[prone]]
      <br />**3 Malice** Each ally adjacent to a target that is knocked [[prone]] can make a free strike."
  - name: "Thunder Rush"
    desc:
      "
      <br />**Keywords** Area, Charge, Melee, Weapon
      <br />**Distance** 1 × 2 line within 1
      <br />**Target** All enemies and objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 11 damage
      <br />✸ 17+ 14 damage 
      <br />**Effect:** Push 10. The grandguard shifts into every 2 squares left behind by targets."
traits:
  - name: "Wide Guard"
    desc: "The grandguard imposes a bane on strikes against each ally within 2."
  - name: "Infernal Ichor"
    desc: "If the grandguard’s stamina drops to 0, they spray burning blood. Each creature within 1 of the grandguard takes 3 fire damage."


```
