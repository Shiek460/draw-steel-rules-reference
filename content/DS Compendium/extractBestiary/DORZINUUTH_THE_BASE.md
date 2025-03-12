# DORZINUUTH THE BASE
```statblock
name: "DORZINUUTH THE BASE"
level: 6
roles:
  - LEADER
ancestry:
  - Draconian
  - Dragon
  - Humanoid
ev: 32
stamina: 180
immunities: lightning 6
speed: 5 (flying, hover)
size: 1L /
stability: 6
free_strike: 7
characteristics:
  - +4
  - +1
  - +1
  - +2
  - +3
actions:
  - name: "Punishing Flail"
    desc: "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 damage; M< 2 [[prone]]
      <br />★ 12–16 16 damage; M< 3 [[prone]]
      <br />✸ 17+ 19 damage; M< 4 [[prone]] 2 Malice M< 4 [[bleeding]] (save ends)."
maneuvers:
  - name: "I’ll Cut A Path"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 5 × 1 line Within 1
      <br />**Target** All enemies in the line 
      <br />**Effect:** Dorzinuuth shifts to an unoccupied square adjacent to the end of the line and then rolls power.
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 12 damage; M< 3 [[prone]]
      <br />✸ 17+ 15 damage; M< 4 [[prone]] "
ta:
  - name: "Watch Your Six!"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** 1 Ally 
      <br />**Trigger** An ally within distance takes damage while Dorzinuuth isn’t flying. 
      <br />**Effect:** Dorzinuuth shields his ally with his wings, halving the damage. 
      <br />**End Effect:** At the end of his turn, Dorzinuuth can take 10 damage to end one save ends effect affecting him. This damage can’t be reduced in any way."
traits:
  - name: "Sheltering Wings"
    desc: "Strikes made against Dorzinuuth have a bane while he isn’t flying."
  - name: "Remember Your Oath"
    desc: "After Dorzinuuth hears a character recite the Dragon Phalanx oath, he has a bane on all strikes made against that character."
va:
  - name: "Roaring Gambit (Villain Action 1)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** 5 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** Dorzinuuth lets loose a powerful roar. Each target must make a Might test.
      <br />`dice: 2d10 + 4`
      <br />✸ ≤11 [[frightened]] (save ends)
      <br />★ 12–16 [[frightened]] (EoT)
      <br />✦ 17+ no effect 
      <br />**Effect:** Each ally within distance has an edge on their next attack."
  - name: "Wings of Second Wind (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self and 10 burst
      <br />**Target** Self and all allies 
      <br />**Effect:** Each target shifts or flies up to their speed and regains 10 stamina."
  - name: "Snap, Crackle, Pop (Villain Action 3)"
    desc: "
      <br />**Keywords** Magic, Melee
      <br />**Distance** 5 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Dorzinuuth covers all allies in an electrifying mesh. Whenever a target takes damage from a melee strike or ability, the attacker takes 6 lightning damage."

```
