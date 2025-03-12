# LORD SYUUL
```statblock
name: "LORD SYUUL"
level: 6
roles:
  - SOLO
ancestry:
  - Horror
  - Voiceless Talker
ev: 80
stamina: 450
immunities: psychic 10
speed: 7 (teleport, hover)
size: 1M /
stability: 3
free_strike: 7
characteristics:
  - +1
  - +3
  - +4
  - +4
  - +3
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** Lord Syuul takes up to two turns each round. He can’t take turns consecutively. He can use two actions on each of his turns. While [[dazed]], he can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of his turn, Lord Syuul can take 10 damage to end one save ends effect affecting him. This damage can’t be reduced in any way."
  - name: "Mind Over Manners"
    desc: "When Lord Syuul uses an ability with the Psionic keyword, he can do so as if he were in the space of any creature within [[Line of Effect]] he has observed using an ability with the Psionic keyword."
actions:
  - name: "Tentacle Grab"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 damage; A< 2 [[grabbed]]
      <br />★ 12–16 17+ damage; A< 3 [[grabbed]]
      <br />✸ 17+ 20 damage; A< 4 [[grabbed]] 
      <br />**2 **Malice** The distance of this ability increases to Melee 10. Each target [[grabbed]] by Lord Syuul is immediately pulled 10."
  - name: "Dampening Grenade"
    desc:
      "
      <br />**Keywords** Area, Psionic, Ranged
      <br />**Distance** 2 cube within 5
      <br />**Target** All enemies 
      <br />**Effect:** All psionic or magical abilities within the affected area have a double bane. All tests against psionic or magical effects within this area have a double edge.
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 6 damage; effect ends after 2 turns.
      <br />★ 12–16 10 damage; effect ends after 1 round.
      <br />✸ 17+ 13 damage; effect ends with the encounter."
  - name: "Mind Blown"
    desc:
      "
      <br />**Keywords** Melee, Psionic, Strike
      <br />**Distance** Melee 1
      <br />**Target** One [[grabbed]] enemy
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 12 damage
      <br />★ 12–16 20 damage
      <br />✸ 17+ 24 damage 
      <br />**Effect:** If this action reduces the target to 0 stamina and they have a brain, their brain explodes, instantly killing them."
maneuvers:
  - name: "You Come With Me"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Lord Syuul teleports 5 along with each creature and object he has [[grabbed]]. He can release them as part of this maneuver."
ta:
  - name: "Adaptability"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** Lord Syuul takes typed damage. 
      <br />**Effect:** Lord Syuul gains immunity 5 to the triggering type of damage until the start of his next turn."
va:
  - name: "See Only Me (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Psionic
      <br />**Distance** 10 burst
      <br />**Target** All enemies 
      <br />**Effect:** Each target makes a Might test.
      <br />`dice: 2d10 +
      <br />✸ ≤11 16 psychic damage; can’t establish [[Line of Effect]] to creatures besides Lord Syuul, and strikes targeting Lord Syuul have a bane (save ends)
      <br />★ 12–16 13 psychic damage; can’t establish [[Line of Effect]] to creatures besides Lord Syuul (save ends)
      <br />✦ 17+ 7 psychic damage"
  - name: "Phantom Pain (Villain Action 2)"
    desc: "
      <br />**Keywords** Psionic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Lord Syuul teleports up to 10 and projects an illusory double within 10. The double can’t move or act, but Lord Syuul can use psionic abilities as if he were in its space. When a creature touches or damages the double with a melee strike, they take 10 psionic damage. The double disappears when Lord Syuul takes damage."
  - name: "Mindshatter (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Psionic
      <br />**Distance** 5 Burst
      <br />**Target** All creatures
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 7 psychic damage
      <br />★ 12–16 13 psychic damage
      <br />✸ 17+ 16 psychic damage 
      <br />**Effect:** Each target gains damage weakness 3 until the end of the encounter."

```
