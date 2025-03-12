```statblock
name: "WAR DOG PHOSPHORITE"
level: 2
roles:
  - BAND
  - HEXER
ancestry:
  - Humanoid
  - War Dog
ev: 4
immunities: acid 2
stamina: 15
speed: 5
size: 1M /
stability: 0
free_strike: 2
characteristics:
  - +2
  - +0
  - +0
  - +0
  - +1
actions:
  - name: "Caustic Detonator"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 acid damage; M< 0 [[Bleeding]] (save ends)
      <br />★ 12–16 6 acid damage; M< 1 [[Bleeding]] (save ends)
      <br />✸ 17+ 10 acid damage; M< 2 [[Bleeding]] (save ends)
      <br />**Effect:** A detonator attaches to the target. At the end of each round, roll a die. On an odd result, the detonator explodes, triggering the power roll.
      **Special** An adjacent creature can attempt an easy Agility test to remove the detonator as a maneuver. A failure does nothing, a success disarms and destroys the detonator, and a success with a reward allows the disarming creature to throw the detonator onto another target within 5 squares."
maneuvers:
  - name: "Posthumous Promotion"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One war dog with a loyalty collar 
      <br />**Effect:** The target’s loyalty collar detonates, killing them instantly."
traits:
  - name: "Loyalty Collar"
    desc: "When the subcommander dies, they explode, dealing 1d6 damage to each adjacent enemy."


```