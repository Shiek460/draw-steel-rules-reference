# MUMMY LORD
```statblock
name: "MUMMY LORD"
level: 4
roles:
  - LEADER
ancestry:
  - Mummy
  - Undead
ev: 24
stamina: 155
immunities: corruption 6, poison 6 /
weaknesses: fire 5
speed: 6
size: 1M /
stability: 4
free_strike: 6
characteristics:
  - +4
  - +0
  - +2
  - +4
  - +2
actions:
  - name: "Accursed Slam"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 10 corruption damage; I< 2 [[bleeding]] (save ends)
      <br />★ 12–16 14 corruption damage; I< 3 [[bleeding]] (save ends)
      <br />✸ 17+ 17+ corruption damage; I< 4 [[bleeding]] (save ends) 
      <br />**Effect:** The potency of abilities used against a target [[bleeding]] from this ability increase by 1."
  - name: "Binding Curse"
    desc:
      "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 20
      <br />**Target** One creature
      <br />`dice: 2d10 + 4`
      <br />✸ ≤11 7 corruption damage; I< 2 [[frightened]] (save ends)
      <br />★ 12–16 12 corruption damage; I< 3 [[frightened]] (save ends)
      <br />✦ 17+ 16 corruption damage; I< 4 [[frightened]] (save ends) 
      <br />**Effect:** A target [[frightened]] by this ability takes 4 psychic damage whenever they use a move action until the condition ends. 
      <br />**2+ Malice** The mummy lord targets an additional creature for every 2 malice spent."
ta:
  - name: "Summon my Guard!"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** Special 
      <br />**Trigger** The Mummy Lord becomes [[winded]] for the first time. 
      <br />**Effect:** Two mummies and 4 ghoul carvers appear within distance."
traits:
  - name: "Cursed Transference"
    desc: "At the end of their turn, the mummy lord can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way. <br />**5 Malice** The effect is transferred to a creature within 10."
  - name: "Plague of Flies (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 burst
      <br />**Target** All enemies
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 5 poison damage
      <br />★ 12–16 8 poison damage
      <br />✸ 17+ 10 poison damage 
      <br />**Effect:** Each target has a bane on their next strike."
  - name: "Land’s Guardian (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The mummy lord’s speed increases by 2 and adds the burrow keyword to their movement. The mummy lord burrows up to their speed. Each enemy within 2 squares of the mummy lord’s movement must make a Might test.
      <br />✸ ≤11 [[prone]], can’t stand (EoT)
      <br />★ 12–16 [[prone]]
      <br />`dice: 2d10 +
      <br />✦ 17+ no effect"
  - name: "Unbound Horrors (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 burst
      <br />**Target** All enemies
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 5 corruption damage; I< 2 [[frightened]] (save ends)
      <br />★ 12–16 8 corruption damage; I< 3 [[frightened]] (save ends)
      <br />✸ 17+ 10 corruption damage; I< 4 [[frightened]] and [[restrained]] (save ends)"

```
