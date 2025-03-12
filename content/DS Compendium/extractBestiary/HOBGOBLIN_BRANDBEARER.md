# HOBGOBLIN BRANDBEARER
```statblock
name: "HOBGOBLIN BRANDBEARER"
level: 4
roles:
  - MINION
  - HEXER
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 6 for four minions
stamina: 7
immunities: fire 2
speed: 5
size: 1M /
stability: 0
with-captain: Edge on strikes
free_strike: 2
characteristics:
  - 0
  - +1
  - +2
  - 0
  - +3
actions:
  - name: "Searing Grasp"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Strike
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 2 fire damage
      <br />★ 12–16 4 fire damage; M< 2 fire weakness 5 (save ends)
      <br />✸ 17+ 6 fire damage; M< 3 fire weakness 5 (save ends)"
  - name: "Open Furnace" 
    desc: "An enemy that takes fire damage receives 1 additional fire damage for each adjacent brandbearer."
  - name: "Infernal Ichor" 
    desc: "If the brandbearer’s stamina drops to 0, they spray burning blood. Each creature within 1 of the brandbearer takes 2 fire damage."


```
