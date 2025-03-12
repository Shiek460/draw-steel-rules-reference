# GLOOM DRAGON
```statblock
name: "GLOOM DRAGON"
level: 4
roles:
  - SOLO
ancestry:
  - Dragon
  - Elemental
ev: 60
stamina: 350
immunities: psychic 5
speed: 8 (fly, hover)
size: 4 /
stability: 4
free_strike: 6
characteristics:
  - +2
  - +4
  - +1
  - +3
  - +4
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The dragon takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the dragon can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the dragon can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Gloaming Wyrmscale Aura"
    desc: "The dragon’s scales emit a 4 aura of dark fog. An enemy who starts their turn in an affected area takes 2 psychic damage, and the dragon deals an additional 2 psychic damage on abilities per number of enemies in the aura (to a maximum of 6)."
actions:
  - name: "Breath of Brume"
    desc: "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 4 cube within 10
      <br />**Target** All enemies and objects 
      <br />**Effect:** Each target makes a Might test.
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 6 cold damage; P< 3 dragonsealed (save ends)
      <br />★ 12–16 11 cold damage; P< 4 dragonsealed (save ends)
      <br />✸ 17+ 14 cold damage; P< 5 dragonsealed (save ends) 
      <br />**Effect:** The affected area becomes an area of magical darkness. The dragon ignores concealment granted by the darkness. A creature dragonsealed by the dragon has psychic weakness 3 and cold weakness 3 until the condition ends."
  - name: "Phantom Tail Swing"
    desc: "
      <br />**Keywords** Charge, Magic, Melee, Strike
      <br />**Distance** Melee 3
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 10 psychic damage; pull 2
      <br />★ 12–16 15 psychic damage; pull 4
      <br />✸ 17+ 18 psychic damage; pull 6 
      <br />**2 Malice** The pull becomes a vertical slide."
maneuvers:
  - name: "Shadow Skulk (Free Maneuver)"
    desc: "- Once per turn, the dragon shifts up to their speed and leaves behind a 4 cube area of magical darkness. The dragon ignores concealment granted by the darkness. An enemy that ends their turn in the affected area is I< 3 [[frightened]] of the dragon."
  - name: "Visions in the Dark"
    desc: "
      <br />**Cost** 5 Malice
      <br />**Keywords** Area, Magic
      <br />**Distance** 10 burst
      <br />**Target** All dragonsealed enemies 
      <br />**Effect:** Each target takes 3 psychic damage and is I< 3 compelled to immediately make a free strike against one of their allies within range as they hallucinate a threat."
ta:
  - name: "Shroud (Triggered Action)"
    desc: " 
      <br />**Cost** 1 Malice
      <br />**Keywords** Area, Magic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The dragon takes damage. 
      <br />**Effect:** The dragon reduces the damage by 2 for each enemy in their aura."
  - name: "Encroaching Darkness (Free Triggered Action)"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Ranged 10
      <br />**Target** Special 
      <br />**Trigger** A creature moves. 
      <br />**Effect:** The dragon moves two cubes of magical darkness up to 10."
  - name: "Gloom Dragon’s Domain"
    desc: "If the encounter map is a location the dragon has occupied for 1 week or more, illusory magic drenches the air such that even the scenery emanates malice. Each creature other than the dragon in the affected area has a -2 on saving throws made to end the [[frightened]] condition. A [[frightened]] enemy in the affected area takes an additional 3 psychic damage whenever they take damage."
va:
  - name: "Enveloping Umbrage (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 5 burst
      <br />**Target** All enemies
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 Pull 2; I< 3 [[frightened]] (EoT)
      <br />★ 12–16 Push 4; I< 4 [[frightened]] (save ends)
      <br />✸ 17+ Push 6; I< 5 [[frightened]] (save ends) Pall of Nightmares."
  - name: "(Villain Action 2)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 10 burst
      <br />**Target** All dragonsealed enemies
      <br />`dice: 2d10 +
      <br />✦ ≤11 6 psychic damage
      <br />★ 12–16 11 psychic damage
      <br />✸ 17+ 14 psychic damage 
      <br />**Effect:** The targets are I < 4 [[dazed]] as they are assaulted by their hallucinations."
  - name: "Absence of All Light (Villain Action 3)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Special
      <br />**Target** Self 
      <br />**Effect:** The dragon disappears, then reappears anywhere on the encounter map, as do three hallucinatory versions of it at other points on the encounter map (the director determines which one is real). The dragon and each hallucinatory version of it immediately uses Breath of Brume. A creature who deals damage to a hallucination of the dragon causes it to immediately dissipate."

```
