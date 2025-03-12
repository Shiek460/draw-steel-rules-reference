# MINDKILLER
```statblock
name: "MINDKILLER"
level: 6
roles:
  - TROOP
  - HEXER
ancestry:
  - Horror
  - Voiceless Talker
ev: 32
stamina: 140
immunities: psychic 6
speed: 6 (fly, hover)
size: 1M /
stability: 2
free_strike: 7
characteristics:
  - -1
  - +3
  - +2
  - +2
  - +0
actions:
  - name: "Killer Claws"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 11 damage
      <br />★ 12–16 17+ damage; A< 2 [[grabbed]]
      <br />✸ 17+ 21 damage; A< 3 [[grabbed]]"
  - name: "Concealing Strike"
    desc:
      "
      <br />**Keywords** Psionic, Ranged, Strike
      <br />**Distance** Ranged 5
      <br />**Target** 2 creatures
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 10 damage; R< 1 the mindkiller is invisible to the target (save ends)
      <br />★ 12–16 15 damage; R< 2 the mindkiller is invisible to the target (save ends)
      <br />✸ 17+ 18 damage; R< 3 the mindkiller is invisible to the target (save ends)"
maneuvers:
  - name: "Mindwipe"
    desc: "
      <br />**Keywords** Attack, Psionic
      <br />**Distance** Melee 1
      <br />**Target** 1 [[grabbed]] creature 
      <br />**Effect:** R< 2 The mindkiller drains one point from the target’s Reason, Intuition, or Presence score (Director’s choice) and adds it to their own score until the end of the encounter."
ta:
  - name: "Meat Shield"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** 1 [[grabbed]] creature 
      <br />**Trigger** The mindkiller takes damage 
      <br />**Effect:** The mindkiller halves the incoming damage. The target takes the other half of the damage. 
      <br />**3 Malice** The target takes the full damage in place of the mindkiller."
traits:
  - name: "Psionic Conductor"
    desc: "When a non-minion Voiceless Talker within 5 of the mindkiller uses an ability with the Psionic keyword, they can do so as if they were in the mindkiller’s space."
  - name: "Nimble"
    desc: "The mindkiller can move through other creatures and objects at normal speed."

```
