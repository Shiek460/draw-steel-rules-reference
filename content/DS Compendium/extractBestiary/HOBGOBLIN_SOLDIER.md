# HOBGOBLIN SOLDIER
```statblock
name: "HOBGOBLIN SOLDIER"
level: 4
roles:
  - PLATOON
  - BRUTE
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 12
stamina: 70
immunities: fire 4
speed: 5
size: 1M /
stability: 2
free_strike: 6
characteristics:
  - +3
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Fire Flail"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 fire damage
      <br />★ 12–16 10 fire damage
      <br />✸ 17+ 13 fire damage 
      <br />**Effect:** The soldier doesn’t provoke opportunity attacks from each target until the end of the trooper’s turn."
maneuvers:
  - name: "Fight Me, Coward!"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** 1 creature 
      <br />**Effect:** The target is P< 2 [[taunted]] (EoT). While [[taunted]] by this ability, a creature takes 1d6 fire damage whenever they use an ability or attack that doesn’t target the soldier."
traits:
  - name: "Infernal Ichor"
    desc: "If the soldier’s stamina drops to 0, they spray burning blood. Each creature within 1 of the soldier takes 3 fire damage."


```
