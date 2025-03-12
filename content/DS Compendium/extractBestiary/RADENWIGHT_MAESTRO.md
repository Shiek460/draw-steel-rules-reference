# RADENWIGHT MAESTRO
```statblock
name: "RADENWIGHT MAESTRO"
level: 1
roles:
  - LEADER
ancestry:
  - Humanoid
  - Radenwight
ev: 12
stamina: 80
speed: 5 (climb)
size: 1S /
stability: 1
free_strike: 4
characteristics:
  - −2
  - +2
  - +0
  - +0
  - +3
actions:
  - name: "Cacophony"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 3 sonic damage; slide 1; shift 1
      <br />★ 12–16 6 sonic damage; slide 3; shift 3
      <br />✸ 17+ 8 sonic damage; slide 5; shift 5 
      <br />**Effect:** Each ally within distance can use Ready Rodent as a free triggered action once before the end of the round."
maneuvers:
  - name: "Tempo Change"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** Two enemies
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 P< 1 [[slowed]] (save ends)
      <br />★ 12–16 P< 2 [[slowed]] (save ends)
      <br />✸ 17+ P< 3 [[slowed]] (save ends) 
      <br />**3 Malice** Each ally within 3 of a target has their speed increased by 2 until the end of their next turn."
ta:
  - name: "Ever Ready Rodent (Free Triggered Action)"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** Magic, Melee, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** One creature 
      <br />**Trigger** The target deals damage to an ally or takes damage from an ally. 
      <br />**Effect:** The maestro makes a free strike against the target."
traits:
  - name: "End Effect"
    desc: "At the end of their turn, the maestro can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Overture (Villain Action 1)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 10 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Each target shifts up to their speed or takes the Defend action."
  - name: "Solo Act (Villain Action 2)"
    desc: "
      <br />**Keywords** Ranged
      <br />**Distance** Ranged 15
      <br />**Target** One creature 
      <br />**Effect:** Until the end of their next turn, the target halves incoming damage, deals an additional 4 damage on strikes, and their speed is doubled."
  - name: "Rondo of Rat (Villain Action 3)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 10 burst
      <br />**Target** All dead allies in the burst 
      <br />**Effect:** Each target stands, makes a free strike, then collapses again. Allies of the targets can use Ready Rodent as a free triggered action once in conjunction with these free strikes."

```
