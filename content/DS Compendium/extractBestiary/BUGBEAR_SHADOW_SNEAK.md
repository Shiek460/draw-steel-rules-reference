# BUGBEAR SHADOW SNEAK
```statblock
name: "BUGBEAR SHADOW SNEAK"
level: 2
roles:
  - TROOP
  - AMBUSHER
ancestry:
- Bugbear 
- Goblin 
- Humanoid 
- Fey
ev: 16
stamina: 80
speed: 7
size: 1L /
stability: 0
free_strike: 5
characteristics:
  - +2
  - +2
  - 0
  - 0
  - 0
actions:
  - name: "Suckerpunch"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 damage; A<  1 [[grabbed]]
      <br />★ 12–16 13 damage; A<  2 [[grabbed]]
      <br />✸ 17+ 16 damage; [[grabbed]] 
      <br />**Effect:** The target can’t use triggered actions until the start of the next round. This ability deals an additional 4 damage if the sneak started their turn hidden from the target."
  - name: "Shadow Cloak"
    desc:
      "
      <br />**Keywords** Area
      <br />**Distance** 2 burst
      <br />**Target** All enemies in the burst
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage; I<  0 sneak is concealed from the target (save ends)
      <br />★ 12–16 3 damage; I<  1 sneak is concealed from the target (save ends)
      <br />✸ 17+ 4 damage; I<  2 sneak is concealed from the target (save ends) 
      <br />**Effect:** The sneak shifts up to their speed and hides after using this ability."
  - name: "Carving Dagger"
    desc:
      "
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 8
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage; M<  0 [[bleeding]] (save ends)
      <br />★ 12–16 11 damage; M<  1 [[bleeding]] (save ends)
      <br />✸ 17+ 14 damage; M<  2 [[bleeding]] (save ends) 
      <br />**Effect:** The target can’t hide from the sneak or their allies while [[bleeding]] from this ability."
maneuvers:
  - name: "Throw"
    desc: "
      <br />**Keywords** Attack, Melee
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object [[grabbed]] by the sneak 
      <br />**Effect:** Vertical push 4. An ally target doesn’t take damage from being force moved."
ta:
  - name: "Catcher (Free Triggered Action)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** 1 size 1 creature or object 
      <br />**Trigger** The target is force moved into a square adjacent to the sneak. 
      <br />**Effect:** The target is [[grabbed]] by the sneak."
  - name: "Clever Trick"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Special
      <br />**Target** 1 enemy 
      <br />**Trigger** A target attacks the sneak. 
      <br />**Effect:** The sneak chooses an enemy within distance of the attack. The attack targets that enemy instead."


```
