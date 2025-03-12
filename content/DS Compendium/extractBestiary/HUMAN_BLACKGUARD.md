# HUMAN BLACKGUARD
```statblock
name: "HUMAN BLACKGUARD"
level: 1
roles:
  - LEADER
ancestry:
  - Human
  - Humanoid
ev: 12
stamina: 80
immunities: Corruption 2, Psychic 2
speed: 5
size: 1M /
stability: 2
free_strike: 4
characteristics:
  - +3
  - +2
  - +2
  - +0
  - +2
actions:
  - name: "Zweihander Swing"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 1 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 damage; M< 1 [[slowed]] (save ends)
      <br />★ 12–16 6 damage; M< 2 [[slowed]] (save ends)
      <br />✸ 17+ 8 damage; M< 3 [[slowed]] (save ends) 
      <br />**Effect:** An ally within 10 of the blackguard can make a free strike. 
      <br />**1 Malice** The ally can use their signature action instead."
maneuvers:
  - name: "You!"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** One enemy 
      <br />**Effect:** The target is marked until the start of the blackguard’s next turn. The blackguard and each of their allies gain an edge on abilities used against targets marked by the blackguard."
traits:
  - name: "End Effect"
    desc: "At the end of their turn, the blackguard can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Supernatural Insight"
    desc: "The blackguard ignores concealment if it’s granted by a supernatural effect, or the target is supernatural."
ta:
  - name: "Parry!"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** Self or one ally 
      <br />**Trigger** A creature targets the blackguard or an ally adjacent to the blackguard with a strike. 
      <br />**Effect:** The damage is halved."
va:
  - name: "Advance! (Villain Action 1)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The blackguard shifts up to their speed. During or after this movement, they can use their Zweihander Swing twice."
  - name: "Back! (Villain Action 2)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** Slide 5."
  - name: "I Can Throw My Blade and So Should You! (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Magic, Ranged, Weapon
      <br />**Distance** 3 cube within 5
      <br />**Target** Each enemy in the cube 
      <br />**Effect:** The blackguard uses their Zweihander Swing against each enemy in the area. Each ally within 5 of the area can make a free strike against any enemy in the area."

```
