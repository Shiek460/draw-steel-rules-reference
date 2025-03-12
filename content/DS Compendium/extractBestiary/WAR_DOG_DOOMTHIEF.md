# WAR DOG DOOMTHIEF
```statblock
name: "WAR DOG DOOMTHIEF"
level: 5
roles:
  - BAND
  - DEFENDER
ancestry:
  - Humanoid
  - War
  - Dog
ev: 7
stamina: 40
speed: 5
size: 1L /
stability: 2
free_strike: 3
characteristics:
  - +3
  - -1
  - +0
  - +3
  - +1
actions:
  - name: "Ripper Shrikegun"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Weapon
      <br />**Distance** 10 x 3 line within 1
      <br />**Target** all enemies
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 3 damage; push 1
      <br />★ 12  -16 5 damage; push 3
      <br />✦ 17+ 6 damage; push 5; A< 3 [[slowed]] (save ends) 
      <br />**Effect:** The doomthief cannot move on the same turn they use this ability."
traits:
  - name: "Doom Magnet"
    desc: "The doomthief emits a 3 aura of warped fate, blocking [[Draw Steel Rules#LINE OF EFFECT|line of effect]] for enemy abilities that don’t include the doomthief as a target."
  - name: "Loyalty Collar"
    desc: "When the doomthief dies, they explode, dealing 2d6 damage to each adjacent enemy."
maneuvers:
  - name: "Expanding Doom"
    desc: "
      <br />**Cost** 4 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The doomthief gains damage immunity 4 and their doom magnet aura increases by 3 until the start of their next turn."


```
