# VOICELESS TALKER ARTILLERIST
```statblock
name: "VOICELESS TALKER ARTILLERIST"
level: 6
roles:
  - ARTILLERY
  - TROOP
ancestry:
  - Horror
  - Voiceless Talker
ev: 32
stamina: 140
immunities: psychic 6
speed: 5 (teleport, hover)
size: 1M /
stability: 2
free_strike: 7
characteristics:
  - +0
  - +3
  - +1
  - +2
  - +1
actions:
  - name: "Psionic Rifle Burst"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Psionic, Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 11 damage
      <br />★ 12–16 19 damage; spread 1
      <br />✸ 17+ 22 damage; spread 2 
      <br />**Effect:** The blast hits nearby targets, dealing 3 damage to each enemy within a number of squares of the target equal to the result’s spread value. 
      <br />**2 Malice** The attack deals an additional 3 damage to each enemy within the spread distance"
  - name: "Mind Jolt"
    desc:
      "
      <br />**Keywords** Area, Psionic
      <br />**Distance** 1 × 10 line within 10
      <br />**Target** All enemies
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 lightning damage
      <br />★ 12–16 10 lightning damage; I< 2 [[slowed]] (save ends)
      <br />✸ 17+ 13 lightning damage; I< 3 [[slowed]] (save ends)"
maneuvers:
  - name: "In Our Sights"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature 
      <br />**Effect:** The next power roll with the psionic keyword made against the target will automatically be a 17+ until the start of the artillerist’s next turn."
ta:
  - name: "Tactical Reposition"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The artillerist takes damage. 
      <br />**Effect:** The artillerist teleports 5 and doesn’t suffer any additional effects associated with the damage."
traits:
  - name: "Psionic Conductor"
    desc: "When a non-minion Voiceless Talker within 5 of the artillerist uses an ability with the Psionic keyword, they can do so as if they were in the artillerist’s space."
  - name: "Locked On"
    desc: "The artillerist ignores invisibility, cover, and concealment. A creature can’t hide from the artillerist while the artillerist has [[Draw Steel Rules#LINE OF EFFECT|line of effect]] to them."

```
