# TIME RAIDER HELIX
```statblock
name: "TIME RAIDER HELIX"
level: 3
roles:
  - PLATOON
  - CONTROLLER
ancestry:
  - Humanoid
  - Time
  - Raider
ev: 10
stamina: 40
immunities: Psychic 3
speed: 5 (fly)
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - +0
  - +2
  - +2
  - +2
  - +2
actions:
  - name: "Blaster Volley"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Psionic, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** Three creatures
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 corruption damage; push 2
      <br />★ 12–16 8 corruption damage; push 4
      <br />✸ 17+ 11 corruption damage; push 6; [[prone]]"
maneuvers:
  - name: "Kinetic Lane"
    desc: "
      <br />**Keywords** Area, Psionic, Ranged
      <br />**Distance** 4 × 2 line within 10
      <br />**Target** Special 
      <br />**Effect:** The area becomes a psionically charged treadmill that pushes creatures and objects at high speed in one direction of the helix’s choice. Any creature that moves into the area or starts their turn there immediately slides 3 squares toward the square at the end of the area in the chosen direction. Each enemy in the area when it first appears takes 3 damage before they are moved. 
      <br />**3 Malice** The helix creates a second kinetic lane."
traits:
  - name: "Foresight"
    desc: "The helix doesn’t have a bane on strikes against concealed creatures."

```
