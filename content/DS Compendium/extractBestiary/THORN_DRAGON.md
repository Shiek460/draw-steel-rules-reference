# THORN DRAGON
```statblock
name: "THORN DRAGON"
level: 2
roles:
  - SOLO
ancestry:
  - Dragon
  - Elemental
ev: 40
stamina: 250
immunities: poison 5
speed: 8 (fly)
size: 3 /
stability: 6
free_strike: 5
characteristics:
  - +2
  - +3
  - -1
  - +1
  - +2
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The dragon takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the dragon can take one action and one maneuver per turn. "
  - name: "End Effect"
    desc: " At the end of their turn, the dragon can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Withering Wyrmscale Aura"
    desc: " The dragon’s scales emit a 2 aura barrier of withering green magic. When a creature in the affected area regains stamina, they only regain half the stamina. A [[winded]] creature who enters an affected square or starts their turn there takes 1d6 poison damage."
  - name: "Thorn Dragon’s Domain"
    desc: " If the encounter map is a location the dragon has occupied for 1 week or more, each space on the map is considered difficult terrain for all creatures except for the dragon. Each such creature who moves within the area takes 1 damage for each square they enter. A creature [[restrained]] in this area is also [[bleeding]]."
actions:
  - name: "Virulent Breath"
    desc: "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 10 x 1 line within 1
      <br />**Target** All enemies 
      <br />**Effect:** Each target makes a Might test.
      <br />`dice: 2d10 +
      <br />✸ ≤11 12 poison damage; P< 4 dragonsealed (save ends)
      <br />★ 12–16 9 poison damage; P< 3 dragonsealed (save ends)
      <br />✦ 17+ 5 poison damage; P< 2 dragonsealed (save ends) 
      <br />**Effect:** Until the condition ends, a creature dragonsealed by the dragon has their wounds overtaken by nettles and thorns, and they take an additional die of damage from conditions that deal damage, the dragon’s Wyrmscale Aura, and the dragon’s Malign Thicket Villain Action."
  - name: "Spinous Tail Swing"
    desc: "
      <br />**Keywords** Charge, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** Two enemies or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 8 damage; push 2
      <br />★ 12–16 12 damage; push 4
      <br />✸ 17+ 15 damage; push 8 3 Malice Each target is A< 3 [[bleeding]] (save ends)."
maneuvers:
  - name: "Provoking Nettles (Free Maneuver)"
    desc: " Once per turn, the dragon shifts 5 and can move through enemies at normal speed. The first time the dragon passes through a creature’s space during this movement, the creature takes 3 damage."
  - name: "Investiture of Verdure"
    desc: "
      <br />**Cost** 5 Malice
      <br />**Keywords** Area
      <br />**Distance** 10 burst
      <br />**Target** All dragonsealed enemies 
      <br />**Effect:** Each target is pulled 5 toward the dragon. For each creature pulled, the dragon gains 5 temporary stamina."
ta:
  - name: "Prickly Situation (Triggered Action)"
    desc: "
      <br />**Keywords** Magic
      <br />**Distance** 10
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature successfully saves to end their dragonsealed condition. 
      <br />**Effect:** The target is pulled 5 toward the dragon and is [[restrained]] (EoT)."
  - name: "Thorny Scales (Free Triggered Action)"
    desc: " ◆ 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature deals damage to the dragon with a melee strike. 
      <br />**Effect:** The dragon makes a free strike against the target. The target is M < 2 [[bleeding]] (EoT)."
va:
  - name: "Briar Bindings (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 4 burst
      <br />**Target** All enemies
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 5 damage; A< 2 [[restrained]] (save ends)
      <br />★ 12–16 9 damage; A< 3 [[restrained]] (save ends)
      <br />✸ 17+ 12 damage; A< 4 [[restrained]] (save ends)  "
  - name: "Thorned Armor (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The dragon grows longer, sharper thorns upon their scales. A creature who targets the dragon with a melee strike takes 3 damage."
  - name: "Malign Thicket (Villain Action 3)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The dragon’s domain becomes imbued with deadly poison. A creature who takes damage from the dragon’s domain or from striking the dragon takes an additional 1d6 poison damage."

```
