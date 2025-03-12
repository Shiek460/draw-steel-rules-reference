# ARCHDEVIL
```statblock
name: "ARCHDEVIL"
level: 6
roles:
  - LEADER
ancestry:
  - Devil
  - Infernal
ev: 32
stamina: 181
immunities: Fire 8
speed: 7 (fly)
size: 1M /
stability: 2
free_strike: 6
characteristics:
  - +1
  - +3
  - +2
  - +1
  - +4
actions:
  - name: "Infernal Decree"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 12
      <br />**Target** Three creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 10 damage; P<  2 the target can’t hide (save ends)
      <br />★ 12–16 15 damage; P<  3 the target can’t hide (save ends)
      <br />✸ 17+ 19 damage; P<  4 the target can’t hide (save ends) 
      <br />**Cost** 2 Malice 
      <br />**EFfect** Each devil has an edge to strike a target that can’t hide."
maneuvers:
  - name: "Compel the Jury"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 12
      <br />**Target** 2 creatures
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 I< 2 charmed (save ends)
      <br />★ 12–16 I< 3 charmed (save ends)
      <br />✸ 17+ I< 4 charmed (save ends) 
      <br />**Effect:** Until the condition ends, a charmed creature considers the archdevil an ally, and the archdevil can spend 1 malice on their turn to force move a charmed creature up to 3 squares."
ta:
  - name: "Devilish Suggestion"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** Magic
      <br />**Distance** Ranged 5
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature targets the archdevil with a strike. 
      <br />**Effect:** The target makes a Might test.
      <br />`dice: 2d10 + 4`
      <br />✸ ≤11 Charmed (save ends) (see Compel the Jury)
      <br />★ 12–16 The archdevil chooses a new target for the strike
      <br />✦ 17+ The archdevil halves the incoming damage"
traits:
  - name: "End Effect"
    desc: "At the end of their turn, the archdevil can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "True Name"
    desc: "If a creature within 10 squares of the archdevil speaks the archdevil’s true name aloud, the archdevil loses their immunities, the additional effects on their signature attack, and their Devilish Suggestion triggered action."
va:
  - name: "Welcome, Friends (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 burst
      <br />**Target** Each enemy in burst 
      <br />**Effect:** Each target makes a Might test.
      <br />`dice: 2d10 +
      <br />✦ ≤11 15 psychic damage; charmed (save ends)
      <br />★ 12–16 12 psychic damage; charmed (save ends)
      <br />✸ 17+ 7 psychic damage "
  - name: "Heed My Commands! (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self and 5 burst
      <br />**Target** Self and each allies in the burst 
      <br />**Effect:** Each target shifts up to their speed. The archdevil can force move each charmed creature up to half their speed."
  - name: "Deceptive Stratagem (Villain Action 3)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 12
      <br />**Target** 1 ally or charmed creature 
      <br />**Effect:** The archdevil swaps places with the target. Then, each ally and charmed creature within 12 of the archdevil make a free strike against a target of the archdevil’s choice."

```
