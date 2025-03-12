# WODE ELF WARLEADER
```statblock
name: "WODE ELF WARLEADER"
level: 3
roles:
  - LEADER
ancestry:
  - Fey
  - Humanoid
  - Wode
  - Elf
ev: 20
stamina: 120
speed: 7 (teleport)
size: 1M /
stability: 2
free_strike: 5
characteristics:
  - +2
  - +3
  - +2
  - +2
  - +2
actions:
  - name: "Wodeblade"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; M< 1 [[restrained]] (save ends)
      <br />★ 12–16 12 damage; M< 2 [[restrained]] (save ends)
      <br />✸ 17+ 15 damage; M< 3 [[restrained]] (save ends) 
      <br />**Effect:** The warleader strikes each target one at a time and can teleport 3 squares between each strike. <br />**2 Malice** A target [[restrained]] by this ability takes an additional 3 damage."
maneuvers:
  - name: "Fairness is a Human Concept"
    desc: "
      <br />**Cost** 5 Malice
      <br />**Keywords** Area
      <br />**Distance** 10 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Each target can make a free strike and then shifts 3. A target immediately hides at the end of the warleader’s turn while in cover or concealment."
ta:
  - name: "Wode Sickness"
    desc: "
      <br />**Keywords** — 
      <br />**Trigger** An ally ends their turn.
      <br />**Distance** Ranged 10
      <br />**Target** 1 enemy 
      <br />**Effect:** The target must take their turn now, if they have not already taken it. P< 2 the target is [[bleeding]] and has a bane on their strikes until the end of their turn."
traits:
  - name: "End Effect"
    desc: "At the end of their turn, the warleader can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Masking Glamor"
    desc: "The elf immediately hides at the end of their turn while in cover or concealment, even if they are observed." 
va:
  - name: "You Will ALL Witness my Blade (Villain Action 1)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 5 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** The warleader uses Wodeblade against each target with an edge."
  - name: "Suppressing Volley (Villain Action 2)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 5 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** The warleader uses Wodeblade against a single creature or object. Each target then makes a free strike."
  - name: "Is it Now or is it Then? Where are We? (Villain Action 3)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** Self and 5 burst
      <br />**Target** Self and all allies in the burst 
      <br />**Effect:** Each target becomes invisible until the start of the next round. The warleader then uses Wodeblade."


```
