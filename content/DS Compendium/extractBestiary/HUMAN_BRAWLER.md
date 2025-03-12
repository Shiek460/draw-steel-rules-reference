# HUMAN BRAWLER
```statblock
name: "HUMAN BRAWLER"
level: 1
roles:
  - PLATOON
  - BRUTE
ancestry:
  - Human
  - Humanoid
ev: 6
stamina: 40
immunities: Corruption 1, Psychic 1
speed: 5
size: 1M /
stability: 0
free_strike: 4
characteristics:
  - +2
  - +1
  - +0
  - +0
  - +0
actions:
  - name: "Haymaker"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 9 damage
      <br />✸ 17+ 12 damage; M< 2 [[grabbed]], target has a bane on escaping the grab 
      <br />**Effect:** brawler deals an additional 2 damage if the target is already [[grabbed]]."
maneuvers:
  - name: "Throw"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** One creature [[grabbed]] by the brawler 
      <br />**Effect:** Push 5."
traits:
  - name: "Shoot the Hostage"
    desc: "The brawler takes half damage from strikes if they have a creature or object [[grabbed]]. The [[grabbed]] creature or object takes the other half of the damage."
  - name: "Supernatural Insight"
    desc: "The brawler ignores concealment if it’s granted by a supernatural effect, or the target is supernatural."


```
