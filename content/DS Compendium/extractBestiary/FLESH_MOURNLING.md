# FLESH MOURNLING
```statblock
name: "FLESH MOURNLING"
level: 4
roles:
  - BAND
  - DEFENDER
ancestry:
  - Undead
ev: 6
stamina: 35
immunities: corruption 4, poison 4
speed: 6
size: 2 /
stability: 2
free_strike: 2
characteristics:
  - +3
  - +1
  - 0
  - +2
  - -1
actions:
  - name: "Multiarm Strike"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 1 creature or object
      <br />✸ ≤11 5 damage
      <br />★ 12–16 7 damage
      <br />`dice: 2d10 + 3`
      <br />✦ 17+ 9 damage 
      <br />**Effect:** The target can’t shift away from the mournling until the end of their turn. 
      <br />**1 Malice** The mournling targets an additional creature."
  - name: "Horrid Wail"
    desc:
      "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 burst
      <br />**Target** all enemies in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 2 psychic damage
      <br />★ 12–16 3 psychic damage; I< 2 [[frightened]] (save ends)
      <br />✸ 17+ 4 psychic damage; I< 3 [[frightened]] (save ends) 
      <br />**Effect:** If a target is still [[frightened]] by this ability at the end of the encounter, they cannot take a respite activity during their next respite"
traits:
  - name: "Immutable Form"
    desc: "The mournling’s shape can’t change via any external effects." 
  - name: "Arise"
    desc: "The first time in an encounter that the mournling is reduced to 0 stamina with non-fire/non-holy damage and their body isn’t destroyed, they regain half their stamina and fall [[prone]]."

```
