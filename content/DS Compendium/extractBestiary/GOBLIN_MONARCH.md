# GOBLIN MONARCH
```statblock
name: "GOBLIN MONARCH"
level: 1
roles:
  - LEADER
ancestry:
  - Goblin
  - Humanoid
ev: 12
stamina: 80
speed: 6 (climb)
size: 1S /
stability: 1
free_strike: 4
characteristics:
  - +3
  - +2
  - −4
  - +0
  - −3
actions:
  - name: "Handaxe"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 10 damage
      <br />✸ 17+ 13 damage 
      <br />**Effect:** An ally within 10 of the monarch can make a free strike."
maneuvers:
  - name: "Get in Here!"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Ranged 20
      <br />**Target** Special 
      <br />**Effect:** Two goblin runners appear in unoccupied spaces."
ta:
  - name: "Meat Shield"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** One ally 
      <br />**Trigger** A creature targets the monarch with a strike. 
      <br />**Effect:** The ally becomes the target of the triggering strike instead. End 
      <br />**Effect:** At the end of their turn, the monarch can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
traits:
  - name: "Crafty"
    desc: "The goblin doesn’t provoke opportunity attacks by moving."
va:
  - name: "What Are You Waiting For? (Villain Action 1)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 10 burst
      <br />**Target** Each ally 
      <br />**Effect:** Each target can move up to their speed or make a free strike. "
  - name: "Focus Fire (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** One enemy 
      <br />**Effect:** Each ally within 10 squares of the enemy can move up to their speed toward the enemy. "
  - name: "Kill! (Villain Action 3)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 10 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Each target can make a free strike, dealing an additional 3 damage."


```
