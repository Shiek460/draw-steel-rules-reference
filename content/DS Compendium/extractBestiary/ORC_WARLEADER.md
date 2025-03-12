# ORC WARLEADER
```statblock
name: "ORC WARLEADER"
level: 3
roles:
  - LEADER
ancestry:
  - Humanoid
  - Orc
ev: 20
stamina: 120
speed: 6
size: 1M /
stability: 2
free_strike: 5
characteristics:
  - +3
  - +2
  - +1
  - +2
  - +2
actions:
  - name: "Go."
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** 1 ally 
      <br />**Effect:** The target moves up to their speed and uses an action. 
      <br />**1 Malice** The warleader targets a second ally. 
      <br />**3 Malice** The warleader targets a squad instead of a second ally."
  - name: "Mace Lariat"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** All enemies
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 damage; push 1; M< 1 [[dazed]] (save ends)
      <br />★ 12–16 10 damage; push 3; M< 2 [[dazed]] (save ends)
      <br />✸ 17+ 13 damage; push 5; M< 3 [[dazed]] (save ends)"
maneuvers:
  - name: "Lockdown"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** 3 allies 
      <br />**Effect:** Each target moves up to their speed and uses the Grab maneuver with an edge. The warleader moves up to their speed."
ta:
  - name: "Courtesy Call"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature 
      <br />**Trigger** The target gets a tier 1 result on a power roll. 
      <br />**Effect:** The target has a double edge on next power roll."
va:
  - name: "Close In (Villain Action 1)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 10 Burst
      <br />**Target** All allies 
      <br />**Effect:** Each target moves up to their speed. Each enemy within 1 of a target makes a Might test.
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 [[frightened]] of the warleader (save ends)
      <br />★ 12–16 [[frightened]] of the warleader (EoT)
      <br />✦ 17+ no effect"
  - name: "Familial Reinforcements (Villain Action 2)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** Ranged 10
      <br />**Target** All allies 
      <br />**Effect:** The warleader shifts up to their speed and 5 orc blitzers appear in unoccupied spaces within distance."
  - name: "I’ll Do This Myself (Villain Action 3)"
    desc: "
      <br />**Keywords** Attack, Melee, Weapon
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The warleader shifts up to their speed and uses Mace Lariat. Then, the warleader shifts up to their speed and uses Mace Lariat. Finally, the warleader shifts up to their speed and uses Mace Lariat."
traits:
  - name: "End Effect"
    desc: "At the end of their turn, the warleader can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Relentless"
    desc: "If the warleader’s stamina drops to 0, they can take a free strike before dying. If the target is reduced to 0 stamina or killed by the strike, the dohma lives and their stamina is reduced to 1 instead."

```
