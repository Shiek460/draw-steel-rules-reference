# KOBOLD SIGNIFIER
```statblock
name: "KOBOLD SIGNIFIER"
level: 1
roles:
  - BAND
  - SUPPORT
ancestry:
  - Humanoid
  - Kobold
ev: 3
stamina: 15
speed: 5
size: 1S /
stability: 0
free_strike: 1
characteristics:
  - 0
  - +1
  - 0
  - 0
  - +2
actions:
  - name: "Signum"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage
      <br />★ 12–16 4 damage
      <br />✸ 17+ 5 damage 
      <br />**Effect:** An ally within 10 can shift their speed, so long as they end their movement adjacent to an ally. 
      <br />**2+ Malice** 1 additional ally can shift for every 2 malice spent."
maneuvers:
  - name: "Glory to the Legion"
    desc: "
      <br />**Cost** 5 Malice
      <br />**Keywords** Area
      <br />**Distance** 5 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Each target regains 5 stamina."
traits:
  - name: "Upholding High Standards"
    desc: "Each ally that starts their turn within 5 of the signifier has their speed increased by 2 and deals an additional 2 damage on their strikes until the end of their turn. If the signifier is killed, a minion can enter their square to retrieve the signum as a free action and replace their stat block with the signifier stat block."
  - name: "Shield? Shield!"
    desc: "The signifier has cover, a stability of 1, and can act as cover for allies when adjacent to an ally who also has this trait."

```
