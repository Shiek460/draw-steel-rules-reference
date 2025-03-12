# DEVIL JURIST
```statblock
name: "DEVIL JURIST"
level: 5
roles:
  - TROOP
  - ARTILLERY
ancestry:
  - Devil
  - Infernal
ev: 28
stamina: 120
immunities: Fire 5
speed: 6 (fly)
size: 1M /
stability: 0
free_strike: 7
characteristics:
  - 0
  - +2
  - +1
  - +1
  - +3
actions:
  - name: "Fire and Brimstone"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 12
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 fire damage
      <br />★ 12–16 15 fire damage; A<  2 burning (save ends)
      <br />✸ 17+ 18 fire damage; A<  3 burning (save ends) 
      <br />**Effect:** A burning creature or object takes 1d6 fire damage at the start of each of their turns until the condition ends.
      <br />**1 Malice** The jurist can target one additional creature or object for each malice spent."
  - name: "Dismissal with Prejudice"
    desc:
      "
      <br />**Keywords** Area, Magic
      <br />**Distance** 2 burst
      <br />**Target** Each enemy in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 damage; slide 1
      <br />★ 12–16 10 damage; slide 3
      <br />✸ 17+ 12 damage; slide 5 
      <br />**Effect:** M<  2 the target slides an additional 3 squares."
maneuvers:
  - name: "Ashes to Ashes"
    desc: "
      <br />**Keywords** Magic
      <br />**Distance** Ranged 12
      <br />**Target** 1 burning creature 
      <br />**Effect:** The target takes 6 fire damage."
ta:
  - name: "Devilish Charm (Triggered Action)"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** Magic
      <br />**Distance** Ranged 5
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature targets the jurist with a strike. 
      <br />**Effect:** The target makes a Might test.
      <br />`dice: 2d10 + 3`
      <br />✸ ≤11 The jurist chooses a new target for the strike
      <br />★ 12–16 The jurist halves the incoming damage
      <br />✦ 17+ The target is [[dazed]] (EoT)"
traits:
  - name: "Hellfire"
    desc: "Fire damage dealt by the jurist ignores immunity."
  - name: "True Name"
    desc: "If a creature within 10 squares of the jurist speaks the jurist’s true name aloud, the jurist loses their immunities, the additional effects on their signature action, and their Devilish Charm ability."


```
