# HOBGOBLIN INCENDIARIST
```statblock
name: "HOBGOBLIN INCENDIARIST"
level: 5
roles:
  - PLATOON
  - ARTILLERY
ancestry:
  - Goblin
  - Hobgoblin
  - Humanoid
  - Infernal
ev: 14
stamina: 60
immunities: fire 5
speed: 5
size: 1M /
stability: 0
free_strike: 6
characteristics:
  - +1
  - +3
  - 0
  - +2
  - +1
actions:
  - name: "Fire Crossbow"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 fire damage
      <br />★ 12–16 14 fire damage
      <br />✸ 17+ 17+ fire damage; A< 3 burning (save ends) 
      <br />**Effect:** A burning target takes 1d6 fire damage at the start of each of their turns until the condition ends."
  - name: "Fire Ball Volley"
    desc:
      "
      <br />**Keywords** Area, Ranged
      <br />**Distance** 4 Cube within 10
      <br />**Target** All enemies and objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 fire damage; A< 1 burning (save ends)
      <br />★ 12–16 9 fire damage; A< 2 burning (save ends)
      <br />✸ 17+ 11 fire damage; [[prone]]; A< 3 burning (save ends)"
traits:
  - name: "Raining Cinders"
    desc: "The ranged free strike of each ally within 3 of the incendiarist has a distance of 10 and it now deals fire damage."
  - name: "Infernal Ichor"
    desc: "If the incendiarist’s stamina drops to 0, they spray burning blood. Each creature within 1 of the incendiarist takes 3 fire damage."


```
