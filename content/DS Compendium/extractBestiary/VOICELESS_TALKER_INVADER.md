# VOICELESS TALKER INVADER
```statblock
name: "VOICELESS TALKER INVADER"
level: 6
roles:
  - TROOP
  - CONTROLLER
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
  - -1
  - +1
  - +3
  - +2
  - +2
actions:
  - name: "Tentacle"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 damage
      <br />★ 12–16 15 damage; M< 2 [[grabbed]]
      <br />✸ 17+ 18 damage; M< 3 [[grabbed]]"
  - name: "Psionic Boom"
    desc:
      "
      <br />**Keywords** Area, Psionic
      <br />**Distance** 3 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 psychic damage; R< 1 push 2
      <br />★ 12–16 10 psychic damage; R< 2 push 3
      <br />✸ 17+ 12 psychic damage; R< 3 push 4 and [[prone]] 
      <br />**2 Malice** The area of the burst increases to 5."
maneuvers:
  - name: "Tentacle Toss"
    desc: "
      <br />**Keywords** Melee, Psionic
      <br />**Distance** Melee 1
      <br />**Target** 1 [[grabbed]] creature
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 damage; vertical slide 2
      <br />★ 12–16 10 damage; vertical slide 3
      <br />✸ 17+ 12 damage; vertical slide 5"
ta:
  - name: "Brain Drain"
    desc: "
      <br />**Keywords** Psionic
      <br />**Distance** Melee 1
      <br />**Target** 1 creature [[grabbed]] by the invader 
      <br />**Trigger** The target resists an ability’s effect. 
      <br />**Effect:** The potency of the effect increases by 2."
traits:
  - name: "Psionic Amplifier"
    desc: "When a non-minion Voiceless Talker within 5 of the invader uses an ability with the Psionic keyword, they can do so with a double edge and as if they were in the invader’s space."

```
