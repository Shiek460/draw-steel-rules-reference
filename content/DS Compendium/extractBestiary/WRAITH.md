# WRAITH
```statblock
name: "WRAITH"
level: 4
roles:
  - BAND
  - HEXER
ancestry:
  - Undead
ev: 6
stamina: 25
immunities: corruption 4, poison 4
speed: 8 (fly, hover)
size: 1M /
stability: 0
free_strike: 2
characteristics:
  - -2
  - +2
  - +1
  - +1
  - +3
actions:
  - name: "Chilling Gravetouch"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 cold damage; P< 1 [[slowed]] (save ends)
      <br />★ 12–16 7 cold damage; P< 2 [[slowed]] (save ends)
      <br />✸ 17+ 9 cold damage; P< 3 [[slowed]] (save ends) 
      <br />**Effect:** Living creatures killed by this ability return as a ghoul craver the next round, under the Director’s control."
maneuvers:
  - name: "Hidden Movement"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The specter turns invisible, moves up to their speed, and becomes visible again."
ta:
  - name: "Stolen Vitality (Free Triggered Action)"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** 1 enemy 
      <br />**Trigger** The target regains stamina. 
      <br />**Effect:** The target only regains half the stamina they would normally. The wraith regains the remaining stamina."
traits:
  - name: "Agonizing Phasing"
    desc: "The wraith can move through other creatures and objects at normal speed. The first time in a round that the shade passes through a creature, that creature takes 5 corruption damage and has a bane on their next attack. The wraith doesn’t take damage from being force moved into objects."

```
