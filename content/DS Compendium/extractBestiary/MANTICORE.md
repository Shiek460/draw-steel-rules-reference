# MANTICORE
```statblock
name: "MANTICORE"
level: 4
roles:
  - SOLO
ancestry:
  - Beast
  - Manticore
ev: 60
stamina: 350
speed: 10 (fly)
size: 2 /
stability: 3
free_strike: 6
characteristics:
  - +4
  - +3
  - +0
  - +0
  - -1
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The manticore takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the manticore can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the manticore can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Agile Predator"
    desc: "When the manticore deals damage to a creature, they don’t provoke opportunity attacks from that creature during that turn."
actions:
  - name: "Carnivorous Bite"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 12 damage; A< 2 [[bleeding]] (save ends)
      <br />★ 12–16 17+ damage; A< 3 [[bleeding]] (save ends)
      <br />✸ 17+ 21 damage; A< 4 [[bleeding]] (save ends) 
      <br />**Effect:** This ability has an edge against [[frightened]] targets."
  - name: "Tail Spike"
    desc:
      "
      <br />**Keywords** Ranged, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 10 damage; M< 2 3 poison damage
      <br />★ 12–16 15 damage; M< 3 7 poison damage, [[weakened]] (save ends)
      <br />✸ 17+ 19 damage; M< 4 10 poison damage, [[weakened]] (save ends) 
      <br />**1 Malice** A target [[weakened]] from this ability takes 1d6 poison damage at the start of each of their turns until the condition ends."
maneuvers:
  - name: "Harrying Claws"
    desc: "
      <br />**Keywords** Melee
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 +
      <br />✦ ≤11 Slide 1; A< 2 3 damage
      <br />★ 12–16 Slide 2; A< 3 5 damage
      <br />✸ 17+ Slide 4; A< 4 7 damage"
ta:
  - name: "Reflexive Instinct"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature deals damage to the manticore. 
      <br />**Effect:** The manticore shifts up to 5 into the air, then uses their Tail Spike ability against the target."
va:
  - name: "Trumpeting Howl (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 burst
      <br />**Target** All creatures
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 [[frightened]] (EoT) or I< 2 (save ends)
      <br />★ 12–16 [[frightened]] (EoT) or I< 3 (save ends)
      <br />✸ 17+ [[frightened]] (save ends); I< 4 [[dazed]] (save ends)"
  - name: "Cornered Predator (Villain Action 2)"
    desc: "
      <br />**Keywords** Ranged, Weapon
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The manticore shifts up to their speed, then uses their Tail Spike ability against each enemy within 10 squares."
  - name: "Debilitating Poison (Villain Action 3)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Special 
      <br />**Effect:** The manticore sours their own poison with enmity. Until the end of the encounter, the manticore has a double edge on power rolls targeting [[weakened]] creatures. A creature [[weakened]] by the manticore’s Tail Spike ability has their speed halved and takes an additional 1d3 poison damage at the start of each of their turns until the condition ends."


```
