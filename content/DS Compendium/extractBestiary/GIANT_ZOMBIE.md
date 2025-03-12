# GIANT ZOMBIE
```statblock
name: "GIANT ZOMBIE"
level: 4
roles:
  - TROOP
  - BRUTE
ancestry:
  - Undead
ev: 24
stamina: 140
immunities: corruption 4, poison 4
speed: 6
size: 3 /
stability: 2
free_strike: 6
characteristics:
  - +3
  - -1
  - -2
  - +1
  - +2
actions:
  - name: "Rotten Smash"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage
      <br />★ 12–16 14 damage; A< 2 [[grabbed]]
      <br />✸ 17+ 17+ damage; A< 3 [[grabbed]]"
ta:
  - name: "Knocking Heads"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Two creatures or objects 
      <br />**Trigger** The giant zombie grabs both targets or starts their turn with each target [[grabbed]]. 
      <br />**Effect:** The giant zombie smashes the targets together, using their Rotten Smash against both targets with a double edge."
traits:
  - name: "Negative Nerves"
    desc: "When the giant zombie is targeted by an ability, they halve the damage from any tier-1 results."
  - name: "Arise"
    desc: "The first time the giant zombie is reduced to 0 stamina with non  -fire/non  -holy damage and their body isn’t destroyed, they regain half their stamina and fall [[prone]]."

```
