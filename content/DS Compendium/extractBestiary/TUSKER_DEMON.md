# TUSKER DEMON
```statblock
name: "TUSKER DEMON"
level: 2
roles:
  - BAND
  - BRUTE
ancestry:
  - Abyssal
  - Demon
  - Gnoll
ev: 4
stamina: 34
speed: 7
size: 3 /
stability: 3
free_strike: 3
characteristics:
  - +2
  - −1
  - −3
  - 0
  - −1
actions:
  - name: "Gore"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; push 1
      <br />★ 12–16 6 damage; push 2
      <br />✸ 17+ 8 damage; push 3; [[prone]] 
      <br />**Effect:** This ability deals an additional 4 damage while charging."
ta:
  - name: "Vengeful Tusker"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 7
      <br />**Target** Triggering enemy 
      <br />**Trigger** An enemy within distance deals damage to the tusker. 
      <br />**Effect:** The tusker demon charges the target using Gore."
traits:
  - name: "Trample"
    desc: "The tusker demon can move through enemies and objects at normal speed. When the tusker enters a creature’s space for the first time on their turn, the creature takes 5 damage. The tusker demon can end their turn in a [[prone]] size 1 creature’s space, preventing the creature from getting up."
  - name: "Lethe"
    desc: "While [[winded]], the tusker demon has an edge on strikes, and strikes have an edge against them."


```
