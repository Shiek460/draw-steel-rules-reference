# ZOMBIE
```statblock
name: "ZOMBIE"
level: 1
roles:
  - BAND
  - BRUTE
ancestry:
  - Undead
ev: 3
stamina: 20
immunities: corruption 1, poison 1
speed: 5
size: 1M /
stability: 1
free_strike: 2
characteristics:
  - +2
  - +1
  - −5
  - −2
  - +1
actions:
  - name: "Clobber and Clutch"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 6 damage
      <br />✸ 17+ 7 damage; [[grabbed]] 
      <br />**Effect:** A target who starts their turn [[grabbed]] by the zombie takes 2 corruption damage. If a creature takes 5 or more corruption damage this way, they become insatiably hungry for flesh. The target must complete the Find a Cure project to end this effect."
maneuvers:
  - name: "Breakfall"
    desc: "
      <br />**Keywords** Area, Melee
      <br />**Distance** 2 burst
      <br />**Target** Each enemy in the burst 
      <br />**Effect:** The zombie falls [[prone]], expelling a wave of rot and dust.
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 corruption damage
      <br />★ 12–16 3 corruption damage; M< 1 [[weakened]] (save ends)
      <br />✸ 17+ 4 corruption damage; M< 2 [[dazed]] (save ends)"
traits:
  - name: "Endless Knight"
    desc: "The first time the zombie is reduced to stamina 0 by damage that isn’t fire damage or holy damage and their body isn’t destroyed, they regain their full stamina and fall [[prone]]."

```
