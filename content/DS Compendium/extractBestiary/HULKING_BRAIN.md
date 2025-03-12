# HULKING BRAIN
```statblock
name: "HULKING BRAIN"
level: 6
roles:
  - TROOP
  - BRUTE
ancestry:
  - Horror
  - Voiceless Talker
ev: 32
stamina: 180
speed: 5
size: 1L /
stability: 4
free_strike: 7
characteristics:
  - +3
  - +1
  - -2
  - -2
  - +0
actions:
  - name: "Four-Way Grasp"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 4 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 10 damage; A< 2 [[grabbed]]
      <br />✸ 17+ 11 damage; A< 3 [[grabbed]] 
      <br />**2 Malice** The potency of this ability increases by 1."
  - name: "Cerebral Suplex"
    desc:
      "
      <br />**Keywords** Melee
      <br />**Distance** Melee 1
      <br />**Target** All [[grabbed]] enemies
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 damage; M< 1 3 damage
      <br />★ 12–16 10 damage; M< 2 3 damage
      <br />✸ 17+ 13 damage; M< 3 6 damage 
      <br />**Effect:** Each target is no longer [[grabbed]]."
maneuvers:
  - name: "Lumber"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Shift 4. This movement ignores difficult terrain."
ta:
  - name: "Brawny Buffer (Free Triggered Action)"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Ranged 5
      <br />**Target** Self 
      <br />**Trigger** An ally voiceless talker takes damage from an enemy 
      <br />**Effect:** The hulking brain shifts to a square adjacent to the ally and takes the damage instead.
      <br />**2 Malice** The enemy that dealt damage is knocked [[prone]]."
traits:
  - name: "Biceps to Spare"
    desc: "The hulking brain can carry up to 4 size 1 [[grabbed]] creatures at no penalty to their movement."
  - name: "Psionic Conductor"
    desc: "When a non-minion Voiceless Talker within 5 of the hulking brain uses an ability with the Psionic keyword, they can do so as if they were in the hulking brain’s space."

```
