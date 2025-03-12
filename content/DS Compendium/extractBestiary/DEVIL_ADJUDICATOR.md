# DEVIL ADJUDICATOR
```statblock
name: "DEVIL ADJUDICATOR"
level: 6
roles:
  - TROOP
  - CONTROLLER
ancestry:
  - Devil
  - Infernal
ev: 32
stamina: 140
immunities: Fire 5
speed: 6 (fly)
size: 1M /
stability: 1
free_strike: 7
characteristics:
  - 0
  - +1
  - +2
  - +1
  - +3
actions:
  - name: "Infernal Injunction"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 fire damage; I<  1 [[frightened]] (save ends)
      <br />★ 12–16 15 fire damage; I<  2 [[frightened]] (save ends)
      <br />✸ 17+ 18 fire damage; I<  3 [[frightened]] (save ends) 
      <br />**Effect:** The adjudicator can slide a target [[frightened]] by this ability 2 squares."
  - name: "Adjudicator’s Interdiction"
    desc: "
      <br />**Keywords** Magic
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature 
      <br />**Effect:** The target makes a Might test.
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 [[slowed]], bane on power rolls, can’t regain stamina (save ends)
      <br />★ 12–16 [[slowed]], bane on power rolls (save ends)
      <br />✦ 17+ [[slowed]] (save ends)"
maneuvers:
  - name: "Quid Pro Quo"
    desc: "
      <br />**Keywords** Magic
      <br />**Distance** Ranged 10
      <br />**Target** 1 ally or 1 [[frightened]] creature 
      <br />**Effect:** The adjudicator switches places with the target."
ta:
  - name: "Devilish Charm"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** Magic
      <br />**Distance** Ranged 5
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature targets the adjudicator with a strike. 
      <br />**Effect:** The target makes a Might test.
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 The adjudicator chooses a new target for the strike
      <br />★ 12–16 The adjudicator halves the incoming damage
      <br />✦ 17+ The target is [[dazed]] (EoT)"
traits:
  - name: "Vexatious Litigation"
    desc: "A creature has -2 on saving throws while within 10 of the adjudicator if their Presence score is lower than the adjudicator’s."
  - name: "True Name"
    desc: "If a creature within 10 squares of the adjudicator speaks the adjudicator’s true name aloud, the adjudicator loses their immunities, the additional effects on their signature action, and their Devilish Charm ability."


```
