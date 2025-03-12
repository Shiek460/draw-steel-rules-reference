# HOBGOBLIN DEATH CAPTAIN
```statblock
name: "HOBGOBLIN DEATH CAPTAIN"
level: 4
roles:
  - PLATOON
  - SUPPORT
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 12
stamina: 60
immunities: fire 4
speed: 5
size: 1M /
stability: 2
free_strike: 5
characteristics:
  - +2
  - 0
  - +1
  - 0
  - +2
actions:
  - name: "Blightblade"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage
      <br />★ 12–16 8 damage; 4 corruption damage
      <br />✸ 17+ 8 damage; 7 corruption damage 
      <br />**Effect:** The next strike made against the target has a double edge. 
      <br />**Cost** 3 Malice 1 ally adjacent to the target uses their signature action."
maneuvers:
  - name: "On My Mark!"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 5
      <br />**Target** 1 ally 
      <br />**Effect:** The target moves up to their speed and makes a free strike."
traits:
  - name: "Battle Ready"
    desc: "The death captain and each ally within 2 impose a bane on strikes made against them by hidden creatures."
  - name: "Infernal Ichor"
    desc: "If the death captain’s stamina drops to 0, they spray burning blood. Each creature within 1 of the death captain takes 3 fire damage."


```
