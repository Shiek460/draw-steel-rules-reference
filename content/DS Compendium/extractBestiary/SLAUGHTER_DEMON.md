# SLAUGHTER DEMON
```statblock
name: "SLAUGHTER DEMON"
level: 4
roles:
  - TROOP
  - BRUTE
ancestry:
  - Abyssal
  - Demon
  - Hobgoblin
ev: 24
stamina: 140
immunities: fire 5
speed: 7 (burrow)
size: 3 /
stability: 3
free_strike: 6
characteristics:
  - +3
  - 0
  - −1
  - +1
  - 0
actions:
  - name: "Steely Skewer"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage
      <br />★ 12–16 14 damage; A< 2 [[bleeding]] (save ends)
      <br />✸ 17+ 17+ damage; A< 3 [[bleeding]] and [[restrained]] (save ends) 
      <br />**Effect:** A creature [[restrained]] by this attack moves along with the slaughter demon until the condition ends. The slaughter demon can have up to 6 creatures or objects [[restrained]] on their weapons."
  - name: "Tail Stinger"
    desc:
      "
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Melee 5
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 10 poison damage; M< 1 [[weakened]] (save ends)
      <br />★ 12–16 16 poison damage; M< 2 [[weakened]] (save ends)
      <br />✸ 17+ 20 poison damage; M< 3 [[weakened]] (save ends) 
      <br />**Effect:** A target [[weakened]] by this ability has damage weakness 3 until the condition ends."
maneuvers:
  - name: "Drag Below"
    desc: "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** 1 creature or object 
      <br />**Effect:** The slaughter demon makes a free strike against the target and burrows up to their speed. The target is pulled the same number of squares the slaughter demon burrows into, including vertically."
ta:
  - name: "Devour Soul"
    desc: "
      <br />**Keywords** Magic 
      <br />**Trigger** A creature with a soul dies.
      <br />**Distance** 5 burst
      <br />**Target** Triggering creature 
      <br />**Effect:** The target can’t be brought back to life. The slaughter demon gains an edge on all power rolls for the rest of the encounter."
traits:
  - name: "Soulsight"
    desc: "Each creature within 2 of the slaughter demon can’t be hidden from them."
  - name: "Lethe"
    desc: "While [[winded]], the slaughter demon has an edge on strikes, and strikes have an edge against them."


```
