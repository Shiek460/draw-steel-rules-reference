# HUMAN BANDIT CHIEF
```statblock
name: "HUMAN BANDIT CHIEF"
level: 3
roles:
  - LEADER
ancestry:
  - Human
  - Humanoid
ev: 20
stamina: 120
immunities: Corruption 4, Psychic 4
speed: 5
size: 1M /
stability: 2
free_strike: 5
characteristics:
  - +2
  - +3
  - +2
  - +3
  - +2
actions:
  - name: "Whip & Magic Longsword"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** Two enemies or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; pull 1
      <br />★ 12–16 12 damage; pull 2
      <br />✸ 17+ 15 damage; pull 3 
      <br />**Effect:** A target who is adjacent to the bandit chief after the ability resolves takes 5 corruption damage.
      <br />**2 Malice** The bandit chief targets an additional enemy or object."
maneuvers:
  - name: "Kneel, Peasant!"
    desc: "
      <br />**Keywords** Melee, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One enemy or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 Push 1; M< 1 [[prone]]
      <br />★ 12–16 Push 2; M< 2 [[prone]]
      <br />✸ 17+ Push 4; M< 3 [[prone]] 
      <br />**2 Malice** This ability targets each enemy adjacent to the bandit chief."
ta:
  - name: "Bloodstones"
    desc: "
      <br />**Keywords** Magic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The bandit chief makes a power roll. 
      <br />**Effect:** The bandit chief takes 4 corruption damage and increases the result of the power roll by one tier. End 
      <br />**Effect:** At the end of their turn, the bandit chief can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
traits:
  - name: "Supernatural Insight"
    desc: "The bandit chief ignores concealment if it’s granted by a supernatural effect, or the target is supernatural."
va:
  - name: "Shoot! (Villain Action 1)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 10 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Each target makes a ranged free strike."
  - name: "Form Up! (Villain Action 2)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 10 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Each target shifts up to their speed. Until the end of the encounter, the bandit chief and all allies have damage immunity 2 while adjacent to a target."
  - name: "Lead From the Front (Villain Action 3)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Shift 10. During or after this movement, the bandit chief can use their Whip & Magic Longsword against up to four targets. Each ally adjacent to a target can make a free strike against them."


```
