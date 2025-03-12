# PREDATOR A
```statblock
name: "PREDATOR A"
level: 1
roles:
  - TROOP
  - BRUTE
ancestry:
  - Animal
ev: 16
stamina: 80
speed: 5
size: 2 /
stability: 0
free_strike: 5
characteristics:
  - +1
  - +2
  - -2
  - +1
  - +1
actions:
  - name: "Natural Weapon"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 10 damage; M< 1 [[prone]]
      <br />✸ 17+ 13 damage; M< 2 [[prone]] Ready to Strike (Maneuver)
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The predator assesses their environment or lets loose a battle cry and gives themself an edge on their next strike."
ta:
  - name: "Quick Strike"
    desc: "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** Triggering creature or object 
      <br />**Trigger** A creature or object comes within distance. 
      <br />**Effect:** The predator makes a free strike against the target. The predator deals an additional 3 damage if they were hidden from the target."
traits:
  - name: "Nature Calls"
    desc: "The predator ignores 1 bane on their abilities while in an encounter outside or in a natural environment."

```
