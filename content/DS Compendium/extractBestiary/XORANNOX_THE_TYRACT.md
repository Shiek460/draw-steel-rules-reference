# XORANNOX THE TYRACT
```statblock
name: "XORANNOX THE TYRACT"
level: 6
roles:
  - SOLO
ancestry:
  - Horror
  - Overmind
ev: 80
stamina: 450
speed: 5 (fly, hover)
size: 3 /
stability: 3
free_strike: 7
characteristics:
  - +4
  - +2
  - +4
  - +3
  - +3
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** Xorannox takes up to two turns each round. He can’t take turns consecutively. He can use two actions on each of his turns. While [[dazed]], Xorannox can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of his turn, Xorannox can take 10 damage to end one save ends effect affecting him. This damage can’t be reduced in any way."
  - name: "Eyes of the Tyract"
    desc: "Six unique eyestalks float around Xorannox and act on his turn at his command. On each of Xorannox’s turns, he directs one eyestalk to move and use a signature action. When an eyestalk is destroyed, Xorannox can’t use that eyestalk’s ability."
  - name: "Above It All"
    desc: "Xorannox can’t be flanked, [[frightened]], or knocked [[prone]]."
  - name: "Natural Enemies"
    desc: "If Xorannox perceives another overmind or voiceless talker on the battlefield, he targets that threat at least once every turn."
actions:
  - name: "Toothful Thrashing"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 12 damage; slide 2; M< 2 [[bleeding]] (EoT)
      <br />★ 12–16 20 damage; slide 3; M< 3 [[bleeding]] (EoT)
      <br />✸ 17+ 23 damage; vertical slide 3; M< 4 [[bleeding]] (EoT)"
  - name: "Grav Spike"
    desc:
      "
      <br />**Keywords** Area, Psionic, Ranged
      <br />**Distance** 2 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 Vertical push 3
      <br />★ 12–16 Vertical push 5
      <br />✸ 17+ Vertical push 7 
      <br />**Effect:** Xorannox shifts up to his speed before or after using this ability."
maneuvers:
  - name: "Optical Collusion"
    desc: "
      <br />**Keywords** Area, Melee
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Xorannox commands all eyestalks to move up to their speed."
  - name: "Shutout"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** 5 x 2 line within 1
      <br />**Target** Special 
      <br />**Effect:** Xorannox ends all ongoing supernatural effects and suppresses supernatural effects from equipment in the affected area. New supernatural effects cannot activate in the affected area until the end of Xorannox’s next turn."
ta:
  - name: "Cower!"
    desc: "
      <br />**Keywords** Psionic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** Special 
      <br />**Trigger** A creature deals damage to Xorannox. 
      <br />**Effect:** The triggering creature is I< 3 [[frightened]] (save ends)."
va: 
  - name: "Disruption Beam (Villain Action 1)"
    desc: "
      <br />**Keywords** Psionic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** Three creatures
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 psychic damage; R< 2 [[dazed]] (save ends)
      <br />★ 12–16 17+ psychic damage; R< 3 [[dazed]] (save ends)
      <br />✸ 17+ 20 psychic damage; R< 4 [[dazed]] (save ends)"
  - name: "All Eyes, All Rise (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Xorannox reforms all destroyed eyestalks and raises them at full stamina."
  - name: "Panoptibeam (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 2 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** Xorannox directs each remaining eyestalk to use a signature action, targeting each creature in the area."

```
