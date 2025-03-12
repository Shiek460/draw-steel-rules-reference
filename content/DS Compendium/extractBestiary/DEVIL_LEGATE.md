# DEVIL LEGATE
```statblock
name: "DEVIL LEGATE"
level: 5
roles:
  - TROOP
  - DEFENDER
ancestry:
  - Devil
  - Infernal
ev: 28
stamina: 160
immunities: Fire 5
speed: 6
size: 1M /
stability: 2
free_strike: 6
characteristics:
  - +3
  - +1
  - 0
  - +1
  - +2
actions:
  - name: "Infernal Pike"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage
      <br />★ 12–16 14 damage; A<  2 [[slowed]] (save ends)
      <br />✸ 17+ 17+ damage; A<  3 [[slowed]] (save ends) 
      <br />**Effect:** If the targets are adjacent to each other, this ability deals an additional 3 damage."
  - name: "Writ of Execution"
    desc:
      "
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 6 damage; M<  1 [[prone]]
      <br />★ 12–16 11 damage; M<  2 [[prone]] can’t stand (save ends)
      <br />✦ 17+ 14 damage; M<  3 [[prone]] can’t stand (save ends) 
      <br />**Effect:** If the legate charges while using this ability, they ignore difficult terrain and target each creature and object they move through with the power roll (but not its additional effects)."
maneuvers:
  - name: "Law and Order"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** 1 creature 
      <br />**Effect:** The target is [[taunted]] by the legate (save ends). The legate can only have one creature [[taunted]] at a time."
ta:
  - name: "Devilish Charm"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** Magic
      <br />**Distance** Ranged 5
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature targets the legate with a strike. 
      <br />**Effect:** The target makes a Might test.
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 The legate chooses a new target for the strike
      <br />★ 12–16 The legate halves the incoming damage
      <br />✦ 17+ The target is [[dazed]] (EoT) Hellish Bailiff The legate has damage immunity 3 while in one of the nine Hells or within 10 squares of a non minion devil that is a higher level than them."
traits:
  - name: "True Name"
    desc: "If a creature within 10 squares of the legate speaks the legate’s true name aloud, the legate loses their immunities, the additional effects on their signature action, and their Devilish Charm ability."


```
