# ORC EYE OF GROLE
```statblock
name: "ORC EYE OF GROLE"
level: 1
roles:
  - PLATOON
  - ARTILLERY
ancestry:
  - Humanoid
  - Orc
ev: 6
stamina: 20
immunities: affinity 5
speed: 6
size: 1M /
stability: 0
free_strike: 4
characteristics:
  - +1
  - +1
  - 0
  - 0
  - +2
traits:
  - name: "Affinity"
    desc: "The eye has an affinity for one of the following damage types: cold, fire, or lightning. This type determines the eye’s affinity immunity and the damage type of their attacks."
actions:
  - name: "Elemental Discharge"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 6 affinity damage; push 2 or shift 2 away from target
      <br />★ 12–16 9 affinity damage; slide 4 or shift 4 away from target
      <br />✸ 17+ 12 affinity damage; slide 6 or shift 6 away from target"
  - name: "Power Burst"
    desc:
      "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 × 2 line within 1
      <br />**Target** All enemies in the line
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 affinity damage; push 2
      <br />★ 12–16 5 affinity damage; push 3
      <br />✸ 17+ 8 affinity damage; push 4; [[prone]] 
      <br />**Effect:** An enemy has affinity weakness 3 in the affected area."
traits: 
  - name: "Relentless" 
    desc: "If the eye’s stamina drops to 0, they can make a free strike before dying. If the target is reduced to 0 stamina: or killed by the strike, the eye lives and their stamina: is reduced to 1 instead."

```
