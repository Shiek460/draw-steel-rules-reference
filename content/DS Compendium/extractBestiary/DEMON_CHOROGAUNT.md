# DEMON CHOROGAUNT
```statblock
name: "DEMON CHOROGAUNT"
level: 3
roles:
  - LEADER
ancestry:
  - Abyssal
  - Demon
ev: 20
stamina: 120
weaknesses: Holy 5
speed: 5
size: 1L/
stability: 2
free_strike: 5
characteristics:
  - +2
  - +2
  - +2
  - +2
  - +2
actions:
  - name: "Agonizing Harmony"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 5 burst
      <br />**Target** Each enemy in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 4 psychic damage; I<  1 [[slowed]] (save ends)
      <br />★ 12–16 7 psychic damage; I<  2 [[slowed]] (save ends)
      <br />✸ 17+ 10 psychic damage; I<  3 [[slowed]] (save ends) 
      <br />**Effect:** An ally within 10 squares of the chorogaunt can shift up to their speed."
maneuvers:
  - name: "Chaotic Entrancing Harmony"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** 10 burst
      <br />**Target** Each enemy in the burst 
      <br />**Effect:** Each target slides 3, ignoring their stability."
ta:
  - name: "I Thrive on Pain"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** Magic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The chorogaunt is targeted by a strike. 
      <br />**Effect:** Any damage from the attack is halved, and the chorogaunt deals an additional 3 damage with their abilities until the end of their next turn."
traits:
  - name: "End Effect"
    desc: "At the end of their turn, the chorogaunt can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Lethe"
    desc: "While [[winded]], the chorogaunt has an edge on strikes, and strikes have an edge against them."
  - name: "Soulsight"
    desc: "Each creature within 2 of the chorogaunt can’t be hidden from them."
va:
  - name: "Frightening Tones (Villain Action 1)"
    desc: "
      <br />**Keywords** Ranged
      <br />**Distance** Ranged 10
      <br />**Target** Three enemies 
      <br />**Effect:** The chorogaunt allows each target to choose between taking 5 psychic damage or being [[frightened]] (save ends)."
  - name: "Bully the Weak (Villain Action 2)"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** One ally 
      <br />**Effect:** The chorogaunt kills the target, and each other ally deals an additional 3 damage on attacks until the end of the round. The Director gains malice equal to the number of heroes."
  - name: "Running Cacophony (Villain Action 3)"
    desc: "
      <br />**Keywords** Magic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The chorogaunt shifts up to their speed, uses their Agonizing Harmony, shifts up to their speed, and then uses their Agonizing Harmony again."

```
