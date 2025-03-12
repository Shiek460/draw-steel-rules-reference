# HUMAN STORM MAGE
```statblock
name: "HUMAN STORM MAGE"
level: 3
roles:
  - PLATOON
  - CONTROLLER
ancestry:
  - Human
  - Humanoid
ev: 10
stamina: 40
immunities: Corruption 3, Psychic 3
speed: 5
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - +0
  - +0
  - +2
  - +0
  - +1
actions:
  - name: "Lightning Bolt"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 15
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 lightning damage
      <br />★ 12–16 10 lightning damage
      <br />✸ 17+ 13 lightning damage
      <br />**Cost** 5 Malice The ability takes the Area keyword and becomes a 10 × 1 line that targets each enemy and object in the area."
maneuvers:
  - name: "Gust of Wind"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 cube within 1
      <br />**Target** All enemies and objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 Slide 2; M< 0 [[slowed]] (save ends)
      <br />★ 12–16 Slide 4; M< 1 [[slowed]] (save ends)
      <br />✸ 17+ Slide 6; M< 2 [[slowed]] (save ends) 
      <br />**Effect:** The gust of wind disperses gas or vapor and extinguishes any flames, including persistent effects."
traits:
  - name: "Arcane Shield"
    desc: "The mage imposes a bane on incoming melee strikes and abilities. Whenever the mage takes damage from an adjacent enemy, the enemy takes 2 lightning damage and is R< 1 pushed 2."
  - name: "Supernatural Insight"
    desc: "The storm mage ignores concealment if it’s granted by a supernatural effect, or the target is supernatural."


```
