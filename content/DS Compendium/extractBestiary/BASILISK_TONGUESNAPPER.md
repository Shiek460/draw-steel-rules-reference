# BASILISK TONGUESNAPPER
```statblock
name: "BASILISK TONGUESNAPPER"
level: 1
roles:
  - TROOP
  - HEXER
ancestry:
  - Basilisk
  - Beast
ev: 12
stamina: 40
immunities: Poison 2, Acid 2
speed: 8
size: 2 /
stability: 2
free_strike: 4
characteristics:
  - +1
  - +2
  - −3
  - −1
  - −1
actions:
  - name: "Prehensile Tongue"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 acid damage; pull 1
      <br />★ 12–16 10 acid damage; pull 2
      <br />✸ 17+ 14 acid damage; pull 3 
      <br />**Effect:** This ability can pull targets [[restrained]] by Petrifying Eye Beams, ignoring stability. 
      <br />**3 Malice** The toungesnapper targets two additional creatures or objects."
  - name: "Wink"
    desc:
      "
      <br />**Keywords** Melee, Magic, Strike, Ranged
      <br />**Distance** Melee 1 or Ranged 10
      <br />**Target** 1 creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 8 corruption damage; R<  0 [[dazed]] (save ends)
      <br />★ 12–16 10 corruption damage; R<  1 [[dazed]] (save ends)
      <br />✸ 17+ 14 corruption damage; R<  2 [[dazed]] and [[slowed]] (save ends) 
      <br />**Effect:** A creature [[dazed]] by this ability can’t benefit from edges or surges until the condition ends." 
maneuvers:
  - name: "Petrifying Eye Beams"
    desc: "
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** 5 × 2 line within 1
      <br />**Target** Special
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 A<  0 [[restrained]] (save ends)
      <br />★ 12–16 A<  1 [[restrained]] (save ends)
      <br />✸ 17+ [[slowed]] (save ends) or A<  2 [[restrained]] (save ends) 
      <br />**Effect:** The tonguesnapper targets the first unobstructed creature in each column of the area. An already [[slowed]] target has -1 to resisting the potency. Each target magically begins to turn to stone. A creature [[restrained]] by this ability or a creature adjacent to them can use an action to cut the encroaching stone from their body, taking 8 damage which can’t be reduced in any way and ending the effect. A target that ends two consecutive turns [[restrained]] by this ability is petrified until they are cured (see Alchemical Ingredients)."
ta:
  - name: "Neurotoxin Splash"
    desc: "
      <br />**Keywords** — 
      <br />**Trigger** The tonguesnapper takes melee damage.
      <br />**Distance** 2 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** Each target takes 4 acid damage and is M<  2 [[slowed]] (save ends)."
traits:
  - name: "Petrifying Fumes"
    desc: "A creature that starts their turn adjacent to the tonguesnapper is M< 1 [[slowed]] (save ends)."

```
