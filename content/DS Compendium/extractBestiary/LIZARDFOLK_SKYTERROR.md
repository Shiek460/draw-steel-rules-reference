# LIZARDFOLK SKYTERROR
```statblock
name: "LIZARDFOLK SKYTERROR"
level: 1
roles:
  - PLATOON
  - HARRIER
ancestry:
  - Humanoid
  - Lizardfolk
ev: 6
stamina: 30
speed: 7 (swim)
size: 1S /
stability: 0
free_strike: 3
characteristics:
  - +1
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Glaive Rush"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 7 damage
      <br />✸ 17+ 9 damage; [[prone]] 
      <br />**Effect:** The skyterror can shift 4 after using this ability if they are flying."
  - name: "Poison Blowdart"
    desc:
      "
      <br />**Keywords** Ranged, Weapon
      <br />**Distance** Ranged 5
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 3 damage; M< 0 [[weakened]] (save ends)
      <br />★ 12–16 5 damage; M< 1 [[weakened]] (save ends)
      <br />✸ 17+ 7 damage; M< 2 [[weakened]] (save ends) 
      <br />**Effect:** A creature that ends their turn adjacent to a creature or object [[weakened]] by this ability is [[weakened]] (EoT)."
traits:
  - name: "Glider"
    desc: "The skyterror adds the flying keyword to their movement until the end of their next turn whenever they move at least 2 squares along the ground or fall at least 2 squares."
  - name: "Reptilian Escape"
    desc: "While the skyterror still has a tail, whenever the skyterror is [[grabbed]], [[slowed]], [[weakened]], or knocked [[prone]], the skyterror can lose their tail to immediately end the effect and shift 2."

```
