# OLOTHEC
```statblock
name: "OLOTHEC"
level: 6
roles:
  - SOLO
ancestry:
  - Horror
  - Olothec
ev: 80
stamina: 450
immunities: psychic 6
speed: 7 (fly, swim)
size: 2 /
stability: 0
free_strike: 7
characteristics:
  - +4
  - -1
  - +4
  - +2
  - +3
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The olothec takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the olothec can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the olothec can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Gelatinosis"
    desc: "A creature permanently devolves into a slime servant if they spend 1 continuous minute [[weakened]] by Devolving Tentacles, they are reduced to 0 or lower stamina by the psychic damage from Devolving Tentacles, or they suffer all three transformations from Oozing Transformation."
  - name: "Primordial Mind"
    desc: "The olothec is immune to the [[frightened]] and [[taunted]] conditions."
  - name: "Slime Sense"
    desc: "A slimed or transformed creature can’t be hidden or concealed from the olothec."
actions:
  - name: "Devolving Tentacles"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 damage; M< 2 [[weakened]] or slimed (save ends)
      <br />★ 12–16 17+ damage; M< 3 [[weakened]] or slimed (save ends)
      <br />✸ 17+ 20 damage; M< 4 [[weakened]] and slimed (save ends) 
      <br />**Effect:** A slimed target takes 4 psychic damage whenever they roll power until the condition ends."
  - name: "Slime Spew"
    desc:
      "
      <br />**Keywords** Area, Weapon
      <br />**Distance** 7 x 2 line within 1
      <br />**Target** All creatures and objects
      <br />`dice: 2d10 + 4`
      <br />✦ 17+ 6 acid damage; A< 2 push (special)
      <br />★ 12–16 10 acid damage; A< 3 push (special)
      <br />✸ ≤11 13 acid damage; A< 4 push (special), [[prone]] 
      <br />**Effect:** A creature pushed by this ability is pushed to the squares within the line that are furthest from the olothec. 
      <br />**1 Malice** The affected area becomes difficult terrain. A creature that enters an affected square for the first time during a turn is A< 3 knocked [[prone]]."
  - name: "Oozing Transformation"
    desc:
      "
      <br />**Keywords** Psionic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** One creature
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 13 psychic damage; I< 2 transformed (save ends)
      <br />★ 12–16 20 psychic damage; I< 3 transformed (save ends)
      <br />✸ 17+ 23 psychic damage; I< 4 transformed (save ends) 
      <br />**Effect:** Each time a creature is transformed, the Director chooses one of the following transformations. When a creature ends the transformed effect, all transformations end."
  - name: "Transformations"
    desc: "
      <br />- **Head** 
      <br />- The creature’s head becomes a ball of slime. They cannot communicate and they can’t establish [[Line of Effect]] beyond 3 squares. 
      <br />- **Legs**
      <br />- The creature’s legs become pillars of ooze. They are [[slowed]] while on land and add the swim keyword to their speed.
      <br />- **Torso**
      <br />- The creature’s arms become gelatinous. They can’t benefit from edges or surges."
maneuvers:
  - name: "Jaunt"
    desc: "
      <br />**Keywords** Psionic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The olothec teleports to an unoccupied square within 10 or swaps places with a creature or object within 5."
ta:
  - name: "Liquify"
    desc: "
      <br />**Keywords** Psionic, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** One enemy 
      <br />**Trigger**
      <br />**Target** deals damage to the olothec 
      <br />**Effect:** The target takes 8 psychic damage and gains psychic weakness 3 until the end of the olothec’s next turn."
va:
  - name: "Horrifying Form (Villain Action 1)"
    desc: "
      <br />**Keywords** Psionic, Ranged, Strike
      <br />**Distance** Special
      <br />**Target** All enemies
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 10 psychic damage; P< 2 [[frightened]] (save ends)
      <br />★ 12–16 14 psychic damage; P< 3 [[frightened]] (save ends)
      <br />✸ 17+ 17+ psychic damage; P< 4 [[frightened]] (save ends) 
      <br />**Effect:** This ability targets each enemy the olothec has [[Line of Effect]] to. A [[frightened]] enemy can’t save against any other effect until they are no longer [[frightened]]."
  - name: "Psychic Pulse (Villain Action 2)"
    desc: "
      <br />**Keywords** Area, Psionic
      <br />**Distance** 10 burst
      <br />**Target** All creatures 
      <br />**Effect:** Each target takes 12 psychic damage, slides 5, and is M< 3 [[weakened]] and slimed (save ends) (see devolving tentacles). The olothec has damage immunity 4 until the start of their next turn."
  - name: "Return to Perfection (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Ranged, Psionic
      <br />**Distance** 10 burst
      <br />**Target** All creatures
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 7 psychic damage; R< 2 devolved (save ends)
      <br />★ 12–16 13 psychic damage; R< 3 devolved (save ends)
      <br />✸ 17+ 16 psychic damage; R< 4 devolved (save ends) 
      <br />**Effect:** A devolved creature has a -1 modifier  to all their characteristic scores other than Might until the condition ends."

```
