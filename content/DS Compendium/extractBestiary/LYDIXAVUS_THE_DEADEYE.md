# LYDIXAVUS THE DEADEYE
```statblock
name: "LYDIXAVUS THE DEADEYE"
level: 6
roles:
  - TROOP
  - ARTILLERY
ancestry:
  - Draconian
  - Dragon
  - Humanoid
ev: 32
stamina: 140
immunities: cold 6
speed: 5 (flying)
size: 1M /
stability: 2
free_strike: 7
characteristics:
  - -1
  - +3
  - +3
  - +3
  - +1
actions:
  - name: "Breathsnipe"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 15
      <br />**Target** 1 enemy
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 cold damage
      <br />★ 12–16 16 cold damage; the target has a bane on their next strike.
      <br />✸ 17+ 19 cold damage; the target has a double bane on their next strike."
  - name: "Ice Lob"
    desc:
      "
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 2 cube within 10
      <br />**Target** All enemies and objects in the cube
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 7 cold damage; M< 1 [[dazed]] (save ends)
      <br />★ 12–16 13 cold damage; M< 2 [[dazed]] (save ends)
      <br />✸ 17+ 16 cold damage; M< 3 [[dazed]] (save ends) Parting Gift (Maneuver)
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Lydixavus flies up to their speed, leaving a size 1S ice mine in the square they took off from. The ice mine explodes when an enemy enters a square containing it. Lydixavus rolls power for an exploding ice mine as if they used their Ice Lob ability, targeting the triggering creature and each creature and object within 1 of the ice mine."
ta:
  - name: "Wasn’t Aiming For You"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** Lydixavus gets a Tier 1 result on their signature action 
      <br />**Effect:** Lydixavus uses an additional signature action targeting a creature within 5 of the original target."
traits:
  - name: "Scorekeeping Scales"
    desc: "Lydixavus knows the location of every creature who has ever dealt damage to them and has [[Line of Effect]] to each of these creatures while they’re within 20 of Lydixavus."


```
