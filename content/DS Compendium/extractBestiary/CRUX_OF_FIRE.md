# CRUX OF FIRE
```statblock
name: "CRUX OF FIRE"
level: 3
roles:
  - TROOP
  - ARTILLERY
ancestry:
  - Elemental
ev: 20
stamina: 80
immunities: fire 5
speed: 6
size: 1T /
stability: 0
free_strike: 6
characteristics:
  - −1
  - +2
  - 0
  - +1
  - +2
actions:
  - name: "Spitfire"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 12
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 fire damage
      <br />★ 12–16 12 fire damage; A< 1 burning (save ends)
      <br />✸ 17+ 15 fire damage; A< 2 burning (save ends) 
      <br />**Effect:** A burning creature or object takes 1d6 fire damage at the start of each of their turns until the condition ends."
maneuvers:
  - name: "Convocation of Flames"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 5
      <br />**Target** Self or 1 elemental 
      <br />**Effect:** The target receives fire immunity 5 until the start of the crux’s next turn if they don’t already have it. 3 Malice The ground within 3 of the target is wreathed in fire until the end of the encounter. Whenever an enemy first enters the affected area on a turn or starts their turn within it, they take 3 fire damage."
ta:
  - name: "Flame Jet"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Magic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The crux takes damage. 
      <br />**Effect:** The crux ignores any effects associated with the damage and flies up to their speed. If the crux doesn’t end this movement on solid ground, they fall [[prone]]."
traits:
  - name: "Fickle and Free"
    desc: "The crux can’t be [[restrained]], [[slowed]], or knocked [[prone]], and they ignore difficult terrain."


```
