# HUMAN KNAVE
```statblock
name: "HUMAN KNAVE"
level: 2
roles:
  - PLATOON
  - DEFENDER
ancestry:
  - Human
  - Humanoid
ev: 8
stamina: 50
immunities: Corruption 2, Psychic 2
speed: 5
size: 1M/
stability: 0
free_strike: 4
characteristics:
  - +2
  - +0
  - +1
  - +0
  - +0
actions:
  - name: "Morningstar & Javelin"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Ranged, Strike, Weapon
      <br />**Distance** Melee 1 or Ranged 5
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 damage
      <br />★ 12–16 9 damage
      <br />✸ 17+ 12 damage; M< 2 the target has a double bane on their next power roll 
      <br />**Effect:** [[taunted]] (EoT)."
traits:
  - name: "I’m Your Enemy"
    desc: "The knave can make a free strike against an adjacent creature they have [[taunted]] whenever the creature deals damage to a creature other than the knave."
  - name: "Overwhelm"
    desc: "An enemy who starts their turn adjacent to the knave can’t shift."
  - name: "Supernatural Insight"
    desc: "The knave ignores concealment if it’s granted by a supernatural effect, or the target is supernatural."


```
