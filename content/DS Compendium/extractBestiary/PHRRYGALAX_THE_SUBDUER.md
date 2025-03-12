# PHRRYGALAX THE SUBDUER
```statblock
name: "PHRRYGALAX THE SUBDUER"
level: 6
roles:
  - TROOP
  - BRUTE
ancestry:
  - Draconian
  - Dragon
  - Humanoid
ev: 32
stamina: 180 Immunities fire 6
speed: 5 (flying)
size: 1L /
stability: 5
free_strike: 7
characteristics:
  - +3
  - +2
  - +0
  - +0
  - +3
actions:
  - name: "Baneful Blade"
    desc: "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 damage
      <br />★ 12–16 16 damage; M< 1 [[bleeding]] (save ends)
      <br />✸ 17+ 19 damage; M< 2 3 damage, [[bleeding]] (save ends) "
  - name: "Spinning Spit"
    desc: "
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 1 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 7 fire damage
      <br />★ 12–16 13 fire damage
      <br />✸ 17+ 16 fire damage "
maneuvers:
  - name: "Heavy Landing"
    desc: "
      <br />**Keywords** Area
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Phrrygalax flies up to his speed and lands in an unoccupied space on the ground. Each creature adjacent to where he lands is A< 2 knocked [[prone]]."
ta:
  - name: "Armor of the Ancients"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** Phrrygalax takes acid, cold, corruption, fire, lightning, or poison damage. 
      <br />**Effect:** Phrrygalax absorbs the damage instead, recovering stamina equal to the damage dealt. Phrrygalax swaps his current immunity with the triggering damage type."
  - name: "STILL YOUR TONGUE! (Free Triggered Action)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** Phrrygalax hears a creature within 5 reciting the oath of Good King Omund’s Dragon Phalanx 
      <br />**Effect:** Phrrygalax shifts up to his speed and uses Baneful Blade against the enemy, dealing an additional 7 damage."
traits:
  - name: "Oathbreaker’s Vengeance"
    desc: "When Phrrygalax fails a saving throw, he deals an additional 7 damage on his next strike."

```
