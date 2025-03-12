w# TRAINED GELATINOUS CUBE
```statblock
name: "TRAINED GELATINOUS CUBE"
level: 1
roles:
  - TROOP
  - HEXER
ancestry:
  - Animal
  - Kobold
ev: 12
stamina: 40
immunities: Acid 3
speed: 5
size: 2 /
stability: 2
free_strike: 4
characteristics:
  - +2
  - −1
  - −3
  - 0
  - −2
actions:
  - name: "Engulf"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 acid damage; A< 0 [[dazed]] (save ends)
      <br />★ 12–16 10 acid damage; A< 1 [[dazed]] (save ends)
      <br />✸ 17+ 14 acid damage; A< 2 [[restrained]] (save ends) 
      <br />**Effect:** A size: 2 or smaller creature [[restrained]] by this ability is pulled into one of the cube’s squares and moves with the cube. The creature takes 4 acid damage at the start of each of their turn while [[restrained]]. When [[restrained]] ends, the creature moves to the nearest unoccupied square adjacent to the cube. <br />**2 Malice** The cube targets 1 additional creature or object."
ta:
  - name: "You Didn’t Pay Attention! (Free Triggered Action)"
    desc: "
      <br />**Keywords** — 
      <br />**Trigger** A creature moves or is force moved into the cube.
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The cube uses Engulf with a double edge."
traits:
  - name: "Translucent Cube"
    desc: "The cube completely occupies their space, blocking [[Line of Effect]] on enemy abilities. The cube is hidden until they act."

```
