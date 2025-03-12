# LIZARDFOLK DEATHREX
```statblock
name: "LIZARDFOLK DEATHREX"
level: 1
roles:
  - LEADER
ancestry:
  - Humanoid
  - Lizardfolk
ev: 12
stamina: 80
speed: 5 (climb, swim)
size: 2 /
stability: 2
free_strike: 4
characteristics:
  - +3
  - +2
  - 0
  - +1
  - +2
actions:
  - name: "Ripper Spear"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 damage; pull 1; A< 1 [[bleeding]] (save ends)
      <br />★ 12–16 10 damage; pull 1; A< 2 [[bleeding]] (save ends)
      <br />✸ 17+ 13 damage; pull 2; A< 3 [[bleeding]] (save ends) 
      <br />**1 Malice** One target that is adjacent to the deathrex is [[grabbed]] by the deathrex’s mouth."
  - name: "Death Roll"
    desc:
      "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 [[grabbed]] creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; M< 1 [[dazed]] (save ends)
      <br />★ 12–16 12 damage; M< 2 [[dazed]] (save ends)
      <br />✸ 17+ 15 damage; M< 3 [[dazed]] (save ends) 
      <br />**Effect:** The target is released from the grab and slides 5."
maneuvers:
  - name: "Trundle"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The deathrex moves up to their speed. The deathrex can make a free strike on each creature that makes an opportunity attack against them during this movement."
ta:
  - name: "Swat The Fly"
    desc: "
      <br />**Keywords** — 
      <br />**Trigger** The target moves or shifts away from the deathrex.
      <br />**Distance** Melee 1
      <br />**Target** 1 adjacent creature or object 
      <br />**Effect:** Slide 5."
  - name: "Snack Attack (Villain Action 1)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** Self and 10 burst
      <br />**Target** Self and all allies in the burst 
      <br />**Effect:** Each target moves up to their speed and makes a free strike. A target receives temporary stamina: equal to the amount of damage they dealt during this action."
  - name: "Shed Some Skin (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The deathrex shifts up to their speed, leaving behind a skin shed duplicate in the space that they started in. The duplicate has 10 stamina, has no villain actions, shares the rest of the deathrex’s characteristics, and takes their turn at the same time as the deathrex."
  - name: "Thresher Thrasher (Villain Action 3)"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** Self and 10 burst
      <br />**Target** Self and all allies in the burst 
      <br />**Effect:** Each target moves up to their speed. Until the end of the encounter, when a creature enters or starts their turn adjacent to a target, the target can make a free strike against them."
traits:
  - name: "Rex Reptilian Escape"
    desc: " While the deathrex still has a tail, whenever the deathrex is inflicted with an EoT or save ends effect, the deathrex can lose their tail to immediately end the effect and shift 2."

```
