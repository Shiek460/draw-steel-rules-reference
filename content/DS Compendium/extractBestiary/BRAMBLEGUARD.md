# BRAMBLEGUARD
```statblock
name: "BRAMBLEGUARD"
level: 2
roles:
  - PLATOON
  - DEFENDER
ancestry:
  - Elemental
  - High
  - Elf
ev: 8
stamina: 59
speed: 4
size: 2 /
stability: 3
free_strike: 4
characteristics:
  - +2
  - 0
  - 0
  - 0
  - +2
actions:
  - name: "Wall of Roses"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The brambleguard’s speed becomes 0 and they extend themself into a 5 wall until the start of their next turn. Each ally adjacent to the brambleguard at the start of their turn regains 5 stamina and can apply the Magic keyword to their weapon abilities until the end of their turn."
  - name: "Whip Frenzy"
    desc:
      "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 2 burst
      <br />**Target** Each enemy in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 damage
      <br />★ 12–16 7 damage; push 3
      <br />✸ 17+ 10 damage; push 3; A< 2 [[bleeding]] (save ends)"
traits:
  - name: "Thicket and Thorns"
    desc: "The brambleguard blocks [[Line of Effect]] for enemies. An enemy that starts their turn adjacent to a brambleguard takes 4 damage."


```
