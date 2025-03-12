# GOBLIN STINKER
```statblock
name: "GOBLIN STINKER"
level: 1
roles:
  - BAND
  - CONTROLLER
ancestry:
  - Goblin
  - Humanoid
ev: 3
stamina: 10
speed: 5 (climb)
size: 1S /
stability: 0
free_strike: 1
characteristics:
  - −2
  - +1
  - +0
  - +0
  - +2
actions:
  - name: "Toxic Winds"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 3 cube within 15
      <br />**Target** Each enemy in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 poison damage; slide 1
      <br />★ 12–16 2 poison damage; slide 2
      <br />✸ 17+ 3 poison damage; slide 3 <br />**1+ Malice** Increase the slide for one target by 2 squares for each malice spent."
maneuvers:
  - name: "Swamp Gas"
    desc: "
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 3 cube within 10
      <br />**Target** Special 
      <br />**Effect:** The area is filled with a green haze until the start of the stinker’s next turn or until the stinker is reduced to stamina 0. The area is difficult terrain for non-goblin creatures, and each such creature who moves within the area takes 2 poison damage for each square moved. The haze can’t be dispersed by wind."
traits:
  - name: "Crafty"
    desc: "The goblin doesn’t provoke opportunity attacks by moving."

```
