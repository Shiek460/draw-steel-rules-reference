# HUMAN DEATH CULTIST
```statblock
name: "HUMAN DEATH CULTIST"
level: 2
roles:
  - PLATOON
  - SUPPORT
ancestry:
  - Human
  - Humanoid
ev: 8
stamina: 40
immunities: Corruption 2, Psychic 2
speed: 5
size: 1M /
stability: 0
free_strike: 4
characteristics:
  - +0
  - +1
  - +0
  - +0
  - +2
actions:
  - name: "Death Scythe"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 10
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 corruption damage
      <br />★ 12–16 9 corruption damage
      <br />✸ 17+ 12 corruption damage; I< 2 [[weakened]] (save ends)
      <br />**2 Malice** The death cultist regains stamina equal to half the damage dealt by this ability."
maneuvers:
  - name: "Rise, My Minions"
    desc: "
      <br />**Cost** 1 Malice per minion
      <br />**Keywords** Area
      <br />**Distance** 5 burst
      <br />**Target** One or more dead minions Special Each target must have died during this encounter 
      <br />**Effect:** Each target revives with their full stamina. They immediately die at the end of the encounter or if the death cultist is killed. A target can be revived multiple times by this ability."
traits:
  - name: "Supernatural Insight"
    desc: "The death cultist ignores concealment if it’s granted by a supernatural effect, or the target is supernatural."


```
