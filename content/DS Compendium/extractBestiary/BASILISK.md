# BASILISK
```statblock
name: "BASILISK"
level: 1
roles:
  - TROOP
  - BRUTE
ancestry:
  - Basilisk
  - Beast
ev: 12
stamina: 80
immunities: Poison 4
speed: 8
size: 2 /
stability: 2
free_strike: 5
characteristics:
  - +2
  - 0
  - −3
  - −1
  - −1
actions: 
  - name: "Noxious Bite"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 poison damage
      <br />★ 12–16 10 poison damage
      <br />✸ 17+ 13 poison damage 
      <br />**Effect:** This ability has an edge against targets that the basilisk has previously dealt poison damage to."
  - name: "Poison Fumes"
    desc:
      "
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 cube within 1
      <br />**Target** All creatures in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 poison damage; M<  0 [[weakened]] (save ends)
      <br />★ 12–16 6 poison damage; M<  1 [[weakened]] and [[slowed]] (save ends)
      <br />✸ 17+ 9 poison damage; M<  2 [[weakened]] and [[slowed]] (save ends)"
maneuvers:
  - name: "Petrifying Eye Beams"
    desc: "
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 5 × 2 line within 1
      <br />**Target** Special
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 M<  0 [[restrained]] (save ends)
      <br />★ 12–16 M<  1 [[restrained]] (save ends)
      <br />✸ 17+ [[slowed]] (save ends) or M<  2 [[restrained]] (save ends) 
      <br />**Effect:** The basilisk targets the first unobstructed creature in each column of the area. An already [[slowed]] target has -1 to resisting the potency. Each target magically begins to turn to stone. A creature [[restrained]] by this ability or a creature adjacent to them can use an action to cut the encroaching stone from their body, taking 8 damage which can’t be reduced in any way and ending the effect. A target that ends two consecutive turns [[restrained]] by this ability is petrified until they are cured (see Alchemical Ingredients)."
ta:
  - name: "Lash Out"
    desc: "
      <br />**Keywords** — 
      <br />**Trigger** The basilisk takes melee damage.
      <br />**Distance** 1 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** Each target takes 5 damage and is A<  2 [[bleeding]] (save ends)."
traits:
  - name: "Calcifying"
    desc: "The area within 3 squares of the basilisk is considered difficult terrain for enemies."

```
