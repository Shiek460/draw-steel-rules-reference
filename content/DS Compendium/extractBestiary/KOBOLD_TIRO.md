# KOBOLD TIRO
```statblock
name: "KOBOLD TIRO"
level: 1
roles:
  - MINION
  - DEFENDER
ancestry:
  - Humanoid
  - Kobold
ev: 3 for four minions
stamina: 5
speed: 5
size: 1S /
stability: 0
with-captain:
speed: +1
free_strike: 1
characteristics:
  - 0
  - +2
  - 0
  - 0
  - 0
actions:
  - name: "Pugio"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object per minion
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 1 damage
      <br />★ 12–16 2 damage; shift 1
      <br />✸ 17+ 3 damage; shift 2 
      <br />**Effect:** The tiro slices the target with their dagger. The target can’t shift until the start of the tiro’s next turn."
traits:
  - name: "Shield? Shield!"
    desc: "The tiro has cover, a stability of 1, and can act as cover for allies when adjacent to an ally who also has this trait."

```
