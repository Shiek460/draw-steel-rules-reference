# KOBOLD CENTURION
```statblock
name: "KOBOLD CENTURION"
level: 1
roles:
  - LEADER
ancestry:
  - Humanoid
  - Kobold
ev: 12
stamina: 80
speed: 5
size: 1S /
stability: 2
free_strike: 2
characteristics:
  - +2
  - +3
  - +2
  - +0
  - +2
actions:
  - name: "Pilum"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 10
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 damage; M< 1 [[weakened]] (save ends)
      <br />★ 12–16 10 damage; M< 2 [[weakened]] (save ends)
      <br />✸ 17+ 13 damage; M< 3 [[weakened]] (save ends) 
      <br />**Effect:** Each ally adjacent to a target of this ability can make a free strike. <br />**3 Malice** Each target [[weakened]] by this ability is now [[restrained]] while they are [[weakened]]."
maneuvers:
  - name: "Concentrate All Fire on That Hero!"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** One enemy 
      <br />**Effect:** The target is marked until the start of the centurion’s next turn. The centurion and each of their allies have an edge on power rolls made against targets marked by the centurion. 
      <br />**3+ Malice** The centurion targets 1 additional enemy for every 3 malice spent."
ta:
  - name: "Testudo!"
    desc: "
      <br />**Keywords** Weapon 
      <br />**Trigger** A creature uses an ability against the centurion or an ally.
      <br />**Distance** 5 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Each target shifts 2 before the damage is resolved. All kobolds with Shield? Shield! has damage immunity 2 against the triggering ability "
  - name: "Firetail Pilum (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Weapon
      <br />**Distance** 10 × 1 line within 1
      <br />**Target** All enemies in the line 
      <br />**Effect:** The centurion uses Pilum against each target, dealing an additional 5 damage. Each [[weakened]] target takes 2 fire damage at the start of each of their turns until the condition ends."
  - name: "Boom Pilum! (Villain Action 2)"
    desc: "
      <br />**Keywords** Area, Weapon
      <br />**Distance** 5 cube within 10
      <br />**Target** All enemies in the cube 
      <br />**Effect:** The centurion uses Pilum against each target with a double edge. Each target is then pushed 3."
  - name: "Are You Not Entertained?! (Villain Action 3)"
    desc: "
      <br />**Keywords** Attack, Ranged, Weapon
      <br />**Distance** 10 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** Each target is P< 2 [[taunted]] (save ends). For the rest of the encounter the centurion has damage immunity 2. All allies within 10 of the centurion can make a free strike."
traits:
  - name: "End Effect"
    desc: "At the end of their turn, the centurion can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Shield? Shield!"
    desc: "The centurion has cover, a stability of 3, and can act as cover for allies when adjacent to an ally who also has this trait."

```
