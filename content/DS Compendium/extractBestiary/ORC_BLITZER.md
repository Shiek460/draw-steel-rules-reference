# ORC BLITZER
```statblock
name: "ORC BLITZER"
level: 1
roles:
  - MINION
  - HARRIER
ancestry:
  - Humanoid
  - Orc
ev: 3 for four minions
stamina: 4
speed: 7
size: 1M /
stability: 0
with-captain:
speed: +2
free_strike: 1
characteristics:
  - +1
  - +2
  - 0
  - 0
  - 0
actions:
  - name: "Lugged Spear"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage
      <br />★ 12–16 2 damage
      <br />✸ 17+ 3 damage 
      <br />**Effect:** The target takes 3 damage if they start their next turn adjacent to 3 or more blitzers."
traits:
  - name: "Bloodfire Burn"
    desc: "If the blitzer’s stamina drops to 0, they can make a free strike before dying."

```
